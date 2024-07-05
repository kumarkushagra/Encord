# from encord import EncordUserClient
# import json
# import os

# def Export_json(key_path="C:\\Users\\EIOT\\Desktop\\KEY\\exportimportpublickey-private-key.txt", project_ID="396cb84f-0cc8-44af-9bb2-f490b77a7529", directory_path="C:/Users/EIOT/Desktop/Encord/EXPORT", file_name="annotation_data_with_signed_URL.json"):
#     # LOGIN with pvt key
#     user_client = EncordUserClient.create_with_ssh_private_key(ssh_private_key_path=key_path)
    
#     # Specify Project
#     project = user_client.get_project(project_ID)  # CHANGE PROJECT_ID HERE 

#     # Get label rows for the Project
#     label_rows = project.list_label_rows_v2()

#     # Specify directory and file name separately
#     directory_path = directory_path
#     file_name = file_name  # name
#     file_path = os.path.join(directory_path, file_name)

#     # Collect all label data into a list
#     label_data_list = []

#     for label_row in label_rows:
#         # Download label information
#         label_row.initialise_labels()
        
#         # Fetch data with signed URL
#         data_with_signed_url = project.get_data(label_row.data_hash, get_signed_url=True)
        
#         # Debug: print the structure of data_with_signed_url
#         print(f"Data with signed URL for {label_row.data_hash}: {data_with_signed_url}")

#         # Extract the signed URL correctly
#         signed_url = None
#         if isinstance(data_with_signed_url, dict):
#             signed_url_info = data_with_signed_url.get('signed_url')
#             if signed_url_info and isinstance(signed_url_info, dict):
#                 signed_url = signed_url_info.get('file_link')
#         elif isinstance(data_with_signed_url, tuple):
#             signed_url_info = data_with_signed_url[0]
#             if signed_url_info and isinstance(signed_url_info, dict):
#                 signed_url = signed_url_info.get('file_link')

#         # Convert label row to dict and add signed URL data
#         label_row_dict = label_row.to_encord_dict()
#         label_row_dict['signed_url'] = signed_url
        
#         # Add the JSON data to the list
#         label_data_list.append(label_row_dict)

#     # Write the JSON data list to the file
#     with open(file_path, 'w') as f:
#         json.dump(label_data_list, f, indent=4)

# Export_json()






from encord.client import EncordClientProject
from encord.constants.enums import DataType
from encord.exceptions import LabelRowError, WrongProjectTypeError
import json

# Replace these with your actual project ID and private key
PROJECT_ID = "278079d2-e943-4c37-9f6c-f65d90f09160"
PRIVATE_KEY = "C:\\Users\\EIOT\\Desktop\\KEY\\exportimportpublickey-private-key.txt"

def test_authentication(project_id, private_key):
    try:
        client = EncordClientProject.initialise(project_id, private_key)
        print("Authentication successful")
    except Exception as e:
        print(f"Authentication failed: {e}")


test_authentication(PROJECT_ID, PRIVATE_KEY)

