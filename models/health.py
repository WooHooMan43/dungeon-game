from __future__ import annotations

from models.screen import Screen
from models.item import Item
from paths import ITEM_TEXTURES, ITEM_SOUNDS


class Health(Item):
    def __init__(self, dest: tuple[int, int], parent: Screen) -> None:
        super().__init__(
            dest=dest,
            image=parent.images[ITEM_TEXTURES["health"]],
            count=1,
            collectable=False,
            parent=parent,
        )

        self.stack = 1

    def action(self) -> None:
        super().action()
        # Get the player and add 1 coin to its coins attribute.
        player = self.parent.player_sprites.sprite
        player.health += 5
        player.points += 100
        # Stop other item sounds and play the coin "ba-ding!"
        self.parent.item_sounds.stop()
        self.parent.item_sounds.play(
            self.parent.sounds[ITEM_SOUNDS["health"]["pickup"]]
        )
