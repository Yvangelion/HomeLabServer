from PIL import Image
import os

def compress_images(input_folder, output_folder, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            compress_image(input_path, output_path, quality)

def compress_image(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image.save(output_path, 'JPEG', quality=quality)
    print(f"Compressed {input_path} and saved to {output_path}")

# Example usage
input_folder = 'input_images'
output_folder = 'compressed_images'
compress_images(input_folder, output_folder)
