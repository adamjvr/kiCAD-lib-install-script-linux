import os
import urllib.request
import zipfile
import argparse

# Parse the Github URL argument
parser = argparse.ArgumentParser(description='Install KiCAD footprint and symbol libraries from a Github repository.')
parser.add_argument('github_url', metavar='url', type=str, help='the Github URL for the KiCAD library')
args = parser.parse_args()

# Define the library names and URLs
library_name = args.github_url.split("/")[-1].split(".")[0]
footprint_library_url = f'{args.github_url}/archive/master.zip'
symbol_library_url = f'{args.github_url}-symbols/archive/master.zip'

# Define the path to the KiCAD footprint and symbol libraries folders
footprint_libraries_folder_path = f'/home/adam/.local/share/kicad/modules'
symbol_libraries_folder_path = f'/home/adam/.local/share/kicad/symbols'

# Download and extract the footprint library zip file
urllib.request.urlretrieve(footprint_library_url, f"{library_name}.zip")
with zipfile.ZipFile(f"{library_name}.zip", 'r') as zip_ref:
    # Extract the files to a temporary folder with the library name
    zip_ref.extractall(f"{library_name}")
    # Extract the files to the KiCAD footprint libraries folder
    zip_ref.extractall(footprint_libraries_folder_path)
# Remove the temporary zip file
os.remove(f"{library_name}.zip")

# Download and extract the symbol library zip file
urllib.request.urlretrieve(symbol_library_url, f"{library_name}_symbols.zip")
with zipfile.ZipFile(f"{library_name}_symbols.zip", 'r') as zip_ref:
    # Extract the files to a temporary folder with the library name + "-symbols"
    zip_ref.extractall(f"{library_name}-symbols")
    # Extract the files to the KiCAD symbol libraries folder
    zip_ref.extractall(symbol_libraries_folder_path)
# Remove the temporary zip file
os.remove(f"{library_name}_symbols.zip")
