import random

class Tournament:

    def __init__(self, tournament_name, num_players, num_rounds):
        self.tournament_name = tournament_name
        self.player_list = []
        self.num_players = num_players
        self.num_rounds = num_rounds
        self.played_rounds = 0

    def get_tournament_name(self):
        return self.tournament_name
    
    def set_tournament_name(self, name):
        self.tournament_name = name

    def get_num_players(self):
        return self.num_players
    
    def set_num_players(self, num):
        self.num_players = num

    def get_num_rounds(self):
        return self.num_rounds
    
    def set_num_round(self, num):
        if num > 0 and num < 10:
            self.num_rounds = num
        else:
            print("Invalid number of rounds")

    def add_player(self, name, points=0):
        self.player_list.append((name, points))

    def delete_player(self, name):
        for player in self.player_list:
            if player[0] == name:
                self.player_list.remove(player)
                return
            
    def print_players(self):
        for player in self.player_list:
            print(player[0])

    def print_best_player(self):
        best_name = ""
        best_score = 0

        for player in self.player_list:
            if player[1] > best_score:
                best_name = player[0]
                best_score = player[1]

        print(f"Best player {best_name}/{best_score}")

    def generate_random_nums(self):
        num_1 = random.randint(0, len(self.player_list)-1)
        num_2 = ""

        while True:
            num_2 = random.randint(0, len(self.player_list)-1)

            if num_1 != num_2:
                break

        return (num_1, num_2)
    
    def start_round(self):
        if self.played_rounds >= self.num_rounds:
            print(f"All {self.num_rounds} have been played")
            return

        player_numbers = self.generate_random_nums();
        player_one = self.player_list[player_numbers[0]]
        player_two = self.player_list[player_numbers[1]]

        print(f"Round started between {player_one[0]} and {player_two[0]}")

        winner = random.choice([player_one, player_two])
        self.played_rounds += 1
        self.delete_player(winner[0])
        self.add_player(winner[0], (winner[1] + 1))

        print(f"Winner is {winner[0]}")

tournament = Tournament("test", 5, 7)
tournament.add_player("Zack")
tournament.add_player("Freddy")
tournament.add_player("Miles")
tournament.add_player("Ana")
tournament.add_player("Mia")

tournament.start_round()