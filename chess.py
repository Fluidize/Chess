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
      self.board[coordinate[0]][coordinate[1]] = self.board[coordinate[0]][
        coordinate[1]].replace(piece, new_value)
    elif type == "coordinate":
      self.board[value[0]][value[1]] = value.replace("__", new_value)

  def getSquarePiece(self, value, type="square"):
    #arr[0] = color and piece
    #arr[1] = coordinate of piece
    #arr[2] = square notation
    if type == "square":
      coordinate = ()
      for z in range(len(self.board)):
        for i in range(len(self.board[z])):
          if value in self.board[z][i]:
            coordinate = (z, i)
      square = self.board[coordinate[0]][coordinate[1]]
      return [square[:2], coordinate, square[-2:]]
    elif type == "coordinate":
      square = self.board[value[0]][value[1]]
      return [square[:2], value, square[-2:]]

  def setup(self):
    back_rank = ["R", "N", "B", "Q", "K", "B", "N", "R"]
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
    if cur_piece[0] == "w":
      color = "white"

      #king
      
      #pawn
      if cur_piece[1] == "P":
        modifiers = [(-1,0),(-2,0)]
        for modifier in modifiers:
          square = self.getSquarePiece((cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]), "coordinate")
          if square[0] == "__":
            possible_moves.append(square[2])
        modifiers = [(-1,-1),(-1,1)]
        for modifier in modifiers:
          square = self.getSquarePiece((cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]), "coordinate")
          if "b" in square[0]:
            possible_moves.append(square[2])
      if cur_piece[1] == "N":
        modifiers = [(-1,-2),(1,-2),(-2,-1),(-2,1),(2,-1),(2,1),(-1,2),(1,2)]
        for modifier in modifiers:
          square = self.getSquarePiece((cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]), "coordinate")
          possible_moves.append(square[2])

    elif cur_piece[0] == "b":
      color = "black"
      pass
    print(possible_moves)

    if next_square in possible_moves:
      self.changeSquare(current_square)
      self.changeSquare(next_square, cur_piece)
    elif next_square not in possible_moves:
      raise Exception("Illegal Move")

    
  
  def displayBoard(self):
    for rank in self.board:
      for square in rank:
        print(square, end="  ")
      print("\n")


instance = Chess()
instance.setup()
instance.move()
instance.displayBoard()
