class Game:
    players = []
    phrases = []
    pictures = []
    current_round = None
    current_player = None
    ctx = None

    log = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def start(self, ctx):
        self.current_round = 1
        self.current_player = self.players[0]
        self.ctx = ctx

    def __next_turn(self):
        self.current_round += 1
        if self.can_continue():
            self.current_player = self.players[self.current_round-1]

    def add_phrase(self, phrase):
        self.phrases.append(phrase)
        self.__next_turn()
    def get_first_phrase(self):
        return self.phrases[0]
    def get_last_phrase(self):
        last = len(phrases)
        return self.phrases[last-1]
    def add_picture(self, picture):
        self.pictures.append(picture)
        self.__next_turn()

    def can_continue(self):
        kill = self.current_round > len(self.players)
        if kill:
            print(f'killing, round={self.current_round} players={len(self.players)}')
        return not kill

    def __find_medina(self, players):
        for p in players:
            if p.name == 'medini the genie':
                return p

    def add_to_log(self, thing):
        self.log.append(thing)