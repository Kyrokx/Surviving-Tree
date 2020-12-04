import pygame
import math
from game import Game
pygame.init()

# Generer la fenêtre
pygame.display.set_caption("Surviving Tree")
screen = pygame.display.set_mode((1420, 720))

# Fond du jeu
background = pygame.image.load('assets/bg.jpg')
# banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Le bouton play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (410, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#charger le jeu
game = Game()


running = True

# Boucle qui s'ecute
while running:

    #Mettre l'arriere plan
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencer
    if game.is_playing:
        # demarrer le jeu
        game.update(screen)
    #verifier si n'a pas commencer
    else:
        # ajouter l'ecran
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Mouvement du joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_rigth()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    #mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # l'evenement est la fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            #print("La fenetre est fermé")

        # detecter une tache du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #Touche espace
            if event.key == pygame.K_SPACE:
                game.player.launch_profectil()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si le souris appuie sur le bouton play
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en True
                game.start()