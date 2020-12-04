import pygame
import random


# class de monstre
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 200
        self.max_health = 200
        self.attack = 0.2
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1450 + random.randint(0, 3000)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amont):
        # les degats
        self.health -= amont

        # verifier le nombre de point de vie
        if self.health <= 0:
            # Respawn
            self.rect.x = 1450 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

            # si la barre est charger
            if self.game.comet_event.is_full_loaded():
                # retirer les monstre
                self.game.all_monsters.remove(self)


                # declancher la pluie
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        #dessiner la bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 40, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 40, self.rect.y - 20, self.health, 5])


    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
         # sile monstre est en collision
        else:
            # infliguer des degats
            self.game.player.damage(self.attack)