from __future__ import annotations

import pygame
from pygame.event import get
import pygame.sprite, pygame.transform
import math

from models.screen import Screen
from models.item import Item
from models.projectile import Projectile
from paths import PROJECTILE_TEXTURES, ITEM_SOUNDS


class TriangleItem(Item):
    def __init__(
        self, dest: tuple[int, int] = (0, 0), count: int = 0, parent: Screen = None
    ) -> None:
        super().__init__(
            dest=dest,
            image=parent.images[PROJECTILE_TEXTURES["triangle"][0]]
            if parent is not None
            else None,
            count=count,
            collectable=True,
            parent=parent,
        )

        self.stack = 99

    def action(self) -> None:
        super().action()
        self.parent.item_sounds.play(self.parent.sounds[ITEM_SOUNDS["item"]["pickup"]])

    def click_action(self) -> None:

        if self.user.facing == "s":
            dest = (
                self.user.rect.centerx - int(self.rect.width / 2),
                self.user.rect.bottom,
            )
            velo = (0, 8)
        elif self.user.facing == "n":
            dest = (
                self.user.rect.centerx - int(self.rect.width / 2),
                self.user.rect.top - self.rect.height,
            )
            velo = (0, -8)
        elif self.user.facing == "e":
            dest = (
                self.user.rect.right,
                self.user.rect.centery - int(self.rect.height / 2),
            )
            velo = (8, 0)
        elif self.user.facing == "w":
            dest = (
                self.user.rect.left - self.rect.width,
                self.user.rect.centery - int(self.rect.height / 2),
            )
            velo = (-8, 0)
        TriangleProjectile(dest=dest, velo=velo, parent=self.parent)

        self.count -= 1
        if self.count <= 0:
            if self.user is self.parent.player_sprites.sprite:
                self.user.inventory[self.user.inventory.index(self)] = None
            else:
                self.user.selected_item = None
            del self

    # def collide(self) -> None:
    #     super().collide()

    #     colliding_triangles = pygame.sprite.spritecollide(
    #         sprite=self,
    #         group=self.parent.not_player_sprites,
    #         dokill=False,
    #         collided=pygame.sprite.collide_rect,
    #     )

    #     for sprite in colliding_triangles:
    #         if type(sprite) == type(self):
    #             self.count += sprite.count
    #             del sprite


class TriangleProjectile(Projectile):
    def __init__(
        self,
        dest: tuple[int, int],
        parent: Screen,
        velo: tuple[int, int] = (0, 0),
    ) -> None:

        super().__init__(
            dest=dest, image=PROJECTILE_TEXTURES["triangle"][0], parent=parent
        )

        self.velo = list(velo)

        self.spin_frame = 0
        self.spin_frame_max = 8

        self.bounces = 0

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
            triangle = TriangleItem(self.rect.topleft, 1, self.parent)

            clip_n = self.rect.clipline(wall.rect.topleft, wall.rect.topright)
            clip_s = self.rect.clipline(wall.rect.bottomleft, wall.rect.bottomright)
            clip_w = self.rect.clipline(wall.rect.topleft, wall.rect.bottomleft)
            clip_e = self.rect.clipline(wall.rect.topright, wall.rect.bottomright)

            length_n = get_length(clip_n)
            length_s = get_length(clip_s)
            length_w = get_length(clip_w)
            length_e = get_length(clip_e)

            if length_n > length_w and length_n > length_e:
                triangle.rect.centery = wall.rect.top
            elif length_s > length_w and length_s > length_e:
                triangle.rect.centery = wall.rect.bottom
            elif length_w > length_n and length_w > length_s:
                triangle.rect.centerx = wall.rect.left
            elif length_e > length_n and length_e > length_s:
                triangle.rect.centerx = wall.rect.right
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
            sprite.hurt(total_velo / 2)

            self.kill()

    def update(self):
        self.move()

        self.image = self.parent.images[
            PROJECTILE_TEXTURES["triangle"][
                math.floor((self.spin_frame / self.spin_frame_max) * 4)
            ]
        ]

        if self.spin_frame < self.spin_frame_max - 1:
            self.spin_frame += 1
        else:
            self.spin_frame = 0

        super().update()
