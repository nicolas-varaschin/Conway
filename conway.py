''' Conway Game. '''
import pygame
import random
import board
from pygame.locals import *


class Conway(object):
  '''Conway game main controller'''

  def __init__(self):
    self.board = None
    self.done = False
    self.clock_speed = 7
    self.restart()

  def restart(self):
    '''Restarts game with random board'''
    self.board = board.Board(60)
    for _ in range(600):
      self.board[random.randint(0, 59)][random.randint(0, 59)] = 1

  def main(self):
    '''Controls pygame rendering and game'''
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000), DOUBLEBUF)
    clock = pygame.time.Clock()

    cell_size = (20, 20)
    cell = pygame.Surface(cell_size).convert()
    cell.fill((0, 0, 0))

    grid_size = (1000, 1000)
    grid = pygame.Surface(grid_size)
    grid.fill((255, 255, 255))
    pygame.display.flip()

    step = 0
    step_back = False
    while self.done == False:
      grid.fill((min(255, step/5),
                 min(255, step/2),
                 min(255, step)))

      screen.blit(grid, (0, 0))
      for event in pygame.event.get():
        self.manage_event(event)

      for i in range(len(self.board)):
        for j in range(len(self.board)):
          if self.board[i][j]:
            cell.fill(self.board.color(i, j, step))
            screen.blit(cell, (i*20, j*20))
          
      self.board = self.board.next_board()
      if step_back:
        step -= 2
      else:
        step += 2
      if step <= 0:
        step_back = False
      if step >= 255:
        step_back = True

      pygame.display.flip()
      clock.tick(self.clock_speed)
    pygame.quit()
  
  def manage_event(self, event):
    '''Manages pygame events'''
    if event.type == pygame.QUIT or (event.type == KEYDOWN and 
                                         event.key == K_ESCAPE):
      self.done = True
    if event.type == KEYDOWN:
      if event.key == K_SPACE:
        self.clock_speed = 100
      if event.key == K_r:
        self.restart()
      if event.key == K_g:
        self.glider()
    if event.type == KEYUP:
      if event.key == K_SPACE:
        self.clock_speed = 7

  def glider(self):
    '''Restars game with a glider'''
    self.board = board.Board(60)
    self.board[2][2] = 1
    self.board[2][1] = 1
    self.board[2][0] = 1
    self.board[0][1] = 1
    self.board[1][2] = 1

if __name__ == '__main__':
  Conway().main()
