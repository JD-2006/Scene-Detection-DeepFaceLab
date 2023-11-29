import os
import imageio
from PIL import Image
import imagehash
import sys

def hash_difference(hash1, hash2):
    return bin(int(hash1, 16) ^ int(hash2, 16)).count('1')

def find_scene_changes(folder_path, threshold, num_changes):
    image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    if not image_files:
        print("No image files found in the specified folder.")
        return

    previous_hash = None
    scene_changes = []

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)
        current_hash = str(imagehash.phash(image))

        if previous_hash is not None:
            difference = hash_difference(previous_hash, current_hash)
            if difference > threshold:
                scene_changes.append(image_file)

        previous_hash = current_hash

    return scene_changes[:num_changes]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: Scene-Detect-Hash.py <threshold> <num_changes> <folder_path>")
        sys.exit(1)

    threshold = int(sys.argv[1])
    num_changes = int(sys.argv[2])
    folder_path = sys.argv[3]

    if not os.path.exists(folder_path):
        print(f"The specified folder '{folder_path}' does not exist.")
        sys.exit(1)

    scene_changes = find_scene_changes(folder_path, threshold, num_changes)

    if not scene_changes:
        print("No significant scene changes found.")
    else:
        print(f"{len(scene_changes)} most significant scene changes:")
        for scene_change in scene_changes:
            print(scene_change)
