import simpy
def Car(env):
    while True:
      print("Start parking at %d",env.now)
      parking_duration=5
      yield env.timeout(parking_duration)
#simulate the drive function/element
      print("Start driving at %d",env.now)
      trip_duration=2
      yield env.timeout(trip_duration)
    #Create the simulation environment
      env.simpy.Environment()
    #start the car process in the environment
      env.process(Car(env))
      env.run(until=20)