# import os
# import re
# import shutil

# # Open the markdown file and read its content
# note_dir = "C:/Users/kosam/Documents/Workspace/- xhu_notes"
# target_file = rf'{note_dir}/2402_deeplearning_specialization.md'
# with open(target_file, 'r') as file:
#     content = file.read()

# # Find all image references in the markdown file
# image_refs = re.findall(r'/!/[.*?/]/((.*?)/)', content)

# for image_ref in image_refs:
#     # Get the image file name and its extension
#     image_name = os.path.basename(image_ref)
#     image_ext = os.path.splitext(image_name)[1]

#     new_image_ref = image_ref.replace('./', note_dir + '/')
#     print(new_image_ref)
#     # Create a subdirectory with the image extension (if it doesn't exist)
#     subdir = os.path.join(note_dir, "images", "2402_deeplearning_specialization")
#     os.makedirs(subdir, exist_ok=True)

#     # Move the image file to the subdirectory
#     new_path = os.path.join(subdir, image_name).replace("//", "/")
#     print(new_path)
#     shutil.copy(new_image_ref, new_path)

#     # Replace the image reference in the markdown file with the new path
#     new_path_remove = new_path.replace(note_dir + "/", "/./")
#     content = content.replace(image_ref, new_path_remove)

# # Write the updated content back to the markdown file
# with open(target_file, 'w') as file:
#     file.write(content)


# rename all files in the directory to lowercase
from pathlib import Path
import shutil

input_dir = r"C:\Users\kosam\Documents\Workspace\.tmp"
output_dir = r"C:\Users\kosam\Documents\Workspace\.tmp2"
images = Path(input_dir).rglob('*.png')

cutoff = 95
add_buff = 109 - cutoff

for image in images:
    image_index = image.name.split('-')[1].replace('.png', '')

    new_name = image.name.replace(image_index, str(int(image_index) + add_buff))
    shutil.move(image, Path(output_dir, new_name))


marker_File = r"C:/Users/kosam/Documents/Workspace/- xhu_notes/2404_ml_ops_specialization.md"
with open(marker_File, 'r') as file:
    content = file.read()

import re
# Find all image references in the markdown file
image_refs = re.findall(r'/!/[.*?/]/((.*?)/)', content)
