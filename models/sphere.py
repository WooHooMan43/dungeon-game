from __future__ import annotations

import math
import numpy

import pygame.transform

from models.screen import Screen
from models.enemy import Enemy
from paths import ENEMY_SOUNDS, ENEMY_TEXTURES


class SphereEnemy(Enemy):
    def __init__(
        self,
        dest: tuple[int, int],
        path: tuple[tuple[int, int], tuple[int, int]],
        parent: Screen,
    ) -> None:
        super().__init__(
            dest=dest,
            image=ENEMY_TEXTURES["sphere"]["still"]["s"],
            health=10,
            damage=2,
            parent=parent,
        )

        self.path = list(path)

        self.roll_frame = 0
        self.roll_frame_max = 16

        self.done = False

    # def collide(self, dist: tuple[int, int]) -> bool:
    #     # Get a list of all sprites colliding with this Entity.
    #     colliding_sprites = pygame.sprite.spritecollide(
    #         sprite=self,
    #         group=self.parent.collidable_sprites,
    #         dokill=False,
    #         collided=pygame.sprite.collide_rect,
    #     )
    #     for obj in colliding_sprites:
    #         # Apply the following logic for every sprite except itself.
    #         if obj is not self:
    #             if dist[1] != 0:
    #                 self.rect.centery -= dist[1]
    #             if dist[0] != 0:
    #                 self.rect.centerx -= dist[0]
    #             return True
    #     return False

    def hurt(self, health: int | float) -> None:
        super().hurt(health)

        if self.health <= 0:
            # self.parent.enemy_sounds.play() TODO: Add death sound
            self.parent.player_sprites.sprite.points += 30
        else:
            self.parent.enemy_sounds.play(
                self.parent.sounds[ENEMY_SOUNDS["sphere"]["hurt"]]
            )

    def update(self) -> None:

        distance = int(self.parent.tile_side / 10)
        # Is this entity currently on-screen?
        if (
            self.parent.rect.left <= self.rect.centerx <= self.parent.rect.right
            and self.parent.rect.top <= self.rect.centery <= self.parent.rect.bottom
        ) and not self.done:

            self.image = self.parent.images[
                ENEMY_TEXTURES["sphere"]["still"][self.facing]
            ]

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
                # Stop moving until re-triggered.
                self.done = True
        else:
            # Get the player.
            player = self.parent.player_sprites.sprite
            # Courtesy of the many answers from
            # https://stackoverflow.com/questions/39840030/distance-between-point-and-a-line-from-two-points
            # Create points for linear algebra
            p1 = numpy.asarray(
                (
                    self.path[0][0] + int(self.rect.width / 2),
                    self.path[0][1] + int(self.rect.height / 2),
                )
            )
            p2 = numpy.asarray(
                (
                    self.path[1][0] + int(self.rect.width / 2),
                    self.path[1][1] + int(self.rect.height / 2),
                )
            )
            p3 = numpy.asarray(player.rect.center)
            # This is the distance between the center of the player and
            # the path the entity takes.
            d = numpy.cross(p2 - p1, p1 - p3) / numpy.linalg.norm(p2 - p1)
            if abs(d) < self.rect.width:
                self.done = False

            self.image = self.parent.images[ENEMY_TEXTURES["sphere"]["sleep"]]
        # All of the old logic for moving this thing. I originially
        # planned for this to follow the player, but threw it out in
        # exchange for mechanics similar to that of a Thowmp. I'm
        # keeping it, though, because it might be useful in the future.
        # distance = int(self.parent.tile_side / 15)

        # player = self.parent.player_sprites.sprite
        # diff = (
        #     self.rect.centerx - player.rect.centerx,
        #     self.rect.centery - player.rect.centery,
        # )
        # for sprite in self.parent.collidable_sprites:
        #     if sprite is not self:
        #         blocked = sprite.rect.clipline(self.rect.center, player.rect.center)
        #         if blocked:
        #             break

        # if not blocked and (
        #     0 <= self.rect.centerx <= self.parent.rect.width
        #     and 0 <= self.rect.centery <= self.parent.rect.height
        # ):
        #     if (
        #         (self.facing == "e" or self.facing == "w") and abs(diff[0]) > distance
        #     ) or (
        #         (self.facing == "n" or self.facing == "s") and abs(diff[1]) <= distance
        #     ):
        #         if diff[0] > 0:
        #             moved = self.move([-distance, 0])
        #         else:
        #             moved = self.move([distance, 0])
        #     if (
        #         (self.facing == "n" or self.facing == "s") and abs(diff[1]) > distance
        #     ) or (
        #         (self.facing == "e" or self.facing == "w") and abs(diff[0]) <= distance
        #     ):
        #         if diff[1] > 0:
        #             moved = self.move([0, -distance])
        #         else:
        #             moved = self.move([0, distance])
        # else:
        #     self.facing = "s"
        #     moved = False

        # if not blocked:
        #     if self.roll_frame % 4 == 0:
        #         self.parent.enemy_sounds.play(
        #             self.parent.sounds[ENEMY_SOUNDS["sphere"]["roll"]]
        #         )

        # # if (
        # #     not blocked
        # #     and (
        # #         0 <= self.rect.centerx <= self.parent.rect.width
        # #         and 0 <= self.rect.centery <= self.parent.rect.height
        # #     )
        # #     and not moved
        # # ):
        # #     if self.facing == "e":
        # #         moved_around = self.move([0, -distance])
        # #         if not moved_around:
        # #             moved_around = self.move([0, distance])
        # #             if not moved_around:
        # #                 self.move([-distance, 0])

        # #     elif self.facing == "w":
        # #         moved_around = self.move([0, -distance])
        # #         if not moved_around:
        # #             moved_around = self.move([0, distance])
        # #             if not moved_around:
        # #                 self.move([distance, 0])

        # #     if self.facing == "n":
        # #         moved_around = self.move([-distance, 0])
        # #         if not moved_around:
        # #             moved_around = self.move([distance, 0])
        # #             if not moved_around:
        # #                 self.move([0, distance])

        # #     if self.facing == "s":
        # #         moved_around = self.move([-distance, 0])
        # #         if not moved_around:
        # #             moved_around = self.move([distance, 0])
        # #             if not moved_around:
        # #                 self.move([0, -distance])

        # if self.roll_frame < self.roll_frame_max - 1:
        #     self.roll_frame += 1
        # else:
        #     self.roll_frame = 0

        super().update()
