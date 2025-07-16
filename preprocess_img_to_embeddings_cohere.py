
from pathlib import Path
import numpy as np
import json
import cohere
import base64

img_dir = Path("data/imgs")
pdf_img_paths = sorted(list(img_dir.glob("manual_bosch_*.png")))
pdf_img_paths = pdf_img_paths
batch_size = 4
MODEL_NAME = "embed-v4.0"
MODEL_PROVIDER = "cohere"

co = cohere.ClientV2()

image_embeddings = []
image_inputs = []
image_paths = []

print(f"Processing {len(pdf_img_paths)} images in batches of {batch_size}...")
for i in range(0, len(pdf_img_paths), batch_size):
    batch_paths = pdf_img_paths[i:i + batch_size]
    batch_inputs = []
    for pdf_img_path in batch_paths:
        image = pdf_img_path.read_bytes()
        img_b64 = base64.b64encode(image).decode("utf-8")

        image_input = {
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{img_b64}"}
                }
            ]
        }
        batch_inputs.append(image_input)
        image_paths.append(str(pdf_img_path))

    response = co.embed(
        model=MODEL_NAME,
        input_type="image",
        embedding_types=["float"],
        inputs=batch_inputs
    )

    batch_embeddings = response.embeddings.float_
    print("Batch embeddings done. Shape:", np.array(batch_embeddings).shape)
    image_embeddings.extend(batch_embeddings)

# Convert list of numpy arrays to single array
embeddings_array = np.array(image_embeddings)
print("Total embeddings shape:", embeddings_array.shape)

# Create output directory
output_dir = Path("data/embeddings")
output_dir.mkdir(exist_ok=True)

# Save embeddings as numpy array
np.save(output_dir / "image_embeddings.npy", embeddings_array)

# Save metadata as JSON
metadata = {
    "image_paths": image_paths,
    "embedding_shape": embeddings_array.shape,
    "model_name": f"{MODEL_PROVIDER}/{MODEL_NAME}",
    "num_images": len(image_paths)
}
with open(output_dir / "embeddings_metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)

print(f"Saved {len(image_embeddings)} embeddings with shape {embeddings_array.shape}")
print(f"Files saved to: {output_dir}")
print("- image_embeddings.npy (embeddings)")
print("- embeddings_metadata.json (metadata)")
