# The game of life
# Brad Raynaud
# 4/28/2017
#########################
# Imports
import sys
import os
from time import sleep
#########################


def computeNextGen(board):
    nextboard = copyBoard(board)
    for row in range(1, size - 1):
        for col in range(1, size - 1):
            neighbors = countNeighbours(board, row, col)
            if board[row][col] == "*"
                if neightbours < 2 or neighbours > 3:
                    nextboard[row][col] = " "
            else:
                if neighbors == 3:
                    nextboard[row][col] = "*"
    return nextboard


def copyBoard(board):
    nextboard = []
    for row in board:
        nextboard.append([])
        for col in row:
            nextboard[len(nextboard) - 1].append(col)
    return nextboard


def countNeighbours(board, row, col):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (not(i == 0 and j == 0)):
                if board[row + i][col + i] == "*":
                    neighbors += 1
    return neighbors


def printBoard(board):
    print " ",
    for i in range(1, 6):
        print i % 10,
    print
    for row in range(1, 6):
        print row % 10,
        for col in range(1, 6):
            print board[row][col],
        print


board = [[" ", '*', '*', '*', ' ', '*', " "],
         [" ", '*', ' ', ' ', ' ', ' ', " "],
         [" ", ' ', ' ', ' ', '*', '*', " "],
         [" ", ' ', '*', '*', ' ', '*', " "],
         [" ", '*', ' ', '*', ' ', '*', " "]]

NUM_GENS = 25
os.system("clear")
print "Gen 0"
printBoard(board)
for i in range(NUM_GENS):
    sleep(.5)
    os.system("clear")

    print "Gen {}".format(i)
    board = computeNextGen(board)
    printBoard(board)