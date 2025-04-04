with open("alice.txt", mode = "r", encoding = "utf-8") as soubor:
    text = soubor.read()
    text = text.lower()
    text = text.replace(' ', "")
    text = text.replace('\n', "")

    slovnik = {}
    for znak in text:
        if znak not in slovnik:
            slovnik[znak] = 1
        else:
            slovnik[znak] = slovnik[znak] + 1

serazene = dict(sorted(slovnik.items()))

import json  
with open("hw01_output.json", mode = "w", encoding = "utf-8") as soubor2:
    json.dump(serazene, soubor2, indent = 4, ensure_ascii=False)