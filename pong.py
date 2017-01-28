import pygame
import random

# variables
FPS = 60

# size of the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# size of the paddle
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

# size of the ball
BALL_WIDTH = 10
BALL_HEIGHT = 10

# speed of paddle & ball
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

# RGB Colours of paddle and ball
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode(WINDOW_WIDHT, WINDOW_HEIGHT)

def drawBall(ballXPos, ballYPos):
  ball = pygame.rect(ballXpos, ballYpos, BALL_WIDTH, BALL_HEIGHT)
  pygame.draw.rect(screen, WHITE, ball)

def drawPlayerPaddle(playerPaddleYPos):
  playerPaddle = pygame.rect(PADDLE_BUFFER, playerPaddleYPos, PADDLE_WIDTH, PADDLE_HEIGHT)
  pygame.draw.rect(screen, WHITE, playerPaddle)

def drawBotPaddle(botPaddleYPos):
  botPaddle = pygame.rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, botPaddleYPos, PADDLE_WIDTH, PADDLE_HEIGHT)
  pygame.draw.rect(screen, WHITE, botPaddle)

def updateBall(playerPaddleYPos, botPaddleYPos, ballXPos, ballYPos):
  # update x and y position
  ballXPos = ballXPos + ballXDirection * BALL_X_SPEED
  ballYPos = ballYPos + ballYDirection * BALL_Y_SPEED
  score = 0
  
  # check for a collision
  # if the ball hits the left side then switch direction
  if(ballXPos <= PADDLE_BUFFER + PADDLE_WIDTH 
      and ballYPos + BALL_HEIGHT >= playerPaddleYPos 
      and ballYPos - BALL_HEIGHT <= playerPaddleYPos + PADDLE_HEIGHT):
    ballXDirection = 1
  elif(ballXPos <= 0):
    ballXDirection = 1
    score = -1
    return [score, playerPaddleYPos, botPaddleYPos, ballXPos, ballYPos, ballXDirection, ballYDirection]

  # if it hits the right side, switch direction
  if(ballXPos >= WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER 
      and ballYPos + BALL_HEIGHT >= botPaddleYPos 
      and ballYPos - BALL_HEIGHT <= botPaddleYPos + PADDLE_HEIGHT):
    ballXDirection = -1
  elif(ballXPos >= WINDOW_WIDTH - BALL_WIDTH):
    ballXDirection = -1
    score = 1
    return [score, playerPaddleYPos, botPaddleYPos, ballXPos, ballYPos, ballXDirection, ballYDirection]

  # if the ball hits the top border, change direction
  if(ballYPos <= 0):
    ballYPos = 0
    ballYDirection = 1
  elif(ballYPos >= WINDOW_HEIGHT - BALL_HEIGHT):
    ballYPos = WINDOW_HEIGHT - BALL_HEIGHT
    ballYDirection = -1
    return [score, playerPaddleYPos, botPaddleYPos, ballXPos, ballYPos, ballXDirection, ballYDirection]

def updatePlayerPaddle(action, playerPaddleYPos):
  # if moves up
  if(action[1] == 1):
    playerPaddleYPos = playerPaddleYPos - PADDLE_SPEED
  
  #if moves down
  if(action[2] == 1):
    playerPaddleYPos = playerPaddleYPos + PADDLE_SPEED

  # prevent from moving outside the screen
  if(playerPaddleYPos < 0):
    playerPaddleYPos = 0
  
  if(playerPaddleYPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
    playerPaddleYPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    
  return playerPaddleYPos

def updateBotPaddle(action, ballYPos):
  # if moves up
  if(action[1] == 1):
    botPaddleYPos = botPaddleYPos - PADDLE_SPEED
  
  #if moves down
  if(action[2] == 1):
    botPaddleYPos = botPaddleYPos + PADDLE_SPEED

  # prevent from moving outside the screen
  if(botPaddleYPos < 0):
    botPaddleYPos = 0
  
  if(botYPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
    botPaddleYPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    
  return botPaddleYPos
