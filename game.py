import pygame
from player import Player
from monster import Monster
from comet_event import cometFallEvent

# seconde class qui represe,te le jeu
class Game:

    def __init__(self):
        # definir si le jeu a commencer
        self.is_playing = False
        # Generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        # generer l'evenement
        self.comet_event = cometFallEvent(self)
        self.all_players.add(self.player)
        # groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # redemarrer le jeu
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Appliquer la bar de vie du joueur
        self.player.update_health_bar(screen)

        # barre d'evenament du jeu
        self.comet_event.update_bar(screen)

        # recuper les projectil
        for profectil in self.player.all_projectil:
            profectil.move()

        # recuperer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # Appliquer le projectil
        self.player.all_projectil.draw(screen)
        # Les monstres
        self.all_monsters.draw(screen)

        # comet
        self.comet_event.all_comets.draw(screen)


        # recupererles comet
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Mouvement du joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_rigth()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        # mettre a jour l'ecran
        pygame.display.flip()

        # si le joueur ferme la fenetre
        for event in pygame.event.get():
            # l'evenement est la fermeture de la fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                # print("La fenetre est fermé")

            # detecter une tache du clavier
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True

                # Touche espace
                if event.key == pygame.K_SPACE:
                    self.player.launch_profectil()

            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)