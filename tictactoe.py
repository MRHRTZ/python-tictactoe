# # # # # # # # # # # # # # # # # # # # # # # # # 
#    TICTACTOE GAMEBOARD BUILT ON PYTHON 3      #
#             Created By MRHRTZ                 #
#              Made With <3                     #
# # # # # # # # # # # # # # # # # # # # # # # # #

import numpy, random, sys
from colorama import Fore, Style

# Global varible
game = {}

# Constants variable
constant = {
    'coor_has_set': f'\n{Fore.RED}Maaf titik koordinat tersebut sudah diisi.{Style.RESET_ALL}',
    'wrong_coor': f'\n{Fore.RED}Maaf koordinat x atau y tidak valid, gunakan angka 0-2 dan format x,y {Style.RESET_ALL}',
    'turn_ask': f'{Fore.YELLOW}Giliran pemain',
    'input_ask': f'{Fore.MAGENTA}Inputkan Baris, Kolom (gunakan koordinat x,y) : ',
    'winner': f'{Fore.GREEN}Selamat game dimenangkan oleh ',
    'draw': f'{Fore.LIGHTYELLOW_EX}Kedudukan saat ini seri!',
    'exit': f'\n\n{Fore.LIGHTYELLOW_EX}Bye..\n{Style.RESET_ALL}',
    'copyright': f'{Fore.CYAN}# # # # # # # # # # # # # # # # # # # # # # # # # \r\n#    TICTACTOE GAMEBOARD BUILT ON PYTHON 3      #\r\n#             Created By MRHRTZ                 #\r\n#              Made With <3                     #\r\n# # # # # # # # # # # # # # # # # # # # # # # # #{Fore.LIGHTWHITE_EX}\n\n'
}

def initGame():
    # Initial first object
    obj = {
        'board': numpy.full((3,3), 0),
        'player': {
            1: [],
            2: []
        },
        'turn': random.choices(['P1','P2'])[0],
        'isGameOver': False,
        'winner': None,
        'P1': 1,
        'P2': 2
    }

    # Assign to global variable
    game.update(obj)

    return obj


def pointChecker(v_game):
    # Init Variables
    board = v_game['board']
    P1 = 1
    P2 = 2

    # Horizontal check
    h1 = board[0]
    h2 = board[1]
    h3 = board[2]

    H1P1 = numpy.all(numpy.equal(h1, P1))
    H1P2 = numpy.all(numpy.equal(h1, P2))    
    H2P1 = numpy.all(numpy.equal(h2, P1))
    H2P2 = numpy.all(numpy.equal(h2, P2))
    H3P1 = numpy.all(numpy.equal(h3, P1))
    H3P2 = numpy.all(numpy.equal(h3, P2))

    if H1P1 or H2P1 or H3P1:
        v_game['isGameOver'] = True
        v_game['winner'] = P1
    elif H1P2 or H2P2 or H3P2:
        v_game['isGameOver'] = True
        v_game['winner'] = P2
    else:
        turn = v_game['turn']
        v_game['turn'] = 'P1' if turn == 'P2' else 'P2'

    # Vertical check
    v1 = board[:, 0]
    v2 = board[:, 1]
    v3 = board[:, 2]

    V1P1 = numpy.all(numpy.equal(v1, P1))
    V1P2 = numpy.all(numpy.equal(v1, P2)) 
    V2P1 = numpy.all(numpy.equal(v2, P1))
    V2P2 = numpy.all(numpy.equal(v2, P2)) 
    V3P1 = numpy.all(numpy.equal(v3, P1))
    V3P2 = numpy.all(numpy.equal(v3, P2)) 

    if V1P1 or V2P1 or V3P1:
        v_game['isGameOver'] = True
        v_game['winner'] = P1
    elif V1P2 or V2P2 or V3P2:
        v_game['isGameOver'] = True
        v_game['winner'] = P2
    else:
        turn = v_game['turn']
        v_game['turn'] = 'P1' if turn == 'P2' else 'P2'
    
    # Diagonal check
    d1 = numpy.diagonal(board)
    d2 = numpy.fliplr(board).diagonal()

    D1P1 = numpy.all(numpy.equal(d1, P1))
    D1P2 = numpy.all(numpy.equal(d1, P2)) 
    D2P1 = numpy.all(numpy.equal(d2, P1))
    D2P2 = numpy.all(numpy.equal(d2, P2)) 

    if D1P1 or D2P1:
        v_game['isGameOver'] = True
        v_game['winner'] = P1
    elif D1P2 or D2P2:
        v_game['isGameOver'] = True
        v_game['winner'] = P2
    else:
        turn = v_game['turn']
        v_game['turn'] = 'P1' if turn == 'P2' else 'P2'

    nonzero = numpy.count_nonzero(v_game['board'])

    if nonzero == 9:
        v_game['isGameOver'] = True
        v_game['winner'] = 'draw'
    
    return v_game

def setCoordinate(v_game, x, y):
    board = v_game['board']
    turn = v_game['turn']
    stats = {}

    # Validate coordinate
    if x > 2 or y > 2 or x < 0 or y < 0 :
        stats = { 'status': False, 'message': constant['wrong_coor'] }
    else:
        # Check is not set
        if board[y][x] == 0:
            # Set point of selected player
            board[y][x] = 1 if turn == 'P1' else 2
            pointChecker(v_game)
            stats = { 'status': True, 'data': v_game }
        else:
            stats = { 'status': False, 'message': constant['coor_has_set'] }

    return stats

def printBoard(v_game):
    print('')
    numpy.savetxt(sys.stdout.buffer, v_game['board'], fmt="%i")
    input_ask = f"\n{constant['turn_ask']} {v_game[v_game['turn']]}\n{constant['input_ask'] + Fore.LIGHTWHITE_EX}"
    return input_ask
    

def gameFlows(v_game, readable):
    try:
        x, y = input(readable).split(',')
        x, y = int(x), int(y)
        coorSet = setCoordinate(v_game=v_game, x=x, y=y)
        if not coorSet['status']:
            print(coorSet['message'])
            gameFlows(game, readable)
        else:
            if game['isGameOver']:
                if game['winner'] != 'draw':
                    win_str = f'{constant["winner"]} {"Player 1" if game["winner"] == "P1" else "Player 2"} {Style.RESET_ALL}\n\n'
                else:
                    win_str = f'\n{constant["draw"]} {Style.RESET_ALL}\n\n'
                print(win_str)
            else:
                gameFlows(game, printBoard(game))
    except ValueError:
        print(constant['wrong_coor'])
        gameFlows(game, printBoard(game))
    except KeyboardInterrupt:
        print(constant['exit'])


if __name__ == '__main__':
    print(chr(27) + "[2J" + constant['copyright'])
    initGame()
    gameFlows(game, printBoard(game))
    


