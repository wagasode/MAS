from simulation import Simulation
import random

def run():
    population = 10000 # Agent数
    average_degree = 8 # 社会networkの平均次数
    num_episode = 1    # simulationの試行回数
    simulation = Simulation(population, average_degree)
    
    for episode in range(num_episode):
        random.seed()
        simulation.run_one_episode(episode)

if __name__ == "__main__":
    run()
