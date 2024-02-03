import threading
import time

def participant(name):
    for _ in range(5):
        print(f"{name} is running")
        time.sleep(1)
    print(f"{name} finished the race!")

participants = ["King", "Queen", "Warking", "Soldier"]

threads = []
for name in participants:
    thread = threading.Thread(target=participant, args=(name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Race finished")
