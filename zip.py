import sys
import os
from zipfile import ZipFile

def main():
    if len(sys.argv) != 3:
        print("Usage: python zip_images.py <input_folder> <output_zip_file>")
        return

    input_folder = sys.argv[1]
    output_zip_file = sys.argv[2]

    # Ensure the output file has a .zip extension
    if not output_zip_file.lower().endswith(".zip"):
        print("Error: Output file must have a .zip extension.")
        return

    # Check if the input folder exists
    if not os.path.isdir(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return

    # Create a ZipFile object
    with ZipFile(output_zip_file, 'w') as zipf:
        # Iterate through all the files in the input folder
        for foldername, subfolders, filenames in os.walk(input_folder):
            for filename in filenames:
                if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
                    file_path = os.path.join(foldername, filename)
                    # Add file to the zip archive with relative path
                    zipf.write(file_path, os.path.relpath(file_path, input_folder))
                    print(f"Added {filename} to {output_zip_file}")

    print(f"All images from {input_folder} have been zipped into {output_zip_file}")

if __name__ == "__main__":
    main()
