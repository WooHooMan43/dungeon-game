from __future__ import annotations

import pygame
import pygame.sprite, pygame.transform

from models.screen import Screen
from models.weapon import Weapon
from models.entity import Entity
from models.item import Item

from paths import ITEM_SOUNDS, ITEM_TEXTURES, WEAPON_TEXTURES, WEAPON_SOUNDS


class SwordItem(Item):
    def __init__(self, dest: tuple[int, int] = (0, 0), parent: Screen = None) -> None:
        super().__init__(
            dest=dest,
            image=parent.images[ITEM_TEXTURES["sword"]] if parent is not None else None,
            count=1,
            collectable=True,
            parent=parent,
        )

        self.stack = 1

    def action(self) -> None:
        super().action()
        self.parent.item_sounds.play(self.parent.sounds[ITEM_SOUNDS["item"]["pickup"]])

    def click_action(self) -> None:
        SwordWeapon(user=self.user)
        self.parent.weapon_sounds.play(
            self.parent.sounds[WEAPON_SOUNDS["sword"]["swing"]]
        )


class SwordWeapon(Weapon):
    def __init__(self, user: Entity) -> None:
        super().__init__(
            dest=user.parent.rect.bottomright,
            user=user,
            image=WEAPON_TEXTURES["sword"][user.facing][3],
            damage=1,
            parent=user.parent,
        )

        if self.user.facing == "s":
            self.rect.centerx = self.user.rect.centerx
            self.rect.top = self.user.rect.bottom
        elif self.user.facing == "n":
            self.rect.centerx = self.user.rect.centerx
            self.rect.bottom = self.user.rect.top + (
                2 * self.parent.tile_side / self.user.rect.h
            )
        elif self.user.facing == "e":
            self.rect.centery = self.user.rect.centery
            self.rect.left = self.user.rect.right - (
                6 * self.parent.tile_side / self.user.rect.h
            )
        elif self.user.facing == "w":
            self.rect.centery = self.user.rect.centery
            self.rect.right = self.user.rect.left + (
                6 * self.parent.tile_side / self.user.rect.h
            )

        self.use_frame = 0
        self.use_frame_max = 8

    def update(self):
        sword_image: pygame.Surface = self.parent.images[
            WEAPON_TEXTURES["sword"][self.facing][
                self.use_frame
                if self.use_frame < int(self.use_frame_max / 2)
                else (self.use_frame_max - 1) - self.use_frame
            ]
        ]

        self.mask = pygame.mask.from_surface(self.image)

        if self.user.facing == "s":
            self.rect.centerx = self.user.rect.centerx
            self.rect.top = self.user.rect.bottom
        elif self.user.facing == "n":
            self.rect.centerx = self.user.rect.centerx
            self.rect.bottom = self.user.rect.top + (
                2 * self.parent.tile_side / self.user.rect.h
            )
        elif self.user.facing == "e":
            self.rect.centery = self.user.rect.centery
            self.rect.left = self.user.rect.right - (
                6 * self.parent.tile_side / self.user.rect.h
            )
        elif self.user.facing == "w":
            self.rect.centery = self.user.rect.centery
            self.rect.right = self.user.rect.left + (
                6 * self.parent.tile_side / self.user.rect.h
            )

        super().update()

        if self.use_frame < self.use_frame_max - 1:
            self.use_frame += 1
            self.user.stuck = True
        else:
            self.user.stuck = False
            self.kill()
            # del(self)
