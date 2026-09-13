## 1) Board Class

## 2) Pieces

## 3) Turns (White, Black)

## 4) Move Pieces on each turn

## 5) Move validation

## 6) Piece Capturing

## 7) "Check" logic

## 8) Checkmate logic

## 9) Point system (how many of other colors pieces you captured in value terms)

## 9) Castling, En-passant, pawn first-move

## 10) Pawn-promotion

## 11) GUI

## 12) local play against a bot

## 13) inter-computer play against another person

## 14) Make object-oriented


from board import Board
import pieces as pcs
import data as dta


class Game:
    def __init__(self):
        self.board = Board()
        self.white_score = 0
        self.black_score = 0
        self.curr_player = "White"

    def get_square(self, x_val: int, y_val: int):
        return self.board.get_square(x_val, y_val)

    def set_square(self, rep, x_val: int, y_val: int):
        self.board.set_square(rep, x_val, y_val)

    def get_curr_player(self) -> str:
        return self.curr_player

    def change_curr_player(self):
        self.curr_player = "Black" if self.curr_player == "White" else "White"

    def print_board(self):
        self.board.print_board()
        if self.white_score > self.black_score:
            print(f"White +{self.white_score - self.black_score}")
        elif self.white_score < self.black_score:
            print(f"Black +{self.black_score - self.white_score}")

    def put_pieces(self):
        self.board.put_pieces()

    def is_empty(self, x_val: int, y_val: int) -> bool:
        return self.get_square(x_val, y_val) == dta.EMPTY

    def landing_on_own_pieces(self, end_x: int, end_y: int) -> bool:
        if self.is_empty(end_x, end_y):
            return False

        if ((self.get_square(end_x, end_y).get_name()[0] == "w" and self.get_curr_player() == "White")
                or (self.get_square(end_x, end_y).get_name()[0] == "b" and self.get_curr_player() == "Black")):
            return True

        return False

    def landing_on_enemy_pieces(self, end_x: int, end_y: int) -> bool:
        if self.is_empty(end_x, end_y):
            return False

        if ((self.get_square(end_x, end_y).get_name()[0] == "w" and self.get_curr_player() == "Black")
                or (self.get_square(end_x, end_y).get_name()[0] == "b" and self.get_curr_player() == "White")):
            return True

        return False

    def valid_pawn_move(self, start_x: int, start_y: int, end_x: int, end_y: int) -> bool:
        if self.get_curr_player() == "White":
            if start_x == 6 and start_y == end_y and end_x == start_x - 2:
                if self.is_empty(start_x - 1, start_y) and self.is_empty(end_x, start_y):
                    return True
                return False

            if start_y == end_y and end_x == start_x - 1:
                # Straight-ahead pawn moves can only go to an empty square --
                # pawns can't capture (own or enemy) by moving straight.
                return self.is_empty(end_x, end_y)

            if end_x == start_x - 1 and abs(start_y - end_y) == 1:
                return self.landing_on_enemy_pieces(end_x, end_y)
        else:
            if start_x == 1 and start_y == end_y and end_x == start_x + 2:
                if self.is_empty(start_x + 1, start_y) and self.is_empty(end_x, start_y):
                    return True
                return False

            if start_y == end_y and end_x == start_x + 1:
                return self.is_empty(end_x, end_y)

            if end_x == start_x + 1 and abs(start_y - end_y) == 1:
                return self.landing_on_enemy_pieces(end_x, end_y)

        return False

    def valid_king_move(self, start_x: int, start_y: int, end_x: int, end_y: int) -> bool:
        if abs(end_x - start_x) <= 1 and abs(end_y - start_y) <= 1:
            if not self.landing_on_own_pieces(end_x, end_y):
                return True

        return False

    def valid_queen_move(self, start_x: int, start_y: int, end_x: int, end_y: int) -> bool:
        if start_x == end_x or start_y == end_y:
            return self.valid_rook_move(start_x, start_y, end_x, end_y)

        return self.valid_bishop_move(start_x, start_y, end_x, end_y)

    def valid_rook_move(self, start_x: int, start_y: int, end_x: int, end_y: int) -> bool:
        if start_x == end_x:
            iter_y = start_y + 1 if start_y < end_y else start_y - 1

            while iter_y != end_y:
                if not self.is_empty(start_x, iter_y):
                    return False

                iter_y = iter_y + 1 if iter_y < end_y else iter_y - 1

            return not self.landing_on_own_pieces(end_x, end_y)

        elif start_y == end_y:
            iter_x = start_x + 1 if start_x < end_x else start_x - 1

            while iter_x != end_x:
                if not self.is_empty(iter_x, end_y):
                    return False

                iter_x = iter_x + 1 if iter_x < end_x else iter_x - 1

            return not self.landing_on_own_pieces(end_x, end_y)

        else:
            return False

    def valid_bishop_move(self, start_x: int, start_y: int, end_x: int, end_y: int) -> bool:
        if abs(end_x - start_x) == abs(end_y - start_y):
            iter_x = start_x + 1 if start_x < end_x else start_x - 1
            iter_y = start_y + 1 if start_y < end_y else start_y - 1

            while iter_x != end_x and iter_y != end_y:
                if not self.is_empty(iter_x, iter_y):
                    return False

                iter_x = iter_x - 1 if iter_x > end_x else iter_x + 1
                iter_y = iter_y - 1 if iter_y > end_y else iter_y + 1

            return not self.landing_on_own_pieces(end_x, end_y)

        return False

    def valid_knight_move(self, start_x: int, start_y: int, end_x: int, end_y: int) -> bool:
        if (abs(end_x - start_x) == 2 and abs(end_y - start_y) == 1
                or abs(end_x - start_x) == 1 and abs(end_y - start_y) == 2):
            return not self.landing_on_own_pieces(end_x, end_y)

        return False

    def valid_move(self, start_x: int, start_y: int, end_x: int, end_y: int) -> bool:
        if start_x == end_x and start_y == end_y:
            return False

        if self.is_empty(start_x, start_y):
            return False

        piece_name = self.get_square(start_x, start_y).get_name()

        match piece_name:
            case "wP" | "bP":
                return self.valid_pawn_move(start_x, start_y, end_x, end_y)
            case "wN" | "bN":
                return self.valid_knight_move(start_x, start_y, end_x, end_y)
            case "wB" | "bB":
                return self.valid_bishop_move(start_x, start_y, end_x, end_y)
            case "wR" | "bR":
                return self.valid_rook_move(start_x, start_y, end_x, end_y)
            case "wQ" | "bQ":
                return self.valid_queen_move(start_x, start_y, end_x, end_y)
            case "wK" | "bK":
                return self.valid_king_move(start_x, start_y, end_x, end_y)

        return None

    def valid_starting_square(self, square: str) -> bool:
        if len(square) != 2 or not square[0].isalpha() or not square[1].isdigit():
            return False

        valid_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
        valid_numbers = {1, 2, 3, 4, 5, 6, 7, 8}

        if square[0].lower() not in valid_letters or (int(square[1])) not in valid_numbers:
            return False

        x_val, y_val = 8 - int(square[1]), dta.col_map[square[0]]

        if self.is_empty(x_val, y_val):
            return False

        if self.get_square(x_val, y_val).get_name()[0] != self.get_curr_player()[0].lower():
            return False

        return True

    def promote_pawn(self, piece, x, y):
        promoted_from_name = self.get_square(x, y).get_name()

        if self.get_curr_player() == "White":
            self.white_score += dta.name_to_value_map[piece] - dta.name_to_value_map[promoted_from_name]
        else:
            self.black_score += dta.name_to_value_map[piece] - dta.name_to_value_map[promoted_from_name]

        self.set_square(self.board.piece(piece), x, y)

    def score_change_captures(self, x_val: int, y_val: int):
        if self.curr_player == "White":
            self.white_score += self.board.get_square(x_val, y_val).get_value()
        else:
            self.black_score += self.board.get_square(x_val, y_val).get_value()

    def valid_promotion_piece(self, promote_to: str) -> bool:
        if self.get_curr_player() == "White":
            return True if (
                        promote_to == "wQ" or promote_to == "wR" or promote_to == "wN" or promote_to == "wB") else False

        return True if (promote_to == "bQ" or promote_to == "bR" or promote_to == "bN" or promote_to == "bB") else False

