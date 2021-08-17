from __future__ import annotations

import pygame

from models.screen import Screen
from models.game_object import GameObject


class Floor(GameObject):

    # Render this beneath everything else.
    _layer = -1

    def __init__(
        self, image: str | tuple[int, int, int] | pygame.Color, parent: Screen
    ) -> None:
        # Create a surface to cover with an image or color.
        background = pygame.Surface((parent.rect.width, parent.rect.height))
        if isinstance(image, str):
            # If image is a string (filepath), tile that image across the screen
            tiled_image = pygame.transform.scale(
                parent.images[image], (parent.tile_side, parent.tile_side)
            )
            for x in range(0, parent.rect.width, parent.tile_side):
                for y in range(0, parent.rect.height, parent.tile_side):
                    background.blit(tiled_image, (x, y))

        elif isinstance(image, (tuple, pygame.Color)):
            # If its a color or a tuple, fill it with a color
            background.fill(image)
        else:
            # If its none of those, fill it with black
            background.fill((0, 0, 0))

        super().__init__(dest=(0, 0), image=background, parent=parent)

        self.parent.not_player_sprites.add(self)
        self.parent.floor_sprites.add(self)
