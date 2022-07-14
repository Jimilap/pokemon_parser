import requests
from bs4 import BeautifulSoup as bs

url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'
soup = bs(requests.get(url).text, 'html.parser')
file = open("pokemon_list.txt", 'w')

def add():
    with open("pokemon_list.txt", 'a') as file:
        list_ = str("Gdex: " + str(pok[0]) + " Ndex: " + str(pok[1]) + " name: " + str(pok[2]) + " type: " + str(type_))
        file.write(list_ + "\n")
    
    print(list_)

def search(num):
    with open("pokemon_list.txt", 'w') as file: file.write("pokemon_list\n")
    G = soup.select(".mw-parser-output > table:nth-of-type("+ str(int(num) + 1) +")")
    global pok, type_
    pok = [] 
    type_ = str() 
    pokemon = 2 
    info_counter = 1
    for i in G[0].select('tbody>tr'): 
        for a in G[0].select('tr:nth-of-type('+ str(pokemon) +')>td'): 
            info = str(a.text.strip().replace("\n", "")) 
            if info_counter == 1 and not "#" in info: 
                info = "#---"
            pok.append(str(info.replace("['", "").replace("']", "").replace('["', "").replace('"]', "")))
            info_counter += 1

        if len(pok) == 4:
            type_ = pok[3]
            add()
        elif len(pok) == 5:
            type_ = pok[3] + " and " + pok[4] 
            add()
        else: type_ = "null"

        pok.clear()
        pokemon +=1
        info_counter = 1

while True:
    a = str(input("action: "))  
    if a == "stop":
        break
    elif a == "find":
        print("not ready yet")
    elif a == "gen":        
        n = str(input("select generation: "))
        if int(n) > 8 or int(n) < 1:
            print("no such generation")
        else:
            search(n)
    elif a == "all":
        n = int(1)
        while n < 9:
            print("generation " + str(n))
            search(int(n))
            n += 1