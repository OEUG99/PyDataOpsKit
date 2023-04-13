import json
import boto3
import botocore
from botocore.exceptions import ClientError

class AmazonSecretsManager:
    secret_name = None
    region = None
    aws_secret_access_key = None
    aws_session_token = None
    aws_access_key_id = None
    aws_secret_key_name = None

    def __init__(self, secret_name, region, aws_secret_access_key, aws_session_token, aws_access_key_id,
                 aws_secret_key_name):
        self.client = None
        self.secret_name = secret_name
        self.region = region
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_session_token = aws_session_token
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_key_name = aws_secret_key_name


    def get_secret(self, queryKey: str) -> str:
        """ Gets a secret from AWS.

        :param queryKey:
        :type queryKey:
        :return:
        :rtype:
        """
        try:
            self.client = boto3.client('secretsmanager',
                                       aws_secret_access_key=self.aws_secret_access_key,
                                       aws_session_token=self.aws_session_token,
                                       region_name=self.region,
                                       aws_access_key_id=self.aws_access_key_id
                                       )

            response = json.loads(self.client.get_secret_value(SecretId=self.aws_secret_key_name)["SecretString"])
            return response[queryKey]
        except botocore.exceptions.ClientError as e:
            error_message = f"Error getting {queryKey} secret from Secrets Manager: {e}"
            raise Exception(error_message)
