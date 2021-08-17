from __future__ import annotations

import pygame
import pygame.mask, pygame.sprite

from models.screen import Screen

# The base class for about everything in the game. Creates basic
# attributes that each of its subclasses uses.
class GameObject(pygame.sprite.Sprite):
    def __init__(
        self, dest: tuple[int, int], image: pygame.Surface, parent: Screen
    ) -> None:
        super().__init__()

        if image is not None:
            # Create a rect and mask for interactions.
            self.image = image
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            (
                self.rect.x,
                self.rect.y,
            ) = dest  # Just learned about ,= (3-26-2021), pretty cool!

            self.parent = parent
            self.parent.sprites.add(self)

    def draw(self) -> None:
        # Blit the sprite at the position on the parent's image.
        self.parent.image.blit(self.image, (self.rect.x, self.rect.y))

    def update(self) -> None:
        self.draw()
