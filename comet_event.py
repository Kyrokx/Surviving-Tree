import pygame
import random
from comet import Comet

# cree un classe pour gere les commets
class cometFallEvent:

    # cree un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = random.randint(5, 20)
        self.game = game
        self.fall_mode = False

        # definir un groue de sprite pour les comet
        self.all_comets = pygame.sprite.Group()


    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        for i in range(1, 20):
            # faire appretre une boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # si la jauge est pleine
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            # print("Pluie de comet")
            self.meteor_fall()
            #self.reset_percent()
            self.fall_mode = True

    def update_bar(self, surface):

        # ajouter du pourcentage
        self.add_percent()



        # bar moir en arrire plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 20,
            surface.get_width(),
            10
        ])
        # bar rouge jauge d'event
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 20,
            (surface.get_width() / 100) * self.percent,
            10
        ])

