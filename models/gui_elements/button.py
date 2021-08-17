from __future__ import annotations
from os import replace

import pygame
import pygame.mouse, pygame.freetype

from models.screen import Screen
from models.game_object import GameObject

from paths import GUI_SOUNDS

M_LEFT = 0
M_MIDDLE = 1
M_RIGHT = 2


class Button(GameObject):
    def __init__(
        self,
        dest: tuple[int, int],
        area: tuple[int, int],
        parent: Screen,
        text: str,
        size: float = None,
        click: function = None,
        fg: tuple[int, int, int] = (0, 0, 0),
        bg: tuple[int, int, int] = (255, 255, 255),
        hl_fg: tuple[int, int, int] = (0, 0, 0),
        hl_bg: tuple[int, int, int] = (32, 32, 255),
    ) -> None:
        # Write some parameters into variables for use later.
        self.text = text
        self.size = size if size is not None else parent.font.size
        self.fg = fg
        self.bg = bg
        self.hl_fg = hl_fg
        self.hl_bg = hl_bg

        # This is very important. This is a function that will be evecuted
        self.click = click

        self.hovered = False

        # Create a surface and a rect for the button and fill it with
        # the appropriate color.
        image = pygame.Surface(area)
        image_rect = image.get_rect()
        image.fill(bg)
        # Create a surface and a rect for the text.
        label, label_rect = parent.font.render(
            text=text, fgcolor=fg, bgcolor=None, size=self.size
        )
        # Blit the text directly in the center of the button.
        image.blit(
            label,
            ((image_rect.w - label_rect.w) / 2, (image_rect.h - label_rect.h) / 2),
        )

        super().__init__(dest, image, parent)

    def update(self):

        # Get the press status of the mouse buttons.
        buttons = pygame.mouse.get_pressed()

        def getTopLevelCoords(obj: GameObject) -> tuple[int, int]:
            # Get the position of an object in relation to the main
            # display recursively.
            parent_x, parent_y, = (
                getTopLevelCoords(obj.parent) if obj.parent is not None else (0, 0)
            )
            return (obj.rect.x + parent_x, obj.rect.y + parent_y)

        # Get the position of the mouse and the relative displacement
        # between the mouse and the button.
        pos = pygame.mouse.get_pos()
        rel_pos = (
            pos[0] - getTopLevelCoords(self)[0],
            pos[1] - getTopLevelCoords(self)[1],
        )
        # Is the mouse within the boundaries of the button?
        if 0 <= rel_pos[0] < self.rect.width and 0 <= rel_pos[1] < self.rect.height:
            # If so, play a sound and fill the button with a different
            # color.
            if not self.hovered:
                # But only play the sound on the first frame of the
                # hover.
                self.parent.gui_sounds.play(
                    self.parent.sounds[GUI_SOUNDS["button"]["hover"]]
                )
                self.hovered = True
            self.image.fill(self.hl_bg)
            # Create a new text surface and rect in a different color.
            label, label_rect = self.parent.font.render(
                text=self.text, fgcolor=self.hl_fg, bgcolor=None, size=self.size
            )
            # Blit the text to the button.
            self.image.blit(
                label,
                ((self.rect.w - label_rect.w) / 2, (self.rect.h - label_rect.h) / 2),
            )
            # Is the left mouse button pressed?
            if buttons[M_LEFT]:
                # Play a sound and run the click function.
                self.parent.gui_sounds.play(
                    self.parent.sounds[GUI_SOUNDS["button"]["click"]]
                )
                self.click()
        else:
            # Reset the button's color and text color.
            self.hovered = False
            self.image.fill(self.bg)
            label, label_rect = self.parent.font.render(
                text=self.text, fgcolor=self.fg, bgcolor=None, size=self.size
            )
            self.image.blit(
                label,
                ((self.rect.w - label_rect.w) / 2, (self.rect.h - label_rect.h) / 2),
            )

        super().update()
