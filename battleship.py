import keyboard
from random import randint

class Board:
  def __init__(self,is_cpu=False):
    self.grid = self.make_board()
    self.divider = "-" * 39
    self.lives = 17
    self.is_cpu=is_cpu
    self.boats=[
      [2,None,None],
      [3,None,None],
      [3,None,None],
      [4,None,None],
      [5,None,None],
    ]
    self.boat_cords=[]
    

  def make_board(self):
    return [["   " for _ in range(10)] for _ in range(10)]

  def print_board(self, y, x):
    view = [row[:] for row in self.grid]
    view[y][x] = ' ¤ '

    print('\n')
    print('\n')
    for i, row in enumerate(view):
      print("|".join(row))
      if i < len(view) - 1:
        print(self.divider)

  def boat_placer(self):
    while True:
      y,x,z=randint(0,9),randint(0,9),randint(0,1)

      
      
      

  def cursor(self):
    x,y=0,0
    print("\033[2J\033[H", end="")
    player_board.print_board(y,x)

    while True:
      event = keyboard.read_event()

      if event.event_type != 'down':
        continue

      if keyboard.is_pressed('up'):
        if y>0:
          y-=1
      elif keyboard.is_pressed("down"):
        if y<9:
          y+=1
      elif keyboard.is_pressed("left"):
        if x>0:
          x-=1
      elif keyboard.is_pressed("right"):
        if x<9:
          x+=1

      elif keyboard.is_pressed('enter'):
        self.grid[y][x]=' ■ '
        print(y,x)

      print("\033[H", end="")
      self.print_board(y,x)




player_board=Board()
cpu_board=Board(True)

player_board.cursor()