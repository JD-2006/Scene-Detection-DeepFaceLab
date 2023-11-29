import cv2
import os
import sys

def calculate_frame_difference(frame1, frame2):
    # Convert frames to grayscale
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calculate absolute difference between frames
    diff = cv2.absdiff(gray1, gray2)

    # Threshold the difference image
    _, threshold_diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    return threshold_diff

def find_scene_changes(video_folder, num_changes):
    frame_files = sorted(os.listdir(video_folder))
    
    # Read the first frame
    prev_frame = cv2.imread(os.path.join(video_folder, frame_files[0]))

    scene_changes = []

    for frame_file in frame_files[1:]:
        # Read the current frame
        current_frame = cv2.imread(os.path.join(video_folder, frame_file))

        # Calculate frame difference
        diff = calculate_frame_difference(prev_frame, current_frame)

        # Count non-zero pixels in the difference image
        change_count = cv2.countNonZero(diff)

        # Store the file name and change count in a tuple
        scene_changes.append((os.path.basename(frame_file), change_count))

        # Update the previous frame for the next iteration
        prev_frame = current_frame

    # Rank frames based on their significance compared to neighbors
    ranked_changes = sorted(
        enumerate(scene_changes),
        key=lambda x: x[1][1],
        reverse=True
    )

    # Extract the top frames in alphabetical order
    top_frames = sorted(
        (frame_name for _, (frame_name, _) in ranked_changes[:num_changes]),
        key=lambda x: x.lower()
    )

    # Print the top frames with the most significant difference to neighbors
    print("\nTop Frames with Most Significant Difference to Neighbors:")
    for frame_name in top_frames:
        print(f"{frame_name}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: Scene-Detect-CV2.py <num_changes> <video_folder>")
        sys.exit(1)

    num_changes = int(sys.argv[1])
    video_folder = sys.argv[2]

    find_scene_changes(video_folder, num_changes)
