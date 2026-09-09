class WhiteKing:
    def __init__(self):
        self.name = "wK"
        self.has_moved = False

    def get_name(self):
        return self.name

    def has_moved(self):
        return self.has_moved

    def move_toggle(self):
        self.has_moved = True


class BlackKing:
    def __init__(self):
        self.name = "bK"
        self.has_moved = False

    def get_name(self):
        return self.name

    def has_moved(self):
        return self.has_moved

    def move_toggle(self):
        self.has_moved = True


class WhiteQueen:
    def __init__(self):
        self.name = "wQ"
        self.value = 9

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value


class BlackQueen:
    def __init__(self):
        self.name = "bQ"
        self.value = 9

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value


class WhiteRook:
    def __init__(self):
        self.name = "wR"
        self.has_moved = False
        self.value = 5

    def get_name(self):
        return self.name

    def has_moved(self):
        return self.has_moved

    def move_toggle(self):
        self.has_moved = True

    def get_value(self):
        return self.value


class BlackRook:
    def __init__(self):
        self.name = "bR"
        self.has_moved = False
        self.value = 5

    def get_name(self):
        return self.name

    def has_moved(self):
        return self.has_moved

    def move_toggle(self):
        self.has_moved = True

    def get_value(self):
        return self.value


class WhiteBishop:
    def __init__(self):
        self.name = "bB"
        self.value = 3

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value


class BlackBishop:
    def __init__(self):
        self.name = "bB"
        self.value = 3

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value


class WhiteKnight:
    def __init__(self):
        self.name = "wN"
        self.value = 3

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value


class BlackKnight:
    def __init__(self):
        self.name = "bN"
        self.value = 3

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

class WhitePawn:
    def __init__(self):
        self.name = "bP"
        self.value = 1

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value


class BlackPawn:
    def __init__(self):
        self.name = "wP"
        self.value = 1

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value
