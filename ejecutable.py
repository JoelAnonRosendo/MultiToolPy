# This script installs the required dependencies for the project.
import subprocess
import sys

# List of packages to install
packages = ["requests", "cryptography"]

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install each package in the list
for package in packages:
    install(package)

# Install from requirements.txt
install('-r requirements.txt')

print("All dependencies installed successfully.")

# Now, let's execute the MultiToolPy_tkinter.py file
subprocess.run([sys.executable, 'MultiToolPy_tkinter.py'])