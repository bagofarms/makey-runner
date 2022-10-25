import pgzrun
import random

pygame.init()

pygame.display.set_mode((640,640), pygame.FULLSCREEN)
pygame.display.init()

score = 0
game_over = False
velocity_y = 0
gravity = 1

makey = Actor('makey')
makey.x = 100
makey.y = 467

obstacles = []
obstacles_timeout = 0

def update():
	global score, game_over, velocity_y, gravity, obstacles_timeout, obstacles

	obstacles_timeout += 1
	if obstacles_timeout > 50:
		actor = Actor('cactus')
		actor.x = 640
		actor.y = 472
		obstacles.append(actor)
		obstacles_timeout = 0

	for actor in obstacles:
		actor.x -= 8
		if actor.x < -50:
			obstacles.remove(actor)
			score += 1

	if keyboard.up:
		velocity_y = -15

	makey.y += velocity_y
	velocity_y += gravity
	if makey.y > 467:
		velocity = 0
		makey.y = 467

	if makey.collidelist(obstacles) != -1:
		game_over = True

def draw():
	global score, game_over
	# Draw sky
	screen.draw.filled_rect(Rect(0,0,640,640), (0,0,0))
	# Draw ground
	screen.draw.filled_rect(Rect(0,500,640,140), (0,255,0))

	if game_over:
		screen.draw.text('Game Over', centerx=320, centery=320, color=(255,255,255), fontsize=60)
		screen.draw.text('Score: ' + str(score), centerx=320, centery=380, color=(255,255,255), fontsize=40)
	else:
		makey.draw()
		creen.draw.text("Score: " + str(score), (15,10), color=(255,255,255), fontsize=40)

		for actor in obstacles:
			actor.draw();

pgzrun.go()
