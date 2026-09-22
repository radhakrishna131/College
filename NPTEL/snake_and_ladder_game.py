import random
#checking is it ladder
def check_ladder(point):
  chances={9:27,18:37,25:54,28:51,56:64,68:88,76:97}
  if point in chances:
    print("ladder")
    return chances[point]
  return point

#checking is it snake
def check_snake(point):
  chances={16:7,59:17,63:19,67:30,87:24,93:69,95:75,99:77}
  if point in chances:
    print("snake")
    return chances[point]
  return point

#check winning status
def win_status(player_score):
  return player_score==100


def play():
  #intialising players names
  p1=input("Enter player1 name:")
  p2=input("Enter player2 name:")
  pp1,pp2,move=0,0,0 #intial values
  while(True):
    #even numbers are player1 moves
    if move%2==0:
      print("player 1 chance")
      c=input("Do you want to continue(1/0):")
      
      if not c:
        print(f"player 1: {p1} is Quiting so player 2: {p2} is win")

      dice=random.randint(1,6)
      if (pp1+dice)<=100:
        pp1+=dice
      pp1=check_ladder(pp1)
      pp1=check_snake(pp1)
      if win_status(pp1):
        print(f"player1:{p1} win with score {pp1}")
    
    #odd numbers are player 2 moves
    else:
      print("player 2 chance")
      c=input("Do you want to continue(1/0):")
      
      if not c:
        print(f"player 2: {p2} is Quiting so player 1: {p1} is win")
      
      dice=random.randint(1,6)
      if (pp2+dice)<=100:
        pp2+=dice
      pp2=check_ladder(pp2)
      pp2=check_snake(pp2)
      if win_status(pp2):
        print(f"player2:{p2} win with score {pp2}")
    print(f"Player 1 score :{pp1}\nPlayer 2 score: {pp2}")
    #after every time move is incremented
    move+=1
      
play()