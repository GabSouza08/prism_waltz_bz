# echo_effects.py

echo_arts = {}

# ————————————————————————
# Scarlet Solo Echo-Arts
# ————————————————————————
echo_arts.update({

    "Emberlit Vow": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 3,
        "cost":     5
    },
    "Radiant Shield": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 2,
        "cost":     5
    },
    "Flame's Embrace": {
        "type":     "heal",
        "target":   "self",
        "amount":   8,
        "cost":     5
    },
    "Aegis Requiem": {
        "type":     "damage",
        "target":   "enemy",
        "power":    6,
        "cost":     6,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "DEF",
            "amount":   2,
            "duration": 2
        }
    }

})

# ————————————————————————
# Scarlet Duo Echo-Arts (all 32 pairings)
# Each costs 8 Echo Gauge
# ————————————————————————
echo_arts.update({

    # Ana Clara (1) & Eduardo Carlos (0)
    "Aegis of Serenity’s Verse": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   4,
        "duration": 3,
        "cost":     8
    },
    # Ana Clara (1) & Carlos Antonio (2)
    "Serene Flame Accord": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "ATK",
            "amount":   2,
            "duration": 2
        }
    },
    # Ana Clara (1) & Davi Luiz (6)
    "Rampart’s Serene Vow": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 4,
        "cost":     8
    },
    # Ana Clara (1) & Jefferson Lucas (8)
    "Serene Sunwave Vanguard": {
        "type":     "heal",
        "target":   "self",
        "amount":   10,
        "cost":     8
    },

    # Sara Regina (3) & Carlos Antonio (2)
    "Resolute Flame Guardian": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    },
    # Sara Regina (3) & Davi Luiz (6)
    "Rampart’s Flame Vow": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 3,
        "cost":     8
    },
    # Sara Regina (3) & Matthews Guedes (10)
    "Resolute Dawn Warden": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },
    # Sara Regina (3) & Rodrigo Bezerra (14)
    "Resolute Ironflame": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "ATK",
            "amount":   3,
            "duration": 2
        }
    },

    # Sabrina Silva (5) & João Vitor (4)
    "Blazing Crown Bulwark": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   4,
        "duration": 3,
        "cost":     8
    },
    # Sabrina Silva (5) & Jefferson Lucas (8)
    "Crowned Sunwave Vanguard": {
        "type":     "damage",
        "target":   "enemy",
        "power":    13,
        "cost":     8
    },
    # Sabrina Silva (5) & Matthews Guedes (10)
    "Blazing Dawn Warden": {
        "type":     "heal",
        "target":   "self",
        "amount":   12,
        "cost":     8
    },
    # Sabrina Silva (5) & Rodrigo Bezerra (14)
    "Iron-Dawn Counter": {
        "type":     "damage",
        "target":   "enemy",
        "power":    10,
        "cost":     8,
        "bonus": {
            "type":     "status",
            "target":   "enemy",
            "effect":   "burn",
            "duration": 2
        }
    },

    # Maria Clara (7) & Eduardo Carlos (0)
    "Dawnlit Aegis Covenant": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 4,
        "cost":     8
    },
    # Maria Clara (7) & João Vitor (4)
    "Dawnlit Crown Bulwark": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },
    # Maria Clara (7) & Davi Luiz (6)
    "Emissary of the Rampart’s Dawn": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    # Maria Clara (7) & Rodrigo Bezerra (14)
    "Iron-Dawn Counterpoint": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "burn",
        "duration": 2,
        "cost":     8
    },

    # Maria Cecília (9) & Carlos Antonio (2)
    "Rose-Guard Alliance": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    # Maria Cecília (9) & Jefferson Lucas (8)
    "Rosewing Vanguard": {
        "type":     "damage",
        "target":   "enemy",
        "power":    13,
        "cost":     8
    },
    # Maria Cecília (9) & Rodrigo Bezerra (14)
    "Rose-Iron Flare": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "DEF",
            "amount":   2,
            "duration": 2
        }
    },
    # Maria Cecília (9) & João Vitor (4)
    "Rosecrown Bulwark": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 3,
        "cost":     8
    },

    # Maria Luisa (11) & Eduardo Carlos (0)
    "Oracle-Aegis Harmony": {
        "type":     "heal",
        "target":   "self",
        "amount":   10,
        "cost":     8
    },
    # Maria Luisa (11) & João Vitor (4)
    "Oracle-Crown Hymn": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 4,
        "cost":     8
    },
    # Maria Luisa (11) & Jefferson Lucas (8)
    "Oracle Vanguard": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    },
    # Maria Luisa (11) & Matthews Guedes (10)
    "Oracle of the Ramparted Dawn": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },

    # Elen Nayara (13) & Eduardo Carlos (0)
    "Mistbound Aegis": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   4,
        "duration": 3,
        "cost":     8
    },
    # Elen Nayara (13) & João Vitor (4)
    "Mistlit Crown Bulwark": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    # Elen Nayara (13) & Davi Luiz (6)
    "Mistlit Rampart": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },
    # Elen Nayara (13) & Heleno Gomes (12)
    "Mistlit Bastion": {
        "type":     "damage",
        "target":   "enemy",
        "power":    10,
        "cost":     8,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "DEF",
            "amount":   2,
            "duration": 2
        }
    },

    # Esthella Angelina (15) & Carlos Antonio (2)
    "Nocturne Flame Counter": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "burn",
        "duration": 3,
        "cost":     8
    },
    # Esthella Angelina (15) & Matthews Guedes (10)
    "Nocturnal Dawn Warden": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 4,
        "cost":     8
    },
    # Esthella Angelina (15) & Heleno Gomes (12)
    "Nocturnal Bastion": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    },
    # Esthella Angelina (15) & Rodrigo Bezerra (14)
    "Ironlight Counterpoint": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "ATK",
            "amount":   2,
            "duration": 2
        }
    }

})

# ————————————————————————
# Alizarin Solo Echo-Arts
# ————————————————————————
echo_arts.update({

    "Solar Pulse": {
        "type":     "damage",
        "target":   "enemy",
        "power":    10,
        "cost":     5
    },
    "Crimson Burst": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     6
    },
    "Dawn's Edge": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     5
    },
    "Ashen Echo": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "burn",
        "duration": 2,
        "cost":     5
    }

})

# ————————————————————————
# Alizarin Duo Echo‐Arts
# ————————————————————————
echo_arts.update({

    # Andrielly Luiz (1) duos
    "Echo of the Radiant Spear": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Herald of Solar Whispers": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Sentinel of Solar Whispers": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Crest of Solar Whispers": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },

    # Bruna Adrielly (3) duos
    "Herald of the Ashen Dawn": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    },
    "Crusader of the Ember Tide": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "ATK",
            "amount":   2,
            "duration": 2
        }
    },
    "Ashen Rhyme Crusader": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Crusader of the Charcoal Beacon": {
        "type":     "damage",
        "target":   "enemy",
        "power":    10,
        "cost":     8,
        "bonus": {
            "type":     "status",
            "target":   "enemy",
            "effect":   "burn",
            "duration": 2
        }
    },

    # Damylle Kemillly (5) duos
    "Sentinel of the Ember Tide": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   4,
        "duration": 2,
        "cost":     8
    },
    "Crested Ember Chant": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   3,
        "duration": 3,
        "cost":     8
    },
    "Beacon of the Ember-Tide": {
        "type":     "damage",
        "target":   "enemy",
        "power":    13,
        "cost":     8
    },
    "Ember-Tide Shield": {
        "type":     "heal",
        "target":   "self",
        "amount":   12,
        "cost":     8
    },

    # Rayelle Marinho (7) duos
    "Crested Ember Rhyme": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Charcoal-Faced Virtuoso": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "burn",
        "duration": 2,
        "cost":     8
    },
    "Photon-Faced Virtuoso": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 2,
        "cost":     8
    },
    "Virtuoso of Solar Waves": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    },

    # Marilia Oliveira (9) duos
    "Charcoal Pulse Beacon": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },
    "Photon-Pulse Shieldbearer": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Seeker of the Pulse Wave": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Oracle of the Pulse Star": {
        "type":     "heal",
        "target":   "self",
        "amount":   10,
        "cost":     8
    },

    # Evellyn Kauany (11) duos
    "Photon-Ray Shieldbearer": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   4,
        "duration": 3,
        "cost":     8
    },
    "Seeker of the Photon Wave": {
        "type":     "damage",
        "target":   "enemy",
        "power":    13,
        "cost":     8
    },
    "Shieldmaiden of the Morningstar": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Radiant Shield Maiden": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },

    # Wellen Adelaide (13) duos
    "Seeker of the Solar Wave": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    },
    "Morning Wave Bard": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Waveborn Radiant Spear": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "ATK",
            "amount":   2,
            "duration": 2
        }
    },
    "Waveborn Dawn Herald": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },

    # Maria Jullya (15) duos
    "Oracle of the Morningstar": {
        "type":     "heal",
        "target":   "self",
        "amount":   12,
        "cost":     8
    },
    "Spear of the Solar Star": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    },
    "Herald of the Solar Star": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Sentinel of the Solar Star": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 3,
        "cost":     8
    }

})

# ————————————————————————
# Violet Solo Echo-Arts
# ————————————————————————
echo_arts.update({
    "Velvet Waltz": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     5
    },
    "Silent Bloom": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 3,
        "cost":     5
    },
    "Gossamer Veil": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 2,
        "cost":     5
    },
    "Moon's Respite": {
        "type":     "heal",
        "target":   "self",
        "amount":   8,
        "cost":     5
    }
})

# ————————————————————————
# Violet Duo Echo-Arts (32 pairings)
# ————————————————————————
echo_arts.update({

    # Evellyn Oliveira (1) duos
    "Shield of the Twilight Gate": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   4,
        "duration": 3,
        "cost":     8
    },
    "Shield of Moonblessings": {
        "type":     "heal",
        "target":   "self",
        "amount":   10,
        "cost":     8
    },
    "Shield of the Bronze Crescent": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 4,
        "cost":     8
    },
    "Shield of the Celestial Path": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },

    # Bianca Flora (3) duos
    "Moonpetal Sentinel": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 3,
        "cost":     8
    },
    "Petal-Crescent Sentinel": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   2,
        "duration": 4,
        "cost":     8
    },
    "Petal Path Herald": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },
    "Petal Nightshield Echo": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },

    # Maria Yasmim (5) duos
    "Whisperer of the Blooming Crescent": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Whisperer of the Celestial Bloom": {
        "type":     "heal",
        "target":   "self",
        "amount":   10,
        "cost":     8
    },
    "Nightbloom Echo": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },
    "Wanderer of the Bloomheart": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },

    # Ana Victoria (7) duos
    "Herald of Fused Moon Paths": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Nightshield of Moon Resolve": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },
    "Wanderer of the Moon-Fused Resolve": {
        "type":     "heal",
        "target":   "self",
        "amount":   10,
        "cost":     8
    },
    "Seeker of Moon-Fused Fates": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },

    # Emilly Alves (9) duos
    "Echo of Velvet Reflection": {
        "type":     "damage",
        "target":   "enemy",
        "power":    10,
        "cost":     8,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "DEF",
            "amount":   2,
            "duration": 2
        }
    },
    "Wanderer of the Velvet Pulse": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Seeker of the Velvet Fates": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Herald of Starlit Reflection": {
        "type":     "heal",
        "target":   "self",
        "amount":   8,
        "cost":     8
    },

    # Samantha Martinez (11) duos
    "Waltz of the Moonlit Resolve": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Seeker of the Velvet Waltz": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },
    "Herald of the Velvet Waltz": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Gate of the Velvet Waltz": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },

    # Mirelle Freitas (13) duos
    "Seeker of Dreamtide Fates": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },
    "Starlight of the Dreamtide": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Gate of the Dreamtide": {
        "type":     "heal",
        "target":   "self",
        "amount":   10,
        "cost":     8
    },
    "Oracle of Dreamtide Blessings": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },

    # Vitoria Karoline (15) duos
    "Herald of Moonlit Champion": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 4,
        "cost":     8
    },
    "Gate of the Moonlit Will": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 3,
        "cost":     8
    },
    "Oracle of Moonlit Will": {
        "type":     "heal",
        "target":   "self",
        "amount":   10,
        "cost":     8
    },
    "Crescent Will Champion": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    }

})

# ————————————————————————
# Purpur Solo Echo-Arts
# ————————————————————————
echo_arts.update({

    "Dusk Trick": {
        "type":     "damage",
        "target":   "enemy",
        "power":    8,
        "cost":     5
    },
    "Shadowstep": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     5
    },
    "Illusory Dance": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 2,
        "cost":     5
    },
    "Twilight Veil": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     5
    }

})

# ————————————————————————
# Purpur Duo Echo-Arts (32 pairings)
# ————————————————————————
echo_arts.update({

    # Ketillyn Irlly (1) duos
    "Moonrise Fury Trick": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },
    "Shadow-Dusk Trick": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 2,
        "cost":     8
    },
    "Ciphered Dusk Trick": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Twilight-Dusk Trick": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },

    # Bruna Evelyn (3) duos
    "Silken Shadow Blade": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    },
    "Howl of the Silken Moon": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },
    "Duskbringer of Dusk": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "ATK",
            "amount":   2,
            "duration": 2
        }
    },
    "Silken Sovereign of the Moon": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 3,
        "cost":     8
    },

    # Mariana Pontes (5) duos
    "Duskbringer of Mistcall": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },
    "Tidecall Mist Sovereign": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 3,
        "cost":     8
    },
    "Shadow-Mist Wall": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Cipher of Mistcall": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },

    # Isadora Andrade (7) duos
    "Mirrorblade Howl": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },
    "Mirror Fury of Moonrise": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    },
    "Mirrorflame Sovereign": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Twilight Mirror Song": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },

    # Karoline Cassiano (9) duos
    "Sovereign Moonflare": {
        "type":     "damage",
        "target":   "enemy",
        "power":    13,
        "cost":     8
    },
    "Midnight Moonflare": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 2,
        "cost":     8
    },
    "Duskbringer Moonflare": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },
    "Moonrise Crown of Flares": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },

    # Emilly Nayara (11) duos
    "Howl of the Nightbloom Citadel": {
        "type":     "damage",
        "target":   "enemy",
        "power":    14,
        "cost":     8
    },
    "Harbinger of the Nightbloom Song": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },
    "Moonrise Waltz of Blooms": {
        "type":     "heal",
        "target":   "self",
        "amount":   10,
        "cost":     8
    },
    "Tidecall Nightbloom": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 3,
        "cost":     8
    },

    # Fabielly Fonseca (13) duos
    "Harbinger’s Nightsong": {
        "type":     "buff",
        "target":   "self",
        "stat":     "ATK",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Silken Shadow Song": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   3,
        "duration": 2,
        "cost":     8
    },
    "Howl of the Silken Night": {
        "type":     "damage",
        "target":   "enemy",
        "power":    13,
        "cost":     8
    },
    "Cipher of the Nightsong": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },

    # Sophia Romero (15) duos
    "Midnight Tide Sovereign": {
        "type":     "buff",
        "target":   "self",
        "stat":     "DEF",
        "amount":   4,
        "duration": 3,
        "cost":     8
    },
    "Cipher of the Midnight Song": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     8
    },
    "Duskbringer of the Midnight Song": {
        "type":     "damage",
        "target":   "enemy",
        "power":    12,
        "cost":     8
    },
    "Sovereign Moonlit Song": {
        "type":     "heal",
        "target":   "self",
        "amount":   8,
        "cost":     8
    }

})
# ————————————————————————
# sector_7 Solo Echo-Arts
# ————————————————————————
echo_arts.update({

    "Fractured Sigil": {
        "type":     "damage",
        "target":   "enemy",
        "power":    6,
        "cost":     5,
        "bonus": {
            "type":     "buff",
            "target":   "self",
            "stat":     "SPD",
            "amount":   1,
            "duration": 2
        }
    },

    "Echofade": {
        "type":     "buff",
        "target":   "self",
        "stat":     "SPD",
        "amount":   2,
        "duration": 2,
        "cost":     5
    },

    "Thread of Silence": {
        "type":     "status",
        "target":   "enemy",
        "effect":   "stun",
        "duration": 1,
        "cost":     5
    },

    "Remnant Pulse": {
        "type":     "heal",
        "target":   "self",
        "amount":   8,
        "cost":     5
    }

})
