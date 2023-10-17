import pygame
import random
pygame.init()
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
type_of_rock = 0
type_of_rock_dict = {
    1: "normal_rock",
    2: "steel_rock",
    3: "gold_rock",
}


class Tree(pygame.sprite.Sprite):
    def __init__(self, place_x, place_y):
        super().__init__()
        self.place_x = place_x
        self.place_y = place_y
        tree_images = [
            pygame.transform.rotate(pygame.image.load("my_shit/Tree an nature/tree_0.png").convert_alpha(),
                                    random.randint(0, 355)),
            pygame.transform.rotate(pygame.image.load("my_shit/Tree an nature/tree_1.png").convert_alpha(),
                                    random.randint(0, 355)),
            pygame.transform.rotate(pygame.image.load("my_shit/Tree an nature/tree_2.png").convert_alpha(),
                                    random.randint(0, 355)),
            pygame.transform.rotate(pygame.image.load("my_shit/Tree an nature/tree_3.png").convert_alpha(),
                                    random.randint(0, 355)),
            pygame.transform.rotate(pygame.image.load("my_shit/Tree an nature/tree_4.png").convert_alpha(),
                                    random.randint(0, 355)),
            ]
        self.image = random.choice(tree_images)
        self.rect = self.image.get_rect(center=(place_x, place_y))


class Rock(pygame.sprite.Sprite):
    def __init__(self, place_x, place_y, key):
        super().__init__()
        self.place_x = place_x
        self.place_y = place_y
        self.type_of_rock = key
        if key == 1:

            normal_rock_list = [
                pygame.transform.rotate(pygame.image.load(r"my_shit/Rocks/normal_rocks/normal_rock_1.png").convert_alpha(),
                                        random.randint(0, 355)),
                pygame.transform.rotate(pygame.image.load(r"my_shit/Rocks/normal_rocks/normal_rock_2.png").convert_alpha(),
                                        random.randint(0, 355)),
                pygame.transform.rotate(pygame.image.load(r"my_shit/Rocks/normal_rocks/normal_rock_3.png").convert_alpha(),
                                        random.randint(0, 355)),
                pygame.transform.rotate(pygame.image.load(r"my_shit/Rocks/normal_rocks/normal_rock_4.png").convert_alpha(),
                                        random.randint(0, 355)),
                pygame.transform.rotate(pygame.image.load(r"my_shit/Rocks/normal_rocks/normal_rock_5.png").convert_alpha(),
                                        random.randint(0, 355)),
            ]
            self.image = random.choice(normal_rock_list)
            self.rect = self.image.get_rect(center=(place_x, place_y))
        elif key == 2:
            steel_rock_list = [
                pygame.transform.rotate(pygame.image.load(r"my_shit/Rocks/steel_rock/steel_rock_1.png").convert_alpha(),
                                        random.randint(0, 355)),
                pygame.transform.rotate(pygame.image.load(r"my_shit/Rocks/steel_rock/steel_rock_2.png").convert_alpha(),
                                        random.randint(0, 355))
            ]
            self.image = random.choice(steel_rock_list)
            self.rect = self.image.get_rect(center=(place_x, place_y))
        elif key == 3:
            gold_rock_list = [
                pygame.transform.rotate(pygame.image.load(r"my_shit/Rocks/gold_rocks/gold_rock_1.png").convert_alpha(),
                                        random.randint(0, 355))
            ]
            self.image = random.choice(gold_rock_list)
            self.rect = self.image.get_rect(center=(place_x, place_y))



class HQ(pygame.sprite.Sprite):
    def __init__(self, place_x, place_y):
        super().__init__()
        self.place_x = place_x
        self.place_y = place_y
        self.image = pygame.image.load("my_shit/Buildings/HQ.png")
        self.rect = self.image.get_rect(center=(place_x, place_y))


rock_group = pygame.sprite.Group()
tree_group = pygame.sprite.Group()
building_group = pygame.sprite.Group()
'''
for thing in range(20):
    place_x = random.randint(0, width)
    place_y = random.randint(0, height)
    tree = Tree(place_x, place_y)
    tree_group.add(tree)
    with open("something.txt", "a") as f:
        f.write(f"({place_x}, {place_y})\n")
'''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                type_of_rock = 1
            elif event.key == pygame.K_2:
                type_of_rock = 2
            elif event.key == pygame.K_3:
                type_of_rock = 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_buttons_status = pygame.mouse.get_pressed(3)
            left_mouse_button = mouse_buttons_status[0]
            right_mouse_button = mouse_buttons_status[2]
            if left_mouse_button and type_of_rock != 0:
                place_x, place_y = event.pos
                rock = Rock(place_x, place_y, type_of_rock)
                rock_group.add(rock)
                with open("my_shit/Tree an nature/rock_placement.txt", "a") as file:
                    file.write(f"({place_x}, {place_y}) - {type_of_rock_dict[type_of_rock]} \n")
                '''
                place_x, place_y = event.pos
                if not building_group:
                    hq = HQ(place_x, place_y)
                    building_group.add(hq)
                    with open("building_placement.txt", "a") as f:
                        f .write(f"({place_x}, {place_y}) - hq \n")
                '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                with open("my_shit/Tree an nature/tree_placement.txt", "r") as file:
                    for line in file:
                        place_x, place_y = map(int, line.strip('()\n').split(', '))
                        tree = Tree(place_x, place_y)
                        tree_group.add(tree)
                with open("my_shit/Buildings/building_placement.txt", "r") as file:
                    for line in file:
                        place_cord, type = line.split(" - ")
                        place_x, place_y = map(int, place_cord.strip("()\n").split(", "))
                        hq = HQ(place_x, place_y)
                        building_group.add(hq)


    screen.fill((0, 100, 0))
    tree_group.draw(screen)
    rock_group.draw(screen)
    building_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)
