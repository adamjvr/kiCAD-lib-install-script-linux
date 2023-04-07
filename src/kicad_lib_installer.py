import os
import urllib.request
import zipfile
import argparse

# parse the Github URL argument
parser = argparse.ArgumentParser(description='Install KiCAD footprint and symbol libraries from a Github repository.')
parser.add_argument('github_url', metavar='url', type=str, help='the Github URL for the KiCAD library')
args = parser.parse_args()

# define the library names and URLs
library_name = args.github_url.split("/")[-1].split(".")[0]
footprint_library_url = f'{args.github_url}/archive/master.zip'
symbol_library_url = f'{args.github_url}-symbols/archive/master.zip'

# define the path to the KiCAD footprint and symbol libraries folders
footprint_libraries_folder_path = f'/home/adam/.local/share/kicad/modules'
symbol_libraries_folder_path = f'/home/adam/.local/share/kicad/symbols'

# download and extract the footprint library zip file
urllib.request.urlretrieve(footprint_library_url, f"{library_name}.zip")
with zipfile.ZipFile(f"{library_name}.zip", 'r') as zip_ref:
    zip_ref.extractall(f"{library_name}")
    zip_ref.extractall(footprint_libraries_folder_path)
os.remove(f"{library_name}.zip")

# download and extract the symbol library zip file
urllib.request.urlretrieve(symbol_library_url, f"{library_name}_symbols.zip")
with zipfile.ZipFile(f"{library_name}_symbols.zip", 'r') as zip_ref:
    zip_ref.extractall(f"{library_name}-symbols")
    zip_ref.extractall(symbol_libraries_folder_path)
os.remove(f"{library_name}_symbols.zip")
