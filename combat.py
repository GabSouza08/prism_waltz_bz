# --- Standard Library ---
import random
from datetime import datetime

# --- Third-Party ---
import pygame

# --- Game Data & Persistence ---
from data import ChampionStats, duo_indices
from echo_save import save_duel

# --- Optional Assets (if used) ---
from theme_registry import prism_themes
from duel_dialogue import duel_dialogues
from echo_effects import echo_arts as EchoEffects

# --- Things from debug_themed_duel.py ---
from data import houses, solo_echoes
from duel_dialogue import duel_dialogues

pygame.mixer.init()
pygame.mixer.music.set_volume(0.3)  # Start soft volume

MAX_GAUGE = 10


def find_themed_opponent(player_name):
    for theme in prism_themes:
        c1 = theme["champion_1"]["name"]
        c2 = theme["champion_2"]["name"]
        if player_name == c1:
            return theme["champion_2"], theme["champion_2"]["house"], theme["category"], theme["title"]
        if player_name == c2:
            return theme["champion_1"], theme["champion_1"]["house"], theme["category"], theme["title"]
    return None, None, None, None

def get_duel_dialogue(c1, c2):
    for entry in duel_dialogues:
        if {c1, c2} == {entry["champion_1"], entry["champion_2"]}:
            return entry
    return None

def play_theme_track(filename):
    try:
        pygame.mixer.music.load(f"themes/{filename}")
        pygame.mixer.music.play(-1)
        print(f"\n🎵 Playing theme: {filename}")
    except Exception as e:
        print(f"⚠️ Failed to play theme: {e}")

def get_numeric_choice(prompt, min_c, max_c):
    while True:
        try:
            n = int(input(prompt).strip())
            if min_c <= n <= max_c:
                return n
        except ValueError:
            pass
        print(f"Enter a number between {min_c} and {max_c}.")

def tick_buffs(buffs):
    """Decrement duration and remove expired buffs."""
    for buff in buffs:
        buff["duration"] -= 1
    return [b for b in buffs if b["duration"] > 0]

def get_solo_echoes(house, echo_dict):
    titles = solo_echoes.get(house, [])
    return {name: echo_dict[name] for name in titles if name in echo_dict}

def get_duo_echoes(house, champion_index, echo_dict):
    titles = []
    if house in duo_indices and champion_index in duo_indices[house]:
        titles = [title for _, title in duo_indices[house][champion_index]]
    return {name: echo_dict[name] for name in titles if name in echo_dict}


def select_champion():
    print("\n🏛️ Choose a Domus:")
    house_list = list(houses.keys())
    for i, house in enumerate(house_list, 1):
        print(f"  [{i}] {house}")
    h_choice = int(input("> House #: "))
    house = house_list[h_choice - 1]

    print(f"\n🌟 Domus {house} Roster:")
    champ_list = houses[house]
    for i, (name, title) in enumerate(champ_list, 1):
        print(f"  [{i}] {name} — {title}")
    c_choice = int(input("> Champion #: "))
    champ_name, champ_title = champ_list[c_choice - 1]

    print(f"\n🎯 Selected Champion:")
    print(f"🌟 {champ_name} — {champ_title}")
    print(f"🏛️ Affiliation: Domus {house}")
    return house, champ_name, champ_title

def apply_surge_effect(theme, buffs):
    if theme == "Tragedy":
        healed = 5
        print(f"💖 Theme Tragedy: Regain {healed} HP from echo resilience.")
        return {"heal": healed}
    elif theme == "Conflict":
        buffs.append({"stat": "atk", "amount": 2, "duration": 2})
        print("⚔️ Theme Conflict: ATK +2 for 2 turns.")
    elif theme == "Desperation":
        print("💥 Theme Desperat1ion: Echo Gauge surges!")
        return {"echo_boost": 4}
    elif theme == "Final Refrains":
        print("🎶 Theme Final Refrains: Echo Gauge +1.")
        return {"echo_boost": 1}
    elif theme == "Fractured Psyche":
        buffs.append({"stat": "echo_discount", "amount": 1, "duration": 3})
        print("🌀 Theme Fractured Psyche: Echo cost -1 for 3 turns.")
    elif theme == "Reflective":
        buffs.append({"stat": "def", "amount": 1, "duration": 2})
        print("🛡️ Theme Reflective: DEF +1 for 2 turns.")
    return {}

def calculate_effective_cost(base_cost, buffs):
    discount = sum(b["amount"] for b in buffs if b["stat"] == "echo_discount")
    return max(1, base_cost - discount)

def select_valid_echo_art(echo_gauge, arts, buffs):
    valid = []
    for name, art in arts.items():
        cost = calculate_effective_cost(art["cost"], buffs)
        if cost <= echo_gauge:
            valid.append(name)
    return valid

def apply_echo_art(art, target, buffs):
    if art["type"] == "damage":
        target['HP'] -= art["power"]
        print(f"🗡️ Deals {art['power']} damage!")
        if "bonus" in art:
            b = art["bonus"]
            buffs.append({
                "stat": b["stat"],
                "amount": b["amount"],
                "duration": b["duration"]
            })
            print(f"📈 Bonus: +{b['amount']} {b['stat']} ({b['duration']} turns)")
    elif art["type"] == "heal":
        healed = art["amount"]
        target['HP'] = min(target['HP'] + healed, 100)
        print(f"💖 Heals {healed} HP")
    elif art["type"] == "buff":
        buffs.append({
            "stat": art["stat"],
            "amount": art["amount"],
            "duration": art["duration"]
        })
        print(f"📈 Buff: +{art['amount']} {art['stat']} ({art['duration']} turns)")

def get_player_action(player, echo_gauge, player_arts):
    available_echoes = []
    if "echo_gauge" in player and player["echo_gauge"] >= 1:
        available_echoes = select_valid_echo_art(player["echo_gauge"], player_arts, player["buffs"])

    print("\n🎮 Choose your action:")
    print("  [1] Attack")
    print("  [2] Defend")
    
    available_echoes = select_valid_echo_art(echo_gauge, player_arts, player["buffs"])
    if available_echoes:
        print("  [3] Echo Art")

    valid_choices = [1, 2] + ([3] if available_echoes else [])
    choice = get_numeric_choice("> Action #: ", min(valid_choices), max(valid_choices))

    return ["Attack", "Defend", "Echo Art"][choice - 1]

def calculate_damage(attacker, defender, atk_range=(0.8, 1.2)):
    factor = random.uniform(*atk_range)
    raw = attacker["ATK"] * factor
    mitigated = raw - (defender["DEF"] / 2)
    return max(1, int(mitigated))

def run_player_turn(player, enemy, player_arts, echo_gauge, buffs, p_action):
    if p_action == "Attack":
        atk_bonus = sum(b["amount"] for b in buffs if b["stat"].lower() == "atk")
        base_atk = player["ATK"] + atk_bonus
        dmg = calculate_damage({"ATK": base_atk}, enemy)
        enemy["HP"] -= dmg
        print(f"🗡️ {player['name']} attacks! Deals {dmg} damage.")

    elif p_action == "Defend":
        echo_gauge = min(echo_gauge + 2, MAX_GAUGE)
        print(f"🛡️ {player['name']} defends. Echo Gauge: {echo_gauge}/{MAX_GAUGE}")

    elif p_action == "Echo Art":
        available = [name for name, art in player_arts.items() if art["cost"] <= echo_gauge]
        if not available:
            print("⚠️ Not enough Echo Gauge for any Echo-Art.")
            return echo_gauge

        print("\n🎶 Available Echo-Arts:")
        for i, name in enumerate(available, 1):
            cost = player_arts[name]["cost"]
            print(f"  [{i}] {name} — Cost: {cost}")

        choice = get_numeric_choice("> Choose Echo #: ", 1, len(available))
        art_name = available[choice - 1]
        art = player_arts[art_name]
        echo_gauge -= art["cost"]

        print(f"\n✨ {player['name']} uses Echo Art: {art_name}!")

        if art["type"] == "buff":
            buff = {
                "stat": art["stat"].lower(),
                "amount": art["amount"],
                "duration": art["duration"]
            }
            buffs.append(buff)
            print(f"🌀 Buff: +{buff['amount']} {buff['stat'].upper()} for {buff['duration']} turns.")

        elif art["type"] == "heal":
            healed = min(player["max_HP"] - player["HP"], art["amount"])
            player["HP"] += healed
            print(f"💖 Heals {healed} HP → {player['HP']}/{player['max_HP']}")

        elif art["type"] == "damage":
            dmg = art["power"]
            enemy["HP"] -= dmg
            print(f"🔥 Deals {dmg} damage to {enemy['name']}!")

            if "bonus" in art:
                bonus = art["bonus"]
                if bonus["type"] == "buff":
                    buff = {
                        "stat": bonus["stat"].lower(),
                        "amount": bonus["amount"],
                        "duration": bonus["duration"]
                    }
                    buffs.append(buff)
                    print(f"🔁 Bonus Buff: +{buff['amount']} {buff['stat'].upper()} for {buff['duration']} turns.")

    return echo_gauge

def run_enemy_turn(enemy, player, enemy_arts, echo_gauge, buffs):
    print(f"\n🤖 {enemy['name']}'s turn...")

    # Tick buffs
    buffs = tick_buffs(buffs)

    # Choose action
    available_echoes = [name for name, art in enemy_arts.items() if art["cost"] <= echo_gauge]
    use_echo = available_echoes and random.random() < 0.5  # 50% chance to use Echo-Art

    if use_echo:
        art_name = random.choice(available_echoes)
        art = enemy_arts[art_name]
        echo_gauge -= art["cost"]
        print(f"🎵 {enemy['name']} uses Echo Art: {art_name}!")

        if art["type"] == "buff":
            buff = {
                "stat": art["stat"].lower(),
                "amount": art["amount"],
                "duration": art["duration"]
            }
            buffs.append(buff)
            print(f"🌀 Buff: +{buff['amount']} {buff['stat'].upper()} for {buff['duration']} turns.")

        elif art["type"] == "heal":
            healed = min(enemy["max_HP"] - enemy["HP"], art["amount"])
            enemy["HP"] += healed
            print(f"💖 Heals {healed} HP → {enemy['HP']}/{enemy['max_HP']}")

        elif art["type"] == "damage":
            dmg = art["power"]
            player["HP"] -= dmg
            print(f"🔥 Deals {dmg} damage to {player['name']}!")

            if "bonus" in art:
                bonus = art["bonus"]
                if bonus["type"] == "buff":
                    buff = {
                        "stat": bonus["stat"].lower(),
                        "amount": bonus["amount"],
                        "duration": bonus["duration"]
                    }
                    buffs.append(buff)
                    print(f"🔁 Bonus Buff: +{buff['amount']} {buff['stat'].upper()} for {buff['duration']} turns.")

    else:
        # Basic attack
        atk_bonus = sum(b["amount"] for b in buffs if b["stat"].lower() == "atk")
        base_atk = enemy["ATK"] + atk_bonus
        dmg = calculate_damage({"ATK": base_atk}, player)
        player["HP"] -= dmg
        print(f"🗡️ {enemy['name']} attacks! Deals {dmg} damage.")

    return echo_gauge

def start_solo_duel(p_house, p_name, p_bond,
                    e_house, e_name, e_bond,
                    theme_name):
    """
    Runs a solo duel between the player’s champion and an enemy.
    Returns a result dict for logging/saving.
    """
    # Audio setup
    pygame.mixer.music.set_volume(0.3)

    # Load champion stats
    p_stats = ChampionStats[p_house][p_name]
    e_stats = ChampionStats[e_house][e_name]

    player = {
        "name":       p_name,
        "HP":         p_stats["HP"],
        "max_HP":     p_stats["HP"],
        "ATK":        p_stats["ATK"],
        "DEF":        p_stats["DEF"],
        "SPD":        p_stats["SPD"],
        "Affinity":   p_stats["Affinity"],
        "echo_gauge": 0,
        "buffs":      []
    }
    enemy = {
        "name":       e_name,
        "HP":         e_stats["HP"],
        "max_HP":     e_stats["HP"],
        "ATK":        e_stats["ATK"],
        "DEF":        e_stats["DEF"],
        "SPD":        e_stats["SPD"],
        "Affinity":   e_stats["Affinity"],
        "echo_gauge": 0,
        "buffs":      []
    }

    # Prepare Echo‐Arts registries
    solo_echoes   = get_solo_echoes(p_house, EchoEffects)
    duo_echoes    = get_duo_echoes(p_house, p_bond, EchoEffects)
    player_arts   = {**solo_echoes, **duo_echoes}
    enemy_solo    = get_solo_echoes(e_house, EchoEffects)
    enemy_duo     = get_duo_echoes(e_house, e_bond, EchoEffects)
    enemy_arts    = {**enemy_solo, **enemy_duo}

    turn = 1
    triggered_theme = None

    # Main duel loop
    while player["HP"] > 0 and enemy["HP"] > 0:
        print(f"\n— Turn {turn} —")
        print(f"{player['name']} HP: {player['HP']}/{player['max_HP']} | Echo Gauge: {player['echo_gauge']}/{MAX_GAUGE}")
        print(f"{enemy['name']}  HP: {enemy['HP']}/{enemy['max_HP']} | Echo Gauge: {enemy['echo_gauge']}/{MAX_GAUGE}")

        # Tick down buffs on both sides
        player["buffs"] = tick_buffs(player["buffs"])
        enemy["buffs"]  = tick_buffs(enemy["buffs"])

        # Player’s turn
        p_action = get_player_action(player, player["echo_gauge"], player_arts)
        player["echo_gauge"] = run_player_turn(
            player,
            enemy,
            player_arts,
            player["echo_gauge"],
            player["buffs"],
            p_action
        )

        # Check for player victory
        if enemy["HP"] <= 0:
            print(f"\n🏆 {player['name']} wins!")
            break

        # Enemy’s turn
        enemy["echo_gauge"] = run_enemy_turn(
            enemy,
            player,
            enemy_arts,
            enemy["echo_gauge"],
            enemy["buffs"]
        )

        # Theme Surge on turn 10
        if theme_name and turn == 10 and not triggered_theme:
            print(f"\n💥 SURGE: {theme_name.upper()} ruptures the battlefield!")
            pygame.mixer.music.set_volume(0.6)
            input("🌫️ The prism resonates… Press Enter.")
            surge = apply_surge_effect(theme_name, player["buffs"])
            triggered_theme = theme_name

            # Apply heal boost
            if "heal" in surge:
                amt = surge["heal"]
                player["HP"] = min(player["max_HP"], player["HP"] + amt)
                print(f"💖 Heals {amt} HP → {player['HP']}/{player['max_HP']}")

            # Apply echo gauge boost
            if "echo_boost" in surge:
                boost = surge["echo_boost"]
                player["echo_gauge"] = min(MAX_GAUGE, player["echo_gauge"] + boost)
                print(f"🎶 Echo Gauge +{boost} → {player['echo_gauge']}/{MAX_GAUGE}")

        turn += 1

    # Compile result and save
    player_won = player["HP"] > 0
    result = {
        "player_name":    player["name"],
        "opponent_name":  enemy["name"],
        "stage_id":       "SoloDuel",
        "turn_count":     turn - 1,
        "triggered_theme": triggered_theme,
        "player_won":     player_won,
        "timestamp":      datetime.now().isoformat()
    }
    print(f"\n🏆 Result: {'Victory' if player_won else 'Defeat'} in {turn - 1} turns")
    save_duel(result)
    return result

def themed_match():
    print("🌒 Prism Waltz — Combat Tool")

    # === Player Selection ===
    p_house, p_name, p_title = select_champion()
    p_bond = None  # Bond logic can be added later

    # === Opponent Lookup ===
    e_data, e_house, theme_category, theme_title = find_themed_opponent(p_name)
    if not e_data:
        print("⚠️ No themed opponent found for this champion.")
        return
    e_name = e_data["name"]
    e_bond = None

    # === Match Preview ===
    print("\n⚔️ Duel Preview:")
    print(f"🌟 {p_name} — {p_title} [Domus {p_house}]")
    print("🆚")
    print(f"🌑 {e_name} — {theme_title} [Domus {e_house}]")
    print(f"🎭 Theme: {theme_category}")

    # === Theme Music & Dialogue ===
    print(f"\n🎭 Match Found: {p_name} — {p_title} vs {e_name} | Theme: {theme_category}")
    print(f"🎶 Theme Track: {theme_title}")
    play_theme_track(theme_title)

    dialogue = get_duel_dialogue(p_name, e_name)
    if dialogue:
        print("\n📜 Pre-Battle Dialogue:")
        for line in dialogue["intro_lines"]:
            print(f" “{line}”")
            input(" ⏳ Press Enter for next…")
        print(f"🩸 {dialogue['ambient_note']}\n")

    # === Start Solo Duel ===
    result = start_solo_duel(
        p_house=p_house,
        p_name=p_name,
        p_bond=p_bond,
        e_house=e_house,
        e_name=e_name,
        e_bond=e_bond,
        theme_name=theme_category
    )

    # === Outcome & Persistence ===
    print(f"\n🏆 {'Victory' if result['player_won'] else 'Defeat'} in {result['turn_count']} turns!")

def start_duo_battle(p1_house, p1_name, p2_house, p2_name, p1_idx, p2_idx, p1_echo, e1_house, e1_name, e2_house, e2_name, e1_idx, e2_idx, e_echo):
    print(f"🤝 Duo Battle Begins: {p1_name} & {p2_name} vs {e1_name} & {e2_name}")
    return {
        "player_name": f"{p1_name} & {p2_name}",
        "opponent_name": f"{e1_name} & {e2_name}",
        "stage_id": "Duo Arena",
        "turn_count": 0,
        "triggered_theme": None,
        "player_won": True,
        "special_echo_tag": None,
        "system_whisper_text": "Duo bonds shine brightest in the dark.",
        "is_debug": True,
        "timestamp": datetime.now().isoformat()
    }

def start_grand_clash(player_team, *enemy_teams):
    print(f"⚔️ Grand Clash Begins: {player_team[1]} & {player_team[3]} vs {len(enemy_teams)} rival teams")
    return {
        "player_name": f"{player_team[1]} & {player_team[3]}",
        "opponent_name": "Multiple Rivals",
        "stage_id": "Grand Arena",
        "turn_count": 0,
        "triggered_theme": None,
        "player_won": False,
        "special_echo_tag": None,
        "system_whisper_text": "The arena echoes with countless voices.",
        "is_debug": True,
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    try:
        themed_match()
    except Exception as e:
        print(f"❌ Duel interrupted: {e}")
    input("🌒 Prism fades. Press Enter to close the duel...")
