import pygame
import random
import time
pygame.init()
width, height = 1200, 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class SomeBar:
    def __init__(self):
        self.height = 45
        self.x = 0
        self.y = height - self.height
        self.color = (0, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, width, height - self.height)
        # ____tree____
        self.tree = pygame.image.load(r"my_shit/Tree an nature/tree_1.png").convert_alpha()
        self.tree_rect = self.tree.get_rect(topleft=(self.x + 10, self.y))
        self.tree_selected = False
        # ____tree____

    def draw_placing_bar(self):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.tree_selected:
            pygame.draw.rect(screen, (255, 255, 255), self.tree_rect)
        screen.blit(self.tree, self.tree_rect)


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
placing_bar = SomeBar()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if placing_bar.tree_rect.collidepoint(event.pos):
                placing_bar.tree_selected = True

            # this needs fixing
            elif placing_bar.tree_selected:
                if placing_bar.rect.collidepoint(event.pos) or placing_bar.tree_rect.collidepoint(event.pos):
                    placing_bar.tree_selected = False
                else:
                    x, y = event.pos
                    tree = Tree(x, y)
                    tree_group.add(tree)
            # this needs fixing

    screen.fill((0, 100, 0))

    # jk
    '''
    tree = Tree(random.randint(0, width), random.randint(0, height))
    tree_group.add(tree)
    if len(tree_group) % 5 == 0:
        rock = NormalRock(random.randint(0, width), random.randint(0, height))
        normal_rock_group.add(rock)
    '''
    # jk
    #normal_rock_group.draw(screen)
    tree_group.draw(screen)
    placing_bar.draw_placing_bar()
    pygame.display.flip()
    clock.tick(60)