import pygame

# definir le class du profectil
class Projetil(pygame.sprite.Sprite):

    # definir le constructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 4
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0


    def rotate(self):
        # tourner les projectile
        self.angle += 6
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectil.remove(self)


    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectl
            self.remove()
            # Les degat
            monster.damage(self.player.attack)

        # detruire les profectil
        if self.rect.x > 1450:
            # Supprime les projectils
            self.remove()
