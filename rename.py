import os

folder_path = r"E:\demo test yolo data\x ray of scoliosis"

# সব image file গুলো নাও (bmp, png, jpg, jpeg)
extensions = ('.bmp', '.png', '.jpg', '.jpeg', '.BMP', '.PNG', '.JPG', '.JPEG')
files = [f for f in os.listdir(folder_path) if f.endswith(extensions)]
files.sort()  # alphabetical order এ sort করো

print(f"মোট {len(files)} টি ফাইল পাওয়া গেছে।")

# Rename করো
for i, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1]  # extension রাখো (.bmp, .png etc)
    new_name = f"SC{i}{ext}"
    
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    print(f"{filename}  →  {new_name}")

print("\n✅ সব ফাইল rename সম্পন্ন!")