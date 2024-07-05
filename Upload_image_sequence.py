# Import dependencies
import glob
from msilib import Directory
from encord import EncordUserClient
import os

def list_image_files(directory):
    # Supported image extensions
    extensions = ['jpg', 'jpeg', 'png', 'bmp', 'gif', 'tiff', 'dcm']
    # List comprehension to get all image files
    return [file for ext in extensions for file in glob.glob(os.path.join(directory, f'*.{ext}'))]

# Authenticate with Encord. Replace <private_key_path> with the path to your private key
user_client = EncordUserClient.create_with_ssh_private_key(
    ssh_private_key_path="C:\\Users\\EIOT\\Desktop\\KEY\\exportimportpublickey-private-key.txt"
    )


# Specify the Dataset you want to upload your image sequence to. Replace <dataset_hash> with the hash of your Dataset
dataset = user_client.get_dataset(
    "b7a238f0-7375-4320-8a6f-153a58b5d160"
    )

# Create the image sequence. Include the paths of all images that are to be included in the image sequence. 
# The create_video flag must to be set to False
directory="C:/Users/EIOT/Desktop/Encord/UPLOAD/Images/image Sequence"
image_path_list=list_image_files(directory)
if len(image_path_list) !=0:
    dataset.create_image_group(image_path_list,create_video=True)
