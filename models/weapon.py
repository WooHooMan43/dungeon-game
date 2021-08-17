from __future__ import annotations
from models.entity import Entity
from paths import ENEMY_SOUNDS, WEAPON_TEXTURES

import pygame
import pygame.sprite, pygame.transform

from models.screen import Screen
from models.game_object import GameObject
from models.entity import Entity


class Weapon(GameObject):
    def __init__(
        self,
        user: Entity,
        dest: tuple[int, int],
        image: str,
        damage: int,
        parent: Screen,
    ) -> None:
        super().__init__(dest=dest, image=parent.images[image], parent=parent)

        self.user = user
        self.facing = user.facing

        self.damage = damage

        self.parent.not_player_sprites.add(self)
        self.parent.damaging_sprites.add(self)

    def collide(self) -> None:
        colliding_sprites = pygame.sprite.spritecollide(
            sprite=self,
            group=self.parent.damageable_sprites,
            dokill=False,
            collided=pygame.sprite.collide_mask,
        )
        for sprite in colliding_sprites:
            if sprite is not self.user:
                sprite.hurt(self.damage)

    def draw(self) -> None:
        self.parent.image.blit(self.image, (self.rect.x, self.rect.y))

    def update(self) -> None:
        self.collide()
        self.draw()
