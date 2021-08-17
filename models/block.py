from __future__ import annotations

import pygame.transform

from models.screen import Screen
from models.game_object import GameObject


class Block(GameObject):
    def __init__(self, dest: tuple[int, int], image: str, parent: Screen) -> None:
        super().__init__(dest=dest, image=parent.images[image], parent=parent)

        self.parent.collidable_sprites.add(self)
        self.parent.not_player_sprites.add(self)
