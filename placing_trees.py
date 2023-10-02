import pygame
import random
pygame.init()
width, height = 1000, 700
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


tree_group = pygame.sprite.Group()
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            place_x, place_y = event.pos
            tree = Tree(place_x, place_y)
            tree_group.add(tree)
            with open("something.txt", "a") as f:
                f .write(f"({place_x}, {place_y})\n")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                with open("something.txt", "r") as file:
                    for line in file:
                        print(line)
                        place_x, place_y = map(int, line.strip('()\n').split(', '))
                        tree = Tree(place_x, place_y)
                        tree_group.add(tree)

    screen.fill((0, 100, 0))
    tree_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)
