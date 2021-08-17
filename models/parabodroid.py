from __future__ import annotations

import pygame.sprite, pygame.transform
import math

from models.screen import Screen
from models.enemy import Enemy
from paths import ENEMY_TEXTURES, ENEMY_SOUNDS


class Parabodroid(Enemy):
    def __init__(
        self,
        dest: tuple[int, int],
        path: tuple[tuple[int, int], ...],
        parent: Screen,
    ) -> None:
        super().__init__(
            dest=dest,
            image=ENEMY_TEXTURES["paraboloid"]["stand"]["s"],
            health=20,
            damage=3,
            parent=parent,
        )

        self.walk_frame = 0
        self.walk_frame_max = 16

        self.path = list(path)

    def hurt(self, health: int | float) -> None:
        super().hurt(health)

        if self.health <= 0:
            # self.parent.enemy_sounds.play() TODO: Add death sound
            self.parent.player_sprites.sprite.points += 50
        else:
            self.parent.enemy_sounds.play(
                self.parent.sounds[ENEMY_SOUNDS["paraboloid"]["hurt"]]
            )

    def update(self) -> None:
        distance = int(self.parent.tile_side / 10)
        # Is this entity currently on-screen?
        if (
            self.parent.rect.left <= self.rect.centerx <= self.parent.rect.right
            and self.parent.rect.top <= self.rect.centery <= self.parent.rect.bottom
        ):
            # Get the difference in position from the entity to the
            # point it is travelling to.
            diff = (
                self.rect.x - self.path[0][0],
                self.rect.y - self.path[0][1],
            )
            # Self-explanatory movement logic.
            if diff[0] > distance / 2:
                self.move([-distance, 0])
            elif diff[0] < -distance / 2:
                self.move([distance, 0])
            if diff[1] > distance / 2:
                self.move([0, -distance])
            elif diff[1] < -distance / 2:
                self.move([0, distance])
            # Is this entity close to its destination?
            if -distance < diff[0] < distance and -distance < diff[1] < distance:
                # Select the next destination.
                self.path.append(self.path.pop(0))
            # This entity is rarely ever still, but I'm keeping this
            # just in case.
            # self.image = pygame.transform.scale(
            #     self.parent.images[ENEMY_TEXTURES["paraboloid"]["stand"][self.facing]],
            #     (self.parent.tile_side, self.parent.tile_side),
            # )
            # Set the image based on frame and direction.
            self.image = self.parent.images[
                ENEMY_TEXTURES["paraboloid"]["walk"][self.facing][
                    math.floor(self.walk_frame / (self.walk_frame_max / 4))
                ]
            ]
            # Every 8 frames, play a step noise.
            if self.walk_frame % 8 == 0:
                self.parent.enemy_sounds.stop()
                self.parent.enemy_sounds.play(
                    self.parent.sounds[ENEMY_SOUNDS["paraboloid"]["step"]]
                )
            # Reset walk_frame when it is 1 less than the max.
            if self.walk_frame < self.walk_frame_max - 1:
                self.walk_frame += 1
            else:
                self.walk_frame = 0

            self.mask = pygame.mask.from_surface(self.image)

        super().update()
