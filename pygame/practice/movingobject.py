import pygame

pygame.init()

white=(255,255,255)	#white rbg code
black=(0,0,0)		#black rbg code
red=(255,0,0)		#red rbg code

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('First Game')

gameExit= False

lead_x = 300	#head of x blocks
lead_y = 300	#head of y blocks
lead_x_change = 0
lead_y_change = 0

while not gameExit:	#game lopp
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		elif event.type == pygame.KEYDOWN:	#if some key is pressed
			if event.key == pygame.K_LEFT:	#if left key is pressed
				lead_x_change -= 10
			elif event.key == pygame.K_RIGHT:	#if right key is pressed
				lead_x_change += 10
			elif event.key == pygame.K_UP:	#if up key is pressed
				lead_y_change -= 10
			elif event.key == pygame.K_DOWN:	#if down key is pressed 
				lead_y_change +=10
	
	lead_x +=lead_x_change	#updateing lead_x
	lead_y +=lead_y_change	#updating lead_y
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])
	pygame.display.update()

pygame.quit()
quit()
