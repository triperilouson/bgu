def citi():
    def filter_cities(min_population):

        with open('cities.txt', 'r', encoding='utf-8') as file:
            cities = file.readlines()

        filtered_cities = []
        filtered_population = []
        for city in cities:
            city.replace(' ','')
            city_name, population = city.strip().split(':')
            if int(population) > min_population:

                filtered_cities.append(city_name)
                filtered_population.append(population)
            print(city_name)

        filtered_cities.sort()
        if len(filtered_population) == len(filtered_cities):
            with open('filtered_cities.txt', 'w', encoding='utf-8') as file:
                for i in range(len(filtered_population)):
                    c, n = filtered_cities[i], filtered_population[i]
                    file.write(f"{c}:{n}\n")
        else:
            print('error lenth')


    min_population = int(input("put people: "))
    while True:
        try:
            filter_cities(min_population)
            break
        except Exception:
            print('error file')
            break
#citi()
def sum_goods():
    sales = {}
    with open('cities.txt','r', encoding='utf-8')as file:
        lines = file.readlines()
    print(lines)
    flag = 0
    for i in range(len(lines)):

        if i > len(lines) or '{' in lines[i] or '}' in lines[i]:
            continue

        else:
            line = lines[i]
            line = line.replace(' ','')
            line = line.replace(',', '')
            name, price = line.strip().split(':')
            if name != '' and price != '':
                if name in sales:
                    price =  int(price) + int(sales[name])

                sales[name] = price
                print(f'{name}, {price}')

    with open('output.txt','r+', encoding='utf-8')as file:
        for i in sales:
            print(f'{i}:{sales[i]}')
            file.write(f'{i}:{sales[i]}\n')

'''while True:
    try:
        sum_goods()
        break
    except Exception as e:
        print(f'error: {e}')
        break'''
