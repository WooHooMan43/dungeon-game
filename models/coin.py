from __future__ import annotations

from models.screen import Screen
from models.item import Item
from paths import ITEM_TEXTURES, ITEM_SOUNDS


class Coin(Item):
    def __init__(self, dest: tuple[int, int], count: int, parent: Screen) -> None:
        super().__init__(
            dest=dest,
            image=parent.images[ITEM_TEXTURES["coin"]] if parent is not None else None,
            count=count,
            collectable=False,
            parent=parent,
        )

    def action(self) -> None:
        super().action()
        # Get the player and add 1 coin to its coins attribute.
        player = self.parent.player_sprites.sprite
        player.coins += 1
        player.points += 10
        # Stop other item sounds and play the coin "ba-ding!"
        self.parent.item_sounds.stop()
        self.parent.item_sounds.play(self.parent.sounds[ITEM_SOUNDS["coin"]["pickup"]])
