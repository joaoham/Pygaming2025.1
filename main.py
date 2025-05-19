import pygame
from core.player import Player
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hollow Mooni")
    clock = pygame.time.Clock()

    player = Player((100, 500))
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    running = True
    while running:
        screen.fill((30, 30, 30))
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update(keys)
        for sprite in all_sprites:
            sprite.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()