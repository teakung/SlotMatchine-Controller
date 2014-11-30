from practicum import findDevices
from peri import PeriBoard
import time

# i = 0


def main():
    #init
    for i,dev in enumerate(findDevices()):
        board = PeriBoard(dev)

    if rouleteGame(board,1):
        print 'True'
    else:
        print 'False'

    # while True:
    #     for i in range(7):
    #         board.setinLed(i,1)
    #         if board.getSwitch()==True:
    #             board.setoutLed(i,1)
    #             setALLin(board,0)
    #             break
    #         time.sleep(0.1)
    #         if board.getSwitch()==True:
    #             board.setoutLed(i,1)
    #             setALLin(board,0)
    #             break
    #         board.setinLed(i,0)
    #         time.sleep(0.1)
    #         if board.getSwitch()==True:
    #             board.setoutLed(i,1)
    #             setALLin(board,0)
    #             break


def rouleteGame(board,target):
    board.setoutLed(target,1)
    while True:
        for i in range(7):
            board.setinLed(i,1)
            if board.getSwitch()==True:
                if i == target:
                    setALLin(board,0)
                    setALLout(board,0)
                    return True
                else:
                    setALLin(board,0)
                    setALLout(board,0)
                    return False
                setALLin(board,0)
            time.sleep(0.1)
            if board.getSwitch()==True:
                if i == target:
                    setALLin(board,0)
                    setALLout(board,0)
                    return True
                else:
                    setALLin(board,0)
                    setALLout(board,0)
                    return False
                setALLin(board,0)
            board.setinLed(i,0)
            time.sleep(0.1)
            if board.getSwitch()==True:
                if i == target:
                    setALLin(board,0)
                    setALLout(board,0)
                    return True
                else:
                    setALLin(board,0)
                    setALLout(board,0)
                    return False
                setALLin(board,0)




#######################
# roulete Light Method#
#######################
# def rouleteLightIn(board):
#     for i in range(7):
#             board.setinLed(i,1)
#             time.sleep(0.09)
#             board.setinLed(i,0)
#             time.sleep(0.09)

# def rouleteLightOut(board):
#     for i in range(7):
#             board.setoutLed(i,1)
#             time.sleep(0.03)
#             board.setoutLed(i,0)
#             time.sleep(0.03)

def setALLout(board,value):
    for i in range(7):
        board.setoutLed(i,value)

def setALLin(board,value):
    for i in range(7):
        board.setinLed(i,value)

if __name__=='__main__':
    main()