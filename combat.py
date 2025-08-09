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

def resolve_pair_theme(c1, c2):
    """
    Uses your find_themed_opponent in both directions to confirm a curated matchup.
    Returns (theme_category, theme_title) or (None, None).
    """
    e_data, _, theme_category, theme_title = find_themed_opponent(c1)
    if e_data and e_data.get("name") == c2:
        return theme_category, theme_title

    e_data, _, theme_category, theme_title = find_themed_opponent(c2)
    if e_data and e_data.get("name") == c1:
        return theme_category, theme_title

    return None, None


def play_duel_theme_and_dialogue(c1, c2, pause=True, show_header=True, play_audio=True):
    """
    Plays curated theme (if any) and prints rivalry dialogue with optional pauses.
    Returns a dict with metadata about what happened.
    """
    theme_category, theme_title = resolve_pair_theme(c1, c2)
    if not theme_title:
        return {
            "has_curated": False,
            "theme_category": None,
            "theme_title": None,
            "had_dialogue": False
        }

    if show_header:
        print("\n🕯️ Duel Theme:")
        print(f"🎭 {c1} vs {c2} | Theme: {theme_category}")
        print(f"🎶 Theme Track: {theme_title}")

    if play_audio:
        play_theme_track(theme_title)

    had_dialogue = False
    dialogue = get_duel_dialogue(c1, c2)
    if dialogue:
        had_dialogue = True
        print("\n📜 Rivalry Rekindled:")
        for line in dialogue.get("intro_lines", []):
            print(f" “{line}”")
            if pause:
                input(" ⏳ Press Enter to continue…")
        if "ambient_note" in dialogue:
            print(f"🩸 {dialogue['ambient_note']}")

    return {
        "has_curated": True,
        "theme_category": theme_category,
        "theme_title": theme_title,
        "had_dialogue": had_dialogue
    }

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

# fade_effects.py

import time

def trigger_flavor_effects(*fighters):
    for f in fighters:
        if f["HP"] <= 10 and f["HP"] > 0:
            print("\n🩸 Critical Fade Triggered…")
            house = f.get("house", "Default")
            name = f["name"]

            if house == "Alizarin":
                print(f"{name} sinks to one knee — ash curls through the air.")
                print("🔥 'Even pain remembers. I stand on it.'")

            elif house == "Purpur":
                print(f"{name} flickers — twilight threads dance on their skin.")
                print("🪞 'Even fading can fool fate.'")

            elif house == "Scarlet":
                print(f"{name} braces their stance — shield dim but unshattered.")
                print("🛡️ 'My vow was lit in fire. I won’t burn out.'")

            elif house == "Violet":
                print(f"{name} trembles — veil slipping, moonlight bleeding.")
                print("🌙 'Grace lasts longer than breath…'")

            elif house == "Sector_7":
                print(f"{name} falters — echoes fracture with brutal clarity.")
                print("⚡ 'Let despair crack, but not silence me… not yet.'")

            else:
                print(f"{name} staggers… echoes spiral in broken rhythm.")
                print("💠 'I won’t fall as silence.'")

def duo_echo_narration(f, echo_name):
    print("💫 Echo Pulse Surges…")
    time.sleep(0.6)

    partner_name = f.partner.name if hasattr(f, "partner") else "???"
    print(f"{f.name} steps forward — gaze locked with {partner_name}.")
    time.sleep(0.8)

    print("🎶 Their bond glows as twin memories spiral in sync.")
    time.sleep(0.8)

    print(f"🩰 {echo_name} unfolds: A duet of power, resolve, and forgotten rhythm.")
    time.sleep(0.8)

def turn_summary_fade():
    print("Turn ends...")
    time.sleep(0.4)
    print(".")
    time.sleep(0.4)
    print("..")
    time.sleep(0.4)
    print("...")
    time.sleep(0.6)

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

def calculate_damage(attacker, defender, atk_range=(0.9, 1.1)):
    # Step 1: Random variation in ATK
    atk_factor = random.uniform(*atk_range)
    scaled_atk = int(round(attacker["ATK"] * atk_factor))
    # Step 2: Ratio-based mitigation (defense absorbs proportionally)
    mitigation_ratio = 100 / (100 + defender["DEF"])
    raw_damage = scaled_atk * mitigation_ratio
    # Step 3: Clamp to at least 1 and round cleanly
    return max(1, int(round(raw_damage)))


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

def run_enemy_turn(enemy, player, enemy_arts, echo_gauge, buffs,
                   gauge_cap=10, defend_chance=0.25, echo_chance=0.5):
    print(f"\n🤖 {enemy['name']}'s turn...")

    buffs = tick_buffs(buffs)
    def clamp(val): return max(0, min(gauge_cap, val))

    hp_ratio = enemy["HP"] / enemy["max_HP"]
    echo_ready = [name for name, art in enemy_arts.items() if art["cost"] <= echo_gauge]

    # Prioritize Echo Art if available
    if echo_ready and random.random() < echo_chance:
        art_name = random.choice(echo_ready)
        art = enemy_arts[art_name]
        echo_gauge = clamp(echo_gauge - art["cost"])
        print(f"🎵 {enemy['name']} uses Echo Art: {art_name}!")
        # ...handle art effects...
    # Otherwise, randomly defend or attack
    elif random.random() < defend_chance or (hp_ratio < 0.6 and echo_gauge <= 5):
        def_buff = int(round(enemy["DEF"] * 0.5))
        buffs.append({"stat": "def", "amount": def_buff, "duration": 1, "tag": "GUARD"})
        echo_gauge = clamp(echo_gauge + 2)
        print(f"🛡️ {enemy['name']} defends. +{def_buff} DEF for 1 turn. Echo Gauge: {echo_gauge}/{gauge_cap}")
    else:
        atk_bonus = sum(b["amount"] for b in buffs if b["stat"].lower() == "atk")
        final_atk = enemy["ATK"] + atk_bonus
        dmg = calculate_damage({"ATK": final_atk}, player)
        player["HP"] = max(0, player["HP"] - dmg)
        print(f"🗡️ {enemy['name']} attacks! Deals {dmg} damage.")

    return echo_gauge, buffs



def start_solo_duel(p_house, p_name, p_bond,
                    e_house, e_name, e_bond,
                    theme_name,
                    pause_intro=True,
                    play_intro_audio=True):
    """
    Runs a solo duel between the player’s champion and an enemy.
    Returns a result dict for logging/saving.
    """
    pygame.mixer.music.set_volume(0.3)

    # Curated theme + rivalry lines if this pair has one (safe no-op otherwise)
    meta = play_duel_theme_and_dialogue(
        p_name, e_name,
        pause=pause_intro,
        show_header=True,
        play_audio=play_intro_audio
    )

    # Decide which theme drives the turn-10 surge:
    # use provided theme_name, else fall back to curated category if available
    surge_theme = theme_name or meta.get("theme_category")

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
        "buffs":      [],
        "house":      p_house
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
        "buffs":      [],
        "house":      e_house
    }

    solo_echoes   = get_solo_echoes(p_house, EchoEffects)
    duo_echoes    = get_duo_echoes(p_house, p_bond, EchoEffects)
    player_arts   = {**solo_echoes, **duo_echoes}
    enemy_solo    = get_solo_echoes(e_house, EchoEffects)
    enemy_duo     = get_duo_echoes(e_house, e_bond, EchoEffects)
    enemy_arts    = {**enemy_solo, **enemy_duo}

    turn = 1
    triggered_theme = None  # records the surge theme, not the curated duel theme

    while player["HP"] > 0 and enemy["HP"] > 0:
        print(f"\n— Turn {turn} —")
        print(f"{player['name']} HP: {player['HP']}/{player['max_HP']} | Echo Gauge: {player['echo_gauge']}/{MAX_GAUGE}")
        print(f"{enemy['name']}  HP: {enemy['HP']}/{enemy['max_HP']} | Echo Gauge: {enemy['echo_gauge']}/{MAX_GAUGE}")

        player["buffs"] = tick_buffs(player["buffs"])
        enemy["buffs"]  = tick_buffs(enemy["buffs"])

        # 🧿 Player turn
        p_action = get_player_action(player, player["echo_gauge"], player_arts)
        player["echo_gauge"] = run_player_turn(
            player,
            enemy,
            player_arts,
            player["echo_gauge"],
            player["buffs"],
            p_action
        )

        # ✨ Trigger flavor after player turn
        trigger_flavor_effects(player, enemy)

        if enemy["HP"] <= 0:
            print(f"\n🏆 {player['name']} wins!")
            break

        # 🔮 Enemy turn
        enemy["echo_gauge"], enemy["buffs"] = run_enemy_turn(
            enemy,
            player,
            enemy_arts,
            enemy["echo_gauge"],
            enemy["buffs"]
        )

        # ✨ Trigger flavor after enemy turn
        trigger_flavor_effects(player, enemy)

        # 🌌 Theme surge (separate from curated duel theme)
        if surge_theme and turn == 10 and not triggered_theme:
            print(f"\n💥 SURGE: {surge_theme.upper()} ruptures the battlefield!")
            pygame.mixer.music.set_volume(0.6)
            input("🌫️ The prism resonates… Press Enter.")
            surge = apply_surge_effect(surge_theme, player["buffs"])
            triggered_theme = surge_theme

            if "heal" in surge:
                amt = surge["heal"]
                player["HP"] = min(player["max_HP"], player["HP"] + amt)
                print(f"💖 Heals {amt} HP → {player['HP']}/{player['max_HP']}")

            if "echo_boost" in surge:
                boost = surge["echo_boost"]
                player["echo_gauge"] = min(MAX_GAUGE, player["echo_gauge"] + boost)
                print(f"🎶 Echo Gauge +{boost} → {player['echo_gauge']}/{MAX_GAUGE}")

        turn += 1

    # 🗂️ Compile result
    player_won = player["HP"] > 0
    result = {
        "player_name":     player["name"],
        "opponent_name":   enemy["name"],
        "stage_id":        "SoloDuel",
        "turn_count":      turn - 1,
        "triggered_theme": triggered_theme,  # surge theme (if any)
        "curated_theme":   (
            {"category": meta.get("theme_category"), "title": meta.get("theme_title")}
            if meta.get("has_curated") else None
        ),
        "player_won":      player_won,
        "timestamp":       datetime.now().isoformat()
    }

    print(f"\n🏆 Result: {'Victory' if player_won else 'Defeat'} in {turn - 1} turns")
    save_duel(result)
    return result


def start_duo_battle(
    p1_house, p1_name, p2_house, p2_name, p1_idx, p2_idx, player_duo_echo,
    e1_house, e1_name, e2_house, e2_name, e1_idx, e2_idx, enemy_duo_echo,
    theme_name=None
):
    pygame.mixer.music.set_volume(0.3)

    def build_fighter(house, name):
        s = ChampionStats[house][name]
        return {
            "house":      house,
            "name":       name,
            "HP":         s["HP"],
            "max_HP":     s["HP"],
            "ATK":        s["ATK"],
            "DEF":        s["DEF"],
            "SPD":        s["SPD"],
            "Affinity":   s["Affinity"],
            "echo_gauge": 0,
            "buffs":      []
        }

    # Build teams
    P_active  = build_fighter(p1_house, p1_name)
    P_partner = build_fighter(p2_house, p2_name)
    E_active  = build_fighter(e1_house, e1_name)
    E_partner = build_fighter(e2_house, e2_name)

    # Duo echo keys
    player_duo_key = player_duo_echo
    enemy_duo_key  = enemy_duo_echo

    def merged_arts(fighter, duo_key, partner_alive):
        solos = get_solo_echoes(fighter["house"], EchoEffects)
        duos  = get_duo_echoes(fighter["house"], duo_key, EchoEffects) if (duo_key and partner_alive) else {}
        return {**solos, **duos}

    def clamp_hp(f): f["HP"] = max(0, min(f["HP"], f["max_HP"]))
    def clamp_gauge(f): f["echo_gauge"] = max(0, min(f["echo_gauge"], MAX_GAUGE))

    turn = 1
    triggered_theme = None
    curated_theme_start = None
    curated_theme_last_stand = None
    last_stand_theme_fired = False

    # 🎶 Open with theme + dialogue (if curated match)
    meta_start = play_duel_theme_and_dialogue(P_active["name"], E_active["name"])
    if meta_start.get("has_curated"):
        curated_theme_start = {
            "category": meta_start["theme_category"],
            "title": meta_start["theme_title"]
        }

    print(f"\n🤝 Duo Battle Begins: {P_active['name']} & {P_partner['name']} "
          f"vs {E_active['name']} & {E_partner['name']}")

    def maybe_trigger_last_stand_theme():
        nonlocal curated_theme_last_stand, last_stand_theme_fired
        if last_stand_theme_fired:
            return
        allies  = [u for u in (P_active, P_partner) if u["HP"] > 0]
        enemies = [u for u in (E_active, E_partner) if u["HP"] > 0]
        if len(allies) == 1 and len(enemies) == 1:
            a = allies[0]["name"]
            b = enemies[0]["name"]
            meta_last = play_duel_theme_and_dialogue(a, b, pause=False)
            if meta_last.get("has_curated"):
                curated_theme_last_stand = {
                    "category": meta_last["theme_category"],
                    "title": meta_last["theme_title"]
                }
            last_stand_theme_fired = True

    while (P_active["HP"] > 0 or P_partner["HP"] > 0) and (E_active["HP"] > 0 or E_partner["HP"] > 0):
        print(f"\n— Turn {turn} —")
        print(f"{P_active['name']} HP: {P_active['HP']}/{P_active['max_HP']} | Echo Gauge: {P_active['echo_gauge']}/{MAX_GAUGE}  (ACTIVE)")
        print(f"{P_partner['name']} HP: {P_partner['HP']}/{P_partner['max_HP']} | Echo Gauge: {P_partner['echo_gauge']}/{MAX_GAUGE}  (PARTNER)")
        print(f"{E_active['name']}  HP: {E_active['HP']}/{E_active['max_HP']} | Echo Gauge: {E_active['echo_gauge']}/{MAX_GAUGE}  (ACTIVE)")
        print(f"{E_partner['name']}  HP: {E_partner['HP']}/{E_partner['max_HP']} | Echo Gauge: {E_partner['echo_gauge']}/{MAX_GAUGE}  (PARTNER)")

        P_active["buffs"] = tick_buffs(P_active["buffs"])
        E_active["buffs"] = tick_buffs(E_active["buffs"])

        # === PLAYER TURN ===
        player_arts = merged_arts(P_active, player_duo_key, P_partner["HP"] > 0)
        p_action = get_player_action(P_active, P_active["echo_gauge"], player_arts)
        P_active["echo_gauge"] = run_player_turn(
            P_active, E_active, player_arts, P_active["echo_gauge"], P_active["buffs"], p_action
        )
        clamp_hp(P_active); clamp_hp(E_active); clamp_gauge(P_active)

        trigger_flavor_effects(P_active, P_partner, E_active, E_partner)

        if E_active["HP"] <= 0:
            if E_partner["HP"] > 0:
                print(f"💫 {E_active['name']} falls — {E_partner['name']} tags in!")
                E_active, E_partner = E_partner, E_active
                trigger_flavor_effects(E_active)
                maybe_trigger_last_stand_theme()
            else:
                print(f"\n🏆 {P_active['name']} & {P_partner['name']} win!")
                break

        # === ENEMY TURN ===
        enemy_arts = merged_arts(E_active, enemy_duo_key, E_partner["HP"] > 0)
        E_active["echo_gauge"], E_active["buffs"] = run_enemy_turn(
            E_active, P_active, enemy_arts, E_active["echo_gauge"], E_active["buffs"]
        )
        clamp_hp(E_active); clamp_hp(P_active); clamp_gauge(E_active)

        trigger_flavor_effects(P_active, P_partner, E_active, E_partner)

        if P_active["HP"] <= 0:
            if P_partner["HP"] > 0:
                print(f"💫 {P_active['name']} falls — {P_partner['name']} tags in!")
                P_active, P_partner = P_partner, P_active
                trigger_flavor_effects(P_active)
                maybe_trigger_last_stand_theme()
            else:
                print(f"\n🏆 {E_active['name']} & {E_partner['name']} win!")
                break

        maybe_trigger_last_stand_theme()

        if theme_name and turn == 10 and not triggered_theme:
            print(f"\n💥 SURGE: {theme_name.upper()} ruptures the battlefield!")
            pygame.mixer.music.set_volume(0.6)
            input("🌫️ The prism resonates… Press Enter.")
            surge = apply_surge_effect(theme_name, P_active["buffs"])
            triggered_theme = theme_name

            if "heal" in surge:
                amt = surge["heal"]
                P_active["HP"] = min(P_active["max_HP"], P_active["HP"] + amt)
                print(f"💖 Heals {amt} HP → {P_active['HP']}/{P_active['max_HP']}")
            if "echo_boost" in surge:
                boost = surge["echo_boost"]
                P_active["echo_gauge"] = min(MAX_GAUGE, P_active["echo_gauge"] + boost)
                print(f"🎶 Echo Gauge +{boost} → {P_active['echo_gauge']}/{MAX_GAUGE}")

        turn += 1

    player_team_alive = (P_active["HP"] > 0) or (P_partner["HP"] > 0)
    result = {
        "player_team":            f"{p1_name} & {p2_name}",
        "enemy_team":             f"{e1_name} & {e2_name}",
        "stage_id":               "DuoBattle",
        "turn_count":             turn - 1,
        "triggered_theme":        triggered_theme,
        "curated_theme_start":    curated_theme_start,
        "curated_theme_last_stand": curated_theme_last_stand,
        "player_won":             player_team_alive,
        "timestamp":              datetime.now().isoformat()
    }

    print(f"\n🏆 Result: {'Victory' if player_team_alive else 'Defeat'} in {turn - 1} turns")
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

    # 🧠 Unified theme resolution + play (replaces manual preview)
    theme_category, theme_title = resolve_pair_theme(p_name, e_name)
    #play_duel_theme_and_dialogue(p_name, e_name)

    # 🏷️ Get titles
    e_title = e_data.get("title") or "Unknown"
    if e_title == "Unknown" and e_house in houses:
        for name, title in houses[e_house]:
            if name == e_name:
                e_title = title
                break

    # 🧾 Match Preview
    print("\n⚔️ Duel Preview:")
    print(f"🌟 {p_name} — {p_title} [Domus {p_house}]")
    print("🆚")
    print(f"🌑 {e_name} — {e_title} [Domus {e_house}]")
    print(f"🎭 Theme: {theme_category or '—'}")
    
    # === Start Duel ===
    result = start_solo_duel(
        p_house=p_house,
        p_name=p_name,
        p_bond=p_bond,
        e_house=e_house,
        e_name=e_name,
        e_bond=e_bond,
        theme_name=theme_category  # for turn-10 surge
    )

    # Optional: Attach curated theme to result if it wasn’t logged internally
    result["curated_theme"] = (
        {"category": theme_category, "title": theme_title}
        if theme_title else None
    )

    # === Outcome & Persistence ===
    print(f"\n🏆 {'Victory' if result['player_won'] else 'Defeat'} in {result['turn_count']} turns!")


if __name__ == "__main__":
    try:
        themed_match()
    except Exception as e:
        print(f"❌ Duel interrupted: {e}")
    input("🌒 Prism fades. Press Enter to close the duel...")
