from __future__ import annotations

__all__ = ["Screen"]

import pygame
import pygame.sprite, pygame.freetype, pygame.mixer, pygame.time
import os

from utils import load_images, load_sounds, resource_path
from paths import SOUND_PATH, TEXTURE_PATH, BLOCK_TEXTURES

# The base class for layouts. These objects will contain everything
# that exists and even make up the main window.
class Screen(pygame.sprite.Sprite):
    def __init__(
        self,
        surf: pygame.Surface,
        dest: tuple[int, int] = (0, 0),
        parent: Screen | None = None,
    ) -> None:
        super().__init__()

        # Most, if not all of this, is initialization code. It either
        # fetches the parent's attributes or, if it is the main parent,
        # creates the attributes.
        self.image = surf
        self.rect = self.image.get_rect()
        (
            self.rect.x,
            self.rect.y,
        ) = dest

        self.parent = parent

        if parent is not None:
            parent.sprites.add(self)

        self.clock: pygame.time.Clock = (
            parent.clock if parent is not None else pygame.time.Clock()
        )

        self.images: dict[str, pygame.Surface] = (
            parent.images if parent is not None else load_images(TEXTURE_PATH)
        )
        self.sounds: dict[str, pygame.mixer.Sound] = (
            parent.sounds if parent is not None else load_sounds(SOUND_PATH)
        )

        self.tile_side: int = (
            parent.tile_side if parent is not None else int(self.rect.width / 16)
        )

        # self.image_side: int = (
        #     parent.image_side
        #     if parent is not None
        #     else self.images[BLOCK_TEXTURES["bricks"]].get_height()
        # )
        self.font: pygame.freetype.Font = (
            parent.font
            if parent is not None
            else pygame.freetype.Font(
                resource_path(os.path.join("assets", "fonts", "nes-arcade-font-2-1-monospaced.ttf")),
                12,
            )
        )
        self.music_sounds: pygame.mixer.Channel = (
            parent.music_sounds if parent is not None else pygame.mixer.Channel(0)
        )
        self.gui_sounds: pygame.mixer.Channel = (
            parent.gui_sounds if parent is not None else pygame.mixer.Channel(1)
        )
        self.player_sounds: pygame.mixer.Channel = (
            parent.player_sounds if parent is not None else pygame.mixer.Channel(2)
        )
        self.enemy_sounds: pygame.mixer.Channel = (
            parent.enemy_sounds if parent is not None else pygame.mixer.Channel(3)
        )
        self.item_sounds: pygame.mixer.Channel = (
            parent.item_sounds if parent is not None else pygame.mixer.Channel(4)
        )
        self.weapon_sounds: pygame.mixer.Channel = (
            parent.weapon_sounds if parent is not None else pygame.mixer.Channel(5)
        )

        self.sprites = pygame.sprite.LayeredUpdates()
        self.collidable_sprites = pygame.sprite.Group()
        self.damageable_sprites = pygame.sprite.Group()
        self.damaging_sprites = pygame.sprite.Group()
        self.handed_sprites = pygame.sprite.Group()
        self.floor_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.not_player_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.GroupSingle()

    def draw(self) -> None:
        self.parent.image.blit(self.image, (self.rect.x, self.rect.y))

    def update(self) -> None:
        self.sprites.update()

        self.draw()
