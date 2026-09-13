from game import Game
import data as dta


def valid_ending_square(square: str) -> bool:
    if len(square) != 2 or not square[0].isalpha() or not square[1].isdigit():
        return False

    valid_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    valid_numbers = {1, 2, 3, 4, 5, 6, 7, 8}

    if square[0].lower() not in valid_letters or (int(square[1])) not in valid_numbers:
        return False

    return True


def piece_change() -> bool:
    while True:
        response = input("Do you want to change your starting piece? (y/n): ")

        if response != "y" and response != "n":
            print("Invalid response")
            continue

        return response == "y"


def main():
    game = Game()
    game.put_pieces()

    while True:
        game.print_board()

        print("\n")

        print(game.get_curr_player() + " to move")

        valid_start, valid_end = False, False

        while not valid_start or not valid_end:

            while True:
                starting_square: str = str(input("Enter square of piece you'd like to move (ex: a1): "))

                if game.valid_starting_square(starting_square):
                    valid_start = True
                    break

                print("Invalid starting square, enter again")

            start_x, start_y = starting_square[0], starting_square[1]
            start_x, start_y = 8 - int(start_y), dta.col_map[start_x]

            while True:
                ending_square = input("Enter desired square to move it to (ex: a2): ")

                if not valid_ending_square(ending_square):
                    print("Invalid ending square")

                    if piece_change():
                        break
                    else:
                        continue

                end_x, end_y = ending_square[0], ending_square[1]
                end_x, end_y = 8 - int(end_y), dta.col_map[end_x]

                if game.valid_move(start_x, start_y, end_x, end_y):
                    if game.landing_on_enemy_pieces(end_x, end_y):
                        game.score_change_captures(end_x, end_y)
                    valid_end = True
                    break

                print("Invalid move")

                if piece_change():
                    break
                else:
                    continue

        temp = game.get_square(start_x, start_y)
        game.set_square(dta.EMPTY, start_x, start_y)
        game.set_square(temp, end_x, end_y)

        if temp.get_name()[1] == "P" and end_x == 0 and game.get_curr_player() == "White":
            while True:
                promote_to = input("Promote your pawn to a knight, bishop, rook, or queen  (ex: wN): ")
                if game.valid_promotion_piece(promote_to):
                    game.promote_pawn(promote_to, end_x, end_y)
                    break
                else:
                    print("Invalid argument")
        elif temp.get_name()[1] == "P" and end_x == 7 and game.get_curr_player() == "Black":
            while True:
                promote_to = input("Promote your pawn to a knight, bishop, rook, or queen  (ex: wN): ")
                if game.valid_promotion_piece(promote_to):
                    game.promote_pawn(promote_to, end_x, end_y)
                    break
                else:
                    print("Invalid argument")

        game.change_curr_player()


if __name__ == "__main__":
    main()

