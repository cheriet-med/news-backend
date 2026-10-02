import pillow_avif  # noqa: registers AVIF codec with Pillow
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

def convert_to_avif(image_field, quality=50):
    img = Image.open(image_field)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    buf = BytesIO()
    img.save(buf, format="AVIF", quality=quality)
    buf.seek(0)
    name = image_field.name.rsplit(".", 1)[0] + ".avif"
    return ContentFile(buf.read(), name=name)