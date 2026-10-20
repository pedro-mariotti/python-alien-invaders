import pygame

from settings import Settings
from ship import Ship

from bullet_manager import BulletManager
from event_handler import GameEventHandler
from fleet_manager import FleetManager
from game_renderer import GameRenderer

from alien import Alien
from fast_alien import FastAlien

class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        """Construtor da classe que inicializa o jogo e cria os recursos básicos"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Criando uma instância da classe Ship para representar a nave espacial
        self.ship = Ship(self.screen, self.settings)

        # Mudando a cor do plano de fundo em RGB
        self.bg_color = self.settings.bg_color

        self.bullet_manager = BulletManager(self.screen, self.settings, self.ship)  # Cria um grupo para armazenar os projéteis disparados pela nave
        self.fleet_manager = FleetManager(self.screen, self.settings, self.ship, FastAlien)
        self.event_handler = GameEventHandler(self.ship, self.bullet_manager)
        self.renderer = GameRenderer(self.screen, self.bg_color, self.ship, self.bullet_manager.bullets, self.fleet_manager.aliens)
        self.aliens = (pygame.sprite.Group())  # Cria um grupo para armazenar os alienígenas presentes no jogo

    def _update_game_state(self) -> None:
        self.ship.update()
        self.fleet_manager._update_aliens()
        self.bullet_manager._update_bullets(self.fleet_manager.aliens)
        self.fleet_manager._check_ship_collisions()

    def run_game(self):
        """Cria um laço de repetição para a tela sempre ficar visível até
        que o usuário decida fechar a janela."""

        self.fleet_manager.create_fleet()  # Cria a frota de alienígenas para ser desenhada na tela

        while True:
            self.event_handler._check_events()
            self._update_game_state()
            self.renderer._render_screen()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
