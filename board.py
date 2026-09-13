import pieces as pcs
import data as dta


class Board:
    def __init__(self):
        self.board = [[dta.EMPTY] * 8 for _ in range(8)]

    def get_square(self, x_val: int, y_val: int):
        return self.board[x_val][y_val]

    def set_square(self, rep, x_val: int, y_val: int):
        self.board[x_val][y_val] = rep

    @staticmethod
    def piece(col: str):
        match col:
            case "wP":
                return pcs.WhitePawn()
            case "bP":
                return pcs.BlackPawn()
            case "wB":
                return pcs.WhiteBishop()
            case "bB":
                return pcs.BlackBishop()
            case "wN":
                return pcs.WhiteKnight()
            case "bN":
                return pcs.BlackKnight()
            case "wR":
                return pcs.WhiteRook()
            case "bR":
                return pcs.BlackRook()
            case "wQ":
                return pcs.WhiteQueen()
            case "bQ":
                return pcs.BlackQueen()
            case "wK":
                return pcs.WhiteKing()
            case "bK":
                return pcs.BlackKing()

        return None

    def print_board(self):
        for i, row in enumerate(self.board):
            print(8 - i, end=": ")

            for j, col in enumerate(row):
                if col == dta.EMPTY:
                    print("  ", end=" ")
                else:
                    print(col.get_name(), end=" ")

            print("")

        print("    a  b  c  d  e  f  g  h")

    def put_pieces(self):
        for piece_name, squares in dta.get_white_pieces_map().items():
            for square in squares:
                x, y = square[0], square[1]
                self.board[x][y] = self.piece(piece_name)

        for piece_name, squares in dta.black_pieces_map.items():
            for square in squares:
                x, y = square[0], square[1]
                self.board[x][y] = self.piece(piece_name)
