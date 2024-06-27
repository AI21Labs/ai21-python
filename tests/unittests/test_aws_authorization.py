import boto3

from ai21.clients.aws.aws_authorization import AWSAuthorization


class MockCredentials:
    def __init__(self, access_key, secret_key, token):
        self.access_key = access_key
        self.secret_key = secret_key
        self.token = token
        self.method = "env"


def test_prepare_auth_headers__(mock_boto_session: boto3.Session):
    auth_headers_keys = ["X-Amz-Date", "X-Amz-Security-Token", "Authorization"]
    mock_boto_session.get_credentials.return_value = MockCredentials(
        access_key="some-key", secret_key="some-secret", token="some-token"
    )
    aws_authorization = AWSAuthorization(aws_session=mock_boto_session)
    headers = aws_authorization.get_auth_headers(
        url="https://dummy.com",
        service_name="bedrock",
        method="POST",
        data='{"foo": "bar"}',
    )

    for auth_header in auth_headers_keys:
        assert auth_header in headers
