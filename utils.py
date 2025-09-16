from weaviate import WeaviateClient


def connect_to_weaviate() -> WeaviateClient:
    import weaviate
    import os

    client = weaviate.connect_to_embedded(
        version="1.32.5",
        headers={
            "X-Anthropic-Api-Key": os.getenv("ANTHROPIC_API_KEY"),
            "X-Cohere-Api-Key": os.getenv("COHERE_API_KEY")
        },
        environment_variables={
            "LOG_LEVEL": "error",                   # Reduce amount of logs
            "ENABLE_API_BASED_MODULES": "true",     # Enable API-based modules like multi2vec-cohere
        }
    )
    return client
