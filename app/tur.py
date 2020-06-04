##trabalho feito por Duarte e Sergio
from flask import flash
import time

def main(string):

    tapehead = 1

    if string == "1" or string == "0":
        return ("Insert more than one caracter")

    def action(inp, rep, move):
        nonlocal tapehead
        print(tape[tapehead])
        if tape[tapehead] == inp:
            tape[tapehead] = rep
            if move == 'S':
                return True
            if move == 'L':
                tapehead -= 1
            elif move == 'R':
                tapehead += 1
            return True
        return False
    



    #string = input("Enter String: ")
    length = len(string) + (len(string) * 2)
    tape = ['\u0394'] * length
    i = 1

    tapehead = 1
    for s in string:
        tape[i] = s
        i += 1


    state = 1

    R, L, x, d, S = 'R', 'L', 'x', '\u0394', 'S'
    #count = 1
    #tapelist = []
    oldtapehead = -1
    accept = False
    while(oldtapehead != tapehead):
        oldtapehead = tapehead
        #time.sleep(1)
        
        #tapelist[count] = tape
        #count += 1
        
        print(tape, "with tapehead at index", tapehead, "on state", state)

        if state == 1:
            if action('0', '0', R) or action('1', '1', R):
                state = 1
            elif action(d, '$', L):
                print('ok boomer')
                state = 2

        elif state == 2:
            if action('1', '1', L) or action('0', '0', L):
                state = 2
            elif action(d, d, R):
                state = 3

        elif state == 3:
            if action(x, x, R) or action('1', '1', R):
                state = 3
            elif action('0', x, R):
                state = 4
            elif action('$', '$', L):
                state = 7

        elif state == 4:
            if action('1', '1', R) or action('0', '0', R):
                state = 4
            elif action('$', '$', R):
                state = 5

        elif state == 5:
            if action('0', '0', R):
                state = 5
            elif action(d, '0', L):
                state = 6

        elif state == 6:
            if action('0', '0', L) or action('$', '$', L) or action('1', '1', L) or action(x, x, L):
                state = 6
            elif action(d, d, R):
                state = 3

        elif state == 7:
            if action('1', '1', L) or action(x, x, L):
                state = 7
            elif action(d, d, R):
                state = 8

        elif state == 8:
            if action(x, x, R):
                state = 8
            elif action('1', x, R):
                state = 9
            elif action('$', d, L):
                state = 11

        elif state == 9:
            if action('1', '1', R) or action(x, x, R) or action('$', '$', R) or action('0', '0', R):
                state = 9
            elif action(d, '1', L):
                state = 10

        elif state == 10:
            if action('0', '0', L) or action('$', '$', L) or action('1', '1', L) or action(x, x, L):
                state = 10
            elif action(d, d, R):
                state = 8

        elif state == 11:
            if action(x, d, L):
                state = 11
            elif action(d, d, S):
                return tape

    
    if accept:
        print("String accepted on state = ", state)
    else:
        return("String not accepted on state = ", state)
    
    


