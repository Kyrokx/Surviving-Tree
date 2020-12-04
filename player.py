import pygame
from projectil import Projetil


# class du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 350
        self.max_health = 350
        self.attack = 10
        self.velocity = 2
        self.all_projectil = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amont):
        if self.health - amont > amont:
            self.health -= amont
        else:
            # si le joueur n'a plus de piont de vie
            self.game.game_over()

    def update_health_bar(self, surface):
            # dessiner la bar de vie
            pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 40, self.rect.y + 1, self.max_health, 7])
            pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 40, self.rect.y + 1, self.health, 7])

    def launch_profectil(self):
        #creer une nouvelle instance de la classe profectil
        self.all_projectil.add(Projetil(self))


    def move_rigth(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
