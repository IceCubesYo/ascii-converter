import os
import re

# Specify the full path to the input file
input_file_path = r"C:\Users\lolit\Desktop\Dua Lipa\text fixer\input.txt"

# Open the input file and read its contents
with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Remove any non-ASCII characters from the text
text = re.sub(r'[^\x00-\x7F]+', '\n', text)

# Replace the replacement character with a space
text = text.replace('\uFFFD', ' ')

# Perform the character detection and line creation
new_text = ""
for char in text:
    if char == '\uFFFD':
        new_text += '\n'
    else:
        new_text += char

# Prompt the user for the output file name
output_name = input("Enter a name for the output file: ")

# Create the 'output' folder if it doesn't exist
output_folder = r"C:\Users\lolit\Desktop\Dua Lipa\text fixer\output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create a new file in the 'output' folder with the specified name
output_file_path = os.path.join(output_folder, output_name + ".txt")
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(new_text)

# Check if the output file was created
if os.path.exists(output_file_path):
    print(f"Output file saved as '{output_file_path}'.")
else:
    print("Error: Could not save output file.")