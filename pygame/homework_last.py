import pygame
import time
import random
import threading

pygame.init()


def text_get(text_quetion):
    while True:
        try:
            bag_deleted = text_quetion
            screen = pygame.display.set_mode((900, 600))
            screen.fill(0)
            f2 = pygame.font.SysFont('serif', 20)
            input_box = pygame.Rect(250, 400, 400, 100)
            color_inactive = pygame.Color((0, 128, 255))
            color = color_inactive
            text_quetion_render = f2.render(f'{text_quetion}', True, (0, 128, 255))
            text = ''
            place = text_quetion_render.get_rect(center=(450, 100))
            done = False
            clock = pygame.time.Clock()

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            done = True
                            break
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                if not done:
                    screen.fill((0, 0, 0))
                    pygame.draw.rect(screen, color, input_box, 2)
                    txt_surface = f2.render(text, True, color)
                    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
                    screen.blit(text_quetion_render, place)
                    pygame.display.flip()
                    clock.tick(60)
                else:
                    break
            return text
        except Exception:
            screen = pygame.display.set_mode((900, 600))
            screen.fill(0)
            f2 = pygame.font.SysFont('serif', 50)
            text_error = f2.render('enter true (int)', True, (0, 128, 255))
            place_error = text_error.get_rect(center=(450, 300))
            screen.blit(text_error, place_error)
            pygame.display.flip()
            time.sleep(5)
            text_quetion = bag_deleted

while True:
    try:
        unit_time = int(input('What time in the world in seconds? '))
        break
    except Exception as e:
        print(f'{e}, try again')

time_start = time.time()
time_animal_world = 0

class Animal:
    def __init__(self, name, type_animal, size, food_type, habitat, lifespan):
        self.name = name
        self.type_animal = type_animal
        self.size = size
        self.food_type = food_type
        self.habitat = habitat
        self.lifespan = lifespan + time_animal_world
        self.age = 0
        self.satiety = 100
        self.gender = random.choice(['male', 'female'])

class player(Animal):
    def move_player(self,position, direction, speed, image):
        new_position = position[:]
        if direction == 'left':
            new_position[0] -= speed
        elif direction == 'right':
            new_position[0] += speed
        elif direction == 'up':
            new_position[1] -= speed
        elif direction == 'down':
            new_position[1] += speed

        if (0 <= new_position[0] <= 900 - self.size) and (0 <= new_position[1] <= 600 - self.size):
            if player_waze.check_collision(self,new_position[0], new_position[1], image):
                return new_position
        return position

    def shooting(self,position, bullets, direction):

        bullet_speed = 10
        bullet = {'pos': list(position), 'dir': direction, 'speed': bullet_speed}
        bullets.append(bullet)
    def stop_time(self):
        pass
    def chek_arround_2(self, animal_list, player_pose1, player_pose2):
        list_max_sorted = {}
        value_to_find = [i for i in range(1,101)]
        print(value_to_find)
        for animal in animal_list:
            list_pouse = []

            for i in str(animal_list[animal]).strip('<rect(').split(','):
                if len(list_pouse) == 2:
                    break
                list_pouse.append(int(i))
            list_max_sorted[animal] = (list_pouse[0] - player_pose1)**2 + (list_pouse[1] - player_pose2)**2
            for i in value_to_find:
                key = next((k for k, v in list_max_sorted.items() if v == i), None)
                if key != None:

                    for g in flora.animals:
                        m=0
                        for b in flora.animals:
                            m += 1
                            if key == b:
                                m = m-1
                                flora.animals[m].satiety = flora.animals[m].satiety - 10
                                global bullets
                                bullets = []
                                return



                    break
    def chek_arround(self, animal_list, player_pose1, player_pose2):
        list_max_sorted = {}
        value_to_find = [i for i in range(1,101)]
        print(value_to_find)
        for animal in animal_list:
            list_pouse = []

            for i in str(animal_list[animal]).strip('<rect(').split(','):
                if len(list_pouse) == 2:
                    break
                list_pouse.append(int(i))
            list_max_sorted[animal] = (list_pouse[0] - player_pose1)**2 + (list_pouse[1] - player_pose2)**2
            for i in value_to_find:
                key = next((k for k, v in list_max_sorted.items() if v == i), None)
                if key != None:

                    for g in flora.animals:
                        m=0
                        for b in flora.animals:
                            m += 1
                            if key == b:
                                m = m-1
                                flora.information_2(m)
                                break


                    break


    def my_stats(self):
        text = text_get(
            f'{player1.type_animal}, \n{player1.name}, \n{player1.satiety}, \n{player1.food_type}, \n{player1.lifespan},\n {player1.age}, \n{player1.gender}')
        print(player1)
    def life(self, animal_list,player_pose1, player_pose2):

        list_max_sorted = {}
        value_to_find = [i for i in range(1, 101)]
        print(value_to_find)
        for animal in animal_list:
            list_pouse = []

            for i in str(animal_list[animal]).strip('<rect(').split(','):
                if len(list_pouse) == 2:
                    break
                list_pouse.append(int(i))
            list_max_sorted[animal] = (list_pouse[0] - player_pose1) ** 2 + (list_pouse[1] - player_pose2) ** 2
            for i in value_to_find:
                key = next((k for k, v in list_max_sorted.items() if v == i), None)
                if key != None:

                    for g in flora.animals:
                        m = 0
                        for b in flora.animals:
                            m += 1
                            if key == b:
                                m = m - 1
                                if flora.animals[m].food_type == 'animals':
                                    text_get('game over')
                                    time.sleep(10)
                                    pygame.quit()
                                    return e

                                break

                    break

    def speed_jump(self):
        pass


def handle_bullets():
    global bullets
    for bullet in bullets:
        if bullet['dir'] == 'left':
            bullet['pos'][0] -= bullet['speed']
        elif bullet['dir'] == 'right':
            bullet['pos'][0] += bullet['speed']
        elif bullet['dir'] == 'up':
            bullet['pos'][1] -= bullet['speed']
        elif bullet['dir'] == 'down':
            bullet['pos'][1] += bullet['speed']

    bullets = [bullet for bullet in bullets if 0 <= bullet['pos'][0] <= 900 and 0 <= bullet['pos'][1] <= 600]


player1 = player('player1', "Lion", 15, "plants", "land", 1000)

class DefFlora:
    def __init__(self):
        self.animals = []
        self.plant_food_supply = 1000

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_food(self):
        food = int(text_get('Count of food'))
        self.plant_food_supply += food

    def information(self):
        for animal in self.animals:
            text = text_get(f'{animal.type_animal}, \n{animal.name}, \n{animal.satiety}, \n{animal.food_type}, \n{animal.lifespan},\n {animal.age}, \n{animal.gender}')
            print(animal)
    def information_2(self, l):
        text_get(f'{self.animals[l].type_animal}, \n{self.animals[l].name}, \n{self.animals[l].satiety}, \n{self.animals[l].food_type}, \n{self.animals[l].lifespan},\n {self.animals[l].age}, \n{self.animals[l].gender}')

    def reproduce(self, first: Animal, second: Animal):
        if first.habitat != second.habitat or first.type_animal != second.type_animal:
            print('Error: habitat or type animal mismatch')
            return
        if first.gender == second.gender:
            print('Error: same gender')
            return
        if first.habitat == 'water' and first.satiety > 50 and second.satiety > 50:
            for _ in range(10):
                self.add_animal(Animal(first.name, first.type_animal, first.size, first.food_type, first.habitat, first.lifespan))
        elif first.habitat == 'air' and first.satiety > 42 and first.age > 3 and second.age > 3:
            for _ in range(4):
                self.add_animal(Animal(first.name, first.type_animal, first.size, first.food_type, first.habitat, first.lifespan))
        elif first.habitat == 'land' and first.satiety > 20 and first.age > 5 and second.age > 5:
            for _ in range(2):
                self.add_animal(Animal(first.name, first.type_animal, first.size, first.food_type, first.habitat, first.lifespan))

    def death_life(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or flora.animals == []:
                    pygame.quit()
                    done = True
                    break
            time_plus(self)
            for animal in self.animals:
                if animal.age > animal.lifespan:
                    self.plant_food_supply += animal.size
                    self.animals.remove(animal)
                else:
                    if animal.food_type == 'plants':
                        if self.plant_food_supply > 0:
                            self.plant_food_supply -= 1
                            animal.satiety += 26
                        else:
                            animal.satiety -= 9
                    elif animal.food_type == 'animals':
                        prey = random.choice(self.animals)
                        if prey.name != animal.name:
                            if random.random() < 0.5:
                                animal.satiety += 53
                                self.animals.remove(prey)
                        else:
                            animal.satiety -= 16
                if animal.satiety < 10:
                    self.animals.remove(animal)
            time.sleep(unit_time)

flora = DefFlora()

bullets = []

initial_animals = [
    ('fish1', "Fish", 10, "plants", "water", 150),
    ('eagle1', "Eagle", 15, "animals", "air", 100),
    ('lion1', "Lion", 15, "animals", "land", 150),
('fish1', "Fish", 10, "plants", "water", 150),
    ('eagle1', "Eagle", 10, "animals", "air", 100),
    ('lion1', "Lion", 15, "animals", "land", 150),
('fish1', "Fish", 10, "plants", "water", 150),
    ('eagle1', "Eagle", 15, "animals", "air", 100),
    ('lion1', "Lion", 15, "animals", "land", 150),
('fish1', "Fish", 10, "plants", "water", 150),
    ('eagle1', "Eagle", 15, "animals", "air", 100),
    ('lion1', "Lion", 15, "animals", "land", 150),
('fish1', "Fish", 10, "plants", "water", 150),
    ('eagle1', "Eagle", 15, "animals", "air", 100),
    ('lion1', "Lion", 15, "animals", "land", 150),
('fish1', "Fish", 10, "plants", "water", 150),
    ('eagle1', "Eagle", 15, "animals", "air", 100),
    ('lion1', "Lion", 15, "animals", "land", 150),
('fish1', "Fish", 10, "plants", "water", 150),
    ('eagle1', "Eagle", 15, "animals", "air", 100),
    ('lion1', "Lion", 15, "animals", "land", 150),
('fish1', "Fish", 10, "plants", "water", 150),
    ('eagle1', "Eagle", 15, "animals", "air", 100),
    ('lion1', "Lion", 15, "animals", "land", 150),
('fish1', "Fish", 10, "plants", "water", 150),
    ('eagle1', "Eagle", 15, "animals", "air", 100),
    ('lion1', "Lion", 15, "animals", "land", 150),('fish1', "Fish", 10, "plants", "water", 150),
    ('eagle1', "Eagle", 15, "animals", "air", 100),
    ('lion1', "Lion", 15, "animals", "land", 150),
]


def time_plus(self):
    global time_animal_world
    time_animal_world += 1
class player_waze:


    def check_collision(self,x, y, image):
        flag = 0
        # Проверка цвета пикселя под игроком
        for i in range(2):
            color = image.get_at((x+i, y+i))
            if color == (0,0,0) :
                flag =1
        if flag ==1:
            return True
        else:
            return False



def cycle3_pygame_click():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or flora.animals == []:
            pygame.quit()
            done = True
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                flora.add_animal(
                    Animal(text_get('Name'), text_get('Type'), int(text_get('Size')), text_get('Food type'),
                           text_get('Habitat'), int(text_get('Lifespan'))))
            if event.key == pygame.K_3:
                flora.add_food()
            if event.key == pygame.K_4:
                flora.reproduce(flora.animals[int(text_get('number 1 animal'))],
                                flora.animals[int(text_get('number 2 animal'))])

            if event.key == pygame.K_5:
                flora.information()
            if event.key == pygame.K_9:
                player.my_stats('self')
def check_collision(animal_list):
    global bullets
    while len(bullets)>1:
        del bullets[1]
    for bullet in bullets:
        player.chek_arround_2("self", animal_list,bullet['pos'][0], bullet['pos'][1])
def pygame_cycle():


        animal_list = {}
        screen = pygame.display.set_mode((900, 600))
        color_inactive = pygame.Color((0, 128, 255))
        color = color_inactive
        clock = pygame.time.Clock()

        player_pos = [80, 200]
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        BLUE = (0, 0, 255)
        WIDTH, HEIGHT = 900, 600

        # Загрузка изображения лабиринта
        image = pygame.image.load("C:\\Users\schuk\OneDrive\Рабочий стол\maze2.png")
        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
        maze_rect = image.get_rect()
        done = False
        while not done:
            threading.Thread(target=cycle3_pygame_click())
            for animal in flora.animals:
                to_remove = []
                for animal_check in animal_list:
                    if animal_check not in flora.animals:
                        to_remove.append(animal_check)
                for animal_check in to_remove:
                    del animal_list[animal_check]
                if animal not in animal_list:
                    animal_list[animal] = pygame.Rect(random.uniform(10, 885),  random.uniform(10, 585), animal.size, animal.size)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                direction = 'left'
                player_pos = player1.move_player(player_pos, direction, 5, image)
                player.life("self", animal_list, player_pose1=player_pos[0], player_pose2=player_pos[1])
            if keys[pygame.K_RIGHT]:
                direction = 'right'
                player_pos =  player1.move_player(player_pos, direction, 5, image)
                player.life("self", animal_list, player_pose1=player_pos[0], player_pose2=player_pos[1])
            if keys[pygame.K_UP]:
                direction = 'up'
                player_pos =  player1.move_player(player_pos, direction, 5, image)
                player.life("self", animal_list, player_pose1=player_pos[0], player_pose2=player_pos[1])
            if keys[pygame.K_DOWN]:
                direction = 'down'
                player_pos =  player1.move_player(player_pos, direction, 5, image)
                player.life("self", animal_list, player_pose1=player_pos[0], player_pose2=player_pos[1])
            if keys[pygame.K_SPACE]:
                player1.shooting(player_pos,bullets, direction)

            handle_bullets()
            check_collision(animal_list)

            thread3 = threading.Thread(target=cycle5(animal_list, player_pos))
            thread3.start()

            screen.fill((0, 0, 0))
            screen.blit(image, maze_rect)
            pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player1.size, player1.size))
            for animal in animal_list:
                list_pouse = []
                for i in str(animal_list[animal]).strip('<rect(').split(','):
                    if len(list_pouse) == 2:
                        break
                    list_pouse.append(int(i))

                pouse_1 = int(list_pouse[0]) + random.uniform(0, 2) + random.uniform(-1, 0)
                pouse_2 = int(list_pouse[1]) + random.uniform(0, 2)+ random.uniform(-1, 0)
                if pouse_1 > 890or pouse_2 > 590 :
                    pouse_1 =list_pouse[0]
                    pouse_2 =list_pouse[1]
                elif pouse_1 <15 or pouse_2 < 15:
                    pouse_1 = int(list_pouse[0]) +1
                    pouse_2 = int(list_pouse[1]) +1
                elif not player_waze.check_collision('self',x = int(pouse_1 ),y = int(pouse_2), image=image):
                    pouse_1 = list_pouse[0]
                    pouse_2 = list_pouse[1]

                animal_list[animal] = pygame.Rect(int(pouse_1), int(pouse_2), animal.size, animal.size)
                if animal.food_type == 'animals':
                    color = (9,100,100)
                    pygame.draw.rect(screen, color, animal_list[animal], 2)
                elif animal.food_type == 'plants':
                    color = (0, 0, 255)
                    pygame.draw.rect(screen, color, animal_list[animal], 2)



            pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player1.size, player1.size))
            for bullet in bullets:
                pygame.draw.rect(screen, (0, 255, 0), (bullet['pos'][0], bullet['pos'][1], 5, 5))
            pygame.display.flip()
            clock.tick(60)
def cycle5(animal_list, player_pos):


    for event in pygame.event.get():
        if event.type == pygame.QUIT or flora.animals == []:
            pygame.quit()
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                player.chek_arround("self", animal_list, player_pose1 =player_pos[0], player_pose2 = player_pos[1])

class MainClass:
    def function_main(self):

        for name, type_animal, size, food_type, habitat, lifespan in initial_animals:
            flora.add_animal(Animal(name, type_animal, size, food_type, habitat, lifespan))

        thread2 = threading.Thread(target=pygame_cycle)
        thread1 = threading.Thread(target=flora.death_life)


        thread2.start()
        thread1.start()

if __name__ == "__main__":
    main_class = MainClass()
    main_class.function_main()