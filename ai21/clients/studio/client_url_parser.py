from ai21.constants import STUDIO_HOST


def create_client_url(base_url: str) -> str:
    allowed_urls = ["https://api-stage.ai21.com", STUDIO_HOST]

    if base_url in allowed_urls:
        return f"{base_url}/studio/v1"

    return base_url
