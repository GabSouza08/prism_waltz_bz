import random
import time
from data import ChampionStats, solo_echoes, duo_indices, houses
from echo_effects import echo_arts
from fade_effects import low_hp_fade, duo_echo_narration, turn_summary_fade

MAX_GAUGE = 10

class Fighter:
    def __init__(self, house, name):
        base = ChampionStats[house][name]
        self.house     = house
        self.name      = name
        self.HP        = base["HP"]
        self.ATK       = base["ATK"]
        self.DEF       = base["DEF"]
        self.SPD       = base["SPD"]
        self.affinity  = base["Affinity"]
        self.echo_gauge = 0
        self.buffs      = {}
        self.status     = {}
        self.partner    = None
        self.duo_echo   = None

    def is_alive(self):
        return self.HP > 0

    def clamp_echo_gauge(self):
        self.echo_gauge = min(self.echo_gauge, MAX_GAUGE)

    def apply_buffs_and_status(self):
        self.status = {k: v - 1 for k, v in self.status.items() if v > 1}
        self.buffs  = {k: (amt, dur - 1) for k, (amt, dur) in self.buffs.items() if dur > 1}

    def basic_attack(self, target):
        atk_mod = self.ATK + self.buffs.get("ATK", (0, 0))[0]
        def_mod = target.DEF + target.buffs.get("DEF", (0, 0))[0]
        damage = max(1, atk_mod - def_mod)
        target.HP -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage! [HP → {target.HP}]")
        low_hp_fade(target)
        self.clamp_echo_gauge()

    def can_use_echo(self, art_name):
        return art_name in echo_arts and self.echo_gauge >= echo_arts[art_name]["cost"]

    def use_echo(self, art_name, target):
        art = echo_arts.get(art_name)
        if not art:
            print(f"{self.name} tried an unknown Echo-Art.")
            return
        if self.echo_gauge < art["cost"]:
            print(f"⚠️ Not enough Echo Gauge for {art_name}.")
            return
        self.echo_gauge -= art["cost"]
        self.clamp_echo_gauge()
        print(f"\n✨ {self.name} activates {art_name}!")
        if art["type"] == "damage":
            power = art["power"]
            dmg = power + self.ATK + self.buffs.get("ATK", (0, 0))[0]
            target.HP -= dmg
            print(f"→ Deals {dmg} damage! {target.name} HP → {target.HP}")
            low_hp_fade(target)
        elif art["type"] == "heal":
            amt = art["amount"]
            self.HP += amt
            print(f"→ Heals for {amt}. HP → {self.HP}")
        elif art["type"] == "buff":
            stat, amt, dur = art["stat"], art["amount"], art["duration"]
            self.buffs[stat] = (amt, dur)
            print(f"→ Buffs +{amt} {stat} for {dur} turns")
        elif art["type"] == "status":
            effect, dur = art["effect"], art["duration"]
            target.status[effect] = dur
            print(f"→ Inflicts {effect} on {target.name} ({dur} turns)")

# --- Utility functions ---
def get_champion_index(house, name):
    if house not in ChampionStats:
        return None
    names = list(ChampionStats[house].keys())
    try:
        return names.index(name)
    except ValueError:
        return None

def auto_assign_duo_echo(f1, f2):
    if f1.house != f2.house:
        return False
    i1 = get_champion_index(f1.house, f1.name)
    i2 = get_champion_index(f2.house, f2.name)
    for idx, echo_name in duo_indices.get(f1.house, {}).get(i1, []):
        if idx == i2:
            f1.partner = f2
            f2.partner = f1
            f1.duo_echo = echo_name
            f2.duo_echo = echo_name
            print(f"💫 Bonded: {f1.name} + {f2.name} → Echo: '{echo_name}'")
            return True
    for idx, echo_name in duo_indices.get(f2.house, {}).get(i2, []):
        if idx == i1:
            f1.partner = f2
            f2.partner = f1
            f1.duo_echo = echo_name
            f2.duo_echo = echo_name
            print(f"💫 Bonded: {f1.name} + {f2.name} → Echo: '{echo_name}'")
            return True
    return False

def echo_bar(gauge):
    filled = "█" * gauge
    empty = "·" * (MAX_GAUGE - gauge)
    return f"[{filled}{empty}] {gauge}/{MAX_GAUGE}"

def display_hud(f):
    bond = f"Partner: {f.partner.name}" if f.partner else "No partner"
    duo = f"Duo Echo: {f.duo_echo}" if f.duo_echo else "No duo echo"
    print(f"""
╭━━ {f.name} ━━╮
│ HP:    {f.HP}      Echo Gauge: {echo_bar(f.echo_gauge)}
│ ATK:   {f.ATK}     DEF: {f.DEF}     SPD: {f.SPD}
│ Buffs:  {', '.join(f.buffs.keys()) if f.buffs else 'None'}
│ Status: {', '.join(f.status.keys()) if f.status else 'None'}
│ {bond}
│ {duo}
╰━━━━━━━━━━━━━╯
""")

# --- 1v1 Duel ---
def start_duel(p_house, p_name, e_house, e_name,
               partner_idx=None, duo_echo=None,
               enemy_partner_idx=None, enemy_duo_echo=None):
    p = Fighter(p_house, p_name)
    e = Fighter(e_house, e_name)
    if partner_idx is not None and duo_echo is not None:
        partner_name = houses[p_house][partner_idx][0]
        p.partner = Fighter(p_house, partner_name)
        p.duo_echo = duo_echo
    if enemy_partner_idx is not None and enemy_duo_echo is not None:
        enemy_partner_name = houses[e_house][enemy_partner_idx][0]
        e.partner = Fighter(e_house, enemy_partner_name)
        e.duo_echo = enemy_duo_echo
    fighters = [p, e]
    turn = 1
    for f in fighters:
        display_hud(f)
    while p.is_alive() and e.is_alive():
        print(f"\n–– Turn {turn} ––")
        for f in fighters:
            if not p.is_alive() or not e.is_alive():
                break
            display_hud(f)
            f.apply_buffs_and_status()
            if "stun" in f.status:
                print(f"{f.name} is stunned and skips their turn.")
                continue
            if f is p:
                print(f"\n{f.name} [Echo Gauge: {f.echo_gauge}]")
                choice = input("Action? [1] Attack [2] Solo Echo [3] Duo Echo [0] Pass → ")
                if choice == "1":
                    f.basic_attack(e)
                elif choice == "2":
                    player_echoes = solo_echoes[p.house]
                    usable = [name for name in player_echoes if f.can_use_echo(name)]
                    usable = [name for name in usable if echo_arts[name]["target"] == "enemy"]
                    if not usable:
                        print("⚠️ No usable Solo Echo-Arts.")
                    else:
                        for i, name in enumerate(usable, 1):
                            print(f"  [{i}] {name} (Cost: {echo_arts[name]['cost']})")
                        idx = int(input("Choose Echo #: ")) - 1
                        if 0 <= idx < len(usable):
                            f.use_echo(usable[idx], e)
                        else:
                            print("Invalid selection.")
                elif choice == "3":
                    if f.duo_echo and f.partner:
                        echo_name = f.duo_echo
                        art = echo_arts.get(echo_name)
                        if not art:
                            print(f"⚠️ Echo-Art '{echo_name}' not found.")
                        elif f.echo_gauge < art["cost"]:
                            print(f"⚠️ Not enough Echo Gauge.")
                        elif not f.partner.is_alive():
                            print(f"⚠️ Partner {f.partner.name} can’t fight.")
                        else:
                            duo_echo_narration(f, echo_name)
                            f.use_echo(echo_name, e)
                    else:
                        print("⚠️ You haven’t formed a bond yet.")
                elif choice == "0":
                    f.echo_gauge = min(f.echo_gauge + 2, MAX_GAUGE)
                    print(f"{f.name} gathers focus… Echo Gauge → {f.echo_gauge}")
                else:
                    print("Invalid action. Turn skipped.")
            else:
                if f.echo_gauge >= 5 and random.random() > 0.3:
                    f.basic_attack(p)
                else:
                    f.echo_gauge = min(f.echo_gauge + 2, MAX_GAUGE)
                    print(f"{f.name} channels energy… Echo Gauge → {f.echo_gauge}")
            time.sleep(0.3)
        turn_summary_fade()
        turn += 1
    winner = p if p.is_alive() else e
    print(f"\n🏆 {winner.name} wins the duel!")

# --- 2v2 Duel ---
def start_duel_2v2(p1_house, p1_name, p2_house, p2_name,
                   e1_house, e1_name, e2_house, e2_name,
                   p1_idx=None, p2_idx=None, e1_idx=None, e2_idx=None,
                   player_duo_echo=None, enemy_duo_echo=None):
    p1 = Fighter(p1_house, p1_name)
    p2 = Fighter(p2_house, p2_name)
    e1 = Fighter(e1_house, e1_name)
    e2 = Fighter(e2_house, e2_name)
    if p1_idx is not None and player_duo_echo is not None:
        partner_name = houses[p1_house][p2_idx][0]
        p1.partner = Fighter(p1_house, partner_name)
        p1.duo_echo = player_duo_echo
    if e1_idx is not None and enemy_duo_echo is not None:
        partner_name = houses[e1_house][e2_idx][0]
        e1.partner = Fighter(e1_house, partner_name)
        e1.duo_echo = enemy_duo_echo
    fighters = sorted([p1, p2, e1, e2], key=lambda f: f.SPD, reverse=True)
    turn = 1
    for f in fighters:
        display_hud(f)
    while any(f.is_alive() for f in [p1, p2]) and any(f.is_alive() for f in [e1, e2]):
        print(f"\n–– Turn {turn} ––")
        for f in fighters:
            if not f.is_alive():
                continue
            display_hud(f)
            f.apply_buffs_and_status()
            if "stun" in f.status:
                print(f"{f.name} is stunned and skips their turn.")
                continue
            if f in [p1, p2]:
                enemies = [e for e in [e1, e2] if e.is_alive()]
                if not enemies:
                    continue
                print(f"\n{f.name} [Echo Gauge: {f.echo_gauge}]")
                print("Choose target:")
                for i, enemy in enumerate(enemies, 1):
                    print(f"  [{i}] {enemy.name}")
                t_idx = int(input("Target #: ")) - 1
                if 0 <= t_idx < len(enemies):
                    target = enemies[t_idx]
                else:
                    print("Invalid target. Skipping.")
                    continue
                choice = input("Action? [1] Attack [2] Solo Echo [3] Duo Echo [0] Pass → ")
                if choice == "1":
                    f.basic_attack(target)
                elif choice == "2":
                    player_echoes = solo_echoes[f.house]
                    usable = [name for name in player_echoes if f.can_use_echo(name)]
                    usable = [name for name in usable if echo_arts[name]["target"] == "enemy"]
                    if not usable:
                        print("⚠️ No usable Solo Echo-Arts.")
                    else:
                        for i, name in enumerate(usable, 1):
                            print(f"  [{i}] {name} (Cost: {echo_arts[name]['cost']})")
                        idx = int(input("Choose Echo #: ")) - 1
                        if 0 <= idx < len(usable):
                            f.use_echo(usable[idx], target)
                        else:
                            print("Invalid selection.")
                elif choice == "3":
                    if f.duo_echo and f.partner:
                        echo_name = f.duo_echo
                        art = echo_arts.get(echo_name)
                        if not art:
                            print(f"⚠️ Echo-Art '{echo_name}' not found.")
                        elif f.echo_gauge < art["cost"]:
                            print(f"⚠️ Not enough Echo Gauge.")
                        elif not f.partner.is_alive():
                            print(f"⚠️ Partner {f.partner.name} can’t fight.")
                        else:
                            duo_echo_narration(f, echo_name)
                            f.use_echo(echo_name, target)
                    else:
                        print("⚠️ You haven’t formed a bond yet.")
                elif choice == "0":
                    f.echo_gauge = min(f.echo_gauge + 2, MAX_GAUGE)
                    f.clamp_echo_gauge()
                    print(f"{f.name} gathers focus… Echo Gauge → {f.echo_gauge}")
                else:
                    print("Invalid action. Turn skipped.")
            else:
                allies = [p for p in [p1, p2] if p.is_alive()]
                if not allies:
                    continue
                target = random.choice(allies)
                if f.echo_gauge >= 5 and random.random() > 0.3:
                    f.basic_attack(target)
                else:
                    f.echo_gauge = min(f.echo_gauge + 2, MAX_GAUGE)
                    f.clamp_echo_gauge()
                    print(f"{f.name} channels energy… Echo Gauge → {f.echo_gauge}")
            time.sleep(0.3)
        turn_summary_fade()
        turn += 1
    winners = [f for f in [p1, p2] if f.is_alive()]
    if winners:
        print("\n🏆 Players win!")
    else:
        print("\n🏆 Enemies win!")

# --- Main Menu ---
def main_menu():
    print("\nPrism Waltz: Battle Menu")
    print("[1] Solo Duel (1v1)")
    print("[2] Duo Battle (2v2)")
    print("[0] Exit")
    choice = input("Select mode: ")
    if choice == "1":
        print("-- Solo Duel Setup --")
        p_house = input("Player House: ")
        p_name = input("Player Champion: ")
        e_house = input("Enemy House: ")
        e_name = input("Enemy Champion: ")
        # If you want to support bonds, also prompt for partner and duo_echo
        partner_idx = None
        duo_echo = None
        # Optionally: prompt for bond info here
        start_duel(p_house, p_name, e_house, e_name, partner_idx, duo_echo)
    elif choice == "2":
        print("-- Duo Battle Setup --")
        p1_house = input("Player 1 House: ")
        p1_name = input("Player 1 Champion: ")
        p2_house = input("Player 2 House: ")
        p2_name = input("Player 2 Champion: ")
        e1_house = input("Enemy 1 House: ")
        e1_name = input("Enemy 1 Champion: ")
        e2_house = input("Enemy 2 House: ")
        e2_name = input("Enemy 2 Champion: ")
        start_duel_2v2(p1_house, p1_name, p2_house, p2_name, e1_house, e1_name, e2_house, e2_name)
    elif choice == "0":
        print("Goodbye!")
        return
    else:
        print("Invalid selection.")
        main_menu()

# Uncomment below to run menu on script start
# if __name__ == "__main__":
#     main_menu()
