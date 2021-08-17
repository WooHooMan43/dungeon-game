from __future__ import annotations

import pygame
import pygame.display, pygame.time, pygame.event, pygame.mixer, pygame.image
import sys

from models.gui_elements import Button, Label

from models import (
    Screen,
    Player,
    Block,
    Coin,
    Health,
    HUD,
    Floor,
    SphereEnemy,
    Parabodroid,
    SwordItem,
    TriangleItem,
)
from paths import BLOCK_TEXTURES, PLAYER_TEXTURES, MUSIC_SOUNDS


class Game(Screen):
    def __init__(self) -> None:
        self._init_pygame()

        # I used to use this, but I feel it is irrelevant and that it
        # would be best to do without it.
        # # Get the size of the current display, and use it to calculate
        # # the size of the game window. Basically allows the highest
        # # possible definition for sprites (attempted using single size,
        # # failed miserably).
        # info = pygame.display.Info()
        # screen_width, screen_height = info.current_w, info.current_h
        # if screen_width > (4 / 3) * screen_height:
        #     screen_width = int((4 / 3) * screen_height)
        # elif screen_width < (4 / 3) * screen_height:
        #     screen_height = int((3 / 4) * screen_width)

        # Create the window
        image_display = pygame.display.set_mode(
            (32 * 16, 32 * 12), pygame.FULLSCREEN | pygame.SCALED, vsync=1
        )
        super().__init__(image_display)

        self.music_sounds.play(self.sounds[MUSIC_SOUNDS["intro"]])

        self.paused = False

        self.screens: dict[str, Screen] = {}

        pause_menu = Screen(
            surf=pygame.Surface(
                (self.rect.width - self.tile_side, self.rect.height - self.tile_side)
            ),
            dest=(0, self.tile_side),
            parent=self,
        )
        pause_menu.remove(self.sprites)
        Label(
            dest=(self.tile_side * 5, self.tile_side * 3),
            area=(4 * self.tile_side, self.tile_side),
            parent=pause_menu,
            text="PAUSED",
            fg=(255, 255, 255),
        )
        Button(
            dest=(self.tile_side * 5, self.tile_side * 5),
            area=(4 * self.tile_side, self.tile_side),
            parent=pause_menu,
            text="RESUME",
            click=self.resume,
        )
        Button(
            dest=(self.tile_side * 5, self.tile_side * 7),
            area=(4 * self.tile_side, self.tile_side),
            parent=pause_menu,
            text="QUIT",
            click=self.exit,
        )
        self.screens["pause"] = pause_menu

        death_screen = Screen(
            surf=pygame.Surface(
                (self.rect.width - self.tile_side, self.rect.height - self.tile_side)
            ),
            dest=(0, self.tile_side),
            parent=self,
        )
        Label(
            dest=(self.tile_side * 5, self.tile_side * 4),
            area=(4 * self.tile_side, self.tile_side),
            parent=death_screen,
            text="YOU DIED",
            fg=(255, 255, 255),
        )
        Button(
            dest=(self.tile_side * 5, self.tile_side * 6),
            area=(4 * self.tile_side, self.tile_side),
            parent=death_screen,
            text="QUIT",
            click=self.exit,
        )
        self.screens["death"] = death_screen

        for key, screen in self.screens.items():
            screen.remove(self.sprites)

    def exit(self):
        pygame.quit()
        sys.exit()

    def pause(self):
        self.screens["pause"].add(self.sprites)
        pygame.mixer.pause()
        self.paused = True

    def resume(self):
        self.screens["pause"].remove(self.sprites)
        pygame.mixer.unpause()
        self.paused = False

    def main_loop(self) -> None:
        # Create a surface for gameplay
        view = Screen(
            surf=pygame.Surface(
                (self.rect.width - self.tile_side, self.rect.height - self.tile_side)
            ),
            dest=(0, self.tile_side),
            parent=self,
        )

        # Creating test objects. Eventually, this will go away, but I
        # haven't yet figured out how to make loadable levels.
        # TODO: Add levels.
        Player(dest=(3 * self.tile_side, self.tile_side * 5), parent=view)

        Floor(image=(32, 32, 32), parent=view)

        for i in range(
            -view.rect.width, view.rect.width - self.tile_side, self.tile_side
        ):
            Block(
                dest=(i, 0),
                image=BLOCK_TEXTURES["bricks"],
                parent=view,
            )
            Block(
                dest=(i, view.rect.height - self.tile_side),
                image=BLOCK_TEXTURES["bricks"],
                parent=view,
            )
        for j in range(0, view.rect.height, self.tile_side):
            Block((-view.rect.width, j), BLOCK_TEXTURES["bricks"], view)
            Block(
                dest=(view.rect.width - self.tile_side, j),
                image=BLOCK_TEXTURES["bricks"],
                parent=view,
            )

        Coin(dest=(self.tile_side * 11, self.tile_side * 5), count=300, parent=view)
        
        Health(dest=(self.tile_side * -13.5, self.tile_side * 5), parent=view)

        for i in range(self.tile_side * -12, self.tile_side * -3, self.tile_side):
            Block(
                dest=(i, self.tile_side),
                image=BLOCK_TEXTURES["bricks"],
                parent=view,
            )
            Block(
                dest=(i, view.rect.height - (self.tile_side * 2)),
                image=BLOCK_TEXTURES["bricks"],
                parent=view,
            )
            Block(
                dest=(i, self.tile_side * 2),
                image=BLOCK_TEXTURES["bricks"],
                parent=view,
            )
            Block(
                dest=(i, view.rect.height - (self.tile_side * 3)),
                image=BLOCK_TEXTURES["bricks"],
                parent=view,
            )
        for i in range(self.tile_side * -12, self.tile_side * -3, self.tile_side * 2):
            Block(
                dest=(i, self.tile_side * 3),
                image=BLOCK_TEXTURES["bricks"],
                parent=view,
            )
            Block(
                dest=(i, view.rect.height - (self.tile_side * 4)),
                image=BLOCK_TEXTURES["bricks"],
                parent=view,
            )

        SphereEnemy(
            dest=(self.tile_side * -5, self.tile_side * 3),
            path=(
                (self.tile_side * 10, self.tile_side * 3),
                (self.tile_side * 10, self.tile_side * 7),
            ),
            parent=view,
        )
        SphereEnemy(
            dest=(self.tile_side * -7, self.tile_side * 3),
            path=(
                (self.tile_side * 8, self.tile_side * 3),
                (self.tile_side * 8, self.tile_side * 7),
            ),
            parent=view,
        )
        SphereEnemy(
            dest=(self.tile_side * -9, self.tile_side * 3),
            path=(
                (self.tile_side * 6, self.tile_side * 3),
                (self.tile_side * 6, self.tile_side * 7),
            ),
            parent=view,
        )
        SphereEnemy(
            dest=(self.tile_side * -11, self.tile_side * 3),
            path=(
                (self.tile_side * 4, self.tile_side * 3),
                (self.tile_side * 4, self.tile_side * 7),
            ),
            parent=view,
        )

        Parabodroid(
            dest=(self.tile_side * 9, self.tile_side * 3),
            path=(
                (self.tile_side * 9, self.tile_side * 3),
                (self.tile_side * 13, self.tile_side * 3),
                (self.tile_side * 13, self.tile_side * 7),
                (self.tile_side * 9, self.tile_side * 7),
            ),
            parent=view,
        )
        Parabodroid(
            dest=(self.tile_side * 13, self.tile_side * 3),
            path=(
                (self.tile_side * 13, self.tile_side * 3),
                (self.tile_side * 13, self.tile_side * 7),
                (self.tile_side * 9, self.tile_side * 7),
                (self.tile_side * 9, self.tile_side * 3),
            ),
            parent=view,
        )
        Parabodroid(
            dest=(self.tile_side * 13, self.tile_side * 7),
            path=(
                (self.tile_side * 13, self.tile_side * 7),
                (self.tile_side * 9, self.tile_side * 7),
                (self.tile_side * 9, self.tile_side * 3),
                (self.tile_side * 13, self.tile_side * 3),
            ),
            parent=view,
        )
        Parabodroid(
            dest=(self.tile_side * 9, self.tile_side * 7),
            path=(
                (self.tile_side * 9, self.tile_side * 7),
                (self.tile_side * 9, self.tile_side * 3),
                (self.tile_side * 13, self.tile_side * 3),
                (self.tile_side * 13, self.tile_side * 7),
            ),
            parent=view,
        )

        TriangleItem(
            dest=(self.tile_side * -13.5, self.tile_side * 8),
            count=99,
            parent=view,
        )

        SwordItem(dest=(self.tile_side * -13.5, self.tile_side * 2), parent=view)

        HUD(parent=self)

        self.screens["main"] = view

        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self) -> None:
        # Initialization. This was in the tutorial.
        pygame.init()
        pygame.display.set_caption("Dungeon Game")
        pygame.display.set_icon(pygame.image.load(PLAYER_TEXTURES["stand"]["s"]))

    def _handle_input(self) -> None:
        # Handle some non-game related events, including closing and
        # pausing the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not self.paused:
                        self.pause()
                    else:
                        self.resume()

    def _process_game_logic(self) -> None:
        # Loop the music and update each and every sprite on screen.
        if not self.music_sounds.get_busy():
            self.music_sounds.play(self.sounds[MUSIC_SOUNDS["main"]])

        if not self.paused:
            self.sprites.update()
        else:
            for key, screen in self.screens.items():
                if key != "main":
                    if screen in self.sprites:
                        screen.update()

    def _draw(self) -> None:
        # Update the display every frame at 30 fps.
        self.clock.tick(30)
        pygame.display.flip()
