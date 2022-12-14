import numpy as np
import matplotlib.pyplot as plt

# --- 単一Agentによるシミュレーション --- #
# --- 2次元平面で動作するAgent --- #

TIME_LIMIT = 100

class Agent():
    def __init__(self, category):
        self.category = category
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 1

    def calc_next_state(self):
        if self.category == 0:
            self.category0()
        else:
            print("不明なカテゴリーの検出")
    
    def category0(self):
        self.dx = self.reverse(self.dx)
        self.dy = self.reverse(self.dy)
        self.x += self.dx
        self.y += self.dy

    def reverse(self, i):
        if i == 0:
            return 1
        else:
            return 0
    def put_state(self):
        print(f"x={self.x}, y={self.y}")

def calc_next_time(agent_list):
    for i in range(len(agent_list)):
        agent_list[i].calc_next_state()
        agent_list[i].put_state()
        x_list.append(agent_list[i].x)
        y_list.append(agent_list[i].y)

agents = [Agent(0)]
x_list = []
y_list = []

for t in range(TIME_LIMIT):
    calc_next_time(agents)
    plt.clf()
    plt.axis([0, 60, 0, 60])
    plt.plot(x_list, y_list, ".")
    plt.pause(0.01)
    x_list.clear()
    y_list.clear()
plt.show()
