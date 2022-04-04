class Board:
  pass

  def __init__(self):
    self.reset()

  def reset(self):
    self.cells= ["1", "", "", "", "", "", "", "", ""]

  def display(self):
    print(self.cells)
  
  def position(self, string):
      index = int(string) -1
      return self.cells[index]
  
  def update(self, string, player):
    index = int(string) - 1
    self.cells[index] = player.token()

board = Board()
board.display()

board.position('1')

board.update('1')
