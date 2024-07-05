from encord import EncordUserClient
import os

# Authenticate with Encord. Replace <private_key_path> with the path to your private key
user_client = EncordUserClient.create_with_ssh_private_key(
    ssh_private_key_path="C:\\Users\\EIOT\\Desktop\\KEY\\exportimportpublickey-private-key.txt"
)

# Specify the Dataset you want to upload your images to. Replace <dataset_hash> with the hash of your Dataset
dataset = user_client.get_dataset("b7a238f0-7375-4320-8a6f-153a58b5d160")  # Ensure the correct dataset ID is used

# CHANGE the local directory address
directory = "C:/Users/EIOT/Desktop/Encord/UPLOAD/Images/Single Image"

# Iterating through each video at a time
for filename in os.listdir(directory):
    # Check if the file is a video (you might need to adjust this depending on video file extensions)
    if filename.endswith((".jpg", ".jpeg", ".png")):  # Correct the condition to check for multiple extensions
        # Construct full file path
        file_path = os.path.join(directory, filename)
        # Upload the video to the Dataset
        dataset.upload_image(file_path)

