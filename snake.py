import pygame
import random

width = 640
height = 640

rows = 20
cols = 20

bs = width // rows

snake = []
color = (125, 125, 125) 

# right direction
x_dir = 1  
y_dir = 0

def move():
	global snake, x_dir, y_dir
	keys = pygame.key.get_pressed()

	if(keys[pygame.K_LEFT]):
		x_dir = -1
		y_dir = 0
	if(keys[pygame.K_RIGHT]):
		x_dir = 1
		y_dir = 0
	if(keys[pygame.K_UP]):
		x_dir = 0
		y_dir = -1
	if(keys[pygame.K_DOWN]):
		x_dir = 0
		y_dir = 1



def draw_snake(win):
	global snake
	for x,y in snake:
		pygame.draw.circle(win, color, (x*bs + bs//2, y*bs - bs//2), bs//2)

def redraw(win, food):
	win.fill((255, 255, 255))
	draw_snake(win)
	pygame.draw.circle(win, food[2], (food[0]*bs + bs//2, food[1]*bs - bs//2), bs//2)
	pygame.display.update()

def check():
	global snake
	head = snake[0]
	x, y = head
	if(x>=0 and x<rows and y>=0 and y<cols):
		return True
	return False

def generate_food():
	x = random.randint(1, rows-1)
	y = random.randint(1, cols-1)
	food_color = random_color()
	return [x, y, food_color]

def random_color():
	x1 = random.randint(20, 230)
	x2 = random.randint(20, 230)
	x3 = random.randint(20, 230)

	return (x1, x2, x3)



if __name__ == '__main__':
	score = 0
	pygame.display.set_caption("Snake Game : Score : " + str(score))
	win = pygame.display.set_mode((width,height))
	clock = pygame.time.Clock()
	x = rows // 2
	y = cols // 2

	snake.append([x, y])
	snake.append([x-1, y])
	snake.append([x-2, y])
	snake.append([x-3, y])

	food = generate_food()

	while(1):
		clock.tick(7)
		# code
		x1 = snake[0][0] + x_dir
		y1 = snake[0][1] + y_dir

		snake.insert(0, [x1, y1]) #insert at head
		if(x1 == food[0] and y1 == food[1]):
			score += 10
			color = food[2]
			pygame.display.set_caption("Snake Game : Score : " + str(score))
			food = generate_food()
		else:
			snake.pop() #remove the last entry

		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()

		move()
		redraw(win, food)
		if(not check()):
			print("Your Score : ", score)
			print("Game Over")
			pygame.quit()
			break
