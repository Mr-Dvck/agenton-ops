import os
import requests
from PIL import Image
from io import BytesIO

URL = "https://raw.githubusercontent.com/googlefonts/noto-emoji/main/png/128/emoji_u1f4b0.png"
OUTPUT_ICO = r"C:\BC RESEARCH\AI_FACTORY\AgentOn\dashboard\money_bag.ico"

def main():
    print(f"Downloading money bag emoji from: {URL}")
    response = requests.get(URL, timeout=15)
    response.raise_for_status()
    
    img = Image.open(BytesIO(response.content))
    
    # Save as ICO file with standard icon sizes
    print(f"Saving icon to: {OUTPUT_ICO}")
    img.save(OUTPUT_ICO, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)])
    print("Successfully created money bag icon!")

if __name__ == "__main__":
    main()
