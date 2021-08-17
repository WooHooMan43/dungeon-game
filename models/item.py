from __future__ import annotations

import pygame
import pygame.sprite, pygame.transform
import copy

from models.screen import Screen
from models.game_object import GameObject
from models.entity import Entity

# The base class for all item objects.
class Item(GameObject):
    def __init__(
        self,
        dest: tuple[int, int],
        image: pygame.Surface,
        count: int,
        collectable: bool,
        parent: Screen,
    ) -> None:
        super().__init__(dest=dest, image=image, parent=parent)

        # These specify the count and max count an item can have (will
        # be used for dropping items).
        self.count = count
        self.stack: int = 0

        # This specifies if the item can be held or go in the player's
        # inventory.
        self.collectable = collectable

        # This is the entity that has this item (Important for using
        # the item).
        self.user: Entity | None = None

        self.parent.not_player_sprites.add(self)

    def copy(self):
        # Create a copy of the item for storage in an inventory.
        copyobj = type(self)(parent=self.parent)
        copyobj.image = self.image.copy()
        copyobj.rect = self.rect.copy()
        copyobj.mask = self.mask.copy()
        copyobj.count = 1
        copyobj.stack = self.stack
        copyobj.collectable = self.collectable
        # Remove it from groups to prevent duplicates.
        copyobj.remove(copyobj.groups())
        return copyobj

    def action(self) -> None:
        # This is used when the entity collects the item.
        # Reduce the count and remove the item if the count is 0.
        self.count -= 1
        if self.count <= 0:
            self.kill()
        return

    def click_action(self) -> None:
        # This is used when the entity uses the item.
        return

    def collide(self) -> None:
        # Can this item be put in an inventory?
        if self.collectable:
            # Get a list of all sprites that can hold things that are
            # colliding with the sprite's mask.
            colliding_sprites = pygame.sprite.spritecollide(
                sprite=self,
                group=self.parent.handed_sprites,
                dokill=False,
                collided=pygame.sprite.collide_mask,
            )

            for sprite in colliding_sprites:
                # Is the collector the player?
                if sprite in self.parent.player_sprites:
                    # Find an inventory slot containing the same type
                    # of item.
                    for item in range(len(sprite.inventory)):
                        # Is the item at this index the same type as
                        # this item?
                        if type(sprite.inventory[item]) == type(self):
                            # Is the item's stack > count?
                            if (
                                sprite.inventory[item].stack
                                > sprite.inventory[item].count
                                or sprite.inventory[item].stack < 1
                            ):
                                # Add one to the item's count.
                                sprite.inventory[item].count += 1
                                # Collect the item.
                                self.action()
                                break
                    else:
                        # Find the first empty slot in the inventory.
                        for item in range(len(sprite.inventory)):
                            # Is there no item at this index?
                            if sprite.inventory[item] == None:
                                # Create an item in the inventory.
                                sprite.inventory[item] = self.copy()
                                sprite.inventory[item].user = sprite
                                # Collect the item.
                                self.action()
                                break
                else:
                    # Is the entity currently holding an item?
                    if sprite.selected_item == None:
                        # Create an item in the inventory.
                        sprite.selected_item = self.copy()
                        sprite.selected_item.user = sprite
                        # Collect the item.
                        self.action()
                    # Is the entity holding the same type of item?
                    elif type(sprite.selected_item) == type(self):
                        # Is the item's stack > count?
                        if sprite.selected_item.stack > sprite.selected_item.count:
                            sprite.selected_item.count += 1
                            # Collect the item.
                            self.action()
        else:
            # Check if the player is colliding with the item.
            colliding_sprite = pygame.sprite.spritecollideany(
                sprite=self,
                group=self.parent.player_sprites,
                collided=pygame.sprite.collide_mask,
            )
            if colliding_sprite is not None:
                # Collect the item.
                self.action()

    def draw(self) -> None:
        self.parent.image.blit(self.image, (self.rect.x, self.rect.y))

    def update(self) -> None:
        self.collide()
        self.draw()
