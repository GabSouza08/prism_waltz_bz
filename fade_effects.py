# fade_effects.py

import time

def low_hp_fade(f):
    if f.HP > 0 and f.HP <= 10:
        print("\n🩸 Critical Fade Triggered…")
        time.sleep(0.5)

        if f.house == "Alizarin":
            print(f"{f.name} sinks to one knee — ash curls through the air.")
            time.sleep(0.6)
            print("🔥 'Even pain remembers. I stand on it.'")

        elif f.house == "Purpur":
            print(f"{f.name} flickers — twilight threads dance on their skin.")
            time.sleep(0.6)
            print("🪞 'Even fading can fool fate.'")

        elif f.house == "Scarlet":
            print(f"{f.name} braces their stance — shield dim but unshattered.")
            time.sleep(0.6)
            print("🛡️ 'My vow was lit in fire. I won’t burn out.'")

        elif f.house == "Violet":
            print(f"{f.name} trembles — veil slipping, moonlight bleeding.")
            time.sleep(0.6)
            print("🌙 'Grace lasts longer than breath…'")

        else:
            print(f"{f.name} staggers… echoes spiral in broken rhythm.")
            time.sleep(0.6)
            print("💠 'I won’t fall as silence.'")

        time.sleep(0.8)


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