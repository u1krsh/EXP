!curl
sL https://deb.nodesource.com/setup_14.x | sudo E bash
!sudo apt
get install y nodejs
!npm install
g yarn
!yarn
version
!yarn init
y
!yarn add axios
!yarn start
!yarn start
import subprocess
import subprocess
# Define the Yarn command to install a package
# Define the Yarn command to install a package
package_name = "axios"
package_name = "axios"
yarn_command = f"yarn add {package_name}
yarn_command = f"yarn add {package_name}""
try:
try:
# Run the Yarn command using subprocess# Run the Yarn command using subprocess
subprocess.run(yarn_command, shell=True, check=True)subprocess.run(yarn_command, shell=True, check=True)
print(f"Successfully installed {package_name} using Yarn.")print(f"Successfully installed {package_name} using Yarn.")
except subprocess.CalledProcessError as e:
except subprocess.CalledProcessError as e:
print(f"Error: Yarn command failed wprint(f"Error: Yarn command failed with error code {e.returncode}.")ith error code {e.returncode}.")