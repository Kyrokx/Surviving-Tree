import pygame
import random

# cree une classe comet
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir l'inmage
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # verifier si les comey sont fini
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        # si elle ne tombe pas sur le sol
        if self.rect.y >= 500:
            self.remove()

            # si il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                # remttre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode= False

        # verifier si la boule de jeu touche le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print(" toucher")
            # retirer la boule de feu
            self.remove()
            # retirer des vie
            self.comet_event.game.player.damage(20)

