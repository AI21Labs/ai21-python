from typing import Optional, Dict

from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import boto3


class AWSAuthorization:
    def __init__(self, aws_session: boto3.Session):
        self._aws_session = aws_session

    def get_auth_headers(
        self,
        *,
        url: str,
        service_name: str,
        method: str,
        data: Optional[str],
    ) -> Dict[str, str]:
        request = AWSRequest(method=method, url=url, data=data)
        credentials = self._aws_session.get_credentials()

        signer = SigV4Auth(
            credentials=credentials, service_name=service_name, region_name=self._aws_session.region_name
        )
        signer.add_auth(request)

        prepped = request.prepare()

        return {key: value for key, value in dict(prepped.headers).items() if value is not None}
