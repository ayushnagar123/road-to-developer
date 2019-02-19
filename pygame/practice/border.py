import pygame

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('First Game')

gameExit= False

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()	#returns pygame clock object

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change = -10
			elif event.key == pygame.K_RIGHT:
				lead_x_change = 10
			elif event.key == pygame.K_UP:
				lead_y_change = -10
			elif event.key == pygame.K_DOWN: 
				lead_y_change = 10
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				lead_x_change = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				lead_y_change = 0
	
	if lead_x>=790 or lead_x<=10 or lead_y>=590 or lead_y<=10:
		gameExit=True
	lead_x +=lead_x_change
	lead_y +=lead_y_change
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, red, [0,0,800,10])
	pygame.draw.rect(gameDisplay, red, [0,0,10,600])
	pygame.draw.rect(gameDisplay, red, [790,0,10,600])
	pygame.draw.rect(gameDisplay, red, [0,590,800,10])
	pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])
	pygame.display.update()
	
	clock.tick(10)		#frames per second 30 most suitable

pygame.quit()
quit()
