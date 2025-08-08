# main.py

import time
import random
from data import houses, solo_echoes, duo_indices
from echo_save import save_duel, load_all_duels
from combat import start_solo_duel, start_duo_battle
from theme_registry import theme_map



def get_numeric_choice(prompt, min_c, max_c):
    while True:
        try:
            n = int(input(prompt).strip())
            if min_c <= n <= max_c:
                return n
        except ValueError:
            pass
        print(f"Enter a number between {min_c} and {max_c}.")


def show_title_screen():
    title = r"""
░█████████  ░██       ░██ ░██████████  ░██████  
░██     ░██ ░██       ░██     ░██     ░██   ░██ 
░██     ░██ ░██  ░██  ░██     ░██    ░██        
░█████████  ░██ ░████ ░██     ░██    ░██        
░██         ░██░██ ░██░██     ░██    ░██        
░██         ░████   ░████     ░██     ░██   ░██ 
░██         ░███     ░███     ░██      ░██████                                    
        🌒 Prism Waltz — Terminal Chronicle 🌒
"""
    print(title)
    input("Press Enter to begin your journey…")


def show_roster(house):
    print(f"\nDomus {house} Roster:")
    for idx, (name, title) in enumerate(houses[house], 1):
        print(f"  [{idx}] {name} — {title}")


def select_champion():
    print("\nChoose your Domus:")
    for i, h in enumerate(houses.keys(), 1):
        print(f"  [{i}] {h}")
    h_choice = get_numeric_choice("> House #: ", 1, len(houses))
    house = list(houses.keys())[h_choice - 1]
    show_roster(house)

    c_choice = get_numeric_choice("> Champion #: ", 1, len(houses[house]))
    champ_idx = c_choice - 1
    name, title = houses[house][champ_idx]

    print(f"\n✨ You are {name} — {title}.")
    print("   Solo Echo-Arts:", *solo_echoes[house])
    print("   Form a duo bond to unlock a special Duo Echo.\n")
    time.sleep(0.5)

    return house, champ_idx


def form_bond(house, champ_idx):
    partners = duo_indices.get(house, {}).get(champ_idx)
    if not partners:
        print("\nNo duo bonds available for this champion.")
        return None

    print("\nSelect a partner to bond with:")
    for i, (p_idx, echo) in enumerate(partners, 1):
        p_name, p_title = houses[house][p_idx]
        print(f"  [{i}] {p_name} — {p_title} (Echo: {echo})")
    choice = get_numeric_choice("> Partner #: ", 1, len(partners))
    p_idx, echo = partners[choice - 1]
    p_name, _ = houses[house][p_idx]

    print(f"\n🤝 Bond formed with {p_name}!")
    print(f"Unlocked Duo Echo: {echo}\n")
    time.sleep(0.5)

    return (p_idx, echo)


def select_random_opponent(player_house, player_idx):
    all_slots = [
        (h, idx)
        for h, champs in houses.items()
        for idx in range(len(champs))
        if not (h == player_house and idx == player_idx)
    ]
    ohouse, oidx = random.choice(all_slots)
    oname = houses[ohouse][oidx][0]
    print(f"\n🎲 Random Opponent: {oname} — {ohouse}")
    time.sleep(0.5)
    return ohouse, oidx

def solo_duel():
    print("\n-- Solo Duel Setup --")

    # Player selection
    p_house, p_idx = select_champion()
    p_name = houses[p_house][p_idx][0]  # ← assign name here
    p_bond = form_bond(p_house, p_idx)

    # Enemy selection
    e_house, e_idx = select_random_opponent(p_house, p_idx)
    e_name = houses[e_house][e_idx][0]  # ← assign name here
    e_bond = form_bond(e_house, e_idx)

    # 🎭 Find theme based on current matchup
    duel_key = (p_house, p_name, e_house, e_name)
    theme_name = theme_map.get(duel_key, None)

    # Run duel
    result = start_solo_duel(
        p_house, p_name, p_bond,
        e_house, e_name, e_bond,
        theme_name
    )

    # Save result
    save_duel({
        "mode":     "Solo",
        "player":   result.get("player_name"),
        "opponent": result.get("opponent_name"),
        "stage":    result.get("stage_id"),
        "turns":    result.get("turn_count"),
        "theme":    result.get("triggered_theme"),
        "outcome":  "Win" if result.get("player_won") else "Loss",
        "echo_tag": result.get("special_echo_tag"),
        "whisper":  result.get("system_whisper_text")
    })

    input("\nPress Enter to return to Main Menu…")




def duo_battle():
    print("\n-- Duo Battle Setup --")
    # Player team
    p1_house, p1_idx = select_champion()
    p1_name = houses[p1_house][p1_idx][0]
    p1_bond = form_bond(p1_house, p1_idx)

    if p1_bond:
        p2_idx, p1_echo = p1_bond
        p2_house = p1_house
        p2_name = houses[p2_house][p2_idx][0]
    else:
        p2_house, p2_idx = select_random_opponent(p1_house, p1_idx)
        p2_name = houses[p2_house][p2_idx][0]
        p1_echo = None

    # Enemy team
    e1_house, e1_idx = select_random_opponent(p1_house, p1_idx)
    e1_name = houses[e1_house][e1_idx][0]
    e1_bond = form_bond(e1_house, e1_idx)

    if e1_bond:
        e2_idx, e_echo = e1_bond
        e2_house = e1_house
        e2_name = houses[e2_house][e2_idx][0]
    else:
        e2_house, e2_idx = select_random_opponent(e1_house, e1_idx)
        e2_name = houses[e2_house][e2_idx][0]
        e_echo = None

    result = start_duo_battle(
        p1_house, p1_name, p2_house, p2_name, p1_idx, p2_idx, p1_echo,
        e1_house, e1_name, e2_house, e2_name, e1_idx, e2_idx, e_echo
    )
    save_duel({
        "mode":     "Duo",
        "player":   result.get("player_name"),
        "opponent": result.get("opponent_name"),
        "stage":    result.get("stage_id"),
        "turns":    result.get("turn_count"),
        "theme":    result.get("triggered_theme"),
        "outcome":  "Win" if result.get("player_won") else "Loss",
        "echo_tag": result.get("special_echo_tag"),
        "whisper":  result.get("system_whisper_text")
    })
    input("\nPress Enter to return to Main Menu…")

def view_saved_duels():
    print("\n-- Saved Duels --")
    all_duels = load_all_duels()
    if not all_duels:
        print("No saved duels found.")
        return

    # Display list
    for idx, duel in enumerate(all_duels, 1):
        mode = duel.get("mode", "Unknown")
        theme = duel.get("theme", "—")
        outcome = duel.get("outcome", "—")
        timestamp = duel.get("timestamp", "—")

        if mode == "Solo":
            player = duel.get("player", "???")
            opponent = duel.get("opponent", "???")
            print(f"  [{idx}] {player} vs {opponent} | Theme: {theme} | Outcome: {outcome}")

        elif mode == "Duo":
            team_1 = " + ".join(duel.get("team_1", ["???"]))
            team_2 = " + ".join(duel.get("team_2", ["???"]))
            echo = duel.get("echo_tag", "—")
            print(f"  [{idx}] {team_1} vs {team_2} | Echo: {echo} | Outcome: {outcome}")

        elif mode == "Grand Clash":
            player_team = " + ".join(duel.get("player_duo", ["???"]))
            enemies = duel.get("enemies", [])
            enemy_strs = [" + ".join(e.get("duo", ["???"])) for e in enemies]
            enemy_block = " | ".join(enemy_strs)
            print(f"  [{idx}] {player_team} vs {enemy_block} | Theme: {theme}")

        else:
            print(f"  [{idx}] Unknown mode — saved on {timestamp}")

    # Selection
    choice = get_numeric_choice(
        "\nSelect a duel to view details (or 0 to return): ", 0, len(all_duels)
    )
    if choice == 0:
        return

    duel = all_duels[choice - 1]
    mode = duel.get("mode", "Unknown")
    print(f"\n📜 Duel Details — Mode: {mode}")
    print(f"  Date: {duel.get('timestamp', '—')}")
    print(f"  Theme: {duel.get('theme', '—')}")
    print(f"  Outcome: {duel.get('outcome', '—')}")
    print(f"  Turns: {duel.get('turns', '—')}")
    echo = duel.get("echo_tag", None)
    if echo:
        print(f"  Echo Tag: {echo}")
    whisper = duel.get("whisper", None)
    if whisper:
        print(f"  Whisper: “{whisper}”")

    # Participants
    if mode == "Solo":
        print(f"  {duel.get('player', '???')} vs {duel.get('opponent', '???')}")
    elif mode == "Duo":
        print(f"  Team 1: {' + '.join(duel.get('team_1', ['???']))}")
        print(f"  Team 2: {' + '.join(duel.get('team_2', ['???']))}")
    elif mode == "Grand Clash":
        print(f"  Player Duo: {' + '.join(duel.get('player_duo', ['???']))}")
        print("  Enemies:")
        for team in duel.get("enemies", []):
            duo = " + ".join(team.get("duo", ["???"]))
            house = team.get("house", "—")
            echo = team.get("echo", "—")
            print(f"    - {duo} ({house}) Echo: {echo}")

    input("\nPress Enter to return to Saved Duels menu…")



def main_menu():
    show_title_screen()
    while True:
        print("""
Prism Waltz: Battle Menu
 [1] Solo Duel (1v1)
 [2] Duo Battle (2v2)
 [3] View Echoes/Saved Duels
 [0] Exit
""")
        choice = get_numeric_choice("Select mode: ", 0, 3)

        if choice == 0:
            print("Thank you for playing! Farewell, Echo Traveler.")
            break
        elif choice == 1:
            solo_duel()
        elif choice == 2:
            duo_battle()
        elif choice == 3:
            view_saved_duels()

if __name__ == "__main__":
    main_menu()
