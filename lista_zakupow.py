lista_zakupow = {
    "piekarnia": ["Chleb","Paczek","Bulki"],
    "warzywniak": ["Marchew","Seler","Rukola"]}


for key, value in lista_zakupow.items():
    print("Ide do",key.upper(),"i kupuje tam",value)
    ilosc = len(value)
    
print("W sumie kupiłem",v,"produktow")