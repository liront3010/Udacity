#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The first player to get 3 points, wins"""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    def __init__(self):
        self.my_move = random.choice(moves)
        self.their_move = random.choice(moves)

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Rock, paper, scissors? > ")
            choice = choice.lower()
            if choice in moves:
                return choice
            print('Invalid move! Try Again.')


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def learn(self, my_move, their_move):
        move_index = moves.index(self.my_move)
        if move_index + 1 >= len(moves):
            self.my_move = moves[0]
        else:
            self.my_move = moves[move_index + 1]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            self.p1_score += 1
            print("** PLAYER ONE WINS **")
        elif beats(move2, move1) is True:
            self.p2_score += 1
            print("** PLAYER TWO WINS **")
        else:
            print("** It is a TIE! **")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        while True:
            self.round += 1
            print(f"""\n=== Round: {self.round} ===""")
            self.play_round()
            print(f"""Score -  Player One: {self.p1_score} \
Player Two: { self.p2_score}""")
            if self.p1_score == 3:
                print("\n** PLAYER ONE WINS THE GAME! **")
                break
            elif self.p2_score == 3:
                print("\n** PLAYER TWO WINS THE GAME! **")
                break
        print(f"""Final score - Player One: {self.p1_score} \
Player Two: { self.p2_score}""")
        print("Game over!")


if __name__ == '__main__':
    players = [
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
