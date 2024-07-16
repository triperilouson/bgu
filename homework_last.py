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
            text = text_get(
                f'{animal.type_animal}, \n{animal.name}, \n{animal.satiety}, \n{animal.food_type}, \n{animal.lifespan},\n {animal.age}, \n{animal.gender}')
            print(animal)

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
            try:
                time_plus()
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
            except Exception:
                print('stop')

flora = DefFlora()

initial_animals = [
    ('fish1', "Fish", 100, "plants", "water", 150),
    ('eagle1', "Eagle", 150, "animals", "air", 100),
    ('lion1', "Lion", 150, "animals", "land", 150),
('fish1', "Fish", 100, "plants", "water", 150),
    ('eagle1', "Eagle", 150, "animals", "air", 100),
    ('lion1', "Lion", 150, "animals", "land", 150),
('fish1', "Fish", 100, "plants", "water", 150),
    ('eagle1', "Eagle", 150, "animals", "air", 100),
    ('lion1', "Lion", 150, "animals", "land", 150),
('fish1', "Fish", 100, "plants", "water", 150),
    ('eagle1', "Eagle", 150, "animals", "air", 100),
    ('lion1', "Lion", 150, "animals", "land", 150),
('fish1', "Fish", 100, "plants", "water", 150),
    ('eagle1', "Eagle", 150, "animals", "air", 100),
    ('lion1', "Lion", 150, "animals", "land", 150),
('fish1', "Fish", 100, "plants", "water", 150),
    ('eagle1', "Eagle", 150, "animals", "air", 100),
    ('lion1', "Lion", 150, "animals", "land", 150),
('fish1', "Fish", 100, "plants", "water", 150),
    ('eagle1', "Eagle", 150, "animals", "air", 100),
    ('lion1', "Lion", 150, "animals", "land", 150),
('fish1', "Fish", 100, "plants", "water", 150),
    ('eagle1', "Eagle", 150, "animals", "air", 100),
    ('lion1', "Lion", 150, "animals", "land", 150),
('fish1', "Fish", 100, "plants", "water", 150),
    ('eagle1', "Eagle", 150, "animals", "air", 100),
    ('lion1', "Lion", 150, "animals", "land", 150),('fish1', "Fish", 100, "plants", "water", 150),
    ('eagle1', "Eagle", 150, "animals", "air", 100),
    ('lion1', "Lion", 150, "animals", "land", 150),
]

def time_plus():
    global time_animal_world
    time_animal_world += 1

def pygame_cycle():
        animal_list = {}
        screen = pygame.display.set_mode((900, 600))
        color_inactive = pygame.Color((0, 128, 255))
        color = color_inactive
        clock = pygame.time.Clock()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        flora.add_animal(Animal(text_get('Name'), text_get('Type'), int(text_get('Size')), text_get('Food type'), text_get('Habitat'), int(text_get('Lifespan'))))
                    if event.key == pygame.K_3:
                        flora.add_food()
                    if event.key == pygame.K_4:
                        lora.reproduce(flora.animals[int(text_get('number 1 animal'))],flora.animals[int(text_get('number 2 animal'))])
                    if event.key == pygame.K_5:
                        flora.information()

                for animal in flora.animals:
                    to_remove = []
                    for animal_check in animal_list:
                        if animal_check not in flora.animals:
                            to_remove.append(animal_check)
                    for animal_check in to_remove:
                        del animal_list[animal_check]
                    if animal not in animal_list:
                        animal_list[animal] = pygame.Rect(random.uniform(0, 900),  random.uniform(0, 600), 10,10)

                screen.fill((0, 0, 0))
                for animal in animal_list:
                    pygame.draw.rect(screen, color, animal_list[animal], 2)
                    clock.tick(60)
                    pygame.display.flip()

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