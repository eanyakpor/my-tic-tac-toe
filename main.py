import TicTacToe 
def main():
    name = input("Enter a name: ")
    marker = input("Enter a marker: ")

    game = TicTacToe.TicTacToe(name,marker)
    game.play_game() 
if __name__ == "__main__":
    main()
