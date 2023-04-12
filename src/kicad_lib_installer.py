import os
import sys
import subprocess

# Get the repository URL from the command line argument
if len(sys.argv) < 2:
    print("Please provide a GitHub repository URL for a KiCAD library as a command line argument.")
    sys.exit(1)
repo_url = sys.argv[1]

# Get the user's home folder path
home_folder = os.path.expanduser("~")

# Clone the repository to the user's home folder
# Get the repository name from the URL and remove the .git extension
repo_name = repo_url.split("/")[-1].replace(".git", "")
# Construct the path to the repository in the user's home folder
repo_path = os.path.join(home_folder, repo_name)
# Run the git clone command to clone the repository
subprocess.run(["git", "clone", repo_url, repo_path])

# Install the libraries into KiCAD
# Construct the path to the KiCAD library folder in the user's home folder
kicad_lib_path = os.path.join(home_folder, "Documents", "KiCAD", "library")
# Search the cloned repository directory for all KiCAD symbol and footprint library files
for root, dirs, files in os.walk(os.path.join(repo_path, "library")):
    for file in files:
        # If the file is a KiCAD symbol or footprint library file, copy it to the KiCAD library folder
        if file.endswith(".lib"):
            subprocess.run(["cp", os.path.join(root, file), os.path.join(kicad_lib_path, file)])
        elif file.endswith(".pretty"):
            subprocess.run(["cp", "-r", os.path.join(root, file), os.path.join(kicad_lib_path, file)])
