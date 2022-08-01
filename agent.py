import random as rnd
import numpy as np

class Agent:
    def __init__(self):
        self.point = 0.0
        self.strategy = None
        self.next_strategy = None
        self.neighbors_id = []

    def decide_next_strategy(self, agents):
        #--- Pairwise-Fermiモデル　によって次のゲームでの戦略を決定 ---#

        #--- 戦略決定時に参照する隣接Agent　をランダムに選択 ---#
        opponent_id = rnd.choice(self.neighbors_id)
        opponent = agents[opponent_id]

        if opponent.strategy != self.strategy and rnd.random() < 1/(1 + np.exp((self.point - opponent.point)/0.1)):
            self.next_strategy = opponent.strategy

    def update_strategy(self):
        self.strategy = self.next_strategy
