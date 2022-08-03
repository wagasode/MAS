import random
import numpy as np
import matplotlib.pyplot as plt

# --- 複数Agentによるシミュレーション --- #
# --- 2次元平面で動作するAgent --- #

TIME_LIMIT = 100
AGENT_NUM  = 30
SEED       = 65535
H          = 0.01 
M          = 80

class Agent():
    def __init__(self, category):
        self.category = category
        self.x = 0
        self.y = 0
        self.vx = random.random()
        self.vy = random.random()
        self.m = M

    def calc_next_state(self):
        if self.category == 0:
            self.category0()
        else:
            print("不明なカテゴリーの検出\n")
    
    def category0(self):
        c0x = self.x
        c0y = self.y
        c0vx = self.vx
        c0vy = self.vy
        dvx, dvy = 0, 0
        for i in range(len(agents)):
            # --- Agentの移動を記述 --- #
            ax = agents[i].x
            ay = agents[i].y
            avx = agents[i].vx
            avy = agents[i].vy
            
            # --- 次のステップの速度を計算 --- #
            
            # --- 次のステップの位置を計算 --- #
            self.x += self.vx * H
            self.y += self.vy * H


    def put_state(self):
        print(f"category={self.category}, x={self.x}, y={self.y}")

def calc_next_time(agent_list):
    for i in range(len(agent_list)):
        agent_list[i].calc_next_state()
        if agent_list[i].category == 0:
            x_list_0.append(agent_list[i].x)
            y_list_0.append(agent_list[i].y)

random.seed(SEED)
# --- 全Agentのcategoryは0で統一 --- #
agents = [Agent(0) for i in range(AGENT_NUM)]

x_list_0  = []
y_list_0  = []

for t in range(TIME_LIMIT):
    calc_next_time(agents)

    plt.clf()
    plt.axis([-40, 40, -40, 40])
    plt.plot(x_list_0, y_list_0, ".")
    plt.pause(0.01)

    x_list_0.clear()
    y_list_0.clear()
plt.show()
