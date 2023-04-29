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
        
        self.__5_BRICKS = random.sample(self.__LEVEL_1_BRICKS, 5)

        self.__POWER_UP_1 = ImageSprite("images/star.png")
        self.__POWER_UP_1.setScale(0.1)
        self.__POWERED_BRICK_1 = self.__5_BRICKS[0]
        self.__POWER_UP_1.setPosition(self.__POWERED_BRICK_1.getPOS())
        self.__POWER_UP_1.setSpeed(6)
        self.__FALL_1 = False

        self.__POWER_UP_2 = ImageSprite("images/star.png")
        self.__POWER_UP_2.setScale(0.1)
        self.__POWERED_BRICK_2 = self.__5_BRICKS[1]
        self.__POWER_UP_2.setPosition(self.__POWERED_BRICK_2.getPOS())
        self.__POWER_UP_2.setSpeed(6)
        self.__FALL_2 = False

        self.__POWER_UP_3 = ImageSprite("images/star.png")
        self.__POWER_UP_3.setScale(0.1)
        self.__POWERED_BRICK_3 = self.__5_BRICKS[2]
        self.__POWER_UP_3.setPosition(self.__POWERED_BRICK_3.getPOS())
        self.__POWER_UP_3.setSpeed(6)
        self.__FALL_3 = False

        self.__POWER_UP_4 = ImageSprite("images/star.png")
        self.__POWER_UP_4.setScale(0.1)
        self.__POWERED_BRICK_4 = self.__5_BRICKS[3]
        self.__POWER_UP_4.setPosition(self.__POWERED_BRICK_4.getPOS())
        self.__POWER_UP_4.setSpeed(6)
        self.__FALL_4 = False

        self.__POWER_UP_5 = ImageSprite("images/star.png")
        self.__POWER_UP_5.setScale(0.1)
        self.__POWERED_BRICK_5 = self.__5_BRICKS[4]
        self.__POWER_UP_5.setPosition(self.__POWERED_BRICK_5.getPOS())
        self.__POWER_UP_5.setSpeed(6)
        self.__FALL_5 = False
    
        
    def reset(self):
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
        self.__BRICKS_2_1 = [] #level 2, row 1
        for i in range(3):
            self.__BRICKS_2_1.append(Box(50, 80))
        WIDTH = 400
        for brick in self.__BRICKS_2_1:
            brick.setPosition((WIDTH, 100))
            WIDTH += 90

        # -- level 2 second row bricks -- #
        self.__BRICKS_2_2 = [] #level 2 row 2
        for i in range(5):
            self.__BRICKS_2_2.append(Box(50, 80))
        WIDTH = 310
        for brick in self.__BRICKS_2_2:
            brick.setPosition((WIDTH, 160))
            WIDTH += 90

        # -- level 2 third row bricks -- #
        self.__BRICKS_2_3 = [] #level 2 row 3
        for i in range(10):
            self.__BRICKS_2_3.append(Box(50, 80))
        WIDTH = 90
        for brick in self.__BRICKS_2_3:
            brick.setPosition((WIDTH, 220))
            WIDTH += 90
        
        # -- level 2 fourth row bricks -- #
        self.__BRICKS_2_4 = [] #level 2 row 4
        for i in range(10):
            self.__BRICKS_2_4.append(Box(50, 80))

        WIDTH = 90
        for brick in self.__BRICKS_2_4:
            brick.setPosition((WIDTH, 280))
            WIDTH += 90

        # -- level 2 fifth row bricks -- #
        self.__BRICKS_2_5 = [] #level 2 row 5
        for i in range(5):
            self.__BRICKS_2_5.append(Box(50, 80))

        WIDTH = 310
        for brick in self.__BRICKS_2_5:
            brick.setPosition((WIDTH, 340))
            WIDTH += 90

        # -- level 2 sixth row bricks -- #
        self.__BRICKS_2_6 = [] #level 2, row 1
        for i in range(3):
            self.__BRICKS_2_6.append(Box(50, 80))
        WIDTH = 400
        for brick in self.__BRICKS_2_6:
            brick.setPosition((WIDTH, 400))
            WIDTH += 90




        self.__LEVEL_2_BRICKS = [] #aggregation (groupng objects)/aggregation of bricks
        for bricks in self.__BRICKS_2_1:
            self.__LEVEL_2_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_2_2:
            self.__LEVEL_2_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_2_3:
            self.__LEVEL_2_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_2_4:
            self.__LEVEL_2_BRICKS.append(bricks)

        for bricks in self.__BRICKS_2_5:
            self.__LEVEL_2_BRICKS.append(bricks)
        
        for bricks in self.__BRICKS_2_6:
            self.__LEVEL_2_BRICKS.append(bricks)
        
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
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_1.getPOS(), self.__POWERED_BRICK_1.getDimensions()):
                    self.__POWERED_BRICK_1.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_1 = True

                if self.__FALL_1:
                    self.__POWER_UP_1.marqueeY(self.__WINDOW.getHeight())
                
                if self.__POWER_UP_1.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__PADDLE.setDimensions((400, 400))
                    self.__POWER_UP_1.setPosition((-1000,-1000))
                
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_2.getPOS(), self.__POWERED_BRICK_2.getDimensions()):
                    self.__POWERED_BRICK_2.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_2 = True
                    
                if self.__FALL_2:
                    self.__POWER_UP_2.marqueeY(self.__WINDOW.getHeight())
                
                if self.__POWER_UP_2.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__PADDLE.setDimensions((400, 400))
                    self.__POWER_UP_2.setPosition((-1000,-1000))

                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_3.getPOS(), self.__POWERED_BRICK_3.getDimensions()):
                    self.__POWERED_BRICK_3.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_3 = True
                    
                if self.__FALL_3:
                    self.__POWER_UP_3.marqueeY(self.__WINDOW.getHeight())
                
                if self.__POWER_UP_3.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__PADDLE.setDimensions((400, 400))
                    self.__POWER_UP_3.setPosition((-1000,-1000))
                
                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_4.getPOS(), self.__POWERED_BRICK_4.getDimensions()):
                    self.__POWERED_BRICK_4.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_4 = True
                    
                if self.__FALL_4:
                    self.__POWER_UP_4.marqueeY(self.__WINDOW.getHeight())
                
                if self.__POWER_UP_4.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__PADDLE.setDimensions((400, 400))
                    self.__POWER_UP_4.setPosition((-1000,-1000))

                if self.__BALL.isSpriteColliding(self.__POWERED_BRICK_5.getPOS(), self.__POWERED_BRICK_5.getDimensions()):
                    self.__POWERED_BRICK_5.setPosition((-10000, -10000))
                    self.__SCORE_VALUE += 10
                    self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE_TEXT.setPosition((0,0))
                    self.__FALL_5 = True
                
                    
                if self.__FALL_5:
                    self.__POWER_UP_5.marqueeY(self.__WINDOW.getHeight())
                
                if self.__POWER_UP_5.isSpriteColliding(self.__PADDLE.getPOS(), self.__PADDLE.getDimensions()):
                    self.__PADDLE.setDimensions((400, 400))
                    self.__POWER_UP_5.setPosition((-1000,-1000))
                
                    
                
                ## brick collisions and testing for finished broken bricks
                for brick in self.__LEVEL_1_BRICKS:         
                    if self.__BALL.isSpriteColliding(brick.getPOS(), brick.getDimensions()):
                            brick.setPosition((-10000, -10000))
                            self.__SCORE_VALUE += 10
                            self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                            self.__SCORE_TEXT.setPosition((0,0))


                if self.__SCORE_VALUE == 400:
                        self.__WINNING_TEXT.setPosition(
                            (
                                self.__WINDOW.getWidth()//2 - self.__WINNING_TEXT.getWidth()//2,
                                self.__WINDOW.getHeight()//2 - self.__WINNING_TEXT.getHeight()//2
                            )
                        )
                        self.__BALL.setSpeed(0)
                        self.__BALL.setPosition((-1000, -1000))

                        if KEYS_PRESSED[pygame.K_RETURN]:
                            self.level2()
                            LEVEL = 2
                            continue
            
                # -- OUTPUTS -- #
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

      
                self.__WINDOW.getSurface().blit(self.__POWER_UP_1.getSurface(), self.__POWER_UP_1.getPOS())
                self.__WINDOW.getSurface().blit(self.__POWER_UP_2.getSurface(), self.__POWER_UP_2.getPOS())
                self.__WINDOW.getSurface().blit(self.__POWER_UP_3.getSurface(), self.__POWER_UP_3.getPOS())
                self.__WINDOW.getSurface().blit(self.__POWER_UP_4.getSurface(), self.__POWER_UP_4.getPOS())
                self.__WINDOW.getSurface().blit(self.__POWER_UP_5.getSurface(), self.__POWER_UP_5.getPOS())
                 



                
            
            
            elif LEVEL == 2:
                ## brick collisions and testing for finished broken bricks
                for brick in self.__LEVEL_2_BRICKS:
                    if self.__BALL.isSpriteColliding(brick.getPOS(), brick.getDimensions()):
                        brick.setPosition((-10000, -10000))
                        self.__SCORE_VALUE += 10
                        self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE_VALUE}")
                        self.__SCORE_TEXT.setPosition((0,0))

                if self.__SCORE_VALUE == 360:
                        self.__WINNING_TEXT.setPosition(
                            (
                                self.__WINDOW.getWidth()//2 - self.__WINNING_TEXT.getWidth()//2,
                                self.__WINDOW.getHeight()//2 - self.__WINNING_TEXT.getHeight()//2
                            )
                        )
                        self.__BALL.setSpeed(0)
                        self.__BALL.setPosition((-1000, -1000))

                        if KEYS_PRESSED[pygame.K_RETURN]:
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
            self.__WINDOW.getSurface().blit(self.__WINNING_TEXT.getSurface(), self.__WINNING_TEXT.getPOS())
            self.__WINDOW.updateFrame()




if __name__ == "__main__":
    pygame.init()
    GAME = Engine()
    GAME.run()
