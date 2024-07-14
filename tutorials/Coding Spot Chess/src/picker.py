# import pygame
# import sys

# from var import *
# from const import *

# pygame.font.init()
# font = pygame.font.SysFont('Georgia',40,bold=True)
# surf = font.render('White', True, 'white')
# surf2 = font.render('Black', True, 'black')
# button = pygame.Rect(250,200,150,100)
# button2 = pygame.Rect(400,200,150,100)
# start = False

# if start == False:
#     class Picker:
#         def __init__(self):
#             pygame.init()
#             self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
#             pygame.display.set_caption('Chess')

#         def mainloop(self):
#             # show methods
            
#             screen = self.screen
#             global pieceColor

#             if start == False:    
#                 for events in pygame.event.get():
#                     if events.type == pygame.QUIT:
#                         pygame.quit()
#                     if events.type == pygame.MOUSEBUTTONDOWN:
#                         if button.collidepoint(events.pos):
#                                 print('white')
#                                 pieceColor = 'white'
#                                 start = True
#                         if button2.collidepoint(events.pos):
#                                 pieceColor = 'black'
#                                 start = True
#                                 print('black')
                
#                 a,b = pygame.mouse.get_pos()
#                 if button.x <= a <= button.x + 150 and button.y <= b <= button.y +100:
#                     pygame.draw.rect(screen,(180,180,180),button )
#                 else:
#                     pygame.draw.rect(screen, (110,110,110),button)
#                 if button2.x <= a <= button2.x + 150 and button2.y <= b <= button2.y +100:
#                     pygame.draw.rect(screen,(180,180,180),button2 )
#                 else:
#                     pygame.draw.rect(screen, (110,110,110),button2)
#                 screen.blit(surf,(button.x +5, button.y+5))
#                 screen.blit(surf2,(button2.x +5, button2.y+5))
#                 pygame.display.update()


# picker = Picker() 
# picker.mainloop()
