import pygame

clock = pygame.time.Clock()
fps = 30
screen_width = 240
screen_height = 176
black = (0, 0, 0, 255)
white = (255, 255, 255, 255)

def main():
	pygame.init()
	screen = pygame.display.set_mode((screen_width, screen_height))
	running = True
	
	background_bottom = pygame.image.load("./Images/Maps/Bottom/PalletTown.png")
	player = pygame.image.load("./Images/Characters/Player.png")
	player.set_colorkey((255, 255, 255))
	background_top = pygame.image.load("./Images/Maps/Top/PalletTown.png")
	background_top.set_colorkey((255, 255, 255))
	hat = pygame.image.load("./Images/Characters/Hat.png")
	hat.set_colorkey((255, 255, 255))
	background_bump = pygame.image.load("./Images/Maps/Bump/PalletTown.png")
	xpos = 32
	ypos = 32
	background_width, background_height = background_bottom.get_rect().size
	player_width, player_height = player.get_rect().size
	center_xpos = 112
	center_ypos = 80
	
	while running:
		clock.tick(fps)
		keys = pygame.key.get_pressed()
		screen.fill((0, 0, 0))
		
		if keys[pygame.K_UP]:
			if ypos - player_height >= 0 and background_bump.get_at((xpos, ypos - player_height)) == white:
				ypos -= player_height
		if keys[pygame.K_DOWN]:
			if ypos + player_height < background_height and background_bump.get_at((xpos, ypos + player_height)) == white:
				ypos += player_height
		if keys[pygame.K_LEFT]:
			if xpos - player_width >= 0 and background_bump.get_at((xpos - player_width, ypos)) == white:
				xpos -= player_width
		if keys[pygame.K_RIGHT]:
			if xpos + player_width < background_width and background_bump.get_at((xpos + player_width, ypos)) == white:
				xpos += player_width
		
		background_pos = (center_xpos - xpos, center_ypos - ypos)
		screen.blit(background_bottom, background_pos)
		screen.blit(player, (center_xpos, center_ypos))
		screen.blit(background_top, background_pos)
		screen.blit(hat, (center_xpos, center_ypos - player_height))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				print(clock.get_fps())

if __name__ == "__main__":
	main()