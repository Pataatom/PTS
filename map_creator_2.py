import pygame
import random
import time
pygame.init()
width, height = 1200, 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Maintenance:
    @staticmethod
    def clear():
        for tree in tree_group:
            tree_group.remove(tree)
        for rock in rock_group:
            rock_group.remove(rock)
    @staticmethod
    def load():
        tree_group.empty()
        rock_group.empty()
        with open("my_shit/Tree an nature/tree_placement.txt", "r") as f:
            for line in f:
                place_x, place_y = map(int, line.strip('()\n').split(', '))
                tree = Tree(place_x, place_y)
                tree_group.add(tree)
        with open("my_shit/Rocks/rock_placement.txt", "r") as f:
            for line in f:
                place_x, place_y = map(int, line.strip('()\n').split(', '))
                rock = NormalRock(place_x, place_y)
                rock_group.add(rock)
    @staticmethod
    def save():
        with open("my_shit/Tree an nature/tree_placement.txt", "w") as f:
            for tree in tree_group:
                f.write(f"{tree.place_x, tree.place_y}\n")
        with open("my_shit/Rocks/rock_placement.txt", "w") as f:
            for rock in rock_group:
                f.write(f"{rock.place_x, rock.place_y}\n")

            ''' maybe someday
            for type in ("normal", "iron", "gold"):
                with open(f"test_{type}_rock.txt", "w") as f:
                    for rock in rock_group:
                        if rock.type == f"{type}":
                            f.write(f"{rock.place_x, rock.place_y}\n")
            '''

class SomeBar:
    def __init__(self):
        self.height = 45
        self.x = 0
        self.y = height - self.height
        self.color = (57, 60, 61)
        self.rect = pygame.Rect(self.x, self.y, width, height - self.height)
        # ____tree____
        self.tree = pygame.image.load(r"my_shit/Tree an nature/tree_1.png").convert_alpha()
        self.tree_rect = self.tree.get_rect(topleft=(self.x + 10, self.y))
        self.tree_selected = False
        # ____tree____

        # ____normal_rock____
        self.normal_rock = pygame.image.load(r"my_shit/Rocks/normal_rocks/normal_rock_1.png").convert_alpha()
        self.normal_rock_rect = self.normal_rock.get_rect(topleft=(self.x + 20 + self.tree_rect.width, self.y))
        self.normal_rock_selected = False
        # ____normal_rock____


    def draw_placing_bar(self):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.tree_selected:
            pygame.draw.rect(screen, (255, 255, 255), self.tree_rect)
        elif self.normal_rock_selected:
            pygame.draw.rect(screen, (255, 255, 255), self.normal_rock_rect)
        screen.blit(self.tree, self.tree_rect)
        screen.blit(self.normal_rock, self.normal_rock_rect)


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
        self.type = "normal"
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

rock_group = pygame.sprite.Group()
tree_group = pygame.sprite.Group()
placing_bar = SomeBar() #object of class Some bar
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # changes in environment
        if event.type == pygame.KEYDOWN:

            # clearing the workplace
            if event.key == pygame.K_DELETE:
                Maintenance.clear()
            # clearing the workplace

            # saving
            if event.key == pygame.K_DOWN:
                Maintenance.save()
            # saving

            # loading
            if event.key == pygame.K_UP:
                Maintenance.load()
            # loading
        # changes in environment

        if event.type == pygame.MOUSEBUTTONDOWN:

            # mapping the mouse buttons
            mouse_buttons_status = pygame.mouse.get_pressed(3)
            left_mouse_button = mouse_buttons_status[0]
            right_mouse_button = mouse_buttons_status[2]
            # mapping the mouse buttons

            if right_mouse_button:
                for tree in tree_group:
                    if tree.rect.collidepoint(event.pos):
                        tree_group.remove(tree)
                for rock in rock_group:
                    if rock.rect.collidepoint(event.pos):
                        rock_group.remove(rock)

            # placing trees
            if placing_bar.tree_selected:
                if placing_bar.rect.collidepoint(event.pos) or placing_bar.tree_rect.collidepoint(event.pos):
                    placing_bar.tree_selected = False
                elif left_mouse_button:
                    x, y = event.pos
                    tree = Tree(x, y)
                    tree_group.add(tree)
            elif placing_bar.tree_rect.collidepoint(event.pos):
                placing_bar.tree_selected = True
            # placing trees

            # placing normal_rocks
            if placing_bar.normal_rock_selected:
                if placing_bar.rect.collidepoint(event.pos) or placing_bar.normal_rock_rect.collidepoint(event.pos):
                    placing_bar.normal_rock_selected = False
                elif left_mouse_button:
                    x, y = event.pos
                    normal_rock = NormalRock(x, y)
                    rock_group.add(normal_rock)
            elif placing_bar.normal_rock_rect.collidepoint(event.pos):
                placing_bar.normal_rock_selected = True
            # placing normal_rocks

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
    rock_group.draw(screen)
    tree_group.draw(screen)
    placing_bar.draw_placing_bar()
    pygame.display.flip()
    clock.tick(60)