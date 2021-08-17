from __future__ import annotations

import pygame
import pygame.mouse, pygame.freetype

from models.screen import Screen
from models.game_object import GameObject

M_LEFT = 0
M_MIDDLE = 1
M_RIGHT = 2


class Label(GameObject):
    def __init__(
        self,
        dest: tuple[int, int],
        parent: Screen,
        text: str,
        size: float = None,
        area: tuple[int, int] = None,
        fg: tuple[int, int, int] = (0, 0, 0),
        bg: tuple[int, int, int] = (0, 0, 0, 0),
    ) -> None:
        # Set the size of the font if it is given. Otherwise, set it
        # to the default font size.
        size = size if size is not None else parent.font.size

        # Was the area specified?
        if area is not None:
            # Create a surface and a rect for the label and fill it
            # with the appropriate color.
            image = pygame.Surface(area)
            image_rect = image.get_rect()
            image.fill(bg)
            # Create a surface and rect for the text.
            label, label_rect = parent.font.render(
                text=text, fgcolor=fg, bgcolor=None, size=size
            )
            # Blit the text directly in the center of the label.
            image.blit(
                label,
                ((image_rect.w - label_rect.w) / 2, (image_rect.h - label_rect.h) / 2),
            )
        else:
            # Create a surface and rect for the label, including text.
            label, label_rect = parent.font.render(
                text=text, fgcolor=fg, bgcolor=bg, size=size
            )
            image = label

        super().__init__(dest, image, parent)
