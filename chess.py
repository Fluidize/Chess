class Chess:

  def __init__(self):
    board = []
    ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]
    files = ["8", "7", "6", "5", "4", "3", "2", "1"]
    for file in files:
      smallarr = []
      for rank in ranks:
        smallarr.append("__" + rank + file)
      board.append(smallarr)

    self.board = board
  
  def changeSquare(self, value, new_value="__", type="square"):
    #without specifying new value, square will be reset
    if type == "square":
        coordinate = ()
        for z in range(len(self.board)):
            for i in range(len(self.board[z])):
                if value in self.board[z][i]:
                    coordinate = (z, i)
        piece = self.board[coordinate[0]][coordinate[1]][:2]
        self.board[coordinate[0]][coordinate[1]] = self.board[coordinate[0]][coordinate[1]].replace(piece, new_value)
    elif type == "coordinate":
      self.board[value[0]][value[1]] = value.replace("__",new_value)
    
  
  def getSquarePiece(self, value, type="square"):
    if type == "square":
        coordinate = ()
        print(value)
        for z in range(len(self.board)):
            for i in range(len(self.board[z])):
                print(value , self.board[z][i])
                if value in self.board[z][i]:
                    coordinate = (z, i)
        square = self.board[coordinate[0]][coordinate[1]]
        return [square[:2], coordinate, square[-2:]]
    elif type == "coordinate":
       square = self.board[value[0]][value[1]]
       return [square[:2], value, square[-2:]]
  
  def setup(self):
    back_rank = ["R","N","B","Q","K","B","N","R"]
    for rank in self.board:
      for square in rank:
        if "2" in square:
          self.changeSquare(square, "wP")
        if "7" in square:
          self.changeSquare(square, "bP")
    for rank in self.board:
      if "8" in rank[0]:
        color = "b"
      elif "1" in rank[0]:
        color = "w"
      else:
        continue
      for z in range(len(rank)):
          self.changeSquare(rank[z], color + back_rank[z])
  
  def move(self):
    current_square = input("Square: ")
    next_square = input("Move to: ")
    cur_piece, cur_coordinate, sqr = self.getSquarePiece(current_square)
    possible_moves = []
    print(cur_piece,cur_coordinate,current_square)
    if cur_piece[0] == "w":
      color = "white"
      if cur_piece[1] == "P":
        possible_moves = [self.getSquarePiece((cur_coordinate[0]-1,cur_coordinate[1]), "coordinate")[2], self.getSquarePiece((cur_coordinate[0]-2,cur_coordinate[1]), "coordinate")[2]]
        if next_square in possible_moves:
           self.changeSquare(current_square)
           self.changeSquare(next_square, cur_piece)
    elif cur_piece[0] == "b":
      color = "black"
      pass
    
    
    
  
  def displayBoard(self):
    for rank in self.board:
      for square in rank:
        print(square, end="  ")
      print("\n")
  


instance = Chess()
instance.setup()
instance.move()
instance.displayBoard()