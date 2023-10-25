import pygame
import random
pygame.init()
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


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


class HQ(pygame.sprite.Sprite):
    def __init__(self, place_x, place_y):
        super().__init__()
        self.place_x = place_x
        self.place_y = place_y
        self.image = pygame.image.load("my_shit/Buildings/HQ.png")
        self.rect = self.image.get_rect(center=(place_x, place_y))


class NormalRock(pygame.sprite.Sprite):
    def __init__(self, place_x, place_y):
        super().__init__()
        self.place_x = place_x
        self.place_y = place_y
        self.normal_rock_list = [
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
        self.image = random.choice(self.normal_rock_list)
        self.rect = self.image.get_rect(center=(place_x, place_y))

normal_rock_group = pygame.sprite.Group()
tree_group = pygame.sprite.Group()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill((0, 100, 0))
    # jk
    rock = NormalRock(random.randint(0, width), random.randint(0, height))
    normal_rock_group.add(rock)
    tree = Tree(random.randint(0, width), random.randint(0, height))
    tree_group.add(tree)
    # jk
    normal_rock_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)