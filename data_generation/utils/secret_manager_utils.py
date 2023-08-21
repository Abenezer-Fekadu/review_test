import ast
from google.cloud import secretmanager


def get_secret_value_Dict(project_id="", secret_id="", version_id="latest"):

    client = secretmanager.SecretManagerServiceClient()

    secret_name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    response = client.access_secret_version(request={"name": secret_name})
    secret_value = ast.literal_eval(response.payload.data.decode("UTF-8"))

    return secret_value
