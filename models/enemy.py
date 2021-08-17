from __future__ import annotations

from models.screen import Screen
from models.entity import Entity

# The base class for enemies. Contains code for when the entity is
# hurt.
class Enemy(Entity):
    def __init__(
        self,
        dest: tuple[int, int],
        image: str,
        health: int | float,
        damage: int | float,
        parent: Screen,
    ) -> None:
        super().__init__(dest=dest, image=image, parent=parent)

        self.damage = damage
        self.health = health
        self.hurt_cooldown = 0

        parent.not_player_sprites.add(self)
        parent.enemy_sprites.add(self)
        parent.damageable_sprites.add(self)

    def hurt(self, health: int | float) -> None:
        # Start the cooldown timer.
        self.hurt_cooldown = 20
        # Subtract the amount of health that has been damaged and kill
        # the enemy if its health is 0.
        self.health -= health
        if self.health <= 0:
            self.kill()

    def update(self) -> None:
        # Decrease the cooldown.
        if self.hurt_cooldown > 0:
            self.hurt_cooldown -= 1

        super().update()
