import os
import shutil

# --- CONFIGURATION ---
# Point this to your MINI dataset folder
# Example: r'C:\Users\mnha\Downloads\aerial-rec-scene\fmow_rgb_data\mini-dataset\MLRSNet_mini'
TARGET_DATASET = r'C:\Users\manha\Desktop\asse_project\data\fmow_sa' 

# Define the groupings
# We map specific folder names to "Super Classes"
MAPPINGS = {
    # --- URBAN (Man-made structures) ---
    'Urban': [
        'airport', 'airplane', 'baseball_diamond', 'basketball_court', 'bridge', 
        'building', 'bus_station', 'commercial_area', 'dense_residential', 
        'freeway', 'golf_course', 'ground_track_field', 'harbor', 'intersection', 
        'mobile_home_park', 'overpass', 'parking_lot', 'park', 'port', 
        'railway', 'railway_station', 'residential', 'runway', 'ship', 
        'sparce_residential', 'stadium', 'storage_tank', 'tennis_court', 
        'train_station', 'transportation', 'vehicle', 'dense_residential_area', 'harbor&port', 'industrial_area', 'parkway', 
        'roundabout', 'shipping_yard', 'sparse_residential_area', 
        'swimming_pool', 'transmission_tower', 'wind_turbine', 'airport_hangar', 'airport_terminal', 'border_checkpoint', 'bunker', 
        'casino', 'construction_site', 'dam', 'educational_institution', 
        'electric_substation', 'factory_or_powerplant', 'fire_station', 
        'gas_station', 'ghost_town', 'ground_transportation_station', 'helipad', 
        'hospital', 'impoverished_settlement', 'lighthouse', 'military_facility', 
        'multi_unit_residential', 'nuclear_powerplant', 'office_building', 
        'oil_or_gas_facility', 'parking_lot_or_garage', 'place_of_worship', 
        'police_station', 'post_office', 'prison', 'race_track', 'railway_bridge', 
        'recreational_facility', 'road_bridge', 'shopping_mall', 
        'single_unit_residential', 'space_facility', 'surface_mine', 'toll_booth', 
        'tunnel_opening', 'waste_disposal', 'water_tower', 
        'water_treatment_facility', 'wind_farm', 'zoo'
    ],
    
    # --- AGRICULTURE (Farming) ---
    'Agriculture': [
        'agricultural', 'chaparral', 'crop_field', 'farmland', 'field', 
        'meadow', 'orchard', 'terrace', 'vineyard', 'eroded_farmland', 'vegetable_greenhouse', 'aquaculture', 'barn', 'crop_field', 'nursery', 'orchard'
    ],
    
    # --- NATURE (Natural landscape) ---
    'Nature': [
        'beach', 'chaparral', 'cloud', 'desert', 'forest', 'grassland', 
        'island', 'lake', 'mountain', 'river', 'sea_ice', 'snowberg', 
        'swamp', 'wetland', 'water', 'bareland', 'lake_or_pond'
    ]
}

def group_folders():
    if not os.path.exists(TARGET_DATASET):
        print("Error: Target folder not found.")
        return

    print(f"Organizing: {TARGET_DATASET}")
    
    # Iterate through the 3 Super Classes
    for super_class, sub_classes in MAPPINGS.items():
        
        # 1. Create the Super Folder (e.g., "Urban")
        super_folder_path = os.path.join(TARGET_DATASET, super_class)
        if not os.path.exists(super_folder_path):
            os.makedirs(super_folder_path)
            
        # 2. Find and Move the sub-folders
        for sub_name in sub_classes:
            # We look for folders that verify loosely against the name
            # (e.g. matching "airport" in "airport_hangar" if exact match fails)
            
            current_path = os.path.join(TARGET_DATASET, sub_name)
            
            # If the specific folder exists (e.g., .../airport)
            if os.path.exists(current_path):
                # We move the *contents* of airport into Urban
                # OR we move the whole folder into Urban. 
                # Moving the whole folder is safer for traceability.
                
                new_path = os.path.join(super_folder_path, sub_name)
                
                try:
                    shutil.move(current_path, new_path)
                    print(f"  Moved '{sub_name}' -> '{super_class}'")
                except Exception as e:
                    print(f"  Error moving {sub_name}: {e}")

    print("\nOrganization Complete!")
    print("Check your folder. You should see Urban, Agriculture, and Nature.")

if __name__ == "__main__":
    group_folders()