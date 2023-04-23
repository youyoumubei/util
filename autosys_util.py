import subprocess
import re
from datetime import datetime

# Define the job name to retrieve
job_name = "my_autosys_job"

# Construct the command to query the Autosys database
command = f"autorep -J {job_name} -r"

# Execute the command and capture the output
output = subprocess.check_output(command, shell=True, text=True)

# Use regular expressions to extract the begin and end times from the output
begin_match = re.search(r"^\s*Start Time:\s+(.*)$", output, re.MULTILINE)
end_match = re.search(r"^\s*End Time:\s+(.*)$", output, re.MULTILINE)

# Convert the begin and end times to datetime objects
begin_time = datetime.strptime(begin_match.group(1), "%m/%d/%Y %I:%M:%S %p")
end_time = datetime.strptime(end_match.group(1), "%m/%d/%Y %I:%M:%S %p")

# Calculate the time difference between the begin and end times
time_difference = end_time - begin_time

# Print the results
print(f"Begin Time: {begin_time}")
print(f"End Time: {end_time}")
print(f"Time Difference: {time_difference}")
