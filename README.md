# 🖼️ Image Resizer Tool

A simple Python script that resizes multiple images to 600×600(default) pixels using `Tkinter` for file selection and `Pillow` for image processing.

---

## 📦 Features

- ✅ Select multiple images via a GUI dialog
- ✅ Resize images to 600×600 pixels
- ✅ Save them with `_resized` suffix
- ✅ Output stored in a `resized_images/` folder
- ✅ Keeps original format and extension

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/image-resizer-tool.git
cd image-resizer-tool
```

### 2. Install dependencies

Make sure you have Python 3 and install Pillow:

```bash
pip install Pillow
```

### 3. Run the script

```bash
python resize_images.py
```

A file dialog will open. Select the images you want to resize. The resized versions will be saved to the `resized_images/` directory.

---

## 🗂️ Output Structure

```
resized_images/
├── photo1_resized.jpg
├── photo2_resized.png
└── ...
```

---

## 🛠️ Customize

To change the target size, modify the `img_size` variable in the script:

```python
img_size = (600, 600)
```

---

## 📄 License

MIT – free to use, modify, and distribute.

---

Made with ❤️ by VR
