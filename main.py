import  random, math, os, pygame, json
import pygame.display, pygame.time, pygame.image, pygame.sprite, pygame.event, pygame.key, pygame.transform, pygame.mixer

# Custom Imports
from load import load_images, load_sounds, load_level
import paths

pygame.init()

# Create a fullscreen display
flags = pygame.FULLSCREEN | pygame.SCALED
info = pygame.display.Info()

# Get the size of the current display, and use it to
# calculate the size of the game window
if info.current_w > (4/3) * info.current_h:

	dimensions = ( int( (4/3) * info.current_h ), info.current_h )
	tile_side = int(info.current_h/12)

elif info.current_w < (4/3) * info.current_h:

	dimensions = ( info.current_w , int( (3/4) * info.current_w ) )
	tile_side = int(info.current_w/16)
else:

	dimensions = ( info.current_w , info.current_h )
	tile_side = int(info.current_w/16)

# Create the window
game_window = pygame.display.set_mode(dimensions, flags, vsync=1)

# Create the clock
clock = pygame.time.Clock()

# Get the assets
image_list = load_images(os.path.join('assets', 'textures'))
sounds_list = load_sounds(os.path.join('assets', 'sounds'))

# Create groups for collisions, drawing, movement, etc.
all_sprites_group = pygame.sprite.LayeredUpdates()
collidables_group = pygame.sprite.Group()
not_player_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):

	def __init__(self, dest):

		super().__init__()
		self.image = pygame.transform.scale(image_list[paths.player_textures['stand']['s']], (tile_side, tile_side))
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y ,= dest # Just learned about ,= (3-26-2021), pretty cool!
		self.facing = 's'

		self.stats = {
						'coins': 0
					}

		all_sprites_group.add(self)
		player_group.add(self)

	def move(self, dist):

		self.rect.x += dist[0]
		self.rect.y += dist[1]

		if dist[1] > 0 and dist[0] == 0: self.facing = 's'
		elif dist[1] < 0 and dist[0] == 0: self.facing = 'n'
		if dist[0] > 0 and dist[1] == 0: self.facing = 'e'
		elif dist[0] < 0 and dist[1] == 0: self.facing = 'w'

		self.collide(dist)

	def collide(self, dist):

		for thing in all_sprites_group:

			# Sprite collision logic
			if thing in collidables_group and self.rect.colliderect(thing.rect):
				""" If the sprite
						a. can be collided with and
						b. is being collided with
					then apply the collision logic. """
				if dist[1] > 0 and dist[0] == 0: self.rect.bottom = thing.rect.top
				elif dist[1] < 0 and dist[0] == 0: self.rect.top = thing.rect.bottom
				if dist[0] > 0 and dist[1] == 0: self.rect.right = thing.rect.left
				elif dist[0] < 0 and dist[1] == 0: self.rect.left = thing.rect.right

			# Wall Collision logic
			# Move the objects on screen when the player goes off screen
			if self.rect.center[0] <= 0: thing.rect.x += dimensions[0]
			elif self.rect.center[0] >= dimensions[0]: thing.rect.x -= dimensions[0]
			if self.rect.center[1] <= 0: thing.rect.y += dimensions[1]
			elif self.rect.center[1] >= dimensions[1]: thing.rect.y -= dimensions[1]

	def draw(self):

		game_window.blit(self.image, (self.rect.x, self.rect.y))

	def update(self):

		distance = int(tile_side/5)

		# Key logic
		keys = pygame.key.get_pressed()
		if keys[pygame.K_s]: self.move([0, distance])
		if keys[pygame.K_w]: self.move([0, -distance])
		if keys[pygame.K_d]: self.move([distance, 0])
		if keys[pygame.K_a]: self.move([-distance, 0])

		self.image = pygame.transform.scale(image_list[paths.player_textures['stand'][self.facing]], (tile_side, tile_side))

		self.draw()

class Block(pygame.sprite.Sprite):

	def __init__(self, dest, image):

		super().__init__()

		self.image = pygame.transform.scale(image_list[image], (tile_side, tile_side))
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y ,= dest # Just learned about ,= (3-26-2021), pretty cool!

		all_sprites_group.add(self)
		collidables_group.add(self)
		not_player_group.add(self)

	def draw(self):

		game_window.blit(self.image, (self.rect.x, self.rect.y))

	def update(self):

		self.draw()

class Floor(pygame.sprite.Sprite):

	_layer = -1

	def __init__(self, image):

		super().__init__()

		self.image = pygame.Surface(dimensions)
		self.rect = self.image.get_rect()

		if isinstance(image, str):

			# If image is a string (filepath), tile that image across the screen
			self.tiled_image = pygame.transform.scale(image_list[image], (tile_side, tile_side))
			for x in range(16):
				for y in range(12):
					self.image.blit(self.tiled_image, ( x*tile_side, y*tile_side ))

		elif isinstance(image, (tuple, list, pygame.Color)):

			# If its a color or a sequence, fill it with a color
			self.image.fill(image)
		else:

			# If its none of those, fill it with black
			self.image.fill((0,0,0))

		all_sprites_group.add(self)
		not_player_group.add(self)

	def draw(self):

		game_window.blit(self.image, (0,0))

	def update(self):

		self.draw()

class Item(pygame.sprite.Sprite):

	def __init__(self, dest, image, count):

		super().__init__()
		self.image = pygame.transform.scale(image_list[image], (tile_side, tile_side))
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y ,= dest # Just learned about ,= (3-26-2021), pretty cool!

		self.count = count
		self.stack: int

		all_sprites_group.add(self)
		not_player_group.add(self)

	def action(self):
		pass

	def collide(self):

		for player in player_group:
			if self.rect.colliderect(player.rect):
				self.action()
				self.count -= 1
				if self.count <= 0: self.kill()

	def draw(self):

		game_window.blit(self.image, (self.rect.x, self.rect.y))
	
	def update(self):

		self.collide()
		self.draw()

class Coin(Item):

	def __init__(self, dest, count):

		super().__init__(dest, paths.item_textures['coin'], count)

	def action(self):

		for player in player_group:
			player.stats['coins'] += 1

		sounds_list[paths.item_sounds['coin']['pickup']].play()
		
# Creating test objects
for i in range(0, dimensions[0], tile_side):
	Block((i, 0), paths.block_textures['bricks'])
	Block((i, dimensions[1] - tile_side), paths.block_textures['bricks'])
for j in range(tile_side, dimensions[1] - tile_side, tile_side):
	# Block((0, j), paths.block_textures['bricks'])
	Block((dimensions[0] - tile_side, j), paths.block_textures['bricks'])

Block((tile_side*5,tile_side*5), paths.block_textures['bricks'])

Coin((tile_side*7,tile_side*7), 300)

Player((tile_side,tile_side))

Floor(paths.block_textures['tile'])

running = True

while running == True:

	events = pygame.event.get()

	for event in events:
		# Quit the game
		if event.type == pygame.QUIT: running = False

	"""
	Run the update() method of every sprite.
	Essentially eliminates game logic inside the loop.
	Most, if not all sprites should, will, or do have a draw function built-in.
	"""
	all_sprites_group.update() # Oh goodness, I officially love this thing

	# Update the display and tick the clock
	pygame.display.update()

	clock.tick(30)

pygame.quit()