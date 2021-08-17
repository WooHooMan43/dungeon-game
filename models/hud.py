from __future__ import annotations

import pygame.transform
import pygame

from models.screen import Screen
from models.game_object import GameObject
from paths import HUD_TEXTURE, ITEM_BORDER, SELECTED_TEXTURE


class HUD(GameObject):

    _layer = 2

    def __init__(self, parent: Screen) -> None:
        super().__init__(dest=(0, 0), image=parent.images[HUD_TEXTURE], parent=parent)

        self.parent.not_player_sprites.add(self)

    def update(self) -> None:
        super().update()
        # Reset the HUD every frame so any transparency isn't stacked.
        self.image = pygame.transform.scale(
            self.parent.images[HUD_TEXTURE],
            (self.parent.rect.width, self.parent.rect.height),
        )

        # Get the data from the player by looking through each Screen
        # on the main display.
        for obj in self.parent.sprites:
            if isinstance(obj, Screen):
                player = obj.player_sprites.sprite
                # Is there a player in this Screen?
                if player is not None:
                    # Show the number of coins the player has.
                    self.parent.font.render_to(
                        self.image,
                        dest=(self.parent.rect.width - self.parent.tile_side * 2, 0),
                        text="POINTS",
                        fgcolor=(255, 255, 255),
                        bgcolor=None,
                        size=self.parent.tile_side / 4,
                    )
                    pts_image, pts_rect, = self.parent.font.render(
                        text=str(player.points),
                        fgcolor=(255, 255, 255),
                        bgcolor=None,
                        size=self.parent.tile_side / 4,
                    )

                    self.image.blit(
                        pts_image,
                        (
                            self.parent.rect.width
                            - self.parent.tile_side * 2
                            - self.parent.tile_side / 4
                            - pts_rect.width,
                            0,
                        ),
                    )

                    self.image.blit(
                        self.parent.images[SELECTED_TEXTURE],
                        (
                            self.parent.rect.width - self.parent.tile_side,
                            self.parent.tile_side * player.selected_item
                            + self.parent.tile_side,
                        ),
                    )

                    for item in range(len(player.inventory)):
                        self.image.blit(
                            self.parent.images[ITEM_BORDER],
                            (
                                self.parent.rect.width - self.parent.tile_side,
                                self.parent.tile_side * item + self.parent.tile_side,
                            ),
                        )
                        if player.inventory[item] is not None:
                            self.image.blit(
                                player.inventory[item].image,
                                (
                                    self.parent.rect.width - self.parent.tile_side,
                                    self.parent.tile_side * item
                                    + self.parent.tile_side,
                                ),
                            )
                            if player.inventory[item].stack > 1:
                                self.parent.font.render_to(
                                    surf=self.image,
                                    dest=(
                                        self.parent.rect.width - self.parent.tile_side,
                                        self.parent.tile_side * item
                                        + self.parent.tile_side,
                                    ),
                                    text=str(player.inventory[item].count),
                                    fgcolor=(255, 255, 255),
                                    bgcolor=None,
                                    size=self.parent.tile_side / 4,
                                )

                    self.parent.font.render_to(
                        self.image,
                        dest=(
                            self.parent.rect.width - self.parent.tile_side * 2,
                            self.parent.tile_side / 2,
                        ),
                        text="HEALTH",
                        fgcolor=(255, 255, 255),
                        bgcolor=None,
                        size=self.parent.tile_side / 4,
                    )
                    health_bar = pygame.Surface(
                        (
                            player.max_health * self.parent.tile_side / 4,
                            self.parent.tile_side / 4,
                        )
                    )
                    health_overlay = pygame.transform.scale(
                        pygame.Surface(
                            (
                                player.max_health * self.parent.tile_side / 4,
                                self.parent.tile_side / 4,
                            )
                        ),
                        (
                            int(player.health * self.parent.tile_side / 4),
                            int(self.parent.tile_side / 4),
                        ),
                    )
                    health_bar.fill("darkred")
                    health_overlay.fill(pygame.Color("red"))
                    self.image.blit(
                        health_bar,
                        (
                            self.parent.rect.width
                            - self.parent.tile_side * 2
                            - health_bar.get_width(),
                            int(self.parent.tile_side / 2),
                        ),
                    )
                    self.image.blit(
                        health_overlay,
                        (
                            self.parent.rect.width
                            - self.parent.tile_side * 2
                            - health_bar.get_width(),
                            int(self.parent.tile_side / 2),
                        ),
                    )

                    self.parent.font.render_to(
                        self.image,
                        dest=(
                            self.parent.rect.width - self.parent.tile_side,
                            self.parent.rect.height - self.parent.tile_side / 2,
                        ),
                        text="FPS",
                        fgcolor=(255, 255, 255),
                        bgcolor=None,
                        size=self.parent.tile_side / 4,
                    )
                    self.parent.font.render_to(
                        self.image,
                        dest=(
                            self.parent.rect.width - self.parent.tile_side,
                            self.parent.rect.height - self.parent.tile_side / 4,
                        ),
                        text=str(round(self.parent.clock.get_fps())),
                        fgcolor=(255, 255, 255),
                        bgcolor=None,
                        size=self.parent.tile_side / 4,
                    )
