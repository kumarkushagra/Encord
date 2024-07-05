
# Authenticate with Encord. Replace <private_key_path> with the path to your private key
user_client = EncordUserClient.create_with_ssh_private_key(
    ssh_private_key_path="C:\\Users\\EIOT\\Desktop\\KEY\\exportimportpublickey-private-key.txt"
)

from encord import EncordUserClient
from encord.orm.dataset import StorageLocation




# DATASET CREATION (in encord)
dataset_title = input("Enter the name of the dataset: ")
dataset = user_client.create_dataset(dataset_title, StorageLocation.CORD_STORAGE)
dataset_id = dataset.dataset_hash
print(dataset_id)
