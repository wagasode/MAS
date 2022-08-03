import random
import numpy as np
import matplotlib.pyplot as plt

# --- 複数Agentによるシミュレーション --- #
# --- 2次元平面で動作するAgent --- #
# --- 2種類のAgentが相互作用する --- #

TIME_LIMIT = 200
AGENT_NUM  = 300
SEED       = 65535
R          = 0.2   # 近隣を規定する数値
DX         = 0.1
DY         = 0.1

class Agent():
    def __init__(self, category):
        self.category = category
        self.x = 0
        self.y = 0

    def calc_next_state(self):
        if self.category == 0:
            self.category0()
        elif self.category == 1:
            self.category1()
        else:
            print("不明なカテゴリーの検出\n")
    
    def category0(self):
        for i in range(len(agents)):
            if agents[i].category == 1:
                c0x = self.x
                c0y = self.y
                ax  = agents[i].x
                ay  = agents[i].y
                # --- category1のAgentが隣接しているなら、自身もcategory1に変化 --- #
                if ((c0x-ax)**2 + (c0y-ay)**2) < R:
                    self.category = 1
            else:
                self.x += (random.random() - 0.5)
                self.y += (random.random() - 0.5)

    def category1(self):
        self.x += DX
        self.y += DY

    def put_state(self):
        print(f"category={self.category}, x={self.x}, y={self.y}")

def calc_next_time(agent_list):
    for i in range(len(agent_list)):
        agent_list[i].calc_next_state()
        if agent_list[i].category == 0:
            x_list_0.append(agent_list[i].x)
            y_list_0.append(agent_list[i].y)
        elif agent_list[i].category == 1:
            x_list_1.append(agent_list[i].x)
            y_list_1.append(agent_list[i].y)

random.seed(SEED)
agents = [Agent(0) for i in range(AGENT_NUM)]
agents[0].category = 1
agents[0].x = -5
agents[0].y = -5

x_list_0, x_list_1 = [], []
y_list_0, y_list_1 = [], []

for t in range(TIME_LIMIT):
    calc_next_time(agents)

    plt.clf()
    plt.axis([-40, 40, -40, 40])
    plt.plot(x_list_0, y_list_0, ".")
    plt.plot(x_list_1, y_list_1, "+")
    plt.pause(0.01)

    x_list_0.clear()
    x_list_1.clear()
    y_list_0.clear()
    y_list_1.clear()
plt.show()
