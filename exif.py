from PIL import Image
import piexif
import os

def extract_exif(image_path):
    try:
        image = Image.open(image_path)

        # Check if the image has EXIF data
        if 'exif' not in image.info:
            print("No EXIF data found.")
            return None

        exif_data = piexif.load(image.info['exif'])

        # Print available EXIF keys for debugging
        print("Available EXIF data keys:", exif_data.keys())

        # Check if Exif section is empty
        if not exif_data['Exif']:
            print("No EXIF data found in Exif section:", exif_data)
            return None

        # Extract relevant information using integer keys
        camera_info = {
            "Make": exif_data['0th'].get(271, b'').decode('utf-8', 'ignore'),  # 271 = Make
            "Model": exif_data['0th'].get(272, b'').decode('utf-8', 'ignore'),  # 272 = Model
            "DateTime": exif_data['0th'].get(306, b'').decode('utf-8', 'ignore'),  # 306 = DateTime
            "ExposureTime": exif_data['Exif'].get(33434, b''),  # 33434 = ExposureTime
            "FNumber": exif_data['Exif'].get(33437, b''),  # 33437 = FNumber
            "ISOSpeedRatings": exif_data['Exif'].get(34855, b''),  # 34855 = ISOSpeedRatings
            
        }

        return camera_info
    except KeyError as ke:
        print(f"Key error: {ke}. Please check if the image contains all expected EXIF data.")
        return None
    except Exception as e:
        print(f"Error extracting EXIF data: {e}")
        return None

def main():
    image_path = input("Enter the path to the image: ")
    if os.path.exists(image_path):
        exif_info = extract_exif(image_path)
        if exif_info:
            print("EXIF Data:")
            for key, value in exif_info.items():
                print(f"{key}: {value}")
    else:
        print("Image not found. Please check the path.")

if __name__ == "__main__":
    main()
