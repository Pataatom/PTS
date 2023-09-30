class Scout:
    def __init__(self, x, y):
        self.image = pygame.image.load("my_shit/pixil-frame-0 (1).png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2
        self.state = "up"
        self.state_dict = {
            "up": self.image,
            "down": pygame.transform.rotate(self.image, 180),
            "left": pygame.transform.rotate(self.image, 90),
            "right": pygame.transform.rotate(self.image, 270)
        }

    def scout_auto(self, x, y):
        if x % 2 != 0:
            x += 1
        if y % 2 != 0:
            y += 1
        if  self.rect.centerx > x:
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
        return self.state

    def place_on_screen(self):
        screen.blit(self.state_dict[self.state], self.rect)