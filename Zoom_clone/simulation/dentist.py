import simpy
import random

RANDOM_SEED = 42
NUM_DENTISTS = 2
NUM_ASSISTANTS = 3
NUM_RECEPTIONISTS = 1
TREATMENT_TIME_MEAN = 30
TREATMENT_TIME_STD = 10
ARRIVAL_INTERVAL_MEAN = 10
ARRIVAL_INTERVAL_STD = 5
APPOINTMENT_INTERVAL_MEAN = 60
APPOINTMENT_INTERVAL_STD = 15
SIM_TIME = 480  

class DentalClinic:
    #constructor
    def __init__(self, env, num_dentists, num_assistants, num_receptionists):
        self.env = env
        self.dentists = simpy.Resource(env, num_dentists)
        self.assistants = simpy.Resource(env, num_assistants)
        self.receptionists = simpy.Resource(env, num_receptionists)
        self.patients_processed = 0

    def patient_visit(self, patient):
        print(f"Patient {patient} arrives at the dental clinic at {self.env.now:.1f} minutes.")
        yield self.env.process(self.book_appointment(patient))
        yield self.env.process(self.check_in(patient))
        yield self.env.process(self.perform_treatment(patient))
        print(f"Patient {patient} leaves the dental clinic at {self.env.now:.1f} minutes.")
        self.patients_processed += 1

    def book_appointment(self, patient):
        print(f"Patient {patient} is booking an appointment.")
        yield self.env.timeout(random.normalvariate(APPOINTMENT_INTERVAL_MEAN, APPOINTMENT_INTERVAL_STD))

    def check_in(self, patient):
        print(f"Patient {patient} checks in at the reception.")
        yield self.env.timeout(random.normalvariate(5, 2))  # Check-in time

    def perform_treatment(self, patient):
        print(f"Patient {patient} starts treatment with the dentist at {self.env.now:.1f} minutes.")
        with self.dentists.request() as dentist_req:
            with self.assistants.request() as assistant_req:
                yield dentist_req & assistant_req
                treatment_time = random.normalvariate(TREATMENT_TIME_MEAN, TREATMENT_TIME_STD)
                yield self.env.timeout(treatment_time)
        print(f"Patient {patient} treatment completed.")

def patient_generator(env, clinic):
    patient_id = 0
    while True:
        yield env.timeout(max(0, random.normalvariate(ARRIVAL_INTERVAL_MEAN, ARRIVAL_INTERVAL_STD)))
        patient_id += 1
        env.process(clinic.patient_visit(patient_id))

def run_simulation():
    random.seed(RANDOM_SEED)
    env = simpy.Environment()
    clinic = DentalClinic(env, NUM_DENTISTS, NUM_ASSISTANTS, NUM_RECEPTIONISTS)
    env.process(patient_generator(env, clinic))
    env.run(until=SIM_TIME)
    return clinic

clinic = run_simulation()
print(f"Total patients processed: {clinic.patients_processed}")