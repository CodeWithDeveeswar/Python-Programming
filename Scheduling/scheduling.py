# Scheduling using while loop is not recommended
# While loop scheduling causes high CPU usage
# Not recommended for real-time scheduling
# Inefficient scheduling method
# Not suitable for real-world app

import time
from datetime import datetime

def task():
    # This is the code that runs every 2 minutes
    with open("Scheduling/time_log.txt", "a") as f:
        f.write(f"Script ran at: {datetime.now()}\n")
    print(f"Task ran at: {datetime.now()}")

# Run forever
while True:
    task()
    time.sleep(30)