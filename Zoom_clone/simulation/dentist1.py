import simpy
import random

from dental import Clinic
# Simulation parameters
NUM_DENTISTS = 2
NUM_ASSISTANTS = 3
NUM_PATIENTS = 10
SIM_TIME = 60  # Simulation time in minutes

class DentalClinic:
    def __init__(self, env, num_dentists, num_assistants):
        self.env = env
        self.dentist = simpy.Resource(env, capacity=num_dentists)
        self.assistant = simpy.Resource(env, capacity=num_assistants)
        self.patients = []

class Patient:
    def __init__(self, name, arrival_time, appointment_time):
        self.name = name
        self.arrival_time = arrival_time
        self.appointment_time = appointment_time
        self.start_dental_work_time = None
        self.leave_time = None

def patient_process(env, name, clinic, appointment_time):
    patient = clinic.patients[name]
    print(f"{name} arrives at the clinic at {env.now}")

    # Schedule appointment
    with clinic.dentist.request() as dentist_req, clinic.assistant.request() as assistant_req:
        yield dentist_req & assistant_req
        print(f"{name} schedules an appointment for {patient.appointment_time} and starts dental work at {env.now}")
        patient.start_dental_work_time = env.now
        yield env.timeout(random.randint(20, 30))  # Time taken for dental work

    # Leave the clinic
    patient.leave_time = env.now
    print(f"{name} leaves the clinic at {env.now}")

def clinic_process(env, num_dentists, num_assistants, num_patients):
    clinic = DentalClinic(env, num_dentists, num_assistants)

    # Generate patient appointments
    for i in range(num_patients):
        arrival_time = random.randint(0, SIM_TIME)
        appointment_time = arrival_time + random.randint(5, 15)
        patient_instance = Patient(f'Patient-{i}', arrival_time, appointment_time)
        clinic.patients.append(patient_instance)
        env.process(patient_process(env, patient_instance.name, clinic, patient_instance.appointment_time))

    # Run simulation until SIM_TIME
    yield env.timeout(SIM_TIME)



# Run the simulation
env = simpy.Environment()
env.process(clinic_process(env, NUM_DENTISTS, NUM_ASSISTANTS, NUM_PATIENTS))
env.run()

# Print patient details, arrival time, scheduled appointment, start of dental work, and leaving time
for patient in clinic_process:
    print(f"\nPatient: {patient.name}")
    print(f"  Arrival Time: {patient.arrival_time}")
    print(f"  Scheduled Appointment: {patient.appointment_time}")
    print(f"  Start of Dental Work: {patient.start_dental_work_time}")
    print(f"  Leaving Time: {patient.leave_time}")
