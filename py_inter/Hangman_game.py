import random
import os



stage = \
    '''   
~~~~~~~~~~~~~|~
             |
 0123456789  J    
~~~~~~~~~~~~~~~~~   
'''
symbols = '><(((º>---'
words = []
with open("./archive/data.txt","r",encoding="utf-8")as f:
    words = [i.replace("\n","") for i in f]   

def welcome():
    print('*' * 68)
    print('* welcome to the hangman game :) *')
    print('*' * 68) 


def start_game(words):
    word = random.choice(words).lower() 
    board = ["_"] * len(word)
    return board, word, []


def show_stage(errors): 
    scene = stage
    for i in range(0, len(symbols)):
        symbol = symbols[i] if i < errors else " "
        scene = scene.replace(str(i), symbol)
    print(scene)


def show_board(board, wrong_letters):
    for box in board:
        print(box, end=" ")
    print()
    print()
    if len(wrong_letters) > 0:
        print("letters:", * wrong_letters)


def request_letter(board, wrong_letters):
    valid = False
    while not valid:
        letter = input("Enter a letter (a-z): ").lower()
        valid = "a" <= letter <= "z" and len(letter) == 1
        if not valid:
            print("error, the letter have is between a and z:")
        else:
            valid = letter not in board + wrong_letters
            if not valid:
                print("the repeat letter, try another.")

    return letter


def process_letter(letter,word, board, wrong_letters):
    if letter in word:
        print("cool, you're right a letter ")
        update_board(letter, word, board)
        os.system("clear")
    else:
        print("oh you are faild")    
        wrong_letters.append(letter)
        os.system("clear")




def update_board(letter, word, board):
      for index, letter_word in enumerate(word):
          if letter == letter_word:
              board[index] = letter

    


def check_word(board):
    return "_" not in board
    # if "_" not in board:
    #     print("Congratulations, you have done it! ")
    

def hangman_game(words):

    board, word, wrong_letters = start_game(words)
    while len(wrong_letters) < len(symbols):
        show_stage(len(wrong_letters))
        show_board(board, wrong_letters)
        letter = request_letter(board, wrong_letters)
        process_letter(letter,word, board, wrong_letters)
        if check_word(board):
            print("""

   .g8MMMbgd       db      `7MN.   `7MF'    db       .MMMMbgd MMP""MM""YMM `7MMMMMYMM  
.dP'     `M      ;MM:       MMN.    M      ;MM:     ,MI    "Y P'   MM   `7   MM    `7  
dM'       `     ,V^MM.      M YMb   M     ,V^MM.    `MMb.          MM        MM   d    
MM             ,M  `MM      M  `MN. M    ,M  `MM      `YMMNq.      MM        MMmmMM    
MM.    `7MMF'  AbmmmqMA     M   `MM.M    AbmmmqMA   .     `MM      MM        MM   Y  , 
`Mb.     MM   A'     VML    M     YMM   A'     VML  Mb     dM      MM        MM     ,M 
  `"bmmmdPY .AMA.   .AMMA..JML.    YM .AMA.   .AMMA.P"Ybmmd"     .JMML.    .JMMmmmmMMM   
---------------------------------------------------------------------------------------""")
            break
    else:
        print(f"""

`7MMMMMMq.`7MMMMMYMM  `7MMMMMMMq.  `7MMMMMYb.`7MMF' .MMMMbgd MMP""MM""YMM `7MMMMMYMM  
  MM   `MM. MM    `7    MM   `MM.   MM    `Yb. MM  ,MI    "Y P'   MM   `7   MM    `7  
  MM   ,M9  MM   d      MM   ,M9    MM     `Mb MM  `MMb.          MM        MM   d    
  MMmmdM9   MMmmMM      MMmmdM9     MM      MM MM    `YMMNq.      MM        MMmmMM    
  MM        MM   Y  ,   MM  YM.     MM     ,MP MM  .     `MM      MM        MM   Y  , 
  MM        MM     ,M   MM   `Mb.   MM    ,dP' MM  Mb     dM      MM        MM     ,M 
.JMML.    .JMMmmmmMMM .JMML. .JMM..JMMmmmdP' .JMML.P"Ybmmd"     .JMML.    .JMMmmmmMMM  

the word was {word}.""")    
        show_stage(len(wrong_letters))

    show_board(board, wrong_letters)  

def jugar_otra_vez():
    return input('for play try again press s if not press any key ')


def despedida():
    print('*' * 68)
    print('* thanks for play *')
    print('*' * 68)

def run():
        welcome()
        while True:
            hangman_game(words)
            if jugar_otra_vez() != "s": break

        despedida()         

if __name__ == '__main__':
    run()    