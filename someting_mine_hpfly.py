import pygame

# ____BASIC_SHIT____
pygame.init()
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
scouts = []
selected_unit = None
# ____BASIC_SHIT____


# ____UNITS_BUILDING_AND_SHIT_MENU____
class Units_Bar:
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
        self.image = pygame.image.load("my_shit/Units/Scout/pixil-frame-0 (1).png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 1
        self.state = "up"
        self.moving = False
        self.clicked_num = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.state_dict = {
            "up": self.image,
            "down": pygame.transform.rotate(self.image, 180),
            "left": pygame.transform.rotate(self.image, 90),
            "right": pygame.transform.rotate(self.image, 270)
        }

    def scout_auto(self, x, y):
        global selected_unit
        if abs(x - self.rect.centerx) <= abs(y - self.rect.centery):
            if self.rect.centerx > x:
                self.rect.centerx -= self.speed
                self.state = "left"
            elif self.rect.centerx < x:
                self.rect.centerx += self.speed
                self.state = "right"
            elif self.rect.centery > y:
                self.rect.centery -= self.speed
                self.state = "up"
            elif self.rect.centery < y:
                self.rect.centery += self.speed
                self.state = "down"
        elif abs(x - self.rect.centerx) > abs(y - self.rect.centery):
            if self.rect.centery > y:
                self.rect.centery -= self.speed
                self.state = "up"
            elif self.rect.centery < y:
                self.rect.centery += self.speed
                self.state = "down"
            elif self.rect.centerx > x:
                self.rect.centerx -= self.speed
                self.state = "left"
            elif self.rect.centerx < x:
                self.rect.centerx += self.speed
                self.state = "right"

        if self.rect.centerx == x and self.rect.centery == y:
            self.moving = False
        return self.state

    def clicked_on_scout(self):
        global selected_unit
        if self.clicked_num == 0:
            selected_unit = self
            self.clicked_num = 1
            self.moving = False
        else:
            selected_unit = None
            self.clicked_num = 0

    def place_on_screen(self):
        screen.blit(self.state_dict[self.state], self.rect)
# ____SCOUT_CLASS____


# scout = Scout(width/2, height/2)
unit_bar = Units_Bar()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            # selecting scout unit
            # need to fix the issue when you have selected unit and click on another unit
            if scouts:
                for scout in scouts:
                    if scout.rect.collidepoint(event.pos):
                        scout.clicked_on_scout()
                    elif not scout.rect.collidepoint(event.pos):
                        if scout is selected_unit:
                            selected_unit.mouse_x, selected_unit.mouse_y = event.pos
                            selected_unit.moving = True
            # selecting scout unit

            if unit_bar.scout_rect.collidepoint(event.pos):
                unit_bar.scout_selected = True
            if scouts:
                if not scout.rect.collidepoint(event.pos) and not unit_bar.scout_rect.collidepoint(event.pos)\
                        and unit_bar.scout_selected and not unit_bar.rect.collidepoint(event.pos):
                    x, y = event.pos
                    scouts.append(Scout(x, y))
                    unit_bar.scout_selected = False
            else:
                if not unit_bar.scout_rect.collidepoint(event.pos)\
                        and unit_bar.scout_selected and not unit_bar.rect.collidepoint(event.pos):
                    x, y = event.pos
                    scouts.append(Scout(x, y))
                    unit_bar.scout_selected = False

    # ____WORLD____
    screen.fill((0, 100, 0))
    # ____WORLD____

    # ____UNITS_LOWER_MENU____
    unit_bar.draw_unit_bar()
    # ____UNITS_LOWER_MENU____

    # ____UNITS____

    for scout in scouts:
        if scout is selected_unit:
            if selected_unit.moving:
                selected_unit = None
                scout.clicked_num = 0
            elif not selected_unit.moving:
                pygame.draw.rect(screen, (255,255,255), selected_unit.rect)
        if scout.moving: # if scout.moving and selected_unit is not None and scout is selected_unit:
            scout.scout_auto(scout.mouse_x, scout.mouse_y)
        scout.place_on_screen()
    # ____UNITS____
    pygame.display.flip()
    clock.tick(60)
