import json
import os
import requests

def download_files_from_json(json_file, output_directory):
    with open(json_file, 'r') as f:
        data = json.load(f)

    download_files(data, output_directory)

def download_files(file_info_list, output_directory):
    for item in file_info_list:
        title = item[0]["title"]
        file_link = item[0]["file_link"]
        
        output_file = os.path.join(output_directory, title)
        download_file(file_link, output_file)

def download_file(signed_url, output_file):
    response = requests.get(signed_url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully to {output_file}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

# Example usage:
json_file = "C:/Users/EIOT/Desktop/Encord/EXPORT/annotation_data_with_signed_URL.json"
output_directory = "C:/Users/EIOT/Desktop/DATASET_DOWNLOAD"
download_files_from_json(json_file, output_directory)
