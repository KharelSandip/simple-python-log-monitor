import time
import random
from datetime import datetime

# Creating a file path of the file, where the logs are stored
Log_file = "logs/app.log"

# Creating a log messages
log_messages = [
    "INFO: User logged in",
    "INFO: Request processed successfully",
    "WARNING: High memory usage detected",
    "WARNING: Disk space running low",
    "ERROR: Database connection failed",
    "ERROR: Timeout while calling API",
]

# function to generate the logs
def generate_log():
    """This function will create a real, with a current time logs of a app."""
    # choice a random log from log_messages
    message = random.choice(log_messages)
    # The present formated date and time for each log, 
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # like a real log of a system
    log_line = f"{timestamp} - {message}"
    return log_line

# Run the loop till we mannully kill the app.py 
while True:
    
    log = generate_log()

    # Print to console
    print(log)

    # Append to file
    with open(Log_file, "a") as file:
        file.write(log + "\n")

    # Wait 2–3 seconds
    time.sleep(random.randint(2, 3))