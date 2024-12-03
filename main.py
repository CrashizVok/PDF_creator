import random

def create(name,text):
    with open(f"{name}.pdf","w",encoding="utf-8") as filen:
        filen.writelines("Cím: Egyiptom")
        filen.writelines(text)
        filen.write("\n")
        filen.writelines(text)
        filen.write("\n")
def generate_text():
    pass

if __name__ == "__main__":
    for i in range(10):
        create(f"Asdablu{i}",generate_text())