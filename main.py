import pygame

clock = pygame.time.Clock()
fps = 30
screen_width = 480
screen_height = 360

def main():
	pygame.init()
	screen = pygame.display.set_mode((screen_width, screen_height))
	running = True
	
	image = pygame.image.load("images/smily.jpg")
	xpos = 50
	ypos = 50
	image_width, image_height = image.get_rect().size
	
	while running:
		clock.tick(fps)
		keys = pygame.key.get_pressed()
		screen.fill((0, 0, 0))
		
		if keys[pygame.K_UP]:
			ypos -= 5
		if keys[pygame.K_DOWN]:
			ypos += 5
		if keys[pygame.K_LEFT]:
			xpos -= 5
		if keys[pygame.K_RIGHT]:
			xpos += 5
		
		if xpos >= screen_width:
			xpos = -image_width
		if xpos < -image_width:
			xpos = screen_width
		if ypos >= screen_height:
			ypos = -image_height
		if ypos < -image_height:
			ypos = screen_height
		
		screen.blit(image, (xpos, ypos))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				print(clock.get_fps())

if __name__ == "__main__":
	main()