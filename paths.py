import os

from utils import resource_path

# Each and every variable here is used to shorten the paths of assets
# and make the process of changing paths of assets easier.

TEXTURE_PATH = os.path.join("assets", "textures")
SOUND_PATH = os.path.join("assets", "sounds")

ITEM_TEXTURE_PATH = os.path.join(TEXTURE_PATH, "items")
ENTITY_TEXTURE_PATH = os.path.join(TEXTURE_PATH, "entities")
ENTITY_SOUND_PATH = os.path.join(SOUND_PATH, "entities")

PLAYER_TEXTURE_PATH = os.path.join(ENTITY_TEXTURE_PATH, "cube")
PLAYER_TEXTURES = {
    "stand": {
        "s": resource_path(os.path.join(PLAYER_TEXTURE_PATH, "stand", "s.png")),
        "n": resource_path(os.path.join(PLAYER_TEXTURE_PATH, "stand", "n.png")),
        "e": resource_path(os.path.join(PLAYER_TEXTURE_PATH, "stand", "e.png")),
        "w": resource_path(os.path.join(PLAYER_TEXTURE_PATH, "stand", "w.png")),
    },
    "use": {
        "s": resource_path(os.path.join(PLAYER_TEXTURE_PATH, "use", "s.png")),
        "n": resource_path(os.path.join(PLAYER_TEXTURE_PATH, "use", "n.png")),
        "e": resource_path(os.path.join(PLAYER_TEXTURE_PATH, "use", "e.png")),
        "w": resource_path(os.path.join(PLAYER_TEXTURE_PATH, "use", "w.png")),
    },
    "walk": {
        "s": [
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "s", "0.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "s", "1.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "s", "2.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "s", "3.png")),
        ],
        "n": [
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "n", "0.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "n", "1.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "n", "2.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "n", "3.png")),
        ],
        "e": [
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "e", "0.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "e", "1.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "e", "2.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "e", "3.png")),
        ],
        "w": [
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "w", "0.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "w", "1.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "w", "2.png")),
            resource_path(os.path.join(PLAYER_TEXTURE_PATH, "walk", "w", "3.png")),
        ],
    },
}

SPHERE_TEXTURE_PATH = os.path.join(ENTITY_TEXTURE_PATH, "sphere")
PARABOLOID_TEXTURE_PATH = os.path.join(ENTITY_TEXTURE_PATH, "paraboloid")
CYLINDER_TEXTURE_PATH = os.path.join(ENTITY_TEXTURE_PATH, "cylinder")
ENEMY_TEXTURES = {
    "sphere": {
        "still": {
            "s": resource_path(os.path.join(SPHERE_TEXTURE_PATH, "still", "s.png")),
            "n": resource_path(os.path.join(SPHERE_TEXTURE_PATH, "still", "n.png")),
            "e": resource_path(os.path.join(SPHERE_TEXTURE_PATH, "still", "e.png")),
            "w": resource_path(os.path.join(SPHERE_TEXTURE_PATH, "still", "w.png")),
        },
        "roll": {
            "s": [],
            "n": [],
            "e": [],
            "w": [],
        },
        "sleep": resource_path(os.path.join(SPHERE_TEXTURE_PATH, "sleep.png")),
    },
    "paraboloid": {
        "stand": {
            "s": resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "stand", "s.png")),
            "n": resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "stand", "n.png")),
            "e": resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "stand", "e.png")),
            "w": resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "stand", "w.png")),
        },
        "walk": {
            "s": [
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "s", "0.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "s", "1.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "s", "2.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "s", "3.png")),
            ],
            "n": [
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "n", "0.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "n", "1.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "n", "2.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "n", "3.png")),
            ],
            "e": [
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "e", "0.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "e", "1.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "e", "2.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "e", "3.png")),
            ],
            "w": [
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "w", "0.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "w", "1.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "w", "2.png")),
                resource_path(os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "w", "3.png")),
            ],
        },
    },
    "cylinder": {
        "stand": {
            "s": resource_path(os.path.join(CYLINDER_TEXTURE_PATH, "stand", "s.png")),
            "n": resource_path(os.path.join(CYLINDER_TEXTURE_PATH, "stand", "n.png")),
            "e": resource_path(os.path.join(CYLINDER_TEXTURE_PATH, "stand", "e.png")),
            "w": resource_path(os.path.join(CYLINDER_TEXTURE_PATH, "stand", "w.png")),
        },
        "use": {
            "s": [],
            "n": [],
            "e": [],
            "w": [],
        },
        "walk": {
            "s": [],
            "n": [],
            "e": [],
            "w": [],
        },
    },
}

PROJECTILE_TEXTURES = {
    "circle_bullet": resource_path(os.path.join(ENTITY_TEXTURE_PATH, "bullet", "circle.png")),
    "triangle": [
        resource_path(os.path.join(ENTITY_TEXTURE_PATH, "projectiles", "triangle", "0.png")),
        resource_path(os.path.join(ENTITY_TEXTURE_PATH, "projectiles", "triangle", "1.png")),
        resource_path(os.path.join(ENTITY_TEXTURE_PATH, "projectiles", "triangle", "2.png")),
        resource_path(os.path.join(ENTITY_TEXTURE_PATH, "projectiles", "triangle", "3.png")),
    ],
}

BLOCK_TEXTURES = {
    "bricks": resource_path(os.path.join(TEXTURE_PATH, "blocks", "bricks.png")),
    "tile": resource_path(os.path.join(TEXTURE_PATH, "blocks", "tile.png")),
}

ITEM_TEXTURES = {
    "coin": resource_path(os.path.join(ITEM_TEXTURE_PATH, "coin", "coin.png")),
    "sword": resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "item.png")),
    "health": resource_path(os.path.join(ITEM_TEXTURE_PATH, "health", "health.png")),
}

WEAPON_TEXTURES = {
    "sword": {
        "s": [
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "s", "0.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "s", "1.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "s", "2.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "s", "3.png")),
        ],
        "n": [
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "n", "0.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "n", "1.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "n", "2.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "n", "3.png")),
        ],
        "e": [
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "e", "0.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "e", "1.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "e", "2.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "e", "3.png")),
        ],
        "w": [
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "w", "0.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "w", "1.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "w", "2.png")),
            resource_path(os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "w", "3.png")),
        ],
    }
}

PLAYER_SOUNDS = {
    "step": resource_path(os.path.join(ENTITY_SOUND_PATH, "player", "step.wav")),
    "hurt": resource_path(os.path.join(ENTITY_SOUND_PATH, "player", "hurt.wav")),
}

ENEMY_SOUNDS = {
    "sphere": {
        "roll": resource_path(os.path.join(ENTITY_SOUND_PATH, "sphere", "roll.wav")),
        "hurt": resource_path(os.path.join(ENTITY_SOUND_PATH, "sphere", "hurt.wav")),
    },
    "paraboloid": {
        "step": resource_path(os.path.join(ENTITY_SOUND_PATH, "paraboloid", "step.wav")),
        "hurt": resource_path(os.path.join(ENTITY_SOUND_PATH, "paraboloid", "hurt.wav")),
    },
    "cylinder": {
        "step": resource_path(os.path.join(ENTITY_SOUND_PATH, "cylinder", "step.wav")),
        "hurt": resource_path(os.path.join(ENTITY_SOUND_PATH, "cylinder", "hurt.wav")),
    },
}

ITEM_SOUNDS = {
    "coin": {
        "pickup": resource_path(os.path.join(SOUND_PATH, "items", "coin", "pickup.wav")),
        "drop": resource_path(os.path.join(SOUND_PATH, "items", "coin", "drop.wav")),
    },
    "health": {
        "pickup": resource_path(os.path.join(SOUND_PATH, "items", "health", "pickup.wav")),
    },
    "item": {"pickup": resource_path(os.path.join(SOUND_PATH, "items", "item", "pickup.wav"))},
}

WEAPON_SOUNDS = {
    "sword": {"swing": resource_path(os.path.join(SOUND_PATH, "items", "sword", "swing.wav"))}
}

PROJECTILE_SOUNDS = {
    "triangle": resource_path(os.path.join(SOUND_PATH, "items", "triangle", "throw.wav")),
}

MUSIC_SOUNDS = {
    "intro": resource_path(os.path.join(SOUND_PATH, "music", "main_intro.wav")),
    "main": resource_path(os.path.join(SOUND_PATH, "music", "main.wav")),
}

GUI_SOUNDS = {
    "button": {
        "hover": resource_path(os.path.join(SOUND_PATH, "gui", "button", "hover.wav")),
        "click": resource_path(os.path.join(SOUND_PATH, "gui", "button", "click.wav")),
    }
}

HUD_TEXTURE = resource_path(os.path.join(TEXTURE_PATH, "gui", "hud.png"))
SELECTED_TEXTURE = resource_path(os.path.join(TEXTURE_PATH, "gui", "selected.png"))
ITEM_BORDER = resource_path(os.path.join(TEXTURE_PATH, "gui", "item.png"))
