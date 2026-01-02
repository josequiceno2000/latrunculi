import pygame
from src.ui import UI

def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    program_icon = pygame.image.load("./assets/images/chess_icon.png")
    pygame.display.set_icon(program_icon)
    pygame.display.set_caption("Latrunculi")
    clock = pygame.time.Clock()
    
    ui = UI()
    ui.load_assets()


    player_pos = pygame.Vector2(screen.get_width() // 2, screen.get_height() // 2)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.FULLSCREEN:
                pygame.display.toggle_fullscreen()

        screen.fill(("darkblue"))

        king_surface = pygame.image.load("./assets/images/white_king.svg")
        converted_king_surface = pygame.Surface.convert_alpha(king_surface)

        screen.blit(converted_king_surface, player_pos)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt  

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()