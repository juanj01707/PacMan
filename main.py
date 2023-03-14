import random
print("RULES")
print("If PacMan finds a meal (O) on his way, you will get a point.")
print("If PacMAn finds a ghost (A) on his way, the game will be over.")

Board = int(input("Enter board size: ")) 
matrix = []

# Creating a matrix of size Board
for i in range(Board):
    matrix.append([0] * Board)
 
# fill the board "." Empty space; "O" a meal; and "A" a ghost.
for i in range(Board):
    for j in range(Board):
        if i == 0 and j == 0:
            matrix[i][j] = random.choice(["."])
        else:
          # We repeat the empty spaces and the meal to avoid that there are excess ghosts
            matrix[i][j] = random.choice([".",".",".","O","O","O", "A"])
            
score = 0
game = True

#loop to run PacMan
while game:

    # check board travel
    for i in range(Board):
        if i % 2 == 0:
            
            for j in range(Board):#If the row number is even. It will check if it found an O or an A.
                if matrix[i][j] == "O":
                    score += 1
                if matrix[i][j] == "A":
                    found_A = True
                    game = False
                    break
            if not game:
                break
        else:
            # Checking if the user has found an O or an A. 
            
            for j in range(Board - 1, -1, -1):
                if matrix[i][j] == "O":
                    score += 1
                if matrix[i][j] == "A":
                    found_A = True
                    game = False
                    break
            if not game:
                break
    # Printing the Board and the score.
    for row in matrix:
        print(row)
    print("Points:", score)
    
#END OF GAME MESSAGE
print("GAME OVER")
