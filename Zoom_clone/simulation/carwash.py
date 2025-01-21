import simpy
import random

class Carwash:
    def __init__(self, env, num_servers):
        self.env = env
        self.servers = simpy.Resource(env, capacity=num_servers)

    def park_and_wash(self, car):
        with self.servers.request() as request:
            yield request
            print(f"{env.now}: Car {car} starts parking and washing.")
            yield env.timeout(random.randint(5, 15))  # Simulating washing time
            print(f"{env.now}: Car {car} finishes parking and washing.")

def car_generator(env, carwash):
    car_count = 0
    while True:
        yield env.timeout(random.expovariate(0.1))  # Random inter-arrival time
        car_count += 1
        env.process(carwash.park_and_wash(car_count))

env = simpy.Environment()
carwash = Carwash(env, num_servers=8)
env.process(car_generator(env, carwash))
env.run(until=50)  # Simulation time


 