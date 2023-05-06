import os
from termcolor import colored

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
    self.err_msg = "ILLEGAL MOVE"
    self.colors = ["w", "b"]
    self.castle = {
      "w" : True,
      "b" : True
    }

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
      try:
        square = self.board[coordinate[0]][coordinate[1]]
        return [square[:2], coordinate, square[-2:]]
      except:
        print(colored(self.err_msg, "red"))
    elif type == "coordinate":
      try:
        square = self.board[value[0]][value[1]]
        return [square[:2], value, square[-2:]]
      except:
        pass

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
  
  def check(self): 
      for rank in self.board:
        for square in rank:
          cur_piece, cur_coordinate, sqr = self.getSquarePiece(square)
          possible_moves = []
          if cur_piece[0] == "w": 
            
            if cur_piece[1] == "K":
              modifiers = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
              for modifier in modifiers:
                square = self.getSquarePiece((cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]), "coordinate")
                try:
                    if "w" not in square[2]:
                      possible_moves.append(square[2])
                except:
                  pass
            
            if cur_piece[1] == "Q":
              modifiers = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
              for modifier in modifiers:
                temp_mod = modifier
                while True:
                  square = self.getSquarePiece((cur_coordinate[0] + temp_mod[0], cur_coordinate[1] + temp_mod[1]), "coordinate")
                  try:
                    if "__" in square[0]:
                      possible_moves.append(square[2]) 
                    elif "b" in square[0]:
                      possible_moves.append(square[2])
                      break
                    else:
                      break
                  except:
                    break
                  temp_mod = (temp_mod[0] + modifier[0], temp_mod[1] + modifier[1])
            
            if cur_piece[1] == "P":
              modifiers = [(-1, 0)]
              if "2" in sqr:
                modifiers.append((-2, 0))
              for modifier in modifiers:
                square = self.getSquarePiece(   
                  (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),"coordinate")
                try:
                  if "__" in square[0]:
                    possible_moves.append(square[2])
                  else:
                    break
                except:
                  pass
              modifiers = [(-1, -1), (-1, 1)]
              for modifier in modifiers:
                square = self.getSquarePiece(
                  (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),"coordinate")
                try:
                  if "b" in square[0]:
                    possible_moves.append(square[2])
                except:
                  pass
            #knight
            if cur_piece[1] == "N":
              modifiers = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1),(-1, 2), (1, 2)]
              for modifier in modifiers:
                square = self.getSquarePiece(
                  (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),
                  "coordinate")
                try:
                  if "w" not in square[0]:
                    possible_moves.append(square[2])
                except:
                  pass
            #bishop
            if cur_piece[1] == "B":
              #continous modifiers
              modifiers = [(-1,-1),(-1,1),(1,-1),(1,1)]
              for modifier in modifiers:
                temp_mod = modifier
                while True:
                  square = self.getSquarePiece((cur_coordinate[0] + temp_mod[0], cur_coordinate[1] + temp_mod[1]), "coordinate")
                  try:
                    if "__" in square[0]:
                      possible_moves.append(square[2]) 
                    elif "b" in square[0]:
                      possible_moves.append(square[2])
                      break
                    else:
                      break
                  except:
                    break
                  temp_mod = (temp_mod[0] + modifier[0], temp_mod[1] + modifier[1])
            #rook        
            if cur_piece[1] == "R":
              modifiers = [(-1,0),(1,0),(0,-1),(0,1)]
              for modifier in modifiers:
                temp_mod = modifier
                while True:
                  square = self.getSquarePiece((cur_coordinate[0] + temp_mod[0], cur_coordinate[1] + temp_mod[1]), "coordinate")
                  try:
                    if "__" in square[0]:
                      possible_moves.append(square[2]) 
                    elif "b" in square[0]:
                      possible_moves.append(square[2])
                      break
                    else:
                      break
                  except:
                    break
                  temp_mod = (temp_mod[0] + modifier[0], temp_mod[1] + modifier[1])
  
          elif cur_piece[0] == "b":
              if cur_piece[1] == "K":
                modifiers = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
                for modifier in modifiers:
                  square = self.getSquarePiece((cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]), "coordinate")
                  try:
                      if "b" not in square[2]:
                        possible_moves.append(square[2])
                  except:
                    pass
  
              if cur_piece[1] == "P":
                modifiers = [(1, 0)]
                if "7" in sqr:
                  modifiers.append((2, 0))
                for modifier in modifiers:
                  square = self.getSquarePiece(
                    (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),
                    "coordinate")
                  if "__" in square[0]:
                    possible_moves.append(square[2])
                  else:
                    break
                modifiers = [(1, -1), (1, 1)]
                for modifier in modifiers:
                  square = self.getSquarePiece(
                    (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),
                    "coordinate")
                  if "w" in square[0]:
                    possible_moves.append(square[2])
              
              if cur_piece[1] == "N":
                modifiers = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1),
                            (-1, 2), (1, 2)]
                for modifier in modifiers:
                  square = self.getSquarePiece(
                    (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),
                    "coordinate")
                  try:
                    if "b" not in square[0]:
                      possible_moves.append(square[2])
                  except:
                    pass
              
              if cur_piece[1] == "B":
                #continous modifiers
                modifiers = [(-1,-1),(-1,1),(1,-1),(1,1)]
                for modifier in modifiers:
                  temp_mod = modifier
                  while True:
                    square = self.getSquarePiece((cur_coordinate[0] + temp_mod[0], cur_coordinate[1] + temp_mod[1]), "coordinate")
                    try:
                      if "__" in square[0]:
                        possible_moves.append(square[2]) 
                      elif "w" in square[0]:
                        possible_moves.append(square[2])
                        break
                      else:
                        break
                    except:
                      break
                    temp_mod = (temp_mod[0] + modifier[0], temp_mod[1] + modifier[1])
  
              if cur_piece[1] == "R":
                modifiers = [(-1,0),(1,0),(0,-1),(0,1)]
                for modifier in modifiers:
                  temp_mod = modifier
                  while True:
                    square = self.getSquarePiece((cur_coordinate[0] + temp_mod[0], cur_coordinate[1] + temp_mod[1]), "coordinate")
                    try:
                      if "__" in square[0]:
                        possible_moves.append(square[2]) 
                      elif "w" in square[0]:
                        possible_moves.append(square[2])
                        break
                      else:
                        break
                    except:
                      break
                    temp_mod = (temp_mod[0] + modifier[0], temp_mod[1] + modifier[1])
          #insert king check here
        
  def move(self, color): 
    while True:
      while True:
        inp = input("Move: ").lower()
        
        try:
          if (inp[0] in ("a","b","c","d","e","f","g","h")) and (inp[1] in ("1","2","3","4",'5',"6","7","8")):
              current_square = inp
              next_square = input("To: ")
          else:
            if self.castle[color]:
              castle = inp
              break
        except:
          if self.castle[color]:
            castle = inp
        try:
          cur_piece, cur_coordinate, sqr = self.getSquarePiece(current_square)
        except:
          print(colored("INVALID", "red"))
        
        try:
          if color not in cur_piece:
            if color == "w":
              print(colored("You must move a WHITE piece.","red"))
            elif color == "b":
              print(colored("You must move a BLACK piece.", "red"))
          else:
            break
        except:
          pass
      
      possible_moves = []
      try:
        if cur_piece[0] == "w": 
          #king
          if cur_piece[1] == "K":
            modifiers = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            for modifier in modifiers:
              square = self.getSquarePiece((cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]), "coordinate")
              try:
                  if "w" not in square[2]:
                    possible_moves.append(square[2])
              except:
                pass
          #queen
          if cur_piece[1] == "Q":
            modifiers = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            for modifier in modifiers:
              temp_mod = modifier
              while True:
                square = self.getSquarePiece((cur_coordinate[0] + temp_mod[0], cur_coordinate[1] + temp_mod[1]), "coordinate")
                try:
                  if "__" in square[0]:
                    possible_moves.append(square[2]) 
                  elif "b" in square[0]:
                    possible_moves.append(square[2])
                    break
                  else:
                    break
                except:
                  break
                temp_mod = (temp_mod[0] + modifier[0], temp_mod[1] + modifier[1])
          #pawn
          if cur_piece[1] == "P":
            modifiers = [(-1, 0)]
            if "2" in sqr:
              modifiers.append((-2, 0))
            for modifier in modifiers:
              square = self.getSquarePiece(   
                (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),"coordinate")
              try:
                if "__" in square[0]:
                  possible_moves.append(square[2])
                else:
                  break
              except:
                pass
            modifiers = [(-1, -1), (-1, 1)]
            for modifier in modifiers:
              square = self.getSquarePiece(
                (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),"coordinate")
              try:
                if "b" in square[0]:
                  possible_moves.append(square[2])
              except:
                pass
          #knight
          if cur_piece[1] == "N":
            modifiers = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1),(-1, 2), (1, 2)]
            for modifier in modifiers:
              square = self.getSquarePiece(
                (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),
                "coordinate")
              try:
                if "w" not in square[0]:
                  possible_moves.append(square[2])
              except:
                pass
          #bishop
          if cur_piece[1] == "B":
            #continous modifiers
            modifiers = [(-1,-1),(-1,1),(1,-1),(1,1)]
            for modifier in modifiers:
              temp_mod = modifier
              while True:
                square = self.getSquarePiece((cur_coordinate[0] + temp_mod[0], cur_coordinate[1] + temp_mod[1]), "coordinate")
                try:
                  if "__" in square[0]:
                    possible_moves.append(square[2]) 
                  elif "b" in square[0]:
                    possible_moves.append(square[2])
                    break
                  else:
                    break
                except:
                  break
                temp_mod = (temp_mod[0] + modifier[0], temp_mod[1] + modifier[1])
          #rook        
          if cur_piece[1] == "R":
            modifiers = [(-1,0),(1,0),(0,-1),(0,1)]
            for modifier in modifiers:
              temp_mod = modifier
              while True:
                square = self.getSquarePiece((cur_coordinate[0] + temp_mod[0], cur_coordinate[1] + temp_mod[1]), "coordinate")
                try:
                  if "__" in square[0]:
                    possible_moves.append(square[2]) 
                  elif "b" in square[0]:
                    possible_moves.append(square[2])
                    break
                  else:
                    break
                except:
                  break
                temp_mod = (temp_mod[0] + modifier[0], temp_mod[1] + modifier[1])

        elif cur_piece[0] == "b":
            if cur_piece[1] == "K":
              modifiers = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
              for modifier in modifiers:
                square = self.getSquarePiece((cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]), "coordinate")
                try:
                    if "b" not in square[2]:
                      possible_moves.append(square[2])
                except:
                  pass

            if cur_piece[1] == "P":
              modifiers = [(1, 0)]
              if "7" in sqr:
                modifiers.append((2, 0))
              for modifier in modifiers:
                square = self.getSquarePiece(
                  (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),
                  "coordinate")
                if "__" in square[0]:
                  possible_moves.append(square[2])
                else:
                  break
              modifiers = [(1, -1), (1, 1)]
              for modifier in modifiers:
                square = self.getSquarePiece(
                  (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),
                  "coordinate")
                if "w" in square[0]:
                  possible_moves.append(square[2])
            
            if cur_piece[1] == "N":
              modifiers = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1),
                          (-1, 2), (1, 2)]
              for modifier in modifiers:
                square = self.getSquarePiece(
                  (cur_coordinate[0] + modifier[0], cur_coordinate[1] + modifier[1]),
                  "coordinate")
                try:
                  if "b" not in square[0]:
                    possible_moves.append(square[2])
                except:
                  pass
            
            if cur_piece[1] == "B":
              #continous modifiers
              modifiers = [(-1,-1),(-1,1),(1,-1),(1,1)]
              for modifier in modifiers:
                temp_mod = modifier
                while True:
                  square = self.getSquarePiece((cur_coordinate[0] + temp_mod[0], cur_coordinate[1] + temp_mod[1]), "coordinate")
                  try:
                    if "__" in square[0]:
                      possible_moves.append(square[2]) 
                    elif "w" in square[0]:
                      possible_moves.append(square[2])
                      break
                    else:
                      break
                  except:
                    break
                  temp_mod = (temp_mod[0] + modifier[0], temp_mod[1] + modifier[1])

            if cur_piece[1] == "R":
              modifiers = [(-1,0),(1,0),(0,-1),(0,1)]
              for modifier in modifiers:
                temp_mod = modifier
                while True:
                  square = self.getSquarePiece((cur_coordinate[0] + temp_mod[0], cur_coordinate[1] + temp_mod[1]), "coordinate")
                  try:
                    if "__" in square[0]:
                      possible_moves.append(square[2]) 
                    elif "w" in square[0]:
                      possible_moves.append(square[2])
                      break
                    else:
                      break
                  except:
                    break
                  temp_mod = (temp_mod[0] + modifier[0], temp_mod[1] + modifier[1])
      except:
        pass
      
      try:
        if castle == "o-o":
          if color == "w":
            square_1 = self.getSquarePiece("f1")
            square_2 = self.getSquarePiece("g1")
            pieces = ["e1","h1","f1","wR","g1","wK"]
          elif color == "b":
            square_1 = self.getSquarePiece("f8")
            square_2 = self.getSquarePiece("g8")
            pieces = ["e8","h8","f8","bR","g8","bK"]
          if (square_1[0] == "__") and (square_2[0] == "__"):
            self.changeSquare(pieces[0])
            self.changeSquare(pieces[1])
            self.changeSquare(pieces[2],pieces[3])
            self.changeSquare(pieces[4],pieces[5])
            self.castle[color] = False
          else:
            print(colored(self.err_msg, "red"))
        
        elif castle == "o-o-o":
          if color == "w":
            square_1 = self.getSquarePiece("d1")
            square_2 = self.getSquarePiece("c1")
            square_3 = self.getSquarePiece("b1")
            pieces = ["e1","a1","d1","wR","c1","wK"]
          elif color == "b":
            square_1 = self.getSquarePiece("d8")
            square_2 = self.getSquarePiece("c8")
            square_3 = self.getSquarePiece("b8")  
            pieces = ["e8","a8","d8","bR","c8","bK"]
          if (square_1[0] == "__") and (square_2[0] == "__") and (square_3[0]):
            self.changeSquare(pieces[0])
            self.changeSquare(pieces[1])
            self.changeSquare(pieces[2],pieces[3])
            self.changeSquare(pieces[4],pieces[5])
            self.castle[color] = False
          else:
            print(colored(self.err_msg, "red"))
      except:
        pass
      
      try:
        if next_square in possible_moves:
          if cur_piece[2:] == "wK":
            self.castle["w"] = False
          elif cur_piece[2:] == "bK":
            self.castle["b"] = False
          self.changeSquare(current_square)
          self.changeSquare(next_square, cur_piece)
          break
        elif next_square not in possible_moves:
          raise Exception(self.err_msg)
      except:
        if not inp == ("o-o" or "o-o-o"):
          print(colored(self.err_msg,"red"))

  def displayBoard(self):
    for rank in self.board:
      for square in rank:
        if square[0] == "w":
          print(colored(square,"blue"), end="  ")
        elif square[0] == "b":
          print(colored(square,"red"), end="  ")
        else:
          print(square, end="  ")
      print("\n")

  def start(self):
    flip = False
    self.setup()
    while True:
      os.system('clear')
      move_color = self.colors[int(flip)]
      
      if move_color == "w":
        print(colored("WHITE'S TURN\n", "green"))
      else:
        print(colored("BLACK'S TURN\n", "green"))
      
      self.displayBoard()
      self.move(color=move_color)
      flip = not flip

game = Chess()
game.start()
