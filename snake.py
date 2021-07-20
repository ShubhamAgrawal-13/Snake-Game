import pygame
import random

width = 640
height = 640

rows = 40
cols = 40

block = width // rows

snake = []
color = (122, 122, 122)
x_dir = 1
y_dir = 0

colors = [
		(255, 0, 0),
		(0, 255, 0),
		(0, 0, 255),
		(0, 255, 255),
		(255, 0, 255),
		(255, 255, 0)
]

def move():
	global snake, color, x_dir, y_dir
	keys = pygame.key.get_pressed()

	if(keys[pygame.K_LEFT]):
		x_dir = -1
		y_dir = 0
		# color = (255, 0, 0)

	if(keys[pygame.K_RIGHT]):
		x_dir = 1
		y_dir = 0
		# color = (0, 255, 0)

	if(keys[pygame.K_UP]):
		x_dir = 0
		y_dir = -1
		# color = (0, 0, 255)

	if(keys[pygame.K_DOWN]):
		x_dir = 0
		y_dir = 1
		# color = (255, 0, 255)

def draw_snake(win):
	global snake, color
	for x,y in snake:
		pygame.draw.circle(win, color, (x*block + block//2, y*block + block//2), block//2)


def redraw(win, food):
	win.fill((255, 255, 255))
	draw_snake(win)
	pygame.draw.circle(win, food[2], (food[0]*block + block//2, food[1]*block + block//2), block//2)
	pygame.display.update()

def check():
	global snake
	x, y = snake[0]
	# print(x, y)
	if(x>=0 and y>=0 and x<rows and y<cols):
		# val = snake[1:].count([x, y])
		# if val == 0:
		# 	return True
		# return False
		return True
	return False

def generate_food():
	global color
	x_food = random.randint(1, rows-2)
	y_food = random.randint(1, cols-2)
	food_color = colors[random.randint(0, 5)]
	return [x_food, y_food, food_color]


if __name__ == '__main__':
	print("Snake Game")
	score = 0
	pygame.display.set_caption("Snake Game : " + str(score))
	win = pygame.display.set_mode((width,height))
	x = rows//2
	y = cols//2
	snake.append([x, y])
	snake.append([x-1, y])
	snake.append([x-2, y])
	snake.append([x-3, y])
	snake.append([x-4, y])
	clock = pygame.time.Clock()
	food = generate_food()
	while(1):
		clock.tick(10)
		
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
		
		x1 = snake[0][0] + x_dir
		y1 = snake[0][1] + y_dir
		snake.insert(0, [x1, y1])
		if(x1 == food[0] and y1 == food[1]):
			color = food[2]
			score += 10
			pygame.display.set_caption("Snake Game : " + str(score))
			food = generate_food()
		else:
			snake.pop()
		move()
		redraw(win, food)

		if(not check()):
			print("Game Over")
			print("your score is ", score)
			pygame.quit()
			break