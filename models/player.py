from __future__ import annotations

import pygame
import pygame.transform, pygame.key, pygame.mask, pygame.mouse, pygame.event, pygame.sprite
import math

from models.game_object import GameObject
from models.screen import Screen
from models.entity import Entity
from models.item import Item
from paths import PLAYER_TEXTURES, PLAYER_SOUNDS

M_LEFT = 0
M_MIDDLE = 1
M_RIGHT = 2


class Player(Entity):
    _layer = 1

    def __init__(self, dest: tuple[int, int], parent: Screen) -> None:
        super().__init__(dest=dest, image=PLAYER_TEXTURES["stand"]["s"], parent=parent)

        self.walk_frame = 0
        self.walk_frame_max = 16
        self.use_frame = 0
        self.use_frame_max = 4

        self.ready = True
        # All displayed info about a player
        self.coins = 0
        self.points = 0
        self.health = 20
        self.max_health = 20
        self.hurt_cooldown = 0
        self.inventory: list[Item | None] = [None, None, None, None, None]
        self.selected_item = 0

        self.parent.player_sprites.add(self)
        self.parent.handed_sprites.add(self)
        self.parent.damageable_sprites.add(self)

    def hurt(self, health: int | float) -> None:
        def getTopLevelParent(obj: GameObject) -> GameObject:
            return obj if obj.parent is None else getTopLevelParent(obj.parent)

        # Start the cooldown timer.
        self.hurt_cooldown = 30
        # Subtract the amount of health that has been damaged and kill
        # the player if its health is 0.
        self.health -= health
        if self.health <= 0:
            self.kill()
            getTopLevelParent(self).screens["death"].add(
                getTopLevelParent(self).sprites
            )
            pygame.mixer.pause()
            getTopLevelParent(self).paused = True
        else:
            self.parent.player_sounds.play(self.parent.sounds[PLAYER_SOUNDS["hurt"]])

    def collide(self, dist: tuple[int, int]) -> None:
        super().collide(dist)

        for sprite in self.parent.sprites:
            # Is the sprite not a floor?
            if sprite not in self.parent.floor_sprites:
                # Wall Collision logic
                # Move the objects on screen when the player goes off screen
                if self.rect.centerx < 0:
                    sprite.rect.centerx += self.parent.rect.width
                elif self.rect.centerx > self.parent.rect.width:
                    sprite.rect.centerx -= self.parent.rect.width
                if self.rect.centery < 0:
                    sprite.rect.centery += self.parent.rect.height
                elif self.rect.centery > self.parent.rect.height:
                    sprite.rect.centery -= self.parent.rect.height

    def update(self) -> None:
        def getTopLevelCoords(obj: GameObject) -> tuple[int, int]:
            parent_x, parent_y, = (
                getTopLevelCoords(obj.parent) if obj.parent is not None else (0, 0)
            )
            return (obj.rect.x + parent_x, obj.rect.y + parent_y)

        distance = int(self.parent.tile_side / 10)

        # Key logic
        keys = pygame.key.get_pressed()
        buttons = pygame.mouse.get_pressed(3)
        wheel_events = [
            event for event in pygame.event.get() if event.type == pygame.MOUSEWHEEL
        ]
        wheel = wheel_events[0] if len(wheel_events) > 0 else None

        if not self.stuck:

            if keys[pygame.K_s]:
                self.move([0, distance])
            if keys[pygame.K_w]:
                self.move([0, -distance])
            if keys[pygame.K_d]:
                self.move([distance, 0])
            if keys[pygame.K_a]:
                self.move([-distance, 0])

            if buttons[M_LEFT] and self.ready:
                mouse_pos = pygame.mouse.get_pos()
                player_pos = getTopLevelCoords(self)
                rel_pos = (
                    mouse_pos[0] - player_pos[0],
                    mouse_pos[1] - player_pos[1],
                )
                if rel_pos[0] > rel_pos[1]:
                    if -rel_pos[0] < rel_pos[1]:
                        self.facing = "e"
                    else:
                        self.facing = "n"
                else:
                    if -rel_pos[0] > rel_pos[1]:
                        self.facing = "w"
                    else:
                        self.facing = "s"

                item = self.inventory[self.selected_item]
                if item is not None:
                    item.click_action()
                    self.ready = False
                    if item.count <= 0:
                        self.inventory[self.selected_item]
                        del item

            if not buttons[M_LEFT]:
                self.ready = True

            if wheel is not None:
                self.selected_item += wheel.y
                self.selected_item = self.selected_item % len(self.inventory)

            if keys[pygame.K_1]:
                self.selected_item = 0
            elif keys[pygame.K_2]:
                self.selected_item = 1
            elif keys[pygame.K_3]:
                self.selected_item = 2
            elif keys[pygame.K_4]:
                self.selected_item = 3
            elif keys[pygame.K_5]:
                self.selected_item = 4

            if not (
                keys[pygame.K_s]
                or keys[pygame.K_w]
                or keys[pygame.K_d]
                or keys[pygame.K_a]
                or buttons[M_LEFT]
            ):
                self.image = self.parent.images[PLAYER_TEXTURES["stand"][self.facing]]
                self.walk_frame = 0
            elif not buttons[M_LEFT]:
                self.image = self.parent.images[
                    PLAYER_TEXTURES["walk"][self.facing][
                        math.floor(self.walk_frame / (self.walk_frame_max / 4))
                    ]
                ]
                if self.walk_frame % 8 == 0:
                    self.parent.player_sounds.stop()
                    self.parent.player_sounds.play(
                        self.parent.sounds[PLAYER_SOUNDS["step"]]
                    )
            else:
                self.image = self.parent.images[PLAYER_TEXTURES["use"][self.facing]]

            if self.walk_frame < self.walk_frame_max - 1:
                self.walk_frame += 1
            else:
                self.walk_frame = 0

            self.mask = pygame.mask.from_surface(self.image)

        # Get a list of enemies touching the player.
        colliding_enemies = pygame.sprite.spritecollide(
            sprite=self,
            group=self.parent.enemy_sprites,
            dokill=False,
            collided=pygame.sprite.collide_mask,
        )
        for sprite in colliding_enemies:
            # Is the player still on cooldown?
            if self.hurt_cooldown <= 0 and sprite.damage > 0:
                self.hurt(sprite.damage)
                break

        # Decrease the cooldown.
        if self.hurt_cooldown > 0:
            self.hurt_cooldown -= 1

        super().update()
