import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_new_2(mat):
    
    r = random.randint(0,3)
    c = random.randint(0,3)
    
    while mat[r][c]!=0:
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c]=2

def compress(mat):
    new_mat = [[0 for j in range(4)] for i in range(4)]
    changed = False
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if pos != j:
                    changed = True
                pos+=1
  
    return new_mat,changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0
                changed = True
    return mat,changed
    
                
def reverse(mat):
    rev_mat = []
    for i in range(4):
        rev_mat.append([0]*4)
    
    #reversing the mat
    for i in range(4):
        for j in range(4):
            rev_mat[i][j] = mat[i][4-j-1]
    
    return rev_mat

def transpose(mat):
    tra_mat = []
    for i in range(4):
        tra_mat.append([0]*4)
    
    #transposing the mat
    for i in range(4):
        for j in range(4):
            tra_mat[i][j] = mat[j][i]
        
    return tra_mat
    
    
def get_current_status(mat):
    #check for 2048
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    
    #check for 0 
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
        
    #check for same consecutive no except last row and col
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] or mat[i][j] == mat[i+1][j]:
                return 'GAME NOT OVER'
            
    #check for last row
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'GAME NOT OVER'
    
    #check for last col
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'GAME NOT OVER'
    
    return 'LOST'

def move_up(grid):
    #Implement This Function
    new_grid = transpose(grid)
    new_grid,changed = move_left(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,changed

def move_down(grid):
    #Implement This Function
    new_grid = transpose(grid)
    reversed_grid = reverse(new_grid)
    new_grid,changed = move_left(reversed_grid)
    reverse_grid = reverse(new_grid)
    final_grid = transpose(reverse_grid)
    return final_grid,changed

def move_right(grid):
    #Implement This Function
    reversed_grid = reverse(grid)
    new_grid,changed = move_left(reversed_grid)
    final_grid = reverse(new_grid)
    return final_grid,changed

def move_left(grid):
    #Implement This Function
    new_grid,changed1 = compress(grid)
    merge_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    final_grid,temp = compress(merge_grid)
    return final_grid,changed



