import pygame

pygame.init()

white=(255,255,255)	#white rbg code
black=(0,0,0)		#black rbg code
red=(255,0,0)		#red rbg code

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('First Game')

gameExit= False

while not gameExit:	#game lopp
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	
	gameDisplay.fill(white)
	pygame.display.update()

pygame.quit()
quit()
