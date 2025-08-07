# champions.py

from echo_effects import echo_arts

class Champion:
    def __init__(self, name, title, house, index, solo_echoes, duo_echoes):
        self.name        = name
        self.title       = title
        self.house       = house
        self.index       = index
        self.hp          = 100
        self.echo_gauge  = 0
        self.statuses    = {}    # e.g. {"stun": 1, "burn": 2}
        self.buffs       = {}    # e.g. {"ATK": (2,2), "DEF": (3,3)}
        self.solo_echoes = solo_echoes
        self.duo_echoes  = duo_echoes

    def is_stunned(self):
        return self.statuses.get("stun", 0) > 0

    def tick(self):
        # decrement statuses and buffs
        for s in list(self.statuses):
            self.statuses[s] -= 1
            if self.statuses[s] <= 0:
                del self.statuses[s]
        for stat in list(self.buffs):
            amt, dur = self.buffs[stat]
            dur -= 1
            if dur <= 0:
                del self.buffs[stat]
            else:
                self.buffs[stat] = (amt, dur)

    def apply_effect(self, effect):
        t = effect["type"]
        if t == "damage":
            dmg = effect["power"]
            # simple: no DEF mitigation
            self.hp -= dmg
            print(f"→ {self.name} takes {dmg} damage (HP={self.hp})")
        elif t == "heal":
            amt = effect["amount"]
            self.hp += amt
            print(f"→ {self.name} heals {amt} (HP={self.hp})")
        elif t == "buff":
            stat, amt, dur = effect["stat"], effect["amount"], effect["duration"]
            self.buffs[stat] = (amt, dur)
            print(f"→ {self.name} gains +{amt} {stat} for {dur} turns")
        elif t == "status":
            st, dur = effect["effect"], effect["duration"]
            self.statuses[st] = dur
            print(f"→ {self.name} is inflicted with {st} ({dur} turns)")

    def choose_echo(self):
        # list available (cost ≤ gauge)
        choices = []
        for name in self.solo_echoes + self.duo_echoes:
            # assume echo_arts is in global scope
            e = echo_arts[name]
            if e["cost"] <= self.echo_gauge:
                choices.append(name)
        # always allow “pass” to build gauge
        print(f"\n{self.name} (HP={self.hp}, Gauge={self.echo_gauge})")
        for i, n in enumerate(choices, 1):
            print(f"  {i}. {n} [cost {echo_arts[n]['cost']}]")
        print(f"  0. Pass (build +2 gauge)")
        pick = int(input("Choose Echo # → "))
        if pick == 0:
            self.echo_gauge += 2
            print(f"{self.name} builds gauge to {self.echo_gauge}")
            return None
        return choices[pick-1]

