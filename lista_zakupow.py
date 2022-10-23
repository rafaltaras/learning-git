lista_zakupow = {
    "piekarnia": ["Chleb","Paczek","Bulki"],
    "warzywniak": ["Marchew","Seler","Rukola"]}

v = 0
for key, value in lista_zakupow.items():
    print("Ide do",key.upper(),"i kupuje tam",value)
    ilosc = len(value)
    v = v + ilosc
print("W sumie kupiłem",v,"produktow")