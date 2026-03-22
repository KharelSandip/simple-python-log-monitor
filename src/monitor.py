import time

while True:
   # Creating file paths
   Logs_file = "logs/app.log"
   Alert_file = "output/alerts.txt"

   # Alert keywords to detect
   alert_keywords = ["ERROR", "CRITICAL", "timeout", "failed"]

   # Variable to count alerts
   alert_count = 0

   # Open alerts.txt in write mode as "w"
   with open(Alert_file, "w") as alerts:

      # Open app.log in read mode as "r"
      with open(Logs_file, "r") as log_file:

         # Read each line from the log file
         for line in log_file:

               # Check if any alert keyword is in the line
               # Also here, we are looping in the alert_keywords
               if any(keyword.lower() in line.lower() for keyword in alert_keywords):

                  # Write matching line into alerts.txt
                  alerts.write(line)

                  # Print that Alert
                  print(line)

                  # Increase alert count
                  alert_count += 1

   # Print total alerts found
   print(f"Total alerts found: {alert_count}")
   time.sleep(3)