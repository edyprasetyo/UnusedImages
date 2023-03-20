import pandas as pd
import os

cshtml_folder = r'D:\GitProject\Unicorn\UnicornWeb\Unicorn'
cshtml_contents = []
for subdir, _, files in os.walk(cshtml_folder):
    for file in files:
        if file.endswith('.cshtml') or file.endswith('.cs') or file.endswith('.js') or file.endswith('.css') or file.endswith('.html'):
            with open(os.path.join(subdir, file), 'r', encoding='latin-1') as f:
                content = f.read()
                cshtml_contents.append(content)

image_folder = r'D:\GitProject\Unicorn\UnicornWeb\Unicorn\Content'
image_files = []
image_files_path = []
for subdir, _, files in os.walk(image_folder):
    for file in files:
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
            image_files.append(file)
            image_files_path.append(os.path.join(subdir, file))

unused_image_files = []
unused_image_files_path = []
for image_file in image_files:
    if image_file not in str(cshtml_contents):
        unused_image_files.append(image_file)
        unused_image_files_path.append(
            image_files_path[image_files.index(image_file)])


outputFolder = os.path.dirname(os.path.abspath(__file__)) + '\\unused_images'
if os.path.exists(outputFolder):
    os.system('rmdir /s /q "{}"'.format(outputFolder))

# create output folder
os.system('mkdir "{}"'.format(outputFolder))

for image_path in unused_image_files_path:
    os.system(f'copy "{image_path}" "{outputFolder}" > NUL')

total_size = 0
for image_path in unused_image_files_path:
    total_size += os.path.getsize(image_path)

total_size_mb = total_size / (1024 * 1024)

print(f"Total size: {total_size_mb:.2f} MB")

df = pd.DataFrame({'Image Name': unused_image_files,
                  'Image Path': unused_image_files_path})
df.to_csv('unused_images.csv', index=False)
