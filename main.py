import pygame

clock = pygame.time.Clock()
fps = 30
screen_width = 240
screen_height = 176
black = (0, 0, 0, 255)
white = (255, 255, 255, 255)

def check_hitbox(dir, player_width, player_height, xpos, ypos, step_size, background_bump):
	background_width, background_height = background_bump.get_rect().size
	if dir == "up" and ypos - step_size >= 0:
		for i in range(xpos, xpos + player_width):
			if background_bump.get_at((i, ypos - step_size)) == black:
				return False
		return True
	elif dir == "down" and ypos + player_height - 1 + step_size < background_height:
		for i in range(xpos, xpos + player_width):
			if background_bump.get_at((i, ypos + player_height - 1 + step_size)) == black:
				return False
		return True
	elif dir == "left" and xpos - step_size >= 0:
		for i in range(ypos, ypos + player_height):
			if background_bump.get_at((xpos - step_size, i)) == black:
				return False
		return True
	elif dir == "right" and xpos + player_width - 1 + step_size < background_width:
		for i in range(ypos, ypos + player_height):
			if background_bump.get_at((xpos + player_width - 1 + step_size, i)) == black:
				return False
		return True
	return False

def main():
	pygame.init()
	screen = pygame.display.set_mode((screen_width, screen_height))
	running = True
	
	background_bottom = pygame.image.load("./Images/Maps/Bottom/PalletTown.png")
	player = pygame.image.load("./Images/Characters/Player.png")
	player.set_colorkey(white)
	background_top = pygame.image.load("./Images/Maps/Top/PalletTown.png")
	background_top.set_colorkey(white)
	hat = pygame.image.load("./Images/Characters/Hat.png")
	hat.set_colorkey(white)
	background_bump = pygame.image.load("./Images/Maps/Bump/PalletTown.png")
	xpos = 32
	ypos = 32
	background_width, background_height = background_bottom.get_rect().size
	player_width, player_height = player.get_rect().size
	center_xpos = 112
	center_ypos = 80
	step_size = 2
	
	while running:
		clock.tick(fps)
		keys = pygame.key.get_pressed()
		screen.fill(black)
		
		if keys[pygame.K_UP]:
			if check_hitbox("up", player_width, player_height, xpos, ypos, step_size, background_bump):
				ypos -= step_size
		if keys[pygame.K_DOWN]:
			if check_hitbox("down", player_width, player_height, xpos, ypos, step_size, background_bump):
				ypos += step_size
		if keys[pygame.K_LEFT]:
			if check_hitbox("left", player_width, player_height, xpos, ypos, step_size, background_bump):
				xpos -= step_size
		if keys[pygame.K_RIGHT]:
			if check_hitbox("right", player_width, player_height, xpos, ypos, step_size, background_bump):
				xpos += step_size
		
		rects = []
		background_pos = (center_xpos - xpos, center_ypos - ypos)
		rects.append(screen.blit(background_bottom, background_pos))
		rects.append(screen.blit(player, (center_xpos, center_ypos)))
		rects.append(screen.blit(background_top, background_pos))
		rects.append(screen.blit(hat, (center_xpos, center_ypos - player_height)))
		#pygame.display.update(rects)
		pygame.display.flip()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				print("fps: " + str(clock.get_fps()))

if __name__ == "__main__":
	main()