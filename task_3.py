world_champions = {
    2002: 'Бразилия',
    2106: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'

for champion_list in list(world_champions):
    print (f'{champion_list} - {world_champions.get(champion_list)}')

vek_21 = range(2001, 2100)
country_name = 'Италия'

for year in vek_21:
    if year in world_champions and world_champions[year] == country_name:
        print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
        break
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')