import os
import urllib.request
import zipfile

# define the library names and URLs
footprint_library_name = 'my_footprint_library'
footprint_library_url = 'https://example.com/my_footprint_library.zip'
symbol_library_name = 'my_symbol_library'
symbol_library_url = 'https://example.com/my_symbol_library.zip'

# define the path to the KiCAD footprint and symbol libraries folders
footprint_libraries_folder_path = f'/home/adam/.local/share/kicad/modules'
symbol_libraries_folder_path = f'/home/adam/.local/share/kicad/symbols'

# download and extract the footprint library zip file
urllib.request.urlretrieve(footprint_library_url, f"{footprint_library_name}.zip")
with zipfile.ZipFile(f"{footprint_library_name}.zip", 'r') as zip_ref:
    zip_ref.extractall(footprint_libraries_folder_path)
os.remove(f"{footprint_library_name}.zip")

# download and extract the symbol library zip file
urllib.request.urlretrieve(symbol_library_url, f"{symbol_library_name}.zip")
with zipfile.ZipFile(f"{symbol_library_name}.zip", 'r') as zip_ref:
    zip_ref.extractall(symbol_libraries_folder_path)
os.remove(f"{symbol_library_name}.zip")
