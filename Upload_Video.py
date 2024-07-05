
# Import dependencies
from encord import Dataset, EncordUserClient
import os

# Authenticate with Encord. Replace <private_key_path> with the path to your private key
user_client = EncordUserClient.create_with_ssh_private_key(
    ssh_private_key_path="C:\\Users\\EIOT\\Desktop\\KEY\\exportimportpublickey-private-key.txt"
    )

# Specify the Dataset you want to upload your video(s) to. Replace <dataset_hash> with the hash of your Dataset
dataset = user_client.get_dataset(
    "<dataset_ID>"
    )

# Upload the video to the Dataset by specifying the file path to the video

directory = "C:/Users/EIOT/Desktop/Encord/UPLOAD/Video"

# Iterating through each video at a time
for filename in os.listdir(directory):
    # Check if the file is a video (you might need to adjust this depending on video file extensions)
    if filename.endswith(".mp4" or ".AVI"): 
        # Construct full file path
        file_path = os.path.join(directory, filename)
        # Upload the video to the Dataset
        dataset.upload_video(file_path)

