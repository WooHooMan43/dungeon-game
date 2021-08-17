import os

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
        "s": os.path.join(PLAYER_TEXTURE_PATH, "stand", "s.png"),
        "n": os.path.join(PLAYER_TEXTURE_PATH, "stand", "n.png"),
        "e": os.path.join(PLAYER_TEXTURE_PATH, "stand", "e.png"),
        "w": os.path.join(PLAYER_TEXTURE_PATH, "stand", "w.png"),
    },
    "use": {
        "s": os.path.join(PLAYER_TEXTURE_PATH, "use", "s.png"),
        "n": os.path.join(PLAYER_TEXTURE_PATH, "use", "n.png"),
        "e": os.path.join(PLAYER_TEXTURE_PATH, "use", "e.png"),
        "w": os.path.join(PLAYER_TEXTURE_PATH, "use", "w.png"),
    },
    "walk": {
        "s": [
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "s", "0.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "s", "1.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "s", "2.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "s", "3.png"),
        ],
        "n": [
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "n", "0.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "n", "1.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "n", "2.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "n", "3.png"),
        ],
        "e": [
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "e", "0.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "e", "1.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "e", "2.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "e", "3.png"),
        ],
        "w": [
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "w", "0.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "w", "1.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "w", "2.png"),
            os.path.join(PLAYER_TEXTURE_PATH, "walk", "w", "3.png"),
        ],
    },
}

SPHERE_TEXTURE_PATH = os.path.join(ENTITY_TEXTURE_PATH, "sphere")
PARABOLOID_TEXTURE_PATH = os.path.join(ENTITY_TEXTURE_PATH, "paraboloid")
CYLINDER_TEXTURE_PATH = os.path.join(ENTITY_TEXTURE_PATH, "cylinder")
ENEMY_TEXTURES = {
    "sphere": {
        "still": {
            "s": os.path.join(SPHERE_TEXTURE_PATH, "still", "s.png"),
            "n": os.path.join(SPHERE_TEXTURE_PATH, "still", "n.png"),
            "e": os.path.join(SPHERE_TEXTURE_PATH, "still", "e.png"),
            "w": os.path.join(SPHERE_TEXTURE_PATH, "still", "w.png"),
        },
        "roll": {
            "s": [],
            "n": [],
            "e": [],
            "w": [],
        },
        "sleep": os.path.join(SPHERE_TEXTURE_PATH, "sleep.png"),
    },
    "paraboloid": {
        "stand": {
            "s": os.path.join(PARABOLOID_TEXTURE_PATH, "stand", "s.png"),
            "n": os.path.join(PARABOLOID_TEXTURE_PATH, "stand", "n.png"),
            "e": os.path.join(PARABOLOID_TEXTURE_PATH, "stand", "e.png"),
            "w": os.path.join(PARABOLOID_TEXTURE_PATH, "stand", "w.png"),
        },
        "walk": {
            "s": [
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "s", "0.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "s", "1.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "s", "2.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "s", "3.png"),
            ],
            "n": [
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "n", "0.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "n", "1.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "n", "2.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "n", "3.png"),
            ],
            "e": [
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "e", "0.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "e", "1.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "e", "2.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "e", "3.png"),
            ],
            "w": [
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "w", "0.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "w", "1.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "w", "2.png"),
                os.path.join(PARABOLOID_TEXTURE_PATH, "walk", "w", "3.png"),
            ],
        },
    },
    "cylinder": {
        "stand": {
            "s": os.path.join(CYLINDER_TEXTURE_PATH, "stand", "s.png"),
            "n": os.path.join(CYLINDER_TEXTURE_PATH, "stand", "n.png"),
            "e": os.path.join(CYLINDER_TEXTURE_PATH, "stand", "e.png"),
            "w": os.path.join(CYLINDER_TEXTURE_PATH, "stand", "w.png"),
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
    "circle_bullet": os.path.join(ENTITY_TEXTURE_PATH, "bullet", "circle.png"),
    "triangle": [
        os.path.join(ENTITY_TEXTURE_PATH, "projectiles", "triangle", "0.png"),
        os.path.join(ENTITY_TEXTURE_PATH, "projectiles", "triangle", "1.png"),
        os.path.join(ENTITY_TEXTURE_PATH, "projectiles", "triangle", "2.png"),
        os.path.join(ENTITY_TEXTURE_PATH, "projectiles", "triangle", "3.png"),
    ],
}

BLOCK_TEXTURES = {
    "bricks": os.path.join(TEXTURE_PATH, "blocks", "bricks.png"),
    "tile": os.path.join(TEXTURE_PATH, "blocks", "tile.png"),
}

ITEM_TEXTURES = {
    "coin": os.path.join(ITEM_TEXTURE_PATH, "coin", "coin.png"),
    "sword": os.path.join(ITEM_TEXTURE_PATH, "sword", "item.png"),
    "health": os.path.join(ITEM_TEXTURE_PATH, "health", "health.png"),
}

WEAPON_TEXTURES = {
    "sword": {
        "s": [
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "s", "0.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "s", "1.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "s", "2.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "s", "3.png"),
        ],
        "n": [
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "n", "0.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "n", "1.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "n", "2.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "n", "3.png"),
        ],
        "e": [
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "e", "0.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "e", "1.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "e", "2.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "e", "3.png"),
        ],
        "w": [
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "w", "0.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "w", "1.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "w", "2.png"),
            os.path.join(ITEM_TEXTURE_PATH, "sword", "use", "w", "3.png"),
        ],
    }
}

PLAYER_SOUNDS = {
    "step": os.path.join(ENTITY_SOUND_PATH, "player", "step.wav"),
    "hurt": os.path.join(ENTITY_SOUND_PATH, "player", "hurt.wav"),
}

ENEMY_SOUNDS = {
    "sphere": {
        "roll": os.path.join(ENTITY_SOUND_PATH, "sphere", "roll.wav"),
        "hurt": os.path.join(ENTITY_SOUND_PATH, "sphere", "hurt.wav"),
    },
    "paraboloid": {
        "step": os.path.join(ENTITY_SOUND_PATH, "paraboloid", "step.wav"),
        "hurt": os.path.join(ENTITY_SOUND_PATH, "paraboloid", "hurt.wav"),
    },
    "cylinder": {
        "step": os.path.join(ENTITY_SOUND_PATH, "cylinder", "step.wav"),
        "hurt": os.path.join(ENTITY_SOUND_PATH, "cylinder", "hurt.wav"),
    },
}

ITEM_SOUNDS = {
    "coin": {
        "pickup": os.path.join(SOUND_PATH, "items", "coin", "pickup.wav"),
        "drop": os.path.join(SOUND_PATH, "items", "coin", "drop.wav"),
    },
    "health": {
        "pickup": os.path.join(SOUND_PATH, "items", "health", "pickup.wav"),
    },
    "item": {"pickup": os.path.join(SOUND_PATH, "items", "item", "pickup.wav")},
}

WEAPON_SOUNDS = {
    "sword": {"swing": os.path.join(SOUND_PATH, "items", "sword", "swing.wav")}
}

PROJECTILE_SOUNDS = {
    "triangle": os.path.join(SOUND_PATH, "items", "triangle", "throw.wav"),
}

MUSIC_SOUNDS = {
    "intro": os.path.join(SOUND_PATH, "music", "main_intro.wav"),
    "main": os.path.join(SOUND_PATH, "music", "main.wav"),
}

GUI_SOUNDS = {
    "button": {
        "hover": os.path.join(SOUND_PATH, "gui", "button", "hover.wav"),
        "click": os.path.join(SOUND_PATH, "gui", "button", "click.wav"),
    }
}

HUD_TEXTURE = os.path.join(TEXTURE_PATH, "gui", "hud.png")
SELECTED_TEXTURE = os.path.join(TEXTURE_PATH, "gui", "selected.png")
ITEM_BORDER = os.path.join(TEXTURE_PATH, "gui", "item.png")
