lista_zakupow = {
    "piekarnia": ["Chleb","Paczek","Bulki","Rogal"],
    "warzywniak": ["Marchew","Seler","Rukola","Piertuszka"]}

v = 0
for key, value in lista_zakupow.items():
    print("Ide do",key.upper(),"i kupuje tam",value)
    ilosc = len(value)
    v = v + ilosc
print("Zostały zakupione",v,"towarów")
print("new branch")
