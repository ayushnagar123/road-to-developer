import pygame

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

display_width=800
display_height=600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('First Game')

gameExit= False

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0
block_size = 10
border = 10

clock = pygame.time.Clock()	#returns pygame clock object

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change = -block_size
			elif event.key == pygame.K_RIGHT:
				lead_x_change = block_size
			elif event.key == pygame.K_UP:
				lead_y_change = -block_size
			elif event.key == pygame.K_DOWN: 
				lead_y_change = block_size
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				lead_x_change = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				lead_y_change = 0
	
	if lead_x>=display_width-2*border or lead_x<=2*border or lead_y>=display_height-2*border or lead_y<=2*border:
		gameExit=True
	lead_x +=lead_x_change
	lead_y +=lead_y_change
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, red, [0,0,display_width,border])
	pygame.draw.rect(gameDisplay, red, [0,0,border,display_height])
	pygame.draw.rect(gameDisplay, red, [display_width-border,0,border,display_height])
	pygame.draw.rect(gameDisplay, red, [0,display_height-border,display_width,border])
	pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,block_size,block_size])
	pygame.display.update()
	
	clock.tick(10)		#frames per second 30 most suitable

pygame.quit()
quit()
