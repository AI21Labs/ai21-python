def create_client_url(base_url: str) -> str:
    if base_url.endswith(".ai21.com"):
        return f"{base_url}/studio/v1"

    return base_url
