import pygame
from bullet import Bullet



class BulletManager:
    def __init__(self, screen, settings, ship) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets = pygame.sprite.Group()

    def _fire_bullet(self) -> None:
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)
    def _update_bullets(self, aliens) -> None:
        self.bullets.update()
        self._remove_offscreen_bullets()
        self._check_bullet_alien_collisions(aliens)
    
    def _remove_offscreen_bullets(self) -> None:
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self, aliens) -> None:
        pygame.sprite.groupcollide(self.bullets, aliens, True, True)