import numpy as np
import random as rnd
import networkx as nx
import pandas as pd
from agent import Agent

class Simulation:
    def __init__(self, population, average_degree):
        self.agents = self.__generate_agents(population, average_degree)
        self.initial_cooperators = self.__choose_initial_cooperators()

    def __generate_agents(self, population, average_degree):
        # --- Agentをリストに格納し、隣人AgentのIDをセットする --- #

        rearange_edges = average_degree//2
        network = nx.barabasi_albert_graph(population, rearange_edges)
        
        agents = [Agent() for id in range(population)]
        for index, focal in enumerate(agents):
            # --- list()が無いとgeneratorになってしまうので留意 --- #
            neighbors_id = list(network[index])
            for agent_id in neighbors_id:
                focal.neighbors_id.append(agent_id)

        return agents

    def __choose_initial_cooperators(self):
        # --- 1番目のgameでC戦略を取るAgentをランダムに選択 --- #
        population = len(self.agents)
        initial_cooperators = rnd.sample(range(population), k = int(population/2))

        return initial_cooperators

    def __initialize_strategy(self):
        # ---全Agentの戦略を初期化 ---#

        for index, focal in enumerate(self.agents):
            if index in self.initial_cooperators:
                focal.strategy = "C"
            else:
                focal.strategy = "D"

    def __count_payoff(self, Dg, Dr):
        # --- 利得表に基づき全Agentが獲得する利得を計算 --- #

        R = 1     # Reward
        S = -Dr   # Sucker
        T = 1+Dg  # Temptation
        P = 0     # Punishment

        for focal in self.agents:
            focal.point = 0.0
            for nb_id in focal.neighbors_id:
                neighbor = self.agents[nb_id]
                if focal.strategy == "C" and neighbor.strategy == "C":
                    focal.point += R
                elif focal.strategy == "C" and neighbor.strategy == "D":
                    focal.point += S
                elif focal.strategy == "D" and neighbor.strategy == "C":
                    focal.point += T
                elif focal.strategy == "D" and neighbor.strategy == "D":
                    focal.point += P

    def __update_strategy(self):
        # --- 全Agentに戦略を更新させる --- #
        
        for focal in self.agents:
            focal.decide_next_strategy(self.agents)
        for focal in self.agents:
            focal.update_strategy()

    def __count_fc(self):
        # --- C戦略Agentの割合を計算 --- #

        fc = len([agent for agent in self.agents if agent.strategy == "C"])/len(self.agents)

        return fc

    def __play_game(self, episode, Dg, Dr):
        # --- 1つのParameter設定で強調率が収束するまで計算を実施 --- #

        self.__initialize_strategy()
        initial_fc = self.__count_fc()
        fc_hist = [initial_fc]
        print(f"Episode:{episode}, Dr:{Dr:.1f}, Dg:{Dg:.1f}, Time: 0, Fc:{initial_fc:.3f}")

        tmax = 3000
        for t in range(tmax):
            self.__count_payoff(Dg, Dr)
            self.__update_strategy()
            fc = self.__count_fc()
            fc_hist.append(fc)
            print(f"Episode:{episode}, Dr:{Dr:.1f}, Dg:{Dg:.1f}, Time: 0, Fc:{initial_fc:.3f}")

            # --- 収束判定 --- #
            # --- 100回以上戦略更新され、過去100回のgameで得られた強調率の平均値と次のgameでの協調率の差が十分小さくなったら終了 --- #
            if (t >= 100 and np.absolute(np.mean(fc_hist[t-100:t-1]) - fc)/fc < 0.001) or t == tmax-1:
                # --- 過去100回分のgameで得られた協調率の平均値を計算 --- #
                fc_converged = np.mean(fc_hist[t-99:t]) 
                break

            # --- 全Agentの戦略が一致する状態に収束した場合、終了 --- #
            elif fc in [0, 1.0]:
                fc_converged = fc
                break

        print(f"Dr:{Dr:.1f}, Dg:{Dg:.1f}, Time:{t}, Fc:{fc_converged:.3f}")

        return fc_converged

    def run_one_episode(self, episode):
        # --- 全Parameter領域でplay_gameを実行し、計算結果をcsvに出力 --- #

        result = pd.DataFrame({"Dg": [], "Dr": [], "Fc": []})
        self.__choose_initial_cooperators()

        for Dr in np.arange(0, 1.1, 0.1):
            for Dg in np.arange(0, 1.1, 0.1):
                fc_converged = self.__play_game(episode, Dg, Dr)
                new_result = pd.DataFrame([[format(Dg, ".1f"), format(Dr, ".1f"), fc_converged]], columns = ["Dg", "Dr", "Fc"])
                result = result.append(new_result)
        result.to_csv(f"episode{episode}.csv")
