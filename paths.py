import os

texture_path = os.path.join('assets', 'textures')
sound_path = os.path.join('assets', 'sounds')

player_textures = {
			'stand': {
				's': os.path.join(texture_path, 'entities', 'player', 'stand_s.png'),
				'n': os.path.join(texture_path, 'entities', 'player', 'stand_n.png'),
				'e': os.path.join(texture_path, 'entities', 'player', 'stand_e.png'), 
				'w': os.path.join(texture_path, 'entities', 'player', 'stand_w.png')
			},
			'walk': {

			}
		}

block_textures = {
			'bricks': os.path.join(texture_path, 'blocks', 'bricks.png'),
			'tile': os.path.join(texture_path, 'blocks', 'tile.png')
		}

item_textures = {
			'coin': os.path.join(texture_path, 'items', 'coin', 'coin.png'),
		}

item_sounds = {
			'coin': {
				'pickup': os.path.join(sound_path, 'coin', 'pickup.wav'),
				'drop': os.path.join(sound_path, 'coin', 'drop.wav')
			}
		}