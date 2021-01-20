import markovify
import random

with open("every_mordhau_patchnote_ever.txt") as f:
    text = f.read()
text_model = markovify.NewlineText(text, state_size=3)

patchie = open("patchie.txt", "w")

headlines = ["General", "Gameplay", "Combat", "Sound", "Weapons & Equipment", "Performance", "Skins", "Misc", "UI"]
random.shuffle(headlines)

patchie.write("Patch #21 Changelog - NOT FULL CHANGELOG, ONLY PARTIAL")
for i in range(5):
    patchie.write("\n\n" + headlines[i])
    for j in range(random.randint(10, 30)):
        patchie.write("\n" + text_model.make_short_sentence(128, tries=100))
patchie.close()

#open file once generated
with open("patchie.txt", "r") as patch:
    print(patch.read())
