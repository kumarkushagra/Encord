# Import dependencies
from encord import EncordUserClient
import os

# Authenticate with Encord. Replace <private_key_path> with the path to your private key
user_client = EncordUserClient.create_with_ssh_private_key(
    ssh_private_key_path="C:\\Users\\EIOT\\Downloads\\testing_key-private-key.txt"
    
)

# Specify the Dataset you want to upload your DICOM files to. Replace <dataset_hash> with the hash of your Dataset
dataset = user_client.get_dataset(
    "0739f4ef-b5e5-4e6d-896d-5d7c39845dfa"
)

# Directory containing the DICOM files

directory = 'C:/Users/EIOT/Desktop/dicom data/10532105 NASEEMA 55 Y F/RADIWMC001276278 Head AIIMS_DF_HeadRoutineSeq Adult/CT HeadSeq 5.0 H30s'  # Replace this with your directory path
file_paths = []

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_path = file_path.replace("\\", "/")  # Replace backslashes with forward slashes
        file_paths.append(file_path)





print(file_paths)


# # Add a DICOM series to the Dataset by specifying the file path to all files to include.
dataset.create_dicom_series(file_paths)
