from PIL import Image
from tkinter import Tk, filedialog
import os

# Intializing Tkinter GUI without window
root = Tk()
root.withdraw()

# Dialogue for choosing multiple images
file_paths = filedialog.askopenfilenames(
    title="Choose images", filetypes=[("Image files", "*.jpg *.jpeg *.png")]
)

# Preffered image size in px
img_size = (600, 600)

# Folder for saving images
output_folder = "resized_images"
os.makedirs(output_folder, exist_ok=True)

# Looping through images
for path in file_paths:
    try:
        img = Image.open(path)
        img_resized = img.resize(img_size)
        img_resized.show()

        # Generate new name for image
        base_name = os.path.basename(path)
        name, ext = os.path.splitext(base_name)
        new_name = f"{name}_resized{ext}"
        save_path = os.path.join(output_folder, new_name)

        # Save image
        img_resized.save(save_path)
        print(f"Saved: {save_path}")

    except Exception as e:
        print(f"Error {path}: {e}")
