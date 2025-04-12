import json  

with open("alice.txt", mode = "r", encoding = "utf-8") as soubor:
    text = soubor.read()
    text = text.lower().replace("" "", "").replace("\n", "")

    slovnik = {}
    for znak in text:
        if znak not in slovnik:
            slovnik[znak] = 1
        else:
            slovnik[znak] = slovnik[znak] + 1
            #slovnik[znak] += 1 mám ale radši moje vypsání, lépe se v tom orientuji :)
serazene = dict(sorted(slovnik.items()))

with open("hw01_output.json", mode = "w", encoding = "utf-8") as soubor2:
    json.dump(serazene, soubor2, indent = 4, ensure_ascii=False, sort_keys=True)
