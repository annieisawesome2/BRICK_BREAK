'''
title: Image Sprite
author: Annie Sun
date: 2023-04-19
'''

import pygame
from sprite import MySprite

class ImageSprite(MySprite):
    """Load and manipulate images
    """
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.__X_FLIP = False

    def setScale(self, SCALE_X, SCALE_Y=0):
        """resize the image based on a factor

        Args:
            SCALE_X (float): 
            SCALE_Y (float): Defaults to 0.
        """

        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
            self._SURFACE = pygame.transform.scale(self._SURFACE, (self.getWidth()*SCALE_X, self.getHeight()*SCALE_Y))
    


if __name__ == "__main__":
    from window import Window
    pygame.init()


    WINDOW = Window("Image sprite test")
    BUNNY = ImageSprite("images/bunny.png")
    BUNNY.setScale(0.5)
    BUNNY.setSpeed(15)

    

    while True:
        #INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #PROCESSING
        PRESSED_KEYS = pygame.key.get_pressed()
        BUNNY.moveWASD(PRESSED_KEYS)
   

        #OUTPUTS
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BUNNY.getSurface(), BUNNY.getPOS())
        WINDOW.updateFrame()






