import cv2
import os

# Function to resize the image
def resize_image(imagePath, width, height, outputPath):
    # Read the image
    image = cv2.imread(imagePath)
    
    # Resize the image
    resized_image = cv2.resize(image, (width, height))
    
    # Save the resized image
    cv2.imwrite(outputPath, resized_image)
    
    # Return the resized image
    return resized_image

# Function to resize all images in a folder
def resize_images_in_folder(input_folder, output_folder, width, height):
    # Check if the output folder exists, create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List all files in the input folder
    for filename in os.listdir(input_folder):
        input_image_path = os.path.join(input_folder, filename)
        
        # Check if the file is an image 
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            output_image_path = os.path.join(output_folder, filename)
            
            # Resize the image
            resize_image(input_image_path, width, height, output_image_path)

# Main function
def main():
    input_folder = r"C:\Users\mvani\Desktop\Input Folder"
    output_folder = r"C:\Users\mvani\Desktop\Output Folder"
    new_width = 512 
    new_height = 512

    resize_images_in_folder(input_folder, output_folder, new_width, new_height)

# Entry point of the script
if __name__ == "__main__":
    main()

