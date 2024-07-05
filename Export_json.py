from encord import EncordUserClient
import json
import os
def Export_json(key_path="C:\\Users\\EIOT\\Desktop\\KEY\\exportimportpublickey-private-key.txt",project_ID="396cb84f-0cc8-44af-9bb2-f490b77a7529",directory_path="C:/Users/EIOT/Desktop/Encord/EXPORT",file_name="annotation_data.json"):
    # LOGIN with pvt key
    user_client = EncordUserClient.create_with_ssh_private_key(
        ssh_private_key_path=key_path)
    # Specify Project
    project = user_client.get_project(project_ID)  # CHANGE PROJECT_ID HERE 

    # Get label rows for the Project
    label_rows = project.list_label_rows_v2()

    # Specify directory and file name separately
    directory_path = directory_path
    file_name = file_name  # name
    file_path = os.path.join(directory_path, file_name)

    # Collect all label data into a list
    label_data_list = []

    for label_row in label_rows:
        # Download label information
        label_row.initialise_labels()
        # Add the JSON data to the list
        label_data_list.append(label_row.to_encord_dict())

    # Write the JSON data list to the file
    with open(file_path, 'w') as f:
        json.dump(label_data_list, f, indent=4)

Export_json()