import sys
import os
import cv2


def main():
    if len(sys.argv) != 3:
        print("Usage: python grayscale.py <input_folder> <output_folder>")
        return

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            # Open an image file
            img_path = os.path.join(input_folder, filename)

            # Read the image using OpenCV
            img = cv2.imread(img_path)

            # Convert the image to grayscale
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Save the grayscale image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, gray_img)

            print(f"Converted {filename} to grayscale.")


if __name__ == "__main__":
    main()
