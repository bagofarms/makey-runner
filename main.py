import pgzrun, pygame
import random

WIDTH = 64
HEIGHT = 64

draw_once = True
score = 0
game_over = False
velocity_y = 0

gravity = 0.15
jump_force = -3
run_speed = 1

makey = Actor('makey')
makey.x = 10
makey.y = 45

obstacles = []
obstacles_timeout = 0

def on_key_down(key):
	if key == keys.F:
		screen.surface = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
	elif key == keys.W:
		screen.surface = pygame.display.set_mode((WIDTH,HEIGHT))

def update():
	global score, game_over, velocity_y, gravity, obstacles_timeout, obstacles

	obstacles_timeout += 1
	if obstacles_timeout > 50:
		actor = Actor('cactus')
		actor.x = 64
		actor.y = 45
		obstacles.append(actor)
		obstacles_timeout = 0

	for actor in obstacles:
		actor.x -= run_speed
		if actor.x < -5:
			obstacles.remove(actor)
			score += 1

	if keyboard.up:
		if makey.y == 45:
			velocity_y = jump_force

	makey.y += velocity_y
	velocity_y += gravity
	if makey.y > 45:
		velocity_y = 0
		makey.y = 45

	if makey.collidelist(obstacles) != -1:
		game_over = True

def draw():
	global score, game_over, draw_once

	if draw_once:
		# Set screen size
		screen.surface = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
		# Draw ground
		screen.draw.filled_rect(Rect(0,50,64,14), (0,255,0))
		draw_once = False

	# Draw sky
	screen.draw.filled_rect(Rect(0,0,64,50), (0,0,0))

	#if game_over:
	#	screen.draw.text('Game Over', centerx=320, centery=320, color=(255,255,255), fontsize=60)
	#	screen.draw.text('Score: ' + str(score), centerx=320, centery=380, color=(255,255,255), fontsize=40)
	#else:
	makey.draw()
	#screen.draw.text("Score: " + str(score), (15,10), color=(255,255,255), fontsize=40)

	for actor in obstacles:
		actor.draw();

pgzrun.go()
