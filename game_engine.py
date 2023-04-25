import pygame
from text import Text
from sprite import MySprite
from window import Window
from boxes import Box
from image_sprite import ImageSprite
import random

class Engine:
    def __init__(self):
        self.__WINDOW = Window("Brick Break")
        self.__TITLE = Text("Brick Break")
        self.__TITLE.setPosition((self.__WINDOW.getWidth()//2 - self.__TITLE.getWidth()//2, 0))

        self.__BALL = Box(15, 15)
        self.__BALL.setSpeed(10)
        self.__BALL.setPosition((self.__WINDOW.getWidth()//2 - self.__BALL.getWidth()//2, self.__WINDOW.getHeight()//2 - self.__BALL.getHeight()//2))
        

        self.__BG_IMAGE = ImageSprite("images/background.png")
        self.__BG_IMAGE.setScale(1)
        self.__BG_IMAGE.setPosition(
            (
                0, self.__TITLE.getHeight()
            )
        )

        self.__SCORE_VALUE = 0
        self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
        self.__SCORE_TEXT.setPosition((0, 0))


    def run(self):
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            

            self.__BALL.bounceX(self.__WINDOW.getWidth())

            #this part still iffy...check how to fix
            self.__BALL.bounceY(self.__WINDOW.getHeight(), 0 + self.__TITLE.getHeight())
            
        



            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())
            self.__WINDOW.getSurface().blit(self.__BALL.getSurface(), self.__BALL.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())
            self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPOS())
            self.__WINDOW.updateFrame()

    def formatBrick(self):
        BRICK = Box(80, 50)
        BRICK_WIDTH = BRICK.getWidth()

        #available space for two margins is the screen width minus 2 bricks
        AVAILABLE_SPACE_X = self.__WINDOW.getWidth() - (2* BRICK_WIDTH)

        # set the spacing btw bricks as one brick width. The space needed to display one brick is twice its width
        # -- one width for the brick and one for the empty space to its right
        # to find the number of bricks that fit across the screen, divide available space by two times the width of a brick



        # get the bricks width
        #calc horizontal space available for bricks
        #set up loop that counts from 0 to the number of bricks we need to make

        #number of bricks that fit across the screen
        BRICKS = AVAILABLE_SPACE_X //(2*BRICK_WIDTH)

        for i in range(BRICKS):
            BRICK = Box(50, 80)
            BRICK.__X = BRICK_WIDTH + 2 * BRICK_WIDTH * i
            self.BRICKS


if __name__ == "__main__":
    pygame.init()
    GAME = Engine()
    GAME.run()
