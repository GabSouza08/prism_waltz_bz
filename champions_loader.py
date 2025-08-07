# champions_loader.py

from champions import Champion
from data import houses, solo_echoes, duo_indices

def load_champions():
    all_champs = {}
    for house, entries in houses.items():
        all_champs[house] = []
        for idx, (name, title) in enumerate(entries):
            # gather this champion’s duo-echo names (if female index in duo_indices)
            duo_list = []
            if idx in duo_indices[house]:
                duo_list = [duo for _, duo in duo_indices[house][idx]]
            champ = Champion(
                name,
                title,
                house,
                idx,
                solo_echoes[house],
                duo_list
            )
            all_champs[house].append(champ)
    return all_champs

