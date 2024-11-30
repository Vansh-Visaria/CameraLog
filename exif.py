from PIL import Image
import piexif
import os

def extract_exif(image_path):
    try:
        image = Image.open(image_path)
        if 'exif' not in image.info:
            print("No EXIF data found.")
            return None

        exif_data = piexif.load(image.info['exif'])

        print("Available EXIF data keys:", exif_data.keys())

        if not exif_data['Exif']:
            print("No EXIF data found in Exif section:", exif_data)
            return None

        camera_info = {
            "Make": exif_data['0th'].get(271, b'').decode('utf-8', 'ignore'), 
            "Model": exif_data['0th'].get(272, b'').decode('utf-8', 'ignore'), 
            "DateTime": exif_data['0th'].get(306, b'').decode('utf-8', 'ignore'), 
            "ExposureTime": exif_data['Exif'].get(33434, b''), 
            "FNumber": exif_data['Exif'].get(33437, b''),  
            "ISOSpeedRatings": exif_data['Exif'].get(34855, b''),  
            
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
