from captions_service import generate_captions
with open(
    r"C:\Users\rohan\Downloads\cat_dog_petting.jpg",
    "rb"
) as f:
    image_bytes = f.read()
captions = generate_captions(
    image_bytes=image_bytes,
    mime_type="image/jpeg"
)
print(captions)
