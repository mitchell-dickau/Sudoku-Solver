"""
Created on Mon Dec 20 17:15:55 2021

SUDOKU SOLVER
@author: mitchell
"""
#______________________________________________________________________________
#STEPS:
# 1: input board and print board
# 2: function to ID empty cells 
# 3: funciton to try number
# 4: function to validate 
# 5: backtrack if doesn't work

import numpy as np

board = [[0,0,5,0,0,2,0,0,0,],
         [0,0,0,0,4,0,0,1,0,],
         [0,0,6,0,3,0,0,0,0,],
         [0,9,0,0,0,0,0,3,2,],
         [0,0,2,0,0,0,7,4,0,],
         [3,0,7,0,0,0,0,0,0,],
         [0,0,0,0,2,0,5,0,1,],
         [0,8,0,7,0,0,0,0,9,],
         [0,6,0,0,1,0,0,0,8]]

def print_board(bo):
    for r in range(len(bo)):
        if r % 3 == 0 and r != 0 :
            print("- - - - - - - - - - ")
        for c in range(len(bo)):
            if c % 3 == 0 and c != 0 and c != len(bo): 
                print("|", end= "")
            if c == 8 and r != 8:
                print(bo[r][c])
            else: 
                print(str(bo[r][c]) + " ", end= "")
        if r == 8:
            print("\n- - - - - - - - - - " + 
            "\n- - - - - - - - - - ")

def empty_cells(bo):
    count = 1
    coordinates = []
    for r in range(len(bo)):
        for c in range(len(bo)):
            if bo[r][c] != 0:
                continue
            else:
                coordinates.append(tuple((r,c)))
                count += 1
    np.array(coordinates)
    return coordinates


def valid(bo, num, pos):
    # rows
    for n in range(9):
        if bo[n][pos[1]] == num and pos[0] != n:
            return False
    # columns
    for n in range(9):
        if bo[pos[0]][n] == num and pos[1] != n:
            return False
    # box 
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for r in range(box_row*3, box_row*3 +3):
        for c in range(box_col*3, box_col*3 +3):
            if bo[r][c] == num and (r,c) != pos:
                return False
    # valid 
    return True


def solver(bo):
    n = 0 
    val = 1
    cells = empty_cells(bo)
    while any(0 in sublist for sublist in bo):
        cell = cells[n]
        print(f"Current cell is {cell}. Current val is {val}")
        if val > 9:
            bo[cell[0]][cell[1]] = 0
            n = n - 1 
            cell = cells[n]
            val = bo[cell[0]][cell[1]] + 1 
            continue
        if valid(bo, val, cell) == True:
            bo[cell[0]][cell[1]] = val
            print_board(bo)
            n += 1
            val = 1
            if any(0 in sublist for sublist in board) == False:
                print_board(bo)
                print("Sudoku complete!")
            continue 
        if valid(bo, val, cell) == False and val < 9:
            val += 1 
            continue
        if valid(bo, val, cell) == False and val == 9:
            bo[cell[0]][cell[1]] = 0
            n = n - 1 
            cell = cells[n]
            val = bo[cell[0]][cell[1]] + 1 
            continue 
 
solver(board)