import random
import os

szereplok = ["Péter", "Anna", "János", "Katalin", "a kisfiú", "az öregember", "a tanár", "a macska"]
cselekvesek = [
    "elindult a hegyek felé", 
    "megállt egy pillanatra", 
    "nyugodtan ült a padon", 
    "gondolkodott a múlt eseményein", 
    "keresett valamit a zsebében", 
    "felnézett az égre"
]
helyszinek = [
    "a sűrű erdőben", 
    "egy csendes faluban", 
    "a város zajos utcáin", 
    "egy elhagyatott réten", 
    "a folyóparton", 
    "a holdfényes éjszakában"
]
esemenyek = [
    "hirtelen egy különös hangot hallott", 
    "egy ismeretlen alak tűnt fel a távolban", 
    "egy váratlan szellő fújt végig a tájon", 
    "az égbolt elsötétült", 
    "egy rég elfeledett emlék jutott eszébe", 
    "egy szarvas szaladt át előtte"
]
kovetkezmenyek = [
    "ez megváltoztatta az útját", 
    "ráébredt egy fontos igazságra", 
    "visszatért oda, ahonnan elindult", 
    "úgy döntött, hogy tovább megy", 
    "egy új barátot talált", 
    "megértette, mit kell tennie"
]

def generate_sentence():
    szereplo = random.choice(szereplok)
    cselekves = random.choice(cselekvesek)
    helyszin = random.choice(helyszinek)
    esemeny = random.choice(esemenyek)
    kovetkezmeny = random.choice(kovetkezmenyek)
    
    return f"{szereplo} {cselekves} {helyszin}, amikor {esemeny}, és {kovetkezmeny}."

def generate_story(paragraphs=3, sentences_per_paragraph=5):
    story = []
    for _ in range(paragraphs):
        paragraph = "\n".join(generate_sentence() for _ in range(sentences_per_paragraph))
        story.append(paragraph)
    return "\n\n".join(story)

def create_pdf_like_file(name, story):
    os.makedirs("CreatedPDF", exist_ok=True)
    file_path = os.path.join("CreatedPDF", f"{name}.pdf")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Cím: Egy különös utazás\n\n")
        file.write(story)

if __name__ == "__main__":
    for i in range(5):  
        story = generate_story(paragraphs=4, sentences_per_paragraph=7)  
        create_pdf_like_file(f"Történet_{i}", story)
