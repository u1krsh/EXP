import os
import subprocess

# Install OpenJDK 8 (if not already installed)
java_installation_command = "apt-get install openjdk-8-jre-headless -qq > /dev/null"
subprocess.run(java_installation_command, shell=True, check=True)

# Download and extract Apache Pig
pig_download_url = "https://downloads.apache.org/pig/pig-0.17.0/pig-0.17.0.tar.gz"
subprocess.run(["wget", pig_download_url])
subprocess.run(["tar", "-xzf", "pig-0.17.0.tar.gz"])

# Set environment variables
os.environ['PIG_HOME'] = '/content/pig-0.17.0'
os.environ['PATH'] = os.environ['PIG_HOME'] + '/bin:' + os.environ['PATH']
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-8-openjdk-amd64'
os.environ['HADOOP_CONF_DIR'] = '/path/to/hadoop/config/dir'  # Adjust the path if necessary

# Define the Pig script file
pig_script_content = """
A = LOAD 'students.txt' AS (name:chararray, age:int, gpa:float);
B = GROUP A BY age;
C = FOREACH B GENERATE group, A.name;
DUMP C;
"""

# Save the Pig script to a file
with open('/content/students.pig', 'w') as pig_script_file:
    pig_script_file.write(pig_script_content)

input_data_path = '/content/students.txt'
pig_script_path = '/content/students.pig'
pig_command = f'pig -x local -f {pig_script_path} -param input_data={input_data_path}'

try:
    # Run the Pig script
    result = subprocess.run(
        pig_command,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Check if the exit status is 0 (success)
    if result.returncode == 0:
        print("Apache Pig script executed successfully.")
    else:
        print("Apache Pig script executed with errors. Check the output for details.")

    # Print the Pig script output
    print("Standard Output:")
    print(result.stdout)

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")