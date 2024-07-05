from encord import Dataset, EncordUserClient
from encord.orm.dataset import StorageLocation
import os
import glob

# Authenticate with Encord. Replace <private_key_path> with the path to your private key

def Authenticate(key_path="C:\\Users\\EIOT\\Desktop\\KEY\\exportimportpublickey-private-key.txt"):
    user_client = EncordUserClient.create_with_ssh_private_key(
        ssh_private_key_path=key_path
        )
    return user_client

def Create_dataset(key_path,name_of_dataset):
    user_client= Authenticate() #default case is set to PVT key
    # DATASET CREATION (in encord)
    dataset_title = input("Enter the name of the dataset: ")
    dataset = user_client.create_dataset(dataset_title, StorageLocation.CORD_STORAGE)
    dataset_id = dataset.dataset_hash
    print(dataset_id)  #OPTIONAL PRINT STATEMENT
    return dataset_id #optional


def select_dataset(dataset_ID="b7a238f0-7375-4320-8a6f-153a58b5d160"):
    user_client = Authenticate()
    return user_client.get_dataset(dataset_ID)  # Ensure the correct dataset ID is used


def Upload_Single_image(dataset_ID,directory):
    dataset = select_dataset(dataset_ID)
    # Iterating through each video at a time
    for filename in os.listdir(directory):
        # Check if the file is a video (you might need to adjust this depending on video file extensions)
        if filename.endswith((".jpg", ".jpeg", ".png")):  # Correct the condition to check for multiple extensions
            # Construct full file path
            file_path = os.path.join(directory, filename)
            # Upload the video to the Dataset
            dataset.upload_image(file_path)

# CREATES A LIST OF IMAGES & dicomIN A GIVEN DIRECTORY
def list_image_files(directory):
    # Supported image extensions
    extensions = ['jpg', 'jpeg', 'png', 'bmp', 'gif', 'tiff']
    # List comprehension to get all image files
    return [file for ext in extensions for file in glob.glob(os.path.join(directory, f'*.{ext}'))]

def Upload_Group_image(dataset_ID,directory):
    dataset = select_dataset(dataset_ID)
    image_path_list = list_image_files(directory)
    if len(image_path_list) !=0:
        dataset.create_image_group(image_path_list,create_video=False)

def Uplead_Sequence_image(dataset_ID,directory):
    dataset = select_dataset(dataset_ID)
    image_path_list = list_image_files(directory)
    if len(image_path_list) !=0:
        dataset.create_image_group(image_path_list,create_video=True)


def Upload_Video(dataset_ID,directory):
    dataset = select_dataset(dataset_ID)
    # Iterating through each video at a time
    for filename in os.listdir(directory):
        # Check if the file is a video (you might need to adjust this depending on video file extensions)
        if filename.endswith(".mp4" or ".AVI"): 
            # Construct full file path
            file_path = os.path.join(directory, filename)
            # Upload the video to the Dataset
            dataset.upload_video(file_path)

def Upload_DICOM(dataset_ID,directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_path = file_path.replace("\\", "/")  # Replace backslashes with forward slashes
            file_paths.append(file_path)


Authenticate()
select_dataset("278079d2-e943-4c37-9f6c-f65d90f09160")

directory = 'C:/Users/EIOT/Desktop/54879843 Doe Pierre/54879843 CRANEPOLYGONE/CT Crane APC'  # Replace this with your directory path
Upload_DICOM("278079d2-e943-4c37-9f6c-f65d90f09160",directory)



print("Done")