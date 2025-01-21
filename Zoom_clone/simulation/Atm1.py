import simpy
import random

RANDOM_SEED = 42
SIM_DURATION = 600
NUM_ATMS = 5
MAX_TIME_ATM = 600

class ATM:
    def __init__(self, env, name):
        self.env = env
        self.name = name
        self.queue = simpy.Resource(env, capacity=2)

def user(env, user_id, atm_list):
    print(f"User {user_id} starts using {atm_list[user_id % NUM_ATMS].name} at {env.now}")
    with atm_list[user_id % NUM_ATMS].queue.request() as req:
        yield req
        yield env.timeout(random.randint(1, MAX_TIME_ATM))
    print(f"User {user_id} finished at {atm_list[user_id % NUM_ATMS].name} at {env.now}")

    if env.now < SIM_DURATION:
        new_atm = (user_id % NUM_ATMS + 1) % NUM_ATMS
        print(f"User {user_id} moved from {atm_list[user_id % NUM_ATMS].name} to {atm_list[new_atm].name} at {env.now}")
        with atm_list[new_atm].queue.request() as req:
            yield req
            yield env.timeout(random.randint(1, MAX_TIME_ATM))
        print(f"User {user_id} finished at {atm_list[new_atm].name} at {env.now}")

# Setup and start the simulation
print('ATM Simulation')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Create ATMs
atm_list = [ATM(env, f"ATM-{i}") for i in range(NUM_ATMS)]

# Start processes and run
for i in range(10):
    env.process(user(env, i, atm_list))

env.run(until=SIM_DURATION)