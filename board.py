from pieces import WhiteKing, WhiteQueen, WhiteRook, WhiteBishop, WhiteKnight, WhitePawn
from pieces import BlackKing, BlackQueen, BlackRook, BlackBishop, BlackKnight, BlackPawn

class Board:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]

        self.white_pieces_map = {
            "wP" : [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
            "wN": [(7, 1), (7, 6)],
            "wB": [(7, 2), (7, 5)],
            "wR": [(7, 0), (7, 7)],
            "wQ": [(7, 3)],
            "wK": [(7, 4)]
        }
        self.black_pieces_map = {
            "wP": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
            "bN": [(0, 1), (0, 6)],
            "bB": [(0, 2), (0, 5)],
            "bR": [(0, 0), (0, 7)],
            "bQ": [(0, 3)],
            "bK": [(0, 4)]
        }

    def get_white_pieces_map(self):
        return self.white_pieces_map

    def get_black_pieces_map(self):
        return self.black_pieces_map


    def get_square(self, x_val: int, y_val: int) -> str:
        return self.board[x_val][y_val]


    def set_square(self, rep, x_val: int, y_val: int):
        self.board[x_val][y_val] = rep

    @staticmethod
    def piece(col: str):
        match col:
            case "wP":
                return WhitePawn()
            case "bP":
                return BlackPawn()
            case "wB":
                return WhiteBishop()
            case "bB":
                return BlackBishop()
            case "wN":
                return WhiteKnight()
            case "bN":
                return BlackKnight()
            case "wR":
                return WhiteRook()
            case "bR":
                return BlackRook()
            case "wQ":
                return WhiteQueen()
            case "bQ":
                return BlackQueen()
            case "wK":
                return WhiteKing()
            case "bK":
                return BlackKing()

        return None

    def print_board(self):
        for i, row in enumerate(self.board):
            print(8 - i, end=": ")

            for j, col in enumerate(row):
                if col == "  ":
                    print("  ", end = " ")
                else:
                    print(col.get_name(), end = " ")

            print("")

        print("    a  b  c  d  e  f  g  h")


    def put_pieces(self):
        for piece_name, squares in self.white_pieces_map.items():
            for square in squares:
                x, y = square[0], square[1]
                self.board[x][y] = self.piece(piece_name)

        for piece_name, squares in self.black_pieces_map.items():
            for square in squares:
                x, y = square[0], square[1]
                self.board[x][y] = self.piece(piece_name)
