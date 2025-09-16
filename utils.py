from weaviate import WeaviateClient


def connect_to_weaviate() -> WeaviateClient:
    import weaviate
    import os

    WEAVIATE_URL = os.getenv("WEAVIATE_URL")
    WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_URL,
        auth_credentials=WEAVIATE_API_KEY,
        headers={"X-Anthropic-Api-Key": os.getenv("ANTHROPIC_API_KEY")}
    )
    return client
