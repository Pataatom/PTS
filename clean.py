import pygame
import random
# ____BASIC_SHIT____(VAR_INIT)
pygame.init()
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
units = []
selected_unit = None
scout_basic_image_path_01 = "my_shit/Units/Scout/pixil-frame-0 (1).png"
lumber_basic_image_path_01 = "my_shit/Units/Lumber/Lumber Basic.png"
WHITE = (255, 255, 255)
# ____BASIC_SHIT____(VAR_INIT)


# ____UNITS_BUILDING_AND_SHIT_MENU____
class SomeBar:
    def __init__(self):
        self.height = 45
        self.x = 0
        self.y = height - self.height
        self.color = (0,0,0)
        self.rect = pygame.Rect(self.x, self.y, width, height - self.height)
        # ____scout____
        self.scout = pygame.image.load("my_shit/Units/Scout/pixil-frame-0 (1).png").convert_alpha()
        self.scout_transformed = pygame.transform.scale2x(self.scout)
        self.scout_rect = self.scout_transformed.get_rect(topleft=(self.x + 10, self.y))
        self.scout_selected = False
        # ____scout____

    def draw_unit_bar(self):
        pygame.draw.rect(screen, self.color, self.rect)
        if unit_bar.scout_selected:
            pygame.draw.rect(screen, (255, 255, 255), unit_bar.scout_rect)
        screen.blit(self.scout_transformed, self.scout_rect)
# ____UNITS_BUILDING_AND_SHIT_MENU____


# ____SCOUT_CLASS____
class Scout:
    def __init__(self, x, y):
        self.image = pygame.image.load(scout_basic_image_path_01).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 1
        self.state = "up"
        self.moving = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.hit_something = False
        self.state_dict = {
            "up": self.image,
            "down": pygame.transform.rotate(self.image, 180),
            "left": pygame.transform.rotate(self.image, 90),
            "right": pygame.transform.rotate(self.image, 270)
        }

    def auto_movement(self, target_x, target_y):
        global selected_unit
        distance_x = abs(target_x - self.rect.centerx)
        distance_y = abs(target_y - self.rect.centery)
        if distance_x <= distance_y:
            if self.rect.centerx > target_x:
                self.rect.centerx -= self.speed
                self.state = "left"
            elif self.rect.centerx < target_x:
                self.rect.centerx += self.speed
                self.state = "right"
            elif self.rect.centery > target_y:
                self.rect.centery -= self.speed
                self.state = "up"
            elif self.rect.centery < target_y:
                self.rect.centery += self.speed
                self.state = "down"
        elif abs(target_x - self.rect.centerx) > abs(target_y - self.rect.centery):
            if self.rect.centery > target_y:
                self.rect.centery -= self.speed
                self.state = "up"
            elif self.rect.centery < target_y:
                self.rect.centery += self.speed
                self.state = "down"
            elif self.rect.centerx > target_x:
                self.rect.centerx -= self.speed
                self.state = "left"
            elif self.rect.centerx < target_x:
                self.rect.centerx += self.speed
                self.state = "right"

        if self.rect.centerx == target_x and self.rect.centery == target_y:
            self.moving = False
            self.hit_something = False
        return self.state

    def clicked_on_unit(self):
        global selected_unit

        if selected_unit is None:
            selected_unit = self
            self.moving = False

        elif selected_unit is not None and selected_unit != self:
            selected_unit = self

        else:
            selected_unit = None

    def place_on_screen(self):
        screen.blit(self.state_dict[self.state], self.rect)

    def backup_from_hit(self, axis):
        if axis == "x":
            if self.state == "up":
                return self.rect.centerx
            elif self.state == "down":
                return self.rect.centerx
            elif self.state == "left":
                return self.rect.centerx + 10
            elif self.state == "right":
                return self.rect.centerx - 10
        elif axis == "y":
            if self.state == "up":
                return self.rect.centery + 10
            elif self.state == "down":
                return self.rect.centery - 10
            elif self.state == "left":
                return self.rect.centery
            elif self.state == "right":
                return self.rect.centery
# ____SCOUT_CLASS____


# ____LUMBER_CLASS____
class Lumber(Scout):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(lumber_basic_image_path_01).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.state_dict = {
            "up": self.image,
            "down": pygame.transform.rotate(self.image, 180),
            "left": pygame.transform.rotate(self.image, 90),
            "right": pygame.transform.rotate(self.image, 270)
        }

    def place_on_screen(self):
        screen.blit(self.state_dict[self.state], self.rect)
# ____LUMBER_CLASS____


# ____TREE____
class Tree(pygame.sprite.Sprite):
    def __init__(self, place_x, place_y):
        super().__init__()
        self.place_x = place_x
        self.place_y = place_y
        tree_images = [
            pygame.transform.rotate(pygame.image.load("my_shit/Tree an nature/tree_0.png").convert_alpha(),
                                    random.randint(0, 359)),
            pygame.transform.rotate(pygame.image.load("my_shit/Tree an nature/tree_1.png").convert_alpha(),
                                    random.randint(0, 359)),
            pygame.transform.rotate(pygame.image.load("my_shit/Tree an nature/tree_2.png").convert_alpha(),
                                    random.randint(0, 359)),
            pygame.transform.rotate(pygame.image.load("my_shit/Tree an nature/tree_3.png").convert_alpha(),
                                    random.randint(0, 359)),
            pygame.transform.rotate(pygame.image.load("my_shit/Tree an nature/tree_4.png").convert_alpha(),
                                    random.randint(0, 359)),
            ]
        self.image = random.choice(tree_images)
        self.rect = self.image.get_rect(center=(place_x, place_y))

# ____TREE____


units.append(Lumber(500, 200))
unit_bar = SomeBar()
tree_group = pygame.sprite.Group()

# loading tree placement from file
with open("my_shit/Tree an nature/tree_placement.txt", "r") as file:
    for line in file:
        place_x, place_y = map(int, line.strip('()\n').split(', '))
        tree = Tree(place_x, place_y)
        tree_group.add(tree)
# loading tree placement from file

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            # selecting scout unit
            # need to fix the issue when you have selected unit and click on another unit prbly some for loop
            # fckn redo this shit
            if units:
                for unit in units:
                    if unit.rect.collidepoint(event.pos):
                        unit.clicked_on_unit()

                    elif not unit.rect.collidepoint(event.pos) and selected_unit == unit:
                        selected_unit.mouse_x, selected_unit.mouse_y = event.pos
                        selected_unit.moving = True
            # selecting scout unit

            if unit_bar.scout_rect.collidepoint(event.pos):
                unit_bar.scout_selected = True
            if units:
                if not unit.rect.collidepoint(event.pos) and not unit_bar.scout_rect.collidepoint(event.pos)\
                        and unit_bar.scout_selected and not unit_bar.rect.collidepoint(event.pos):
                    x, y = event.pos
                    units.append(Scout(x, y))
                    unit_bar.scout_selected = False
            else:
                if not unit_bar.scout_rect.collidepoint(event.pos)\
                        and unit_bar.scout_selected and not unit_bar.rect.collidepoint(event.pos):
                    x, y = event.pos
                    units.append(Scout(x, y))
                    unit_bar.scout_selected = False

    # ____WORLD____
    screen.fill((0, 100, 0))
    tree_group.draw(screen)
    # ____WORLD____

    # ____UNITS_LOWER_MENU____
    unit_bar.draw_unit_bar()
    # ____UNITS_LOWER_MENU____

    # ____UNITS____

    for unit in units:

        for standing_unit in units:
            if unit != standing_unit:
                if unit.rect.colliderect(standing_unit.rect) and unit.moving:
                    unit.hit_something = True
                    backup_x, backup_y = unit.backup_from_hit("x"), unit.backup_from_hit("y")

        if unit is selected_unit:
            if selected_unit.moving:
                selected_unit = None
            elif not selected_unit.moving:
                pygame.draw.rect(screen, WHITE, selected_unit.rect)

        if unit.moving and not unit.hit_something:
            unit.auto_movement(unit.mouse_x, unit.mouse_y)
        elif unit.moving and unit.hit_something:
            unit.auto_movement(backup_x, backup_y)
        unit.place_on_screen()
    # ____UNITS____
    pygame.display.flip()
    clock.tick(60)
