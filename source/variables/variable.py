from google.cloud import secretmanager
import os, google_crc32c
from dotenv import load_dotenv

load_dotenv()

environment = os.environ.get('ENVIRONMENT')

def access_secret_version(
    project_id: str, secret_id: str, version_id: str
    ) -> secretmanager.AccessSecretVersionResponse:

    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})

    # Verify payload checksum.
    crc32c = google_crc32c.Checksum()
    crc32c.update(response.payload.data)
    if response.payload.data_crc32c != int(crc32c.hexdigest(), 16):
        print("Data corruption detected.")
        return response

    payload = response.payload.data.decode("UTF-8")
    #print(f"Plaintext: {payload}")
    return payload

if environment == 'DEV' :
    MYSQL_HOST=     os.environ.get('DEV_MYSQL_HOST')
    MYSQL_USER=     access_secret_version(os.environ.get('DEV_GCP_PROJECT_ID'),os.environ.get('DEV_SECRET_ID_MYSQL_USER'),os.environ.get('DEV_SECRET_VERSION_MYSQL_USER'))
    MYSQL_PASSWORD= access_secret_version(os.environ.get('DEV_GCP_PROJECT_ID'),os.environ.get('DEV_SECRET_ID_MYSQL_PASSWORD'),os.environ.get('DEV_SECRET_VERSION_MYSQL_PASSWORD'))
    MYSQL_PORT=     os.environ.get('DEV_MYSQL_PORT')
    MYSQL_DATABASE= os.environ.get('DEV_MYSQL_DATABASE')


if environment == 'PROD' :
    MYSQL_HOST =     os.environ.get('PROD_MYSQL_HOST')
    MYSQL_USER=     access_secret_version(os.environ.get('PROD_GCP_PROJECT_ID'),os.environ.get('PROD_SECRET_ID_MYSQL_USER'),os.environ.get('PROD_SECRET_VERSION_MYSQL_USER'))
    MYSQL_PASSWORD= access_secret_version(os.environ.get('PROD_GCP_PROJECT_ID'),os.environ.get('PROD_SECRET_ID_MYSQL_PASSWORD'),os.environ.get('PROD_SECRET_VERSION_MYSQL_PASSWORD'))
    MYSQL_PORT =     os.environ.get('PROD_MYSQL_PORT')
    MYSQL_DATABASE = os.environ.get('PROD_MYSQL_DATABASE')