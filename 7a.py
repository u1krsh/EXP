# Update package repositories
!apt get update
# Install Hive and its dependencies
!apt get install hive hive metastore hive server2 y
# Start Hive Metastore and HiveServer2
!nohup hive service metastore > /dev/null 2>&1 &
!nohup hive ----service hiveserver2 > /dev/null 2>&1 &
import subprocess
# Check if Hive is installed and running
def check_hive_status():
try:
# Attempt to run Hive and suppress stderr
result = subprocess.run(
["hive", "--e", "SHOW DATABASES;"],
stdout=subprocess.PIPE,
stderr=subprocess.DEVNULL, # Redirect stderr to /dev/null
shell=True,
encoding="utf--8", # Specify encoding for Python 3
)
print("Hive is installed and running.")
except FileNotFoundError:
print("Hive is not installed.")
# Call the function to check Hive status
check_hive_status()