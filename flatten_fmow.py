import os
import shutil

# --- CONFIGURATION ---
# Path to the folder shown in your screenshot (the one with hundreds of airport_airport folders)
SOURCE_ROOT = r'C:\Users\manha\Desktop\asse_project\data\fmow_sa'

# Where you want the clean, organized output
OUTPUT_ROOT = r'C:\Users\manha\Desktop\asse_project\data\fmow_sa_flattened'

def flatten_fmow_structure():
    if not os.path.exists(OUTPUT_ROOT):
        os.makedirs(OUTPUT_ROOT)

    print(f"Scanning {SOURCE_ROOT}...")

    # Walk through every single folder and subfolder
    for root, dirs, files in os.walk(SOURCE_ROOT):
        for filename in files:
            # 1. Filter: We only want images (skip .json, .txt)
            if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tif')):
                continue
            
            # 2. Filter: Skip 'msrgb' if you only want RGB
            if 'msrgb' in filename:
                continue

            # 3. Detect Category from the FOLDER name
            # The current folder name is likely "airport_airport_292_airport"
            current_folder_name = os.path.basename(root)
            
            # LOGIC: The category is usually the first part of these long names.
            # However, fMoW names are tricky. "airport_airport_292..." -> Category is likely "airport"
            # "single_unit_residential_..." -> Category is "single_unit_residential"
            
            # We can use the mapping logic again, or try to parse the string.
            # A safe bet for fMoW is to strip the numeric ID and the repeated suffix.
            # BUT, since you likely used my previous script to filter South Africa data, 
            # let's look at the filename itself which usually contains the category.
            
            # Strategy: Use the category found in the filename (which is cleaner)
            # Example filename: "airport_airport_292_0_rgb.jpg"
            
            parts = filename.split('_')
            # Pop 'rgb', pop numbers...
            clean_parts = []
            for p in parts:
                if p == 'rgb' or p.isdigit():
                    continue
                # Stop adding if we hit the ID number part (usually large numbers)
                if len(p) > 0 and p[0].isdigit(): 
                    break 
                clean_parts.append(p)
            
            # Reconstruct category name (e.g., "airport", "single_unit_residential")
            # Note: This simple parsing might need tweaking if filenames vary wildly.
            # A safer way relies on your previous "organize" script logic if that worked.
            
            # Alternative: Assume the parent folder (from your screenshot) starts with the category.
            # "airport_hangar_airport_hangar_6..." -> Starts with "airport_hangar"
            
            # Let's try to extract from the folder name in the screenshot
            folder_parts = current_folder_name.split('_')
            
            # fMoW folder naming convention is usually: [category]_[category]_[id]_[category]
            # e.g., airport_airport_292_airport
            # We want to grab everything BEFORE the first repetition or number.
            
            category_guess = []
            for part in folder_parts:
                if part.isdigit():
                    break
                category_guess.append(part)
            
            # If the category name repeats (airport_airport), take just the distinct sequence
            # Actually, fMoW often doubles names like "airport_airport".
            # The category is generally everything before the first digit.
            category_name = "_".join(category_guess)
            
            # Fix double naming (e.g., "airport_airport" -> "airport")
            # This is a bit hacky but works for fMoW's specific weirdness
            half_len = len(category_name) // 2
            if category_name[:half_len] == category_name[half_len+1:]: # +1 for underscore
                 category_name = category_name[:half_len]

            # 4. Create the Destination Category Folder
            dest_category_folder = os.path.join(OUTPUT_ROOT, category_name)
            if not os.path.exists(dest_category_folder):
                os.makedirs(dest_category_folder)

            # 5. Move/Copy the file
            # We rename it to include the unique ID so we don't overwrite generic names
            unique_name = f"{current_folder_name}_{filename}"
            
            src_path = os.path.join(root, filename)
            dst_path = os.path.join(dest_category_folder, unique_name)
            
            try:
                shutil.copy2(src_path, dst_path)
                # print(f"Copied to {category_name}") # Uncomment if you want spam
            except Exception as e:
                print(f"Error copying {filename}: {e}")

    print("Flattening Complete!")

if __name__ == "__main__":
    flatten_fmow_structure()