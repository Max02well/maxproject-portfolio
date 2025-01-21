import simpy
import random

class Clinic:
    def __init__(self, env, num_dentists, num_assistants):
        self.dentist = simpy.Resource(env, capacity=num_dentists)
        self.assistant = simpy.Resource(env, capacity=num_assistants)
        self.appointments = []

class Patient:
    def __init__(self, name, arrival_time, appointment_time):
        self.name = name
        self.arrival_time = arrival_time
        self.appointment_time = appointment_time

def patient(env, name, clinic):
    print(f"{name} arrives at the clinic at {env.now}")

    with clinic.dentist.request() as req:
        yield req
        print(f"{name} sees the dentist at {env.now}")
        yield env.timeout(random.randint(20, 30))  # Time taken for dental work

    print(f"{name} leaves the clinic at {env.now}")
    clinic.appointments.remove(patient)

def clinic_process(env, num_dentists, num_assistants, num_patients):
    clinic = Clinic(env, num_dentists, num_assistants)

    # Generate patient appointments
    for i in range(num_patients):
        arrival_time = random.randint(0, SIM_TIME)
        appointment_time = arrival_time + random.randint(5, 15)
        patient_instance = Patient(f'Patient-{i}', arrival_time, appointment_time)
        clinic.appointments.append(patient)
        env.process(patient(env, patient, clinic))

    # Schedule patient arrivals based on their appointment times
    for patient_instance in sorted(clinic.appointments, key=lambda x: x.appointment_time):
        yield env.timeout(patient.arrival_time - env.now)
        env.process(patient(env, patient, clinic))

# Run the simulation
NUM_DENTISTS = 2
NUM_ASSISTANTS = 3
NUM_PATIENTS = 10
SIM_TIME = 60  # Simulation time in minutes

env = simpy.Environment()
env.process(clinic_process(env, NUM_DENTISTS, NUM_ASSISTANTS, NUM_PATIENTS))
env.run(until=SIM_TIME)
