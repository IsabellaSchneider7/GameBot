class Game:
    players = []
    phrases = []
    pictures = []
    current_round = None
    current_player = None

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def start(self):
        self.current_round = 1
        self.current_player = self.players[0]

    def __next_turn(self):
        #self.current_player = self.players[self.current_round]
        self.current_round += 1

    def add_phrase(self, phrase):
        self.phrases.append(phrase)
        self.__next_turn()

    def add_picture(self, picture):
        self.pictures.append(picture)
        self.__next_turn()