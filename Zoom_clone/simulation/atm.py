import time
import random
from collections import deque

NUM_ATMS = 3  # Number of ATMs in the bank

class ATM:
    def __init__(self, atm_id):
        self.atm_id = atm_id
        self.withdrawal_queue = deque()
        self.waiting_queue = deque()
        self.current_customer = None

    def serve_customer(self):
        if self.current_customer is None:
            if self.withdrawal_queue:
                self.current_customer = self.withdrawal_queue.popleft()
            elif self.waiting_queue:
                self.current_customer = self.waiting_queue.popleft()
            else:
                print(f"ATM {self.atm_id}: No customers. Waiting for customers...")
                return

        customer_id, time_remaining = self.current_customer
        if time_remaining > 0:
            print(f"ATM {self.atm_id}: Customer {customer_id} is withdrawing. Time remaining: {time_remaining} minute(s).")
            time.sleep(1)
            time_remaining -= 1
            self.current_customer = (customer_id, time_remaining)
        else:
            print(f"ATM {self.atm_id}: Customer {customer_id} has finished the transaction.")
            self.current_customer = None

    def add_customer(self, customer_id):
        withdrawal_time = random.randint(1, 10)  # Random withdrawal time between 1 and 10 minutes
        self.withdrawal_queue.append((customer_id, withdrawal_time))
        print(f"Customer {customer_id} joined ATM {self.atm_id}. Withdrawal time: {withdrawal_time} minute(s).")

    def move_waiting_customer(self, waiting_atm):
        if self.waiting_queue:
            customer_id, _ = self.waiting_queue.popleft()
            waiting_atm.add_customer(customer_id)
            print(f"Customer {customer_id} moved from ATM {self.atm_id} to ATM {waiting_atm.atm_id}.")


def atm_simulation():
    atm_list = [ATM(i+1) for i in range(NUM_ATMS)]
    waiting_atm = atm_list[0]  # ATM to which waiting customers move

    customer_number = 1
    while customer_number <= 5:
        atm_index = (customer_number - 1) % NUM_ATMS
        atm_list[atm_index].add_customer(customer_number)
        customer_number += 1

        for atm in atm_list:
            atm.serve_customer()
            if atm.current_customer is None:
                atm.move_waiting_customer(waiting_atm)

        time.sleep(1)  # Sleep for 1 second to simulate the passage of time

# Run the ATM simulation
atm_simulation()
