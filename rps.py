#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random


moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass

class RockPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def move(self):
        return 'rock'

class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def move(self):
        m = None
        while m not in moves:
            m = input("Enter your choice (rock, paper, scissors): ")
            if m not in moves:
                print("Enter valid choice")
        return m


class ReflectPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.their_last_move = None

    def move(self):
        if self.their_last_move is not None:
            return self.their_last_move
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_last_move = their_move


class CyclePlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.my_last_move_idx = None

    def move(self):
        if self.my_last_move_idx is None:
            self.my_last_move_idx = random.choice(range(len(moves)))
        self.my_last_move_idx = (self.my_last_move_idx + 1) % len(moves)
        return moves[self.my_last_move_idx]

    def learn(self, my_move, their_move):
        self.my_last_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score = [0, 0]
        self.round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.score[0] += 1
        elif beats(move2, move1):
            self.score[1] += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Score: Player 1 {self.score[0]} - {self.score[1]} Player 2")
        print("="*17)

    def play_game(self):
        print("Game start!")
        while not self.check_game_done():
            self.round += 1
            print(f"Round {self.round}:")
            self.play_round()
        print("Game over!")
        self.announce_winner()

    def check_game_done(self):
        return self.score[0] == 3 or self.score[1] == 3

    def announce_winner(self):
        winner_score = max(self.score)
        loser_score = min(self.score)
        if self.score[0] > self.score[1]:
            winner = "Player 1"
            loser = "Player 2"
        else:
            winner = "Player 2"
            loser = "Player 1"
        print(f"{winner} win the game ({winner_score} - {loser_score})")


def reflect_vs_human():
    game = Game(ReflectPlayer(), HumanPlayer())
    game.play_game()


def cycle_vs_human():
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()


def random_vs_human():
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()


def random_vs_random():
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()


if __name__ == '__main__':
    # random_vs_random()
    # random_vs_human()
    # reflect_vs_human()
    cycle_vs_human()
