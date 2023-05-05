'''
Title: Window in Break Break
Date: April 27, 2023
Author: Annie Sun

'''

import pygame
from text import Text
from window import Window
from boxes import Box
from image_sprite import ImageSprite
import random

class Engine:
    ## COMPOSITION ("has a" relationship) -- Creating a complex game engine class by collecting smaller objects together.
    def __init__(self):
        self.__WINDOW = Window("Brick Break")
        self.__TITLE = Text("Brick Break")
        self.__TITLE.setPosition((self.__WINDOW.getWidth()//2 - self.__TITLE.getWidth()//2, 0))
        self.__BALL = Box(15, 15)
        self.__BALL.setSpeed(0)
        self.__BALL.setPosition((self.__WINDOW.getWidth()//2 - self.__BALL.getWidth()//2, 650))

        
        self.__PADDLE = Box(10,80)
        self.__PADDLE.setSpeed(0)
        self.__PADDLE.setPosition((self.__WINDOW.getWidth()//2 - self.__PADDLE.getWidth()//2, 710))
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

        self.__STAR_SCORE_VALUE = 0
        self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
        self.__STAR_SCORE.setColor((255, 255, 0))
        self.__STAR_SCORE.setPosition((160, 0))




        self.__WINNING_TEXT = Text("You Win!")
        self.__WINNING_TEXT.setFontSize(196)
        self.__WINNING_TEXT.setPosition(
            (
                self.__WINDOW.getWidth(),
                self.__WINDOW.getHeight()
            )
        )

        self.__LOSING_TEXT = Text("You Lose!")
        self.__LOSING_TEXT.setColor((153, 0, 0))
        self.__LOSING_TEXT.setFontSize(140)
        self.__LOSING_TEXT.setPosition(
            (
                self.__WINDOW.getWidth(),
                self.__WINDOW.getHeight()
            )
        )

        self.__START_TEXT = Text("Press SPACE to Start. Press A and D for paddle!")
        self.__START_TEXT.setColor((255, 255, 255))
        self.__START_TEXT.setFontSize(50)
        self.__START_TEXT.setPosition(
            (
                150,
                500
            )
        )

        self.__PLAY_AGAIN = Text("press SPACE to play again")
        self.__PLAY_AGAIN.setFontSize(50)
        self.__PLAY_AGAIN.setPosition(
            (
                self.__WINDOW.getWidth(),
                self.__WINDOW.getHeight()
            )
        )

        self.__NEXT_LEVEL = Text("press SPACE to play level 2")
        self.__NEXT_LEVEL.setFontSize(50)
        self.__NEXT_LEVEL.setPosition(
            (
                self.__WINDOW.getWidth(),
                self.__WINDOW.getHeight()
            )
        )


        


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

        self.__LEVEL_1_BRICKS = [] #AGGREGATION (grouping objects)/aggregation of bricks
        for bricks in self.__BRICKS_1_1:
            self.__LEVEL_1_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_1_2:
            self.__LEVEL_1_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_1_3:
            self.__LEVEL_1_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_1_4:
            self.__LEVEL_1_BRICKS.append(bricks)


        #list of random bricks
        self.__5_BRICKS = random.sample(self.__LEVEL_1_BRICKS, 10)

        self.__RAINBOW = ImageSprite("images/rainbow.png")
        self.__RAINBOW.setScale(0.03)
        self.__POWERED_BRICK_1 = self.__5_BRICKS[0]
        self.__RAINBOW.setPosition(self.__POWERED_BRICK_1.getPOS())
        self.__RAINBOW.setSpeed(6)
        self.__FALL_1 = False

        self.__star_2 = ImageSprite("images/star.png")
        self.__star_2.setScale(0.1)
        self.__POWERED_BRICK_2 = self.__5_BRICKS[1]
        self.__star_2.setPosition(self.__POWERED_BRICK_2.getPOS())
        self.__star_2.setSpeed(6)
        self.__FALL_2 = False

        self.__star_3 = ImageSprite("images/star.png")
        self.__star_3.setScale(0.1)
        self.__POWERED_BRICK_3 = self.__5_BRICKS[2]
        self.__star_3.setPosition(self.__POWERED_BRICK_3.getPOS())
        self.__star_3.setSpeed(6)
        self.__FALL_3 = False

        self.__star_4 = ImageSprite("images/star.png")
        self.__star_4.setScale(0.1)
        self.__POWERED_BRICK_4 = self.__5_BRICKS[3]
        self.__star_4.setPosition(self.__POWERED_BRICK_4.getPOS())
        self.__star_4.setSpeed(6)
        self.__FALL_4 = False

        self.__star_5 = ImageSprite("images/star.png")
        self.__star_5.setScale(0.1)
        self.__POWERED_BRICK_5 = self.__5_BRICKS[4]
        self.__star_5.setPosition(self.__POWERED_BRICK_5.getPOS())
        self.__star_5.setSpeed(6)
        self.__FALL_5 = False

        self.__star_6 = ImageSprite("images/star.png")
        self.__star_6.setScale(0.1)
        self.__POWERED_BRICK_6 = self.__5_BRICKS[5]
        self.__star_6.setPosition(self.__POWERED_BRICK_6.getPOS())
        self.__star_6.setSpeed(6)
        self.__FALL_6 = False

        self.__star_7 = ImageSprite("images/star.png")
        self.__star_7.setScale(0.1)
        self.__POWERED_BRICK_7 = self.__5_BRICKS[6]
        self.__star_7.setPosition(self.__POWERED_BRICK_7.getPOS())
        self.__star_7.setSpeed(6)
        self.__FALL_7 = False

        self.__star_8 = ImageSprite("images/star.png")
        self.__star_8.setScale(0.1)
        self.__POWERED_BRICK_8 = self.__5_BRICKS[7]
        self.__star_8.setPosition(self.__POWERED_BRICK_8.getPOS())
        self.__star_8.setSpeed(6)
        self.__FALL_8 = False

        self.__star_9 = ImageSprite("images/star.png")
        self.__star_9.setScale(0.1)
        self.__POWERED_BRICK_9 = self.__5_BRICKS[8]
        self.__star_9.setPosition(self.__POWERED_BRICK_9.getPOS())
        self.__star_9.setSpeed(6)
        self.__FALL_9 = False

        self.__star_10 = ImageSprite("images/star.png")
        self.__star_10.setScale(0.1)
        self.__POWERED_BRICK_10 = self.__5_BRICKS[9]
        self.__star_10.setPosition(self.__POWERED_BRICK_10.getPOS())
        self.__star_10.setSpeed(6)
        self.__FALL_10 = False

    
    def reset(self):
        self.__WINDOW = Window("Brick Break")
        self.__TITLE = Text("Brick Break")
        self.__TITLE.setPosition((self.__WINDOW.getWidth()//2 - self.__TITLE.getWidth()//2, 0))
        self.__BALL = Box(15, 15)
        self.__BALL.setSpeed(0)
        self.__BALL.setPosition((self.__WINDOW.getWidth()//2 - self.__BALL.getWidth()//2, 650))

        
        self.__PADDLE = Box(10,80)


        self.__PADDLE.setSpeed(0)
        self.__PADDLE.setPosition((self.__WINDOW.getWidth()//2 - self.__PADDLE.getWidth()//2, 710))
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

        self.__STAR_SCORE_VALUE = 0
        self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
        self.__STAR_SCORE.setColor((255, 255, 0))
        self.__STAR_SCORE.setPosition((160, 0))

        self.__START_TEXT = Text("Press SPACE to Start. Press A and D for paddle!")
        self.__START_TEXT.setColor((255, 255, 255))
        self.__START_TEXT.setFontSize(50)
        self.__START_TEXT.setPosition(
            (
                150,
                500
            )
        )





        self.__WINNING_TEXT = Text("You Win!")
        self.__WINNING_TEXT.setFontSize(196)
        self.__WINNING_TEXT.setPosition(
            (
                self.__WINDOW.getWidth(),
                self.__WINDOW.getHeight()
            )
        )

        self.__LOSING_TEXT = Text("You Lose!")
        self.__LOSING_TEXT.setColor((153, 0, 0))
        self.__LOSING_TEXT.setFontSize(140)
        self.__LOSING_TEXT.setPosition(
            (
                self.__WINDOW.getWidth(),
                self.__WINDOW.getHeight()
            )
        )

        self.__PLAY_AGAIN = Text("press SPACE to play again")
        self.__PLAY_AGAIN.setFontSize(50)
        self.__PLAY_AGAIN.setPosition(
            (
                self.__WINDOW.getWidth(),
                self.__WINDOW.getHeight()
            )
        )

        self.__NEXT_LEVEL = Text("press SPACE to play level 2")
        self.__NEXT_LEVEL.setFontSize(50)
        self.__NEXT_LEVEL.setPosition(
            (
                self.__WINDOW.getWidth(),
                self.__WINDOW.getHeight()
            )
        )


        


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

        self.__LEVEL_1_BRICKS = [] #aggregation (groupng objects)/aggregation of bricks
        for bricks in self.__BRICKS_1_1:
            self.__LEVEL_1_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_1_2:
            self.__LEVEL_1_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_1_3:
            self.__LEVEL_1_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_1_4:
            self.__LEVEL_1_BRICKS.append(bricks)
    

        self.__5_BRICKS = random.sample(self.__LEVEL_1_BRICKS, 10)

        self.__RAINBOW = ImageSprite("images/rainbow.png")
        self.__RAINBOW.setScale(0.03)
        self.__POWERED_BRICK_1 = self.__5_BRICKS[0]
        self.__RAINBOW.setPosition(self.__POWERED_BRICK_1.getPOS())
        self.__RAINBOW.setSpeed(6)
        self.__FALL_1 = False

        self.__star_2 = ImageSprite("images/star.png")
        self.__star_2.setScale(0.1)
        self.__POWERED_BRICK_2 = self.__5_BRICKS[1]
        self.__star_2.setPosition(self.__POWERED_BRICK_2.getPOS())
        self.__star_2.setSpeed(6)
        self.__FALL_2 = False

        self.__star_3 = ImageSprite("images/star.png")
        self.__star_3.setScale(0.1)
        self.__POWERED_BRICK_3 = self.__5_BRICKS[2]
        self.__star_3.setPosition(self.__POWERED_BRICK_3.getPOS())
        self.__star_3.setSpeed(6)
        self.__FALL_3 = False

        self.__star_4 = ImageSprite("images/star.png")
        self.__star_4.setScale(0.1)
        self.__POWERED_BRICK_4 = self.__5_BRICKS[3]
        self.__star_4.setPosition(self.__POWERED_BRICK_4.getPOS())
        self.__star_4.setSpeed(6)
        self.__FALL_4 = False

        self.__star_5 = ImageSprite("images/star.png")
        self.__star_5.setScale(0.1)
        self.__POWERED_BRICK_5 = self.__5_BRICKS[4]
        self.__star_5.setPosition(self.__POWERED_BRICK_5.getPOS())
        self.__star_5.setSpeed(6)
        self.__FALL_5 = False

        self.__star_6 = ImageSprite("images/star.png")
        self.__star_6.setScale(0.1)
        self.__POWERED_BRICK_6 = self.__5_BRICKS[5]
        self.__star_6.setPosition(self.__POWERED_BRICK_6.getPOS())
        self.__star_6.setSpeed(6)
        self.__FALL_6 = False

        self.__star_7 = ImageSprite("images/star.png")
        self.__star_7.setScale(0.1)
        self.__POWERED_BRICK_7 = self.__5_BRICKS[6]
        self.__star_7.setPosition(self.__POWERED_BRICK_7.getPOS())
        self.__star_7.setSpeed(6)
        self.__FALL_7 = False

        self.__star_8 = ImageSprite("images/star.png")
        self.__star_8.setScale(0.1)
        self.__POWERED_BRICK_8 = self.__5_BRICKS[7]
        self.__star_8.setPosition(self.__POWERED_BRICK_8.getPOS())
        self.__star_8.setSpeed(6)
        self.__FALL_8 = False

        self.__star_9 = ImageSprite("images/star.png")
        self.__star_9.setScale(0.1)
        self.__POWERED_BRICK_9 = self.__5_BRICKS[8]
        self.__star_9.setPosition(self.__POWERED_BRICK_9.getPOS())
        self.__star_9.setSpeed(6)
        self.__FALL_9 = False

        self.__star_10 = ImageSprite("images/star.png")
        self.__star_10.setScale(0.1)
        self.__POWERED_BRICK_10 = self.__5_BRICKS[9]
        self.__star_10.setPosition(self.__POWERED_BRICK_10.getPOS())
        self.__star_10.setSpeed(6)
        self.__FALL_10 = False

        
    def level2(self):
        self.__WINDOW = Window("Brick Break")
        self.__TITLE = Text("Brick Break")
        self.__TITLE.setPosition((self.__WINDOW.getWidth()//2 - self.__TITLE.getWidth()//2, 0))

        self.__BALL = Box(15, 15)
        self.__BALL.setSpeed(10)
        self.__BALL.setPosition((self.__WINDOW.getWidth()//2 - self.__BALL.getWidth()//2, 650))
        
        self.__PADDLE = Box(10, 80)
        self.__PADDLE.setSpeed(15)
        self.__PADDLE.setPosition((self.__WINDOW.getWidth()//2 - self.__PADDLE.getWidth()//2, 710))

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


        self.__WINNING_TEXT = Text("You Win!")
        self.__WINNING_TEXT.setFontSize(196)
        self.__WINNING_TEXT.setPosition(
            (
                self.__WINDOW.getWidth(),
                self.__WINDOW.getHeight()
            )
        )

        

        # -- level 2 first row bricks -- #
    
        ## RED ##
        self.__BRICKS_2_1 = [] #level 2, row 1
        for i in range(3):
            self.__BRICKS_2_1.append(Box(50, 80))
        
        WIDTH = 400
        for brick in self.__BRICKS_2_1:
            brick.HEALTH = 2
            brick.setPosition((WIDTH, 100))
            brick.setColor((255, 51, 51))
            WIDTH += 90

        # -- level 2 second row bricks -- #
        self.__BRICKS_2_2 = [] #level 2 row 2
        ## ORANGE ##
        for i in range(5):
            self.__BRICKS_2_2.append(Box(50, 80))
        WIDTH = 310
        for brick in self.__BRICKS_2_2:
            brick.HEALTH = 1
            brick.setPosition((WIDTH, 160))
            brick.setColor((255, 178, 102))
            WIDTH += 90

        # -- level 2 third row bricks -- #
        ## YELLOW ##
        self.__BRICKS_2_3 = [] #level 2 row 3
        for i in range(10):
            self.__BRICKS_2_3.append(Box(50, 80))
        WIDTH = 90
        for brick in self.__BRICKS_2_3:
            brick.setPosition((WIDTH, 220))
            brick.setColor((255, 255, 102))
            WIDTH += 90
        
        # -- level 2 fourth row bricks -- #
        ## YELLOW ##
        self.__BRICKS_2_4 = [] #level 2 row 4
        for i in range(10):
            self.__BRICKS_2_4.append(Box(50, 80))

        WIDTH = 90
        for brick in self.__BRICKS_2_4:
            brick.setPosition((WIDTH, 280))
            brick.setColor((255, 255, 102))
            WIDTH += 90

        # -- level 2 fifth row bricks -- #
        ## ORANGE ##
        self.__BRICKS_2_5 = [] #level 2 row 5
        for i in range(5):
            self.__BRICKS_2_5.append(Box(50, 80))

        WIDTH = 310
        for brick in self.__BRICKS_2_5:
            brick.HEALTH = 1
            brick.setPosition((WIDTH, 340))
            brick.setColor((255, 178, 102))
            WIDTH += 90

        # -- level 2 sixth row bricks -- #
        ## RED ##
        self.__BRICKS_2_6 = [] #level 2, row 1
        for i in range(3):
            self.__BRICKS_2_6.append(Box(50, 80))
        WIDTH = 400
        for brick in self.__BRICKS_2_6:
            brick.HEALTH = 2
            brick.setPosition((WIDTH, 400))
            brick.setColor((255, 51, 51))
            WIDTH += 90



        self.__RED_BRICKS = []
        self.__ORANGE_BRICKS = []
        self.__YELLOW_BRICKS = []

        for bricks in self.__BRICKS_2_1:
            self.__RED_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_2_2:
            self.__ORANGE_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_2_3:
            self.__YELLOW_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_2_4:
            self.__YELLOW_BRICKS.append(bricks)

        for bricks in self.__BRICKS_2_5:
            self.__ORANGE_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_2_6:
            self.__RED_BRICKS.append(bricks)
    


    def run(self):

        LEVEL = 1
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            KEYS_PRESSED = pygame.key.get_pressed()

             # -- PROCESSING -- #
             #Paddle
            self.__PADDLE.moveAD(KEYS_PRESSED)
            self.__PADDLE.checkBoundaries(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())

            #paddle and ball collision
            self.__BALL.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions())
            
            #ball bounce
            self.__BALL.bounceX(self.__WINDOW.getWidth())
            self.__BALL.bounceY(self.__WINDOW.getHeight(), 0 + self.__TITLE.getHeight())


            
            if LEVEL == 1:
                if KEYS_PRESSED[pygame.K_SPACE]:
                    self.__PADDLE.setSpeed(15)
                    self.__BALL.setSpeed(8)
                    self.__START_TEXT.setPosition((-1000, -1000))

                ## Start of testing collisions for random bricks with stars behind them or a rainbow powerup
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_1.getPOS(), self.__POWERED_BRICK_1.getDimensions()):
                    self.__POWERED_BRICK_1.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_1 = True
                if self.__FALL_1:
                    self.__RAINBOW.marqueeY(self.__WINDOW.getHeight())

                if self.__RAINBOW.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    POS = self.__PADDLE.getPOS()
                    self.__PADDLE = Box(10, 120)
                    self.__PADDLE.setPosition((POS))
                    self.__PADDLE.setSpeed(15)          
                    self.__RAINBOW.setPosition((-1000,-1000))
                
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_2.getPOS(), self.__POWERED_BRICK_2.getDimensions()):
                    self.__POWERED_BRICK_2.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_2 = True
                if self.__FALL_2:
                    self.__star_2.marqueeY(self.__WINDOW.getHeight())
                if self.__star_2.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()): 
                    self.__STAR_SCORE_VALUE += 1
                    self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
                    self.__STAR_SCORE.setPosition((160,0))
                    self.__STAR_SCORE.setColor((255, 255, 0))
                    self.__star_2.setPosition((-1000,-1000))
                    

                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_3.getPOS(), self.__POWERED_BRICK_3.getDimensions()):
                    self.__POWERED_BRICK_3.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_3 = True

                if self.__FALL_3:
                    self.__star_3.marqueeY(self.__WINDOW.getHeight())
                if self.__star_3.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()): 
                    self.__STAR_SCORE_VALUE += 1
                    self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
                    self.__STAR_SCORE.setPosition((160,0))  
                    self.__STAR_SCORE.setColor((255, 255, 0))         
                    self.__star_3.setPosition((-1000,-1000))
                    
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_4.getPOS(), self.__POWERED_BRICK_4.getDimensions()):
                    self.__POWERED_BRICK_4.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_4 = True
                if self.__FALL_4:
                    self.__star_4.marqueeY(self.__WINDOW.getHeight())
                if self.__star_4.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__STAR_SCORE_VALUE += 1
                    self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
                    self.__STAR_SCORE.setPosition((160,0))
                    self.__STAR_SCORE.setColor((255, 255, 0))
                    self.__star_4.setPosition((-1000,-1000))
                    
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_5.getPOS(), self.__POWERED_BRICK_5.getDimensions()):
                    self.__POWERED_BRICK_5.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_5 = True
                if self.__FALL_5:
                    self.__star_5.marqueeY(self.__WINDOW.getHeight())
                if self.__star_5.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__STAR_SCORE_VALUE += 1
                    self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
                    self.__STAR_SCORE.setPosition((160,0))
                    self.__STAR_SCORE.setColor((255, 255, 0))
                    self.__star_5.setPosition((-1000,-1000))
                
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_6.getPOS(), self.__POWERED_BRICK_6.getDimensions()):
                    self.__POWERED_BRICK_6.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_6 = True
                if self.__FALL_6:
                    self.__star_6.marqueeY(self.__WINDOW.getHeight())
                if self.__star_6.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__STAR_SCORE_VALUE += 1
                    self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
                    self.__STAR_SCORE.setPosition((160,0))
                    self.__STAR_SCORE.setColor((255, 255, 0))
                    self.__star_6.setPosition((-1000,-1000))
                
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_7.getPOS(), self.__POWERED_BRICK_7.getDimensions()):
                    self.__POWERED_BRICK_7.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_7 = True
                if self.__FALL_7:
                    self.__star_7.marqueeY(self.__WINDOW.getHeight())
                if self.__star_7.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__STAR_SCORE_VALUE += 1
                    self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
                    self.__STAR_SCORE.setPosition((160,0))
                    self.__STAR_SCORE.setColor((255, 255, 0))
                    self.__star_7.setPosition((-1000,-1000))
                
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_8.getPOS(), self.__POWERED_BRICK_8.getDimensions()):
                    self.__POWERED_BRICK_8.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_8 = True
                if self.__FALL_8:
                    self.__star_8.marqueeY(self.__WINDOW.getHeight())
                if self.__star_8.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__STAR_SCORE_VALUE += 1
                    self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
                    self.__STAR_SCORE.setPosition((160,0))
                    self.__STAR_SCORE.setColor((255, 255, 0))
                    self.__star_8.setPosition((-1000,-1000))
                
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_9.getPOS(), self.__POWERED_BRICK_9.getDimensions()):
                    self.__POWERED_BRICK_9.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_9 = True
                if self.__FALL_9:
                    self.__star_9.marqueeY(self.__WINDOW.getHeight())
                if self.__star_9.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__STAR_SCORE_VALUE += 1
                    self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
                    self.__STAR_SCORE.setPosition((160,0))
                    self.__STAR_SCORE.setColor((255, 255, 0))
                    self.__star_9.setPosition((-1000,-1000))
                
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_10.getPOS(), self.__POWERED_BRICK_10.getDimensions()):
                    self.__POWERED_BRICK_10.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_10 = True
                if self.__FALL_10:
                    self.__star_10.marqueeY(self.__WINDOW.getHeight())
                if self.__star_10.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__STAR_SCORE_VALUE += 1
                    self.__STAR_SCORE = Text(f"STAR SCORE: {self.__STAR_SCORE_VALUE}")
                    self.__STAR_SCORE.setPosition((160,0))
                    self.__STAR_SCORE.setColor((255, 255, 0))
                    self.__star_10.setPosition((-1000,-1000))
                 
        
                    
                
                ## brick collisions and testing for finished broken bricks
                for brick in self.__LEVEL_1_BRICKS:         
                    if self.__BALL.isSpriteColliding(brick.getPOS(), brick.getDimensions()):
                            brick.setPosition((-10000, -10000))
                            self.__SCORE_VALUE += 10
                            self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                            self.__SCORE_TEXT.setPosition((0,0))
                    
                ##Losing screem 
                if self.__BALL.LOSE: 
                    self.__LOSING_TEXT.setPosition(
                            (
                                self.__WINDOW.getWidth()//2 - self.__WINNING_TEXT.getWidth()//2 + 50,
                                self.__WINDOW.getHeight()//2 - self.__WINNING_TEXT.getHeight()//2
                            )
                        )

                    self.__PLAY_AGAIN.setPosition(
                            (
                                self.__WINDOW.getWidth()//2 - self.__WINNING_TEXT.getWidth()//2 + 65,
                                self.__WINDOW.getHeight()//2 - self.__WINNING_TEXT.getHeight()//2 + 100
                            )
                        )
                    
                    for brick in self.__LEVEL_1_BRICKS: 
                        brick.setPosition((-1000, -1000)) 
                    ##taking everything off screen
                    self.__RAINBOW.setPosition((-1000, -1000))
                    self.__star_2.setPosition((-1000, -1000))  
                    self.__star_3.setPosition((-1000, -1000))  
                    self.__star_4.setPosition((-1000, -1000))  
                    self.__star_5.setPosition((-1000, -1000))  
                    self.__star_6.setPosition((-1000, -1000))  
                    self.__star_7.setPosition((-1000, -1000))  
                    self.__star_8.setPosition((-1000, -1000))  
                    self.__star_9.setPosition((-1000, -1000)) 
                    self.__star_10.setPosition((-1000, -1000)) 
                    self.__PADDLE.setPosition((-1000, -1000))  


                    if KEYS_PRESSED[pygame.K_SPACE]:
                        self.reset()



                if self.__SCORE_VALUE == 400:
                        self.__WINNING_TEXT.setPosition(
                            (
                                self.__WINDOW.getWidth()//2 - self.__WINNING_TEXT.getWidth()//2,
                                self.__WINDOW.getHeight()//2 - self.__WINNING_TEXT.getHeight()//2
                            )
                        )
                        self.__NEXT_LEVEL.setPosition(
                            (
                                self.__WINDOW.getWidth()//2 - self.__NEXT_LEVEL.getWidth()//2 ,
                                self.__WINDOW.getHeight()//2 - self.__NEXT_LEVEL.getHeight()//2 + 80
                            )
                        )
                        self.__BALL.setSpeed(0)
                        self.__BALL.setPosition((-1000, -1000))

                        if KEYS_PRESSED[pygame.K_SPACE]:
                            self.__NEXT_LEVEL.setPosition((-1000, -1000))
                            self.level2()
                            LEVEL = 2
                            self.__STAR_SCORE.setPosition((-1000, -1000))
                            continue

                # -- OUTPUTS -- #
                self.__WINDOW.clearScreen()
                


                self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())
                
                

                self.__WINDOW.getSurface().blit(self.__START_TEXT.getSurface(), self.__START_TEXT.getPOS())
                for brick in self.__BRICKS_1_1:
                    self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
                for brick in self.__BRICKS_1_2:
                    self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
                for brick in self.__BRICKS_1_3:
                    self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
                for brick in self.__BRICKS_1_4:
                    self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())

                self.__WINDOW.getSurface().blit(self.__RAINBOW.getSurface(), self.__RAINBOW.getPOS())
                self.__WINDOW.getSurface().blit(self.__star_2.getSurface(), self.__star_2.getPOS())
                self.__WINDOW.getSurface().blit(self.__star_3.getSurface(), self.__star_3.getPOS())
                self.__WINDOW.getSurface().blit(self.__star_4.getSurface(), self.__star_4.getPOS())
                self.__WINDOW.getSurface().blit(self.__star_5.getSurface(), self.__star_5.getPOS())
                self.__WINDOW.getSurface().blit(self.__star_6.getSurface(), self.__star_6.getPOS())
                self.__WINDOW.getSurface().blit(self.__star_7.getSurface(), self.__star_7.getPOS())
                self.__WINDOW.getSurface().blit(self.__star_8.getSurface(), self.__star_8.getPOS())
                self.__WINDOW.getSurface().blit(self.__star_9.getSurface(), self.__star_9.getPOS())
                self.__WINDOW.getSurface().blit(self.__star_10.getSurface(), self.__star_10.getPOS())

                
                
              
                
        
            
            elif LEVEL == 2:
                ## brick collisions for colored bricks and testing for finished broken bricks
        
                for brick in self.__RED_BRICKS:
                    
                    if self.__BALL.isSpriteColliding(brick.getPOS(), brick.getDimensions()):
                        self.__SCORE_VALUE += 10
                        self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                        self.__SCORE_TEXT.setPosition((0,0))

                        if brick.HEALTH == 2:
                            brick.setColor((255, 178, 102)) #orange
                            brick.setHealth()

                        elif brick.HEALTH == 1:
                            brick.setColor((255, 255, 102)) #yellow
                            brick.setHealth()
                          

                        else:
                            brick.setPosition((-1000, -1000))
                            

                for brick in self.__ORANGE_BRICKS:
                    if self.__BALL.isSpriteColliding(brick.getPOS(), brick.getDimensions()):
                        self.__SCORE_VALUE += 10
                        self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                        self.__SCORE_TEXT.setPosition((0,0))

                        if brick.HEALTH == 1:
                            brick.setColor((255, 255, 102))
                            brick.setHealth()
                
                        else:
                            brick.setPosition((-1000, -1000))
                           
                    
                
                for brick in self.__YELLOW_BRICKS:
                    if self.__BALL.isSpriteColliding(brick.getPOS(), brick.getDimensions()):
                        brick.setPosition((-1000, -1000))
                        self.__SCORE_VALUE += 10
                        self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                        self.__SCORE_TEXT.setPosition((0,0))


                if self.__BALL.LOSE:
                    self.__LOSING_TEXT.setPosition(
                            (
                                self.__WINDOW.getWidth()//2 - self.__WINNING_TEXT.getWidth()//2 + 50,
                                self.__WINDOW.getHeight()//2 - self.__WINNING_TEXT.getHeight()//2
                            )
                        )

                    self.__PLAY_AGAIN.setPosition(
                            (
                                self.__WINDOW.getWidth()//2 - self.__WINNING_TEXT.getWidth()//2 + 65,
                                self.__WINDOW.getHeight()//2 - self.__WINNING_TEXT.getHeight()//2 + 100
                            )
                        )

                    for brick in self.__RED_BRICKS: 
                        brick.setPosition((-1000, -1000)) 
                    
                    for brick in self.__ORANGE_BRICKS: 
                        brick.setPosition((-1000, -1000)) 
                    
                    for brick in self.__YELLOW_BRICKS: 
                        brick.setPosition((-1000, -1000)) 

                    if KEYS_PRESSED[pygame.K_SPACE]:
                        self.reset()
                        LEVEL = 1
                        continue



                if self.__SCORE_VALUE == 580:
                        self.__WINNING_TEXT.setPosition(
                            (
                                self.__WINDOW.getWidth()//2 - self.__WINNING_TEXT.getWidth()//2,
                                self.__WINDOW.getHeight()//2 - self.__WINNING_TEXT.getHeight()//2
                            )
                        )
                        self.__BALL.setSpeed(0)
                        self.__BALL.setPosition((-1000, -1000))

                        self.__PLAY_AGAIN.setPosition(
                            (
                                self.__WINDOW.getWidth()//2 - self.__WINNING_TEXT.getWidth()//2 + 65,
                                self.__WINDOW.getHeight()//2 - self.__WINNING_TEXT.getHeight()//2 + 120
                            )
                        )

                        for brick in self.__RED_BRICKS: 
                            brick.setPosition((-1000, -1000)) 
                    
                        for brick in self.__ORANGE_BRICKS: 
                            brick.setPosition((-1000, -1000)) 
                        
                        for brick in self.__YELLOW_BRICKS: 
                            brick.setPosition((-1000, -1000)) 
                        
                        self.__BALL.setPosition((-1111, -1111))

                        if KEYS_PRESSED[pygame.K_SPACE]:
                            self.reset()
                            LEVEL = 1
                            continue
            
                # -- OUTPUTS -- #
                self.__WINDOW.clearScreen()
                self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())
                for brick in self.__BRICKS_2_1:
                    self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
                for brick in self.__BRICKS_2_2:
                    self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
                for brick in self.__BRICKS_2_3:
                    self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
                for brick in self.__BRICKS_2_4:
                    self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS()) 
                for brick in self.__BRICKS_2_5:
                    self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
                for brick in self.__BRICKS_2_6:
                    self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPOS())
            
        
        
            self.__WINDOW.getSurface().blit(self.__BALL.getSurface(), self.__BALL.getPOS())
            self.__WINDOW.getSurface().blit(self.__PADDLE.getSurface(), self.__PADDLE.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())

            self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPOS())
            self.__WINDOW.getSurface().blit(self.__STAR_SCORE.getSurface(), self.__STAR_SCORE.getPOS())
            self.__WINDOW.getSurface().blit(self.__WINNING_TEXT.getSurface(), self.__WINNING_TEXT.getPOS())
            self.__WINDOW.getSurface().blit(self.__LOSING_TEXT.getSurface(), self.__LOSING_TEXT.getPOS())
            self.__WINDOW.getSurface().blit(self.__PLAY_AGAIN.getSurface(), self.__PLAY_AGAIN.getPOS())
            self.__WINDOW.getSurface().blit(self.__NEXT_LEVEL.getSurface(), self.__NEXT_LEVEL.getPOS())
            self.__WINDOW.updateFrame()




if __name__ == "__main__":
    pygame.init()
    GAME = Engine()
    GAME.run()
