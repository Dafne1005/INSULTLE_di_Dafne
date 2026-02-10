def main() -> None:
    print("Hello from insultle!")

import pygame

pygame.init()

Larghezza_Schermo = 822
Altezza_Schermo = 745

schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
pygame.display.set_caption("Insultle") 

#imgSfondo = pygame.image.load("sfondoINSULTLE.png") devo aggiungre il file dopo
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))

running = True
#LetteraA = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 LetteraA = True 
                

pygame.quit()