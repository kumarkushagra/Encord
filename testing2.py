from encord import EncordUserClient
import json

# Initialize Encord client using private key and project ID
private_key = "C:\\Users\\EIOT\\Desktop\\KEY\\exportimportpublickey-private-key.txt"
project_id = "396cb84f-0cc8-44af-9bb2-f490b77a7529"
json_file_path = "C:/Users/EIOT/Desktop/Encord/EXPORT/DICOM_Signed_URL.json"  # Replace with your desired path

# Instantiate Encord client using private key
user_client = EncordUserClient.create_with_ssh_private_key(
    ssh_private_key_path=private_key
)

# Get the project using project ID
project = user_client.get_project(project_id)

# Function to get signed URLs for DICOM images/series
def get_signed_urls(project):
    signed_urls = []
    label_rows = project.list_label_rows_v2()

    print(f"Found {len(label_rows)} label rows.")
    
    for label_row in label_rows:
        label_row.initialise_labels()
        print(f"Processing label row with data_hash: {label_row.data_hash}")
        
        if label_row.metadata is not None:
            print("Metadata:", label_row.metadata)  # Print the metadata for inspection
            # Assuming metadata contains signed URLs (or has methods to get them)
            if 'signed_url' in label_row.metadata:
                signed_url = label_row.metadata['signed_url']
                signed_urls.append(signed_url)
                print(f"Added signed URL: {signed_url}")
            else:
                print("No signed URL found in metadata for this label row.")
        else:
            print("Metadata is None for this label row.")
                
    return signed_urls

# Fetch signed URLs
signed_urls = get_signed_urls(project)

# Save signed URLs to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(signed_urls, json_file, indent=4)

print(f"Signed URLs have been saved to {json_file_path}")
print(f"Total signed URLs saved: {len(signed_urls)}")
