import itertools
import random
import simpy

RANDOM_SEED = 42
NUM_DENTAL_CHAIRS = 4  # Number of dental chairs in the clinic
DENTAL_APPOINTMENT_TIME = 15  # Minutes it takes for a dental appointment
T_INTER = 20  # Create a patient every ~20 minutes
SIM_TIME = 120  # Simulation time in minutes

# Class representing the Dental Clinic
class DentalClinic:
    # Constructor
    def __init__(self, env, num_chairs, appointment_time):
        self.env = env
        self.dental_chairs = simpy.Resource(env, num_chairs)
        self.appointment_time = appointment_time

    def perform_dental_checkup(self, patient):
        # Simulate the time it takes for a dental checkup
        yield self.env.timeout(self.appointment_time)
        print(f"Dental clinic completed the checkup for {patient}.")

# Function representing a patient's actions
def patient(env, name, clinic):
    print(f'{name} arrives at the dental clinic at {env.now:.2f}.')
    with clinic.dental_chairs.request() as request:
        # Request a dental chair
        yield request

        print(f'{name} starts dental checkup at {env.now:.2f}.')
        # Simulate the process of a dental checkup
        yield env.process(clinic.perform_dental_checkup(name))

        print(f'{name} leaves the dental clinic at {env.now:.2f}.')

# Function to set up the simulation
def setup(env, num_chairs, appointment_time, t_inter):
    # Create the dental clinic instance
    dental_clinic = DentalClinic(env, num_chairs, appointment_time)

    # Use itertools.count() to generate patient names
    patient_count = itertools.count()

    # Create 3 initial patients
    for _ in range(3):
        env.process(patient(env, f'Patient {next(patient_count)}', dental_clinic))

    # Create more patients while the simulation is running
    while True:
        yield env.timeout(random.randint(t_inter - 5, t_inter + 5))
        env.process(patient(env, f'Patient {next(patient_count)}', dental_clinic))

# Setup and start the simulation
print('Dr.Strong Dental Clinic Simulation')
random.seed(RANDOM_SEED)  # Set random seed for reproducibility

# Create an environment and start the setup process
env = simpy.Environment()
env.process(setup(env, NUM_DENTAL_CHAIRS, DENTAL_APPOINTMENT_TIME, T_INTER))

# Run the simulation until SIM_TIME
env.run(until=SIM_TIME)
