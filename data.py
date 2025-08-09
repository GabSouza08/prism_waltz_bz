# data.py

# 1) Champion roster per House
houses = {
    "Scarlet": [
        ("Eduardo Carlos",    "Golden Aegis Keeper"),        # 0
        ("Ana Clara",         "Daughter of Serenity’s Verse"),# 1 (F)
        ("Carlos Antonio",    "Guardian of Quiet Flame"),    # 2
        ("Sara Regina",       "Resolute Flamebearer"),       # 3 (F)
        ("João Vitor",        "Bulwark of the Ember Crown"), # 4
        ("Sabrina Silva",     "Crown of Blazing Resolve"),   # 5 (F)
        ("Davi Luiz",         "Sunlit Rampart Protector"),    # 6
        ("Maria Clara",       "Dawnlit Emissary"),           # 7 (F)
        ("Jefferson Lucas",   "Vanguard of the Sunwave"),     # 8
        ("Maria Cecília",     "Rose of the Ember Chapel"),    # 9 (F)
        ("Matthews Guedes",   "Rampart-Warden of Dawn"),      # 10
        ("Maria Luisa",       "Brightvoice Oracle"),         # 11 (F)
        ("Heleno Gomes",      "Bastion-Watcher of Daybreak"), # 12
        ("Elen Nayara",       "Lantern of Morning Mist"),     # 13 (F)
        ("Rodrigo Bezerra",   "Ironflare Duelist"),           # 14
        ("Esthella Angelina", "Nightlight’s Counterpoint")    # 15 (F)
    ],
    "Alizarin": [
        ("Achiles Martins",    "The Radiant Spear"),             # 0
        ("Andrielly Luiz",     "Echo of Solar Whispers"),        # 1 (F)
        ("Adriel Melo",        "Herald of the Golden Dawn"),     # 2
        ("Bruna Adrielly",     "Ashen Dawn Crusader"),           # 3 (F)
        ("Anderson Marinho",   "Hearthstone Sentinel"),          # 4
        ("Damylle Kemilly",   "Ember-Tide Chantress"),          # 5 (F)
        ("Arthur Lucas",       "Crestbearer of Sunstone Rhyme"), # 6
        ("Rayelle Marinho",    "Ember-Faced Virtuoso"),          # 7 (F)
        ("Brian Morone",       "Charcoal Beacon"),               # 8
        ("Marilia Oliveira",   "Scarlet-Pulse Emissary"),        # 9 (F)
        ("Felipe Emmanuel",    "Lightbearer of the First Ray"),  # 10
        ("Evellyn Kauany",     "Photon-Shield Maiden"),          # 11 (F)
        ("Gabriel Lacerda",    "Seeker of Solar Chants"),        # 12
        ("Wellen Adelaide",    "Waveborn Flame"),                # 13 (F)
        ("Tulyo Martins",      "Morningstar Bard"),              # 14
        ("Maria Jullya",       "Solar-Star Oracle")              # 15 (F)
    ],
    "Violet": [
        ("Carlos Eduardo",     "Warden of the Twilight Gate"),   # 0
        ("Evellyn Oliveira",   "Photon-Shield Maiden"),          # 1 (F)
        ("José Izaquiel",      "Oracle of Moon Blessings"),      # 2
        ("Bianca Flora",       "Petalwing Sentinel"),            # 3 (F)
        ("Josenilton Oliveira","Bronze-Crescent Keeper"),         # 4
        ("Maria Yasmim",       "Bloomheart Whisperer"),           # 5 (F)
        ("João Pedro",         "Celestial Pathway Herald"),       # 6
        ("Ana Victoria",       "Moon-Fused Resolve"),            # 7 (F)
        ("Manoel Henrique",    "Echo of the Nightshield"),       # 8
        ("Emilly Alves",       "Pulse of Velvet Reflection"),     # 9 (F)
        ("Jobson Santana",     "Moonlit Wanderer"),               # 10
        ("Samantha Martinez",  "Waltz of Velvet Resolve"),        # 11 (F)
        ("Jonathan Nazareno",  "Seeker of Silver Fates"),         # 12
        ("Mirelle Freitas",    "Dreamtide Luminary"),            # 13 (F)
        ("Ricardo Henrique",   "Starlight Herald"),               # 14
        ("Vitoria Karoline",   "Champion of Moonlit Wills")       # 15 (F)
    ],
    "Purpur": [
        ("Arthur Ivandro",     "Bearer of the Moonrise Fury"),   # 0
        ("Ketillyn Irlly",      "Silver-Dusk Trickster"),          # 1 (F)
        ("David Erick",        "Shadow-Wall Duelist"),            # 2
        ("Bruna Evelyn",       "Silken Moonblade"),               # 3 (F)
        ("Gabriel Andre",      "Dawnbreaker of Dusk"),            # 4
        ("Mariana Pontes",     "Mistbringer of Tidecall"),        # 5 (F)
        ("Gabriel Lucena",     "Nocturnal Cipher Avenger"),       # 6
        ("Isadora Andrade",    "Mirrorblade of Lunar Valor"),     # 7 (F)
        ("Henrique Floripe",   "Moonlit Sovereign"),              # 8
        ("Karoline Cassiano",  "Moonflare Visionary"),            # 9 (F)
        ("Leonardo Lyon",      "Howl of the Lunar Citadel"),       # 10
        ("Emilly Nayara",      "Nightbloom Chanter"),             # 11 (F)
        ("Ronald Bryan",       "Twilight Harbinger"),             # 12
        ("Fabielly Fonseca",   "Silken Nightsong"),               # 13 (F)
        ("Thales Santana",     "Tidecall Duelist of Night"),      # 14
        ("Sophia Romero",      "Midnight Song Sovereign")         # 15 (F)
    ],
    "Sector_7": [
      ("Manuela Cavalcanti",  "Jester of Flawed Whispers"),
      ("Luna França",         "Moondaughter of the Fraying West"),
      ("Ryan Ribeiro",        "Kindling Voice of Forgotten Flame"),
      ("Heitor Miguel",       "Pillarbound Heir of the Silent Code"),
      ("Danilo Cavalcante",   "Mirrorkeeper of Verdant Silence"),
      ("Ricardo Silva",       "Depthwarden of Silver Remains"),
      ("Jhennifer Kelly",     "Seeker of the Unfurled Echo"),
      ("Clara Melo",          "Flame Artisan of the Threaded Lyric"),
      ("Sophia Paulino",      "Warden of Sapphire Silence"),
      ("Lara Pontes",         "Mistwalker of the Hollow Tides"),
      ("Vinicius Alves",      "Archivist of Guttered Light"),
      ("Iury Barbosa",        "Envoy of the Broken Sigil"),
      ("Mickael Ribeiro",     "Stormbinder of the Resonant Wake"),
      ("Jandira Lopes",       "Matron of the Withered Harvest"),
      ("Ivanildo Camilo",     "Vigilkeeper of Blazing Remembrance"),
      ("Thaynara Magno",      "Luminary of the Woven Morrow")
   ]
}



# 2) Solo Echo-Arts per House
solo_echoes = {
    "Scarlet":  ["Emberlit Vow", "Radiant Shield", "Flame's Embrace", "Aegis Requiem"],
    "Alizarin": ["Solar Pulse", "Crimson Burst", "Dawn's Edge", "Ashen Echo"],
    "Violet":   ["Velvet Waltz", "Silent Bloom", "Gossamer Veil", "Moon's Respite"],
    "Purpur":   ["Dusk Trick", "Shadowstep", "Illusory Dance", "Twilight Veil"],
    "Sector_7": ["Fractured Sigil", "Echofade", "Thread of Silence", "Remnant Pulse"]
}

# 3) Duo-bond indices by champion index
#    Each female champion index → list of (partner_index, duo_echo_title)
duo_indices = {
    "Scarlet": {
        1: [ (0, "Aegis of Serenity’s Verse"),
             (2, "Serene Flame Accord"),
             (6, "Rampart’s Serene Vow"),
             (8, "Serene Sunwave Vanguard") ],
        3: [ (2, "Resolute Flame Guardian"),
             (6, "Rampart’s Flame Vow"),
             (10,"Resolute Dawn Warden"),
             (14,"Resolute Ironflame") ],
        5: [ (4, "Blazing Crown Bulwark"),
             (8, "Crowned Sunwave Vanguard"),
             (10,"Blazing Dawn Warden"),
             (14,"Iron-Dawn Counter") ],
        7: [ (0, "Dawnlit Aegis Covenant"),
             (4, "Dawnlit Crown Bulwark"),
             (6, "Emissary of the Rampart’s Dawn"),
             (14,"Iron-Dawn Counter") ],
        9: [ (2, "Rose-Guard Alliance"),
             (8, "Rosewing Vanguard"),
             (14,"Rose-Iron Flare"),
             (4, "Rosecrown Bulwark") ],
        11:[ (0, "Oracle-Aegis Harmony"),
             (4, "Oracle-Crown Hymn"),
             (8, "Oracle Vanguard"),
             (10,"Oracle of the Ramparted Dawn") ],
        13:[ (0, "Mistbound Aegis"),
             (4, "Mistlit Crown Bulwark"),
             (6, "Mistlit Rampart"),
             (12,"Mistlit Bastion") ],
        15:[ (2, "Nocturne Flame Counter"),
             (10,"Nocturnal Dawn Warden"),
             (12,"Nocturnal Bastion"),
             (14,"Ironlight Counterpoint") ]
    },
    "Alizarin": {
        1:  [ (0,"Echo of the Radiant Spear"),
              (2,"Herald of Solar Whispers"),
              (4,"Sentinel of Solar Whispers"),
              (6,"Crest of Solar Whispers") ],
        3:  [ (2,"Herald of the Ashen Dawn"),
              (4,"Crusader of the Ember Tide"),
              (6,"Ashen Rhyme Crusader"),
              (8,"Crusader of the Charcoal Beacon") ],
        5:  [ (4,"Sentinel of the Ember Tide"),
              (6,"Crested Ember Chant"),
              (8,"Beacon of the Ember-Tide"),
              (10,"Ember-Tide Shield") ],
        7:  [ (6,"Crested Ember Rhyme"),
              (8,"Charcoal-Faced Virtuoso"),
              (10,"Photon-Faced Virtuoso"),
              (12,"Virtuoso of Solar Waves") ],
        9:  [ (8,"Charcoal Pulse Beacon"),
              (10,"Photon-Pulse Shieldbearer"),
              (12,"Seeker of the Pulse Wave"),
              (14,"Oracle of the Pulse Star") ],
        11: [ (10,"Photon-Ray Shieldbearer"),
              (12,"Seeker of the Photon Wave"),
              (14,"Shieldmaiden of the Morningstar"),
              (0, "Radiant Shield Maiden") ],
        13: [ (12,"Seeker of the Solar Wave"),
              (14,"Morning Wave Bard"),
              (0, "Waveborn Radiant Spear"),
              (2, "Waveborn Dawn Herald") ],
        15: [ (14,"Oracle of the Morningstar"),
              (0, "Spear of the Solar Star"),
              (2, "Herald of the Solar Star"),
              (4, "Sentinel of the Solar Star") ]
    },
    "Violet": {
        1:  [ (0,"Shield of the Twilight Gate"),
              (2,"Shield of Moonblessings"),
              (4,"Shield of the Bronze Crescent"),
              (6,"Shield of the Celestial Path") ],
        3:  [ (2,"Moonpetal Sentinel"),
              (4,"Petal-Crescent Sentinel"),
              (6,"Petal Path Herald"),
              (8,"Petal Nightshield Echo") ],
        5:  [ (4,"Whisperer of the Blooming Crescent"),
              (6,"Whisperer of the Celestial Bloom"),
              (8,"Nightbloom Echo"),
              (10,"Wanderer of the Bloomheart") ],
        7:  [ (6,"Herald of Fused Moon Paths"),
              (8,"Nightshield of Moon Resolve"),
              (10,"Wanderer of the Moon-Fused Resolve"),
              (12,"Seeker of Moon-Fused Fates") ],
        9:  [ (8,"Echo of Velvet Reflection"),
              (10,"Wanderer of the Velvet Pulse"),
              (12,"Seeker of the Velvet Fates"),
              (14,"Herald of Starlit Reflection") ],
        11: [ (10,"Waltz of the Moonlit Resolve"),
              (12,"Seeker of the Velvet Waltz"),
              (14,"Herald of the Velvet Waltz"),
              (0, "Gate of the Velvet Waltz") ],
        13: [ (12,"Seeker of Dreamtide Fates"),
              (14,"Starlight of the Dreamtide"),
              (0, "Gate of the Dreamtide"),
              (2, "Oracle of Dreamtide Blessings") ],
        15: [ (14,"Herald of Moonlit Champion"),
              (0, "Gate of the Moonlit Will"),
              (2, "Oracle of Moonlit Will"),
              (4, "Crescent Will Champion") ]
    },
    "Purpur": {
        1:  [ (0, "Moonrise Fury Trick"),
              (2, "Shadow-Dusk Trick"),
              (6, "Ciphered Dusk Trick"),
              (12,"Twilight-Dusk Trick") ],
        3:  [ (2, "Silken Shadow Blade"),
              (10,"Howl of the Silken Moon"),
              (4, "Duskbringer of Dusk"),
              (8, "Silken Sovereign of the Moon") ],
        5:  [ (4, "Duskbringer of Mistcall"),
              (14,"Tidecall Mist Sovereign"),
              (2, "Shadow-Mist Wall"),
              (6, "Cipher of Mistcall") ],
        7:  [ (6, "Mirror Avenger Cipher"),
              (0, "Mirror Fury of Moonrise"),
              (8, "Mirrorflame Sovereign"),
              (12,"Twilight Mirror Song") ],
        9:  [ (8, "Sovereign Moonflare"),
              (14,"Midnight Moonflare"),
              (4, "Duskbringer Moonflare"),
              (0, "Moonrise Crown of Flares") ],
        11: [ (10,"Howl of the Nightbloom Citadel"),
              (12,"Harbinger of the Nightbloom Song"),
              (0, "Moonrise Waltz of Blooms"),
              (14,"Tidecall Nightbloom") ],
        13: [ (12,"Harbinger’s Nightsong"),
              (2, "Silken Shadow Song"),
              (10,"Howl of the Silken Night"),
              (6, "Cipher of the Nightsong") ],
        15: [ (14,"Midnight Tide Sovereign"),
              (6, "Cipher of the Midnight Song"),
              (4, "Duskbringer of the Midnight Song"),
              (8, "Sovereign Moonlit Song") ]
    }
}
ChampionStats = {
    "Violet": {
        "Carlos Eduardo":    {"HP": 36, "ATK": 6, "DEF": 7, "SPD": 4, "Affinity": "Twilight Gate"},
        "Evellyn Oliveira":  {"HP": 32, "ATK": 5, "DEF": 6, "SPD": 6, "Affinity": "Moon’s Respite"},
        "José Izaquiel":     {"HP": 34, "ATK": 6, "DEF": 5, "SPD": 5, "Affinity": "Moon Blessings"},
        "Bianca Flora":      {"HP": 31, "ATK": 5, "DEF": 5, "SPD": 6, "Affinity": "Gossamer Veil"},
        "Josenilton Oliveira":{"HP": 35, "ATK": 6, "DEF": 6, "SPD": 4, "Affinity": "Silent Bloom"},
        "Maria Yasmim":      {"HP": 30, "ATK": 5, "DEF": 4, "SPD": 7, "Affinity": "Silent Bloom"},
        "João Pedro":        {"HP": 33, "ATK": 6, "DEF": 5, "SPD": 5, "Affinity": "Gossamer Veil"},
        "Ana Victoria":      {"HP": 32, "ATK": 5, "DEF": 5, "SPD": 6, "Affinity": "Moon’s Respite"},
        "Manoel Henrique":   {"HP": 34, "ATK": 6, "DEF": 5, "SPD": 4, "Affinity": "Velvet Waltz"},
        "Emilly Alves":      {"HP": 31, "ATK": 5, "DEF": 4, "SPD": 7, "Affinity": "Velvet Waltz"},
        "Jobson Santana":    {"HP": 30, "ATK": 6, "DEF": 5, "SPD": 5, "Affinity": "Moon’s Respite"},
        "Samantha Martinez": {"HP": 29, "ATK": 5, "DEF": 5, "SPD": 6, "Affinity": "Velvet Waltz"},
        "Jonathan Nazareno": {"HP": 33, "ATK": 6, "DEF": 5, "SPD": 5, "Affinity": "Silent Bloom"},
        "Mirelle Freitas":   {"HP": 32, "ATK": 5, "DEF": 5, "SPD": 6, "Affinity": "Gossamer Veil"},
        "Ricardo Henrique":  {"HP": 35, "ATK": 6, "DEF": 6, "SPD": 4, "Affinity": "Moon’s Respite"},
        "Vitoria Karoline":  {"HP": 31, "ATK": 5, "DEF": 5, "SPD": 7, "Affinity": "Moon’s Respite"}
    },
    "Alizarin": {
        "Achiles Martins":   {"HP": 34, "ATK": 8, "DEF": 4, "SPD": 6, "Affinity": "Radiant Spear"},
        "Andrielly Luiz":    {"HP": 30, "ATK": 6, "DEF": 3, "SPD": 9, "Affinity": "Solar Whispers"},
        "Adriel Melo":       {"HP": 32, "ATK": 7, "DEF": 4, "SPD": 5, "Affinity": "Golden Dawn"},
        "Bruna Adrielly":    {"HP": 29, "ATK": 7, "DEF": 5, "SPD": 8, "Affinity": "Ashen Dawn"},
        "Anderson Marinho":  {"HP": 33, "ATK": 6, "DEF": 5, "SPD": 4, "Affinity": "Hearthstone"},
        "Damylle Kemilly":   {"HP": 30, "ATK": 6, "DEF": 3, "SPD": 9, "Affinity": "Ember-Tide"},
        "Arthur Lucas":      {"HP": 32, "ATK": 7, "DEF": 4, "SPD": 5, "Affinity": "Sunstone Rhyme"},
        "Rayelle Marinho":   {"HP": 31, "ATK": 7, "DEF": 3, "SPD": 8, "Affinity": "Ember-Faced"},
        "Brian Morone":      {"HP": 33, "ATK": 7, "DEF": 5, "SPD": 4, "Affinity": "Charcoal Beacon"},
        "Marilia Oliveira":  {"HP": 29, "ATK": 6, "DEF": 4, "SPD": 8, "Affinity": "Scarlet-Pulse"},
        "Felipe Emmanuel":   {"HP": 34, "ATK": 6, "DEF": 5, "SPD": 5, "Affinity": "First Ray"},
        "Evellyn Kauany":    {"HP": 30, "ATK": 6, "DEF": 3, "SPD": 9, "Affinity": "Photon-Shield"},
        "Gabriel Lacerda":   {"HP": 31, "ATK": 7, "DEF": 4, "SPD": 6, "Affinity": "Solar Chants"},
        "Wellen Adelaide":   {"HP": 29, "ATK": 7, "DEF": 3, "SPD": 8, "Affinity": "Waveborn Flame"},
        "Tulyo Martins":     {"HP": 32, "ATK": 6, "DEF": 5, "SPD": 6, "Affinity": "Morningstar"},
        "Maria Jullya":      {"HP": 30, "ATK": 6, "DEF": 3, "SPD": 9, "Affinity": "Solar-Star"}
    },
    "Scarlet": {
        "Eduardo Carlos":    {"HP": 36, "ATK": 8, "DEF": 4, "SPD": 6, "Affinity": "Golden Aegis"},
        "Ana Clara":         {"HP": 34, "ATK": 7, "DEF": 3, "SPD": 8, "Affinity": "Serenity’s Verse"},
        "Carlos Antonio":    {"HP": 35, "ATK": 8, "DEF": 4, "SPD": 6, "Affinity": "Quiet Flame"},
        "Sara Regina":       {"HP": 33, "ATK": 8, "DEF": 3, "SPD": 8, "Affinity": "Flamebearer"},
        "João Vitor":        {"HP": 35, "ATK": 7, "DEF": 5, "SPD": 6, "Affinity": "Ember Crown"},
        "Sabrina Silva":     {"HP": 34, "ATK": 7, "DEF": 3, "SPD": 8, "Affinity": "Blazing Resolve"},
        "Davi Luiz":         {"HP": 36, "ATK": 9, "DEF": 4, "SPD": 6, "Affinity": "Sunlit Rampart"},
        "Maria Clara":       {"HP": 33, "ATK": 7, "DEF": 3, "SPD": 8, "Affinity": "Dawnlit Emissary"},
        "Jefferson Lucas":   {"HP": 35, "ATK": 8, "DEF": 4, "SPD": 6, "Affinity": "Sunwave Vanguard"},
        "Maria Cecília":     {"HP": 33, "ATK": 7, "DEF": 3, "SPD": 8, "Affinity": "Ember Chapel"},
        "Matthews Guedes":   {"HP": 35, "ATK": 8, "DEF": 5, "SPD": 6, "Affinity": "Rampart-Warden"},
        "Maria Luisa":       {"HP": 34, "ATK": 7, "DEF": 4, "SPD": 8, "Affinity": "Brightvoice"},
        "Heleno Gomes":      {"HP": 36, "ATK": 8, "DEF": 5, "SPD": 6, "Affinity": "Daybreak Bastion"},
        "Elen Nayara":       {"HP": 33, "ATK": 7, "DEF": 3, "SPD": 8, "Affinity": "Morning Mist"},
        "Rodrigo Bezerra":   {"HP": 35, "ATK": 9, "DEF": 4, "SPD": 6, "Affinity": "Ironflare Duelist"},
        "Esthella Angelina": {"HP": 34, "ATK": 7, "DEF": 3, "SPD": 8, "Affinity": "Nightlight’s Counterpoint"}
    },
    "Purpur": {
        "Arthur Ivandro":    {"HP": 35, "ATK": 7, "DEF": 5, "SPD": 6, "Affinity": "Moonrise Fury"},
        "Ketillyn Irlly":    {"HP": 33, "ATK": 6, "DEF": 4, "SPD": 9, "Affinity": "Silver-Dusk"},
        "David Erick":       {"HP": 34, "ATK": 8, "DEF": 5, "SPD": 6, "Affinity": "Shadow-Wall"},
        "Bruna Evelyn":      {"HP": 32, "ATK": 7, "DEF": 4, "SPD": 9, "Affinity": "Silken Moonblade"},
        "Gabriel Andre":     {"HP": 33, "ATK": 7, "DEF": 5, "SPD": 6, "Affinity": "Dawnbreaker of Dusk"},
        "Mariana Pontes":    {"HP": 31, "ATK": 6, "DEF": 4, "SPD": 8, "Affinity": "Mistbringer"},
        "Gabriel Lucena":    {"HP": 34, "ATK": 7, "DEF": 6, "SPD": 5, "Affinity": "Nocturnal Cipher"},
        "Isadora Andrade":   {"HP": 33, "ATK": 6, "DEF": 4, "SPD": 9, "Affinity": "Mirrorblade"},
        "Henrique Floripe":  {"HP": 35, "ATK": 7, "DEF": 6, "SPD": 6, "Affinity": "Moonlit Sovereign"},
        "Karoline Cassiano": {"HP": 32, "ATK": 6, "DEF": 4, "SPD": 8, "Affinity": "Moonflare Visionary"},
        "Leonardo Lyon":     {"HP": 34, "ATK": 8, "DEF": 5, "SPD": 5, "Affinity": "Howl of the Citadel"},
        "Emilly Nayara":     {"HP": 31, "ATK": 6, "DEF": 4, "SPD": 8, "Affinity": "Nightbloom Chanter"},
        "Ronald Bryan":      {"HP": 33, "ATK": 7, "DEF": 5, "SPD": 6, "Affinity": "Twilight Harbinger"},
        "Fabielly Fonseca":  {"HP": 32, "ATK": 6, "DEF": 4, "SPD": 9, "Affinity": "Silken Nightsong"},
        "Thales Santana":    {"HP": 34, "ATK": 7, "DEF": 5, "SPD": 6, "Affinity": "Tidecall Duelist"},
        "Sophia Romero":     {"HP": 31, "ATK": 6, "DEF": 4, "SPD": 8, "Affinity": "Midnight Song"}
    },
    "Sector_7": {
      "Manuela Cavalcanti":  {"HP": 32, "ATK": 7, "DEF": 4, "SPD": 8, "Affinity": "Thread of Silence"},
      "Luna França":         {"HP": 33, "ATK": 6, "DEF": 5, "SPD": 9, "Affinity": "Echofade"},
      "Ryan Ribeiro":        {"HP": 34, "ATK": 8, "DEF": 4, "SPD": 6, "Affinity": "Fractured Sigil"},
      "Heitor Miguel":       {"HP": 35, "ATK": 7, "DEF": 6, "SPD": 5, "Affinity": "Remnant Pulse"},
      "Danilo Cavalcante":   {"HP": 33, "ATK": 7, "DEF": 5, "SPD": 7, "Affinity": "Thread of Silence"},
      "Ricardo Silva":       {"HP": 31, "ATK": 7, "DEF": 5, "SPD": 8, "Affinity": "Echofade"},
      "Jhennifer Kelly":     {"HP": 32, "ATK": 7, "DEF": 4, "SPD": 9, "Affinity": "Fractured Sigil"},
      "Clara Melo":          {"HP": 34, "ATK": 8, "DEF": 4, "SPD": 6, "Affinity": "Remnant Pulse"},
      "Sophia Paulino":      {"HP": 32, "ATK": 7, "DEF": 5, "SPD": 8, "Affinity": "Thread of Silence"},
      "Lara Pontes":         {"HP": 31, "ATK": 6, "DEF": 5, "SPD": 9, "Affinity": "Echofade"},
      "Vinicius Alves":      {"HP": 33, "ATK": 7, "DEF": 4, "SPD": 9, "Affinity": "Fractured Sigil"},
      "Iury Barbosa":        {"HP": 34, "ATK": 8, "DEF": 4, "SPD": 7, "Affinity": "Remnant Pulse"},
      "Ivanildo Camilo":     {"HP": 35, "ATK": 7, "DEF": 5, "SPD": 6, "Affinity": "Thread of Silence"},
      "Mickael Ribeiro":     {"HP": 32, "ATK": 7, "DEF": 6, "SPD": 6, "Affinity": "Echofade"},
      "Jandira Lopes":       {"HP": 33, "ATK": 6, "DEF": 5, "SPD": 8, "Affinity": "Remnant Pulse"},
      "Thaynara Magno":      {"HP": 33, "ATK": 5, "DEF": 5, "SPD": 8, "Affinity": "Thread of Silence"}
   }
}


# 1) Build inverse (male_index → list of (female_index, echo))
_duo_indices_male = {}
for house, female_map in duo_indices.items():
    inv = {}
    for f_idx, partners in female_map.items():
        for m_idx, echo in partners:
            inv.setdefault(m_idx, []).append((f_idx, echo))
    _duo_indices_male[house] = inv

# 2) Merge female‐ and male‐initiated into one full map
_duo_indices_full = {}
for house in duo_indices:
    merged = {}
    # start with all female entries
    merged.update(duo_indices[house])
    # add/overwrite male entries
    merged.update(_duo_indices_male[house])
    _duo_indices_full[house] = merged

# 3) Replace duo_indices with the merged version
duo_indices = _duo_indices_full