import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Define the filename
filename = "add_item.json"

# Load existing items from the file, or create an empty list if the file doesn't exist
try:
    content = load_from_json_file(filename)
except FileNotFoundError:
    content = []

# Add new arguments to the list
for arg in sys.argv[1:]:  # Start from index 1 to skip the script name
    content.append(arg)

# Save the updated list to the JSON file
save_to_json_file(content, filename)
