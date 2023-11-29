# Scene-Detection-DeepFaceLab
Scripts for DeepFaceLab, Xseg and similar projects for detecting possible significant scene changes to help choose frames for landmarking.

Scene-Detect-CV2.py script analyzes a folder of image frames extracted from a video, using frame differencing to identify significant scene changes. The script calculates the difference between consecutive frames, ranks them based on their significance, and prints the top frames with the most substantial differences to their neighbors in alphabetical order. The user can specify the number of significant frames to display as a command-line argument.

python Scene-Detect-CV2.py 10 "I:\DeepFaceLab_NVIDIA_up_to_RTX2080Ti\workspace\data_dst\aligned"


Scene-Detect-Hash.py analyzes a folder containing image frames, employing perceptual hashing to detect significant scene changes. It computes hash differences between consecutive frames and identifies frames with differences surpassing a specified threshold. The user can set the threshold, the number of significant changes to detect, and provide the path to the folder containing the image frames through command-line arguments. The script then outputs the filenames of the most significant scene changes, or a message if none are found.

python Scene-Detect-Hash.py 14 10 "I:\DeepFaceLab_NVIDIA_up_to_RTX2080Ti\workspace\data_dst\aligned"
