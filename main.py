# Prism Waltz — main.py

import time
import random
from data import houses, solo_echoes, duo_indices
from combat import start_duel, start_duel_2v2

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
    h_choice = get_numeric_choice("\n> House #: ", 1, len(houses))
    house = list(houses.keys())[h_choice - 1]
    show_roster(house)
    c_choice = get_numeric_choice("\n> Champion #: ", 1, len(houses[house]))
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
    choice = get_numeric_choice("\n> Partner #: ", 1, len(partners))
    p_idx, echo = partners[choice - 1]
    p_name, p_title = houses[house][p_idx]
    print(f"\n🤝 Bond formed with {p_name} — {p_title}!")
    print(f"Unlocked Duo Echo: {echo}\n")
    time.sleep(0.5)
    return (p_idx, echo)

def show_status(house, champ_idx, bonded):
    name, title = houses[house][champ_idx]
    print(f"\nChampion: {name} — {title}")
    print("Solo Echo-Arts:", *solo_echoes[house])
    if bonded:
        p_idx, echo = bonded
        p_name, _ = houses[house][p_idx]
        print(f"Bonded Partner: {p_name}")
        print("Duo Echo:", echo)
    else:
        print("No bond formed. Use [2] to form one.")
    print()
    time.sleep(0.5)

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

def main_menu():
    show_title_screen()
    while True:
        print("""
Prism Waltz: Battle Menu
 [1] Solo Duel (1v1)
 [2] Duo Battle (2v2)
 [0] Exit
""")
        choice = get_numeric_choice("Select mode: ", 0, 2)
        if choice == 1:
            # Solo Duel Setup
            print("\n-- Player Setup --")
            p_house, p_idx = select_champion()
            # Manual bond selection for player
            bonded = form_bond(p_house, p_idx)
            if bonded:
                partner_idx, duo_echo = bonded
            else:
                partner_idx, duo_echo = None, None
            player_name = houses[p_house][p_idx][0]
            print("\n-- Enemy Setup --")
            # Exclude player, their bond partner, and their teammate from opponent pool
            exclude_slots = [(p_house, p_idx)]
            if partner_idx is not None:
                exclude_slots.append((p_house, partner_idx))
            # For duo mode, you could add teammate exclusion here
            all_enemy_slots = [
                (h, idx)
                for h, champs in houses.items()
                for idx in range(len(champs))
                if (h, idx) not in exclude_slots
            ]
            e_house, e_idx = random.choice(all_enemy_slots)
            enemy_name = houses[e_house][e_idx][0]
            # Randomly pick a bond for the enemy (only valid duos)
            possible_enemy_bonds = duo_indices.get(e_house, {}).get(e_idx)
            if possible_enemy_bonds:
                enemy_partner_idx, enemy_duo_echo = random.choice(possible_enemy_bonds)
                enemy_partner_name = houses[e_house][enemy_partner_idx][0]
                print(f"Enemy bond: {enemy_name} + {enemy_partner_name} (Echo: {enemy_duo_echo})")
            else:
                enemy_partner_idx, enemy_duo_echo = None, None
            print(f"\n⚔️  {player_name} ({p_house})  vs  {enemy_name} ({e_house})\n")
            time.sleep(0.5)
            start_duel(
                p_house, player_name, e_house, enemy_name,
                partner_idx, duo_echo,
                enemy_partner_idx, enemy_duo_echo
            )
            input("\nPress Enter to return to Main Menu…")
        elif choice == 2:
            # Duo Battle Setup
            print("\n-- Player Team Setup --")
            p1_house, p1_idx = select_champion()
            p1_name = houses[p1_house][p1_idx][0]
            # Try to pick a valid bond for player team
            possible_player_bonds = duo_indices.get(p1_house, {}).get(p1_idx)
            if possible_player_bonds:
                p2_idx, player_duo_echo = random.choice(possible_player_bonds)
                p2_name = houses[p1_house][p2_idx][0]
                print(f"Player bond: {p1_name} + {p2_name} (Echo: {player_duo_echo})")
                p2_house = p1_house
            else:
                # Fallback: pick any random champion not p1
                p2_house, p2_idx = select_random_opponent(p1_house, p1_idx)
                p2_name = houses[p2_house][p2_idx][0]
                player_duo_echo = None
            print("\n-- Enemy Team Setup --")
            # Exclude player, their teammate, and their bond partners from enemy pool
            exclude_slots = [(p1_house, p1_idx), (p2_house, p2_idx)]
            # Exclude player bond partners if any
            possible_player_bonds = duo_indices.get(p1_house, {}).get(p1_idx)
            if possible_player_bonds:
                for idx, _ in possible_player_bonds:
                    exclude_slots.append((p1_house, idx))
            possible_player_bonds2 = duo_indices.get(p2_house, {}).get(p2_idx)
            if possible_player_bonds2:
                for idx, _ in possible_player_bonds2:
                    exclude_slots.append((p2_house, idx))
            all_enemy_slots = [
                (h, idx)
                for h, champs in houses.items()
                for idx in range(len(champs))
                if (h, idx) not in exclude_slots
            ]
            e1_house, e1_idx = random.choice(all_enemy_slots)
            e1_name = houses[e1_house][e1_idx][0]
            # Try to pick a valid bond for enemy team
            possible_bonds = duo_indices.get(e1_house, {}).get(e1_idx)
            # Exclude e1's own bond partners if they overlap with player team
            enemy_exclude = exclude_slots + [(e1_house, e1_idx)]
            valid_enemy_bonds = [b for b in possible_bonds or [] if (e1_house, b[0]) not in enemy_exclude]
            if valid_enemy_bonds:
                e2_idx, enemy_duo_echo = random.choice(valid_enemy_bonds)
                e2_name = houses[e1_house][e2_idx][0]
                print(f"Enemy bond: {e1_name} + {e2_name} (Echo: {enemy_duo_echo})")
                e2_house = e1_house
            else:
                # Fallback: pick any random champion not e1 or excluded
                all_enemy2_slots = [
                    (h, idx)
                    for h, champs in houses.items()
                    for idx in range(len(champs))
                    if (h, idx) not in enemy_exclude
                ]
                e2_house, e2_idx = random.choice(all_enemy2_slots)
                e2_name = houses[e2_house][e2_idx][0]
                enemy_duo_echo = None
            start_duel_2v2(
                p1_house, p1_name, p2_house, p2_name,
                e1_house, e1_name, e2_house, e2_name,
                p1_idx, p2_idx, e1_idx, e2_idx,
                player_duo_echo, enemy_duo_echo
            )
            input("\nPress Enter to return to Main Menu…")
        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main_menu()
