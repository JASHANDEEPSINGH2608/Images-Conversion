import sys
import os
import cv2

def main():
    if len(sys.argv) != 4:
        print("Usage: python scale.py <input_folder> <output_folder> <scale_percentage>")
        return

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Ensure scale percentage is an integer
    try:
        scale_percentage = int(sys.argv[3])
    except ValueError:
        print("Error: Scale percentage must be an integer.")
        return

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            img_path = os.path.join(input_folder, filename)
            try:
                # Read the image using OpenCV
                img = cv2.imread(img_path)
                if img is None:
                    print(f"Error: Could not open {filename}. Skipping.")
                    continue

                # Calculate the new size
                new_width = int(img.shape[1] * scale_percentage / 100)
                new_height = int(img.shape[0] * scale_percentage / 100)
                new_size = (new_width, new_height)

                # Resize the image using OpenCV
                scaled_img = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)

                # Save the scaled image to the output folder
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, scaled_img)

                print(f"Scaled {filename} to {scale_percentage}% of its original size.")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
        else:
            print(f"Skipping non-image file: {filename}")

if __name__ == "__main__":
    main()
