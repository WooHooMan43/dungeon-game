from __future__ import annotations

import pygame
import pygame.sprite, pygame.transform

from models.screen import Screen
from models.game_object import GameObject


class Entity(GameObject):
    def __init__(self, dest: tuple[int, int], image: str, parent: Screen) -> Entity:
        super().__init__(dest=dest, image=parent.images[image], parent=parent)

        self.stuck = False

        self.facing = "s"

    def move(self, dist: tuple[int, int]) -> bool:
        # Change position by the given amounts.
        self.rect.centerx += dist[0]
        self.rect.centery += dist[1]
        # Face the direction it just moved.
        if dist[1] > 0 and dist[0] == 0:
            self.facing = "s"
        elif dist[1] < 0 and dist[0] == 0:
            self.facing = "n"
        if dist[0] > 0 and dist[1] == 0:
            self.facing = "e"
        elif dist[0] < 0 and dist[1] == 0:
            self.facing = "w"
        # Run collision logic
        self.collide(dist)

    def collide(self, dist: tuple[int, int]) -> bool:
        # Get a list of all collidable sprites colliding with this Entity.
        colliding_sprites = pygame.sprite.spritecollide(
            sprite=self,
            group=self.parent.collidable_sprites,
            dokill=False,
            collided=pygame.sprite.collide_rect,
        )

        # Apply the following logic for every sprite except itself.
        for sprite in colliding_sprites:
            if sprite is not self:
                # Is its right side past the left of the other and
                # moving right?
                if self.rect.right > sprite.rect.left and dist[0] > 0:
                    self.rect.right = sprite.rect.left
                # Is its left side past the right of the other and
                # moving left?
                elif self.rect.left < sprite.rect.right and dist[0] < 0:
                    self.rect.left = sprite.rect.right
                # Is its bottom side past the top of the other and
                # moving down?
                if self.rect.bottom > sprite.rect.top and dist[1] > 0:
                    self.rect.bottom = sprite.rect.top
                # Or is its top side past the bottom of the other and
                # moving up?
                elif self.rect.top < sprite.rect.bottom and dist[1] < 0:
                    self.rect.top = sprite.rect.bottom
                return True
        return False
