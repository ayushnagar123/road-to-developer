import pygame

pygame.init()	#intialize pygame module

gameDisplay = pygame.display.set_mode((800,600))	#cavas	#must be a tuple only

pygame.display.set_caption('First Game')	#game title

pygame.display.update()		#only update the canvas		
#pygame.display.flip()=>similar function like flipbook

gameExit= False

while not gameExit:	#till game not exit
	for event in pygame.event.get():
		print(event)	#prints every event happening at the console

pygame.quit()		#uninitialize pygame
quit()
