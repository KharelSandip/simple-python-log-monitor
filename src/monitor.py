TODO - monitor.py (Log Scanner)

Goal:
Read logs and detect errors (basic monitoring system)

Tasks:
1. Define file paths:
   - input: logs/app.log
   - output: output/alerts.txt

2. Define alert keywords:
   - ERROR
   - CRITICAL
   - timeout
   - failed

3. Open log file for reading

4. Loop through each line

5. Check:
   - if line contains any keyword (case-insensitive)

6. If match:
   - write line to alerts.txt

7. Count number of alerts

8. Print summary:
   - total alerts found

Expected Output:
- alerts.txt contains only error lines
- terminal shows count of alerts

