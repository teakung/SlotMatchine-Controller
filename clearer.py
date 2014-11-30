from practicum import findDevices
from peri import PeriBoard
import time

def main():
    for i,dev in enumerate(findDevices()):
        board = PeriBoard(dev)
    setALLout(board,0)
    setALLin(board,0)

def setALLout(board,value):
    for i in range(7):
        board.setoutLed(i,value)

def setALLin(board,value):
    for i in range(7):
        board.setinLed(i,value)

if __name__=='__main__':
    main()