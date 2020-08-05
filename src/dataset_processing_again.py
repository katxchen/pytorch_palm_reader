import cv2
import os


input_images_path = "../../palm_reader/PalmImages"
output_images_path = "../data/resized-images"

if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)

input_size = len(os.listdir(input_images_path))

def convert_image(img_name, i):
    os.system("clear")
    print(f'{i}/{input_size}')
    try:
        img = cv2.imread(f'{input_images_path}/{img_name}', cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img[:,200:1401],(224,224))
        img_converted = cv2.rotate(img, cv2.ROTATE_180)
    
    
        if not cv2.imwrite(f'{output_images_path}/{img_name}', img_converted):
            raise Exception(f"File {img_name} not saved.")
    except:
        pass

def main():
    for i, img_name in enumerate(os.listdir(input_images_path)):
        convert_image(img_name,i+1)

if __name__ == "__main__":
    main()
