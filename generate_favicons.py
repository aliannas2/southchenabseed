from PIL import Image
import os

def generate_favicons(source_file):
    if not os.path.exists(source_file):
        print(f"Error: {source_file} not found.")
        return

    img = Image.open(source_file)
    
    # Ensure it's square, center crop if needed, but logo.png might be rectangular.
    # For a favicon, we usually want it square. Let's assume we resize/contain it.
    # Better approach for logos: Make it square by adding transparency if not square.
    
    # Calculate aspect ratio
    width, height = img.size
    if width != height:
        new_size = max(width, height)
        new_img = Image.new("RGBA", (new_size, new_size), (0, 0, 0, 0))
        left = (new_size - width) // 2
        top = (new_size - height) // 2
        new_img.paste(img, (left, top))
        img = new_img

    # 1. favicon.ico (Multiple sizes for Windows/Legacy)
    icon_sizes = [(16, 16), (32, 32), (48, 48)]
    img.save("favicon.ico", format="ICO", sizes=icon_sizes)
    print("Generated favicon.ico")

    # 2. apple-touch-icon.png (180x180)
    img.resize((180, 180), Image.Resampling.LANCZOS).save("apple-touch-icon.png")
    print("Generated apple-touch-icon.png")

    # 3. android-chrome-192x192.png
    img.resize((192, 192), Image.Resampling.LANCZOS).save("android-chrome-192x192.png")
    print("Generated android-chrome-192x192.png")

    # 4. android-chrome-512x512.png
    img.resize((512, 512), Image.Resampling.LANCZOS).save("android-chrome-512x512.png")
    print("Generated android-chrome-512x512.png")

    # 5. favicon-32x32.png (Modern browsers)
    img.resize((32, 32), Image.Resampling.LANCZOS).save("favicon-32x32.png")
    print("Generated favicon-32x32.png")

    # 6. favicon-16x16.png (Modern browsers)
    img.resize((16, 16), Image.Resampling.LANCZOS).save("favicon-16x16.png")
    print("Generated favicon-16x16.png")

if __name__ == "__main__":
    generate_favicons("logo.png")
