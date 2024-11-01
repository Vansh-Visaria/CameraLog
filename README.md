# EXIF Data Extractor

This project is a simple Python script that extracts EXIF data from image files. It uses the `PIL` (Pillow) library to handle image files and the `piexif` library to parse EXIF data. 

## Features

- Extracts camera information such as:
  - Camera Make
  - Camera Model
  - Date and Time the photo was taken
  - Exposure Time
  - F-Number (Aperture)
  - ISO Speed Ratings
- Handles exceptions and provides informative messages if EXIF data is unavailable or if there are errors.

## Requirements

To run this script, you will need:
- Python 3.x
- The following Python packages:
  - Pillow (`PIL`)
  - Piexif

You can install the required packages using pip:

```bash
pip install Pillow piexif
```
# Usage

Clone the repository or download the script:
```bash
https://github.com/Vansh-Visaria/CameraLog.git
  ```
Run the script using Python:
```bash
python exif_extractor.py
```
Enter the path to the image file when prompted. For example:
```bash
Enter the path to the image: /path/to/your/image.jpg
```

# Outputs

The script will output the following EXIF data if available:
Make: The manufacturer of the camera (e.g., Canon, Nikon).

Model: The model name or number of the camera.

DateTime: The date and time when the photo was taken.

ExposureTime: The exposure time used to capture the image.

FNumber: The f-stop number (aperture) used for the shot.

ISOSpeedRatings: The ISO sensitivity setting used.

If no EXIF data is found, the script will inform the user accordingly.

# Benefits

This project is useful for photographers, developers, and anyone interested in analyzing the metadata of their images. Some benefits include:

Metadata Insight: Understanding how a photo was taken can help improve photography skills.

Image Management: Helps organize and categorize images based on camera settings.

Debugging: Useful for troubleshooting image-related issues in applications or photography workflows.


