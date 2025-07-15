import pygame
import sys
import pygame_gui
pygame.init()
screen = pygame.display.set_mode((500, 500))
manager = pygame_gui.UIManager((500, 500))
clock = pygame.time.Clock()
text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(50, 50, 300, 200), manager=manager,
                                                 object_id= "#main_text_entry")

def get_user_name():
    while True:
        ui_refresh_rate = clock.tick(60)/1000
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            manager.process_events(event)
        manager.update(ui_refresh_rate)
        manager.draw_ui(screen)
        pygame.display.update()
        clock.tick(60)


get_user_name()