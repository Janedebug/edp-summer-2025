from enum import Enum
from dataclasses import dataclass
channels = {'security': [], 'quality': [], 'condition': []}
class SensorType(Enum): HUMIDITY = 'humidity'; TEMPERATURE = 'temperature'; MOTION = 'motion'
class EventType(Enum):
    ANIMAL_ESCAPE = 'animal_escape'; TEMPERATURE_ALERT = 'temperature_alert'
    HUMIDITY_ALERT = 'humidity_alert'; CAGE_CLEANING_NEEDED = 'cage_cleaning_needed'
    ANIMAL_SICK = 'animal_sick'
@dataclass
class Event: name: EventType; payload: dict
class Sensor:
    def __init__(self, id, type, cage): self.id = id; self.type = type; self.cage = cage
    def emit(self, name, payload):
        e = Event(name, payload)
        ch = 'security' if name == EventType.ANIMAL_ESCAPE else \
             'condition' if name == EventType.ANIMAL_SICK else 'quality'
        channels[ch].append(e)
        print(f"[Sensor] {e}")
class Employee:
    def __init__(self, name): self.name = name
    def act(self, task): print(f"[{self.name}] {task}")
# Employees
guard = Employee("Guard John")
vet = Employee("Vet Mable")
cleaner = Employee("Cleaner Kraiven")
# Sensors
Sensor(1, SensorType.HUMIDITY, 'elephants').emit(EventType.HUMIDITY_ALERT, {'value': 85})
Sensor(2, SensorType.TEMPERATURE, 'tigers').emit(EventType.TEMPERATURE_ALERT, {'value': 40})
Sensor(3, SensorType.MOTION, 'elephants').emit(EventType.ANIMAL_ESCAPE, {'cage': 'elephants'})
# Dispatch
print("\n--- Dispatch ---")
tasks = {
    'security': lambda e: (guard.act("Catching & Reporting")),
    'quality': lambda e: (cleaner.act("Cleaning")),
    'condition': lambda e: (vet.act("Treating & Reporting")),
}
for ch, events in channels.items():
    for e in events:
        print(f"[{ch.title()}] {e}")
        tasks[ch](e)







