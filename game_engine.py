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
        
        self.__PADDLE = Box(10, 80)
        self.__PADDLE.setSpeed(15)
        self.__PADDLE.setPosition((self.__WINDOW.getWidth()//2 - self.__PADDLE.getWidth()//2, 680))

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




        # -- level 1 first row bricks -- #
        self.__BRICKS_1_1 = [] #level 1, row 1
        for i in range(10):
            self.__BRICKS_1_1.append(Box(50, 80))
        WIDTH = 90
        for brick in self.__BRICKS_1_1:
            brick.setPosition((WIDTH, 100))
            WIDTH += 90

        # -- level 1 second row bricks -- #
        self.__BRICKS_1_2 = [] #level 1 row 2
        for i in range(10):
            self.__BRICKS_1_2.append(Box(50, 80))
        WIDTH = 100
        for brick in self.__BRICKS_1_2:
            brick.setPosition((WIDTH, 160))
            WIDTH += 90

        # -- level 1 third row bricks -- #
        self.__BRICKS_1_3 = [] #level 1 row 3
        for i in range(10):
            self.__BRICKS_1_3.append(Box(50, 80))
        WIDTH = 90
        for brick in self.__BRICKS_1_3:
            brick.setPosition((WIDTH, 220))
            WIDTH += 90
        
        # -- level 1 fourth row bricks -- #
        self.__BRICKS_1_4 = [] #level 1 row 4
        for i in range(10):
            self.__BRICKS_1_4.append(Box(50, 80))

        WIDTH = 100
        for brick in self.__BRICKS_1_4:
            brick.setPosition((WIDTH, 280))
            WIDTH += 90

        self.__LEVEL_1_BRICKS = []
        for bricks in self.__BRICKS_1_1:
            self.__LEVEL_1_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_1_2:
            self.__LEVEL_1_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_1_3:
            self.__LEVEL_1_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_1_4:
            self.__LEVEL_1_BRICKS.append(bricks)
        


    def run(self):
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            KEYS_PRESSED = pygame.key.get_pressed()
            self.__PADDLE.moveAD(KEYS_PRESSED)
            self.__PADDLE.checkBoundaries(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())

            self.__BALL.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions())

            
            

            self.__BALL.bounceX(self.__WINDOW.getWidth())
            self.__BALL.bounceY(self.__WINDOW.getHeight(), 0 + self.__TITLE.getHeight())




            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())

            for brick in self.__BRICKS_1_1:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
            for brick in self.__BRICKS_1_2:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
            for brick in self.__BRICKS_1_3:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
            for brick in self.__BRICKS_1_4:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())

            for brick in self.__LEVEL_1_BRICKS:
                if self.__BALL.isSpriteColliding(brick.getPOS(), brick.getDimensions()):
                    brick.setPosition((-10000, -10000))
            
            self.__WINDOW.getSurface().blit(self.__BALL.getSurface(), self.__BALL.getPOS())
            self.__WINDOW.getSurface().blit(self.__PADDLE.getSurface(), self.__PADDLE.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())
            self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPOS())
            self.__WINDOW.updateFrame()

 


if __name__ == "__main__":
    pygame.init()
    GAME = Engine()
    GAME.run()
