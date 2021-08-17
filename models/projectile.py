from __future__ import annotations

import pygame
from pygame.event import get
import pygame.sprite, pygame.transform
import math

from models.screen import Screen
from models.entity import Entity


class Projectile(Entity):
    def __init__(
        self,
        dest: tuple[int, int],
        image: str,
        parent: Screen,
        velo: tuple[int, int] = (0, 0),
        bounces: int | None = None,
    ) -> None:
        super().__init__(dest=dest, image=image, parent=parent)

        self.velo = list(velo)

        self.bounces = bounces

    def move(self) -> None:
        mask_rect = self.mask.get_rect()
        if abs(self.velo[0]) >= mask_rect.w or abs(self.velo[1]) >= mask_rect.h:
            for x in range(0, abs(self.velo[0]), mask_rect.w):
                self.rect.x += mask_rect.w if self.velo[0] > 0 else -mask_rect.w
                self.collide()
            for y in range(0, abs(self.velo[1]), mask_rect.h):
                self.rect.y += mask_rect.h if self.velo[1] > 0 else -mask_rect.h
                self.collide()
        else:
            self.rect.x += self.velo[0]
            self.rect.y += self.velo[1]
            self.collide()

    def collide(self) -> None:
        def get_length(line: tuple[tuple[int, int], tuple[int, int]]) -> int:
            if line == ():
                return 0
            else:
                (
                    pt1,
                    pt2,
                ) = line
                return math.sqrt(
                    math.pow(pt2[1] - pt1[1], 2) + math.pow(pt2[0] - pt1[0], 2)
                )

        # Get a wall sprite colliding with this Entity.
        wall = pygame.sprite.spritecollideany(
            sprite=self,
            group=self.parent.collidable_sprites,
            collided=pygame.sprite.collide_mask,
        )

        # Apply the following logic for the sprite colliding with this
        # Entity.
        if wall is not None:
            if self.bounces != None and self.bounces > 0:
                self.bounces -= 1

                clip_n = self.rect.clipline(wall.rect.topleft, wall.rect.topright)
                clip_s = self.rect.clipline(wall.rect.bottomleft, wall.rect.bottomright)
                clip_w = self.rect.clipline(wall.rect.topleft, wall.rect.bottomleft)
                clip_e = self.rect.clipline(wall.rect.topright, wall.rect.bottomright)

                length_n = get_length(clip_n)
                length_s = get_length(clip_s)
                length_w = get_length(clip_w)
                length_e = get_length(clip_e)

                if (length_n > length_w and length_n > length_e) or (
                    length_s > length_w and length_s > length_e
                ):
                    self.velo[1] *= -1
                elif (length_w > length_n and length_w > length_s) or (
                    length_e > length_n and length_e > length_s
                ):
                    self.velo[0] *= -1
            else:
                self.kill()

        # Get a hurtable sprite colliding with this Entity.
        sprite = pygame.sprite.spritecollideany(
            sprite=self,
            group=self.parent.damageable_sprites,
            collided=pygame.sprite.collide_mask,
        )

        if sprite is not None:
            total_velo = math.sqrt(
                math.pow(self.velo[0], 2) + math.pow(self.velo[1], 2)
            )
            sprite.hurt(total_velo / 2.5)

            self.kill()

    def update(self):
        self.move()

        super().update()
