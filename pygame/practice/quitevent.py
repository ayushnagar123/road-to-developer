import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('First Game')

pygame.display.update()

gameExit= False

#quitevent handleing
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	#if quit event occurs QUIT object is called
			gameExit = True

pygame.quit()
quit()
