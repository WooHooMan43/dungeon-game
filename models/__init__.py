# Import every module from this folder

from models.block import Block
from models.coin import Coin
from models.enemy import Enemy
from models.entity import Entity
from models.floor import Floor
from models.game_object import GameObject
from models.health import Health
from models.hud import HUD
from models.item import Item
from models.parabodroid import Parabodroid
from models.player import Player
from models.projectile import Projectile
from models.screen import Screen
from models.sphere import SphereEnemy
from models.sword import SwordItem, SwordWeapon
from models.triangle import TriangleItem, TriangleProjectile
from models.weapon import Weapon

# I'm keeping the code below for the future. I know it's bad practice,
# but hear me out: my vision for this game was for it to be almost
# completely moddable and customizable. Being the novice programmer
# that I am, I don't know how to do that yet, but the code below
# (which I found online) dynamically imports every module in this
# folder, which seems like a crucual step towar my goal.

# from inspect import isclass
# from pkgutil import iter_modules
# from pathlib import Path
# from importlib import import_module

# # iterate through the modules in the current package
# package_dir = Path(__file__).resolve().parent
# for (_, module_name, _) in iter_modules([package_dir]):

#     # import the module and iterate through its attributes
#     module = import_module(f"{__name__}.{module_name}")
#     for attribute_name in dir(module):
#         attribute = getattr(module, attribute_name)

#         if isclass(attribute):
#             # Add the class to this package's variables
#             globals()[attribute_name] = attribute
