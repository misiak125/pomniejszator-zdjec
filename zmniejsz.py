import shutil
import os
from PIL import Image

def compress_under_size(size, file_path, save_path, filename):
    
    current_size = os.stat(file_path).st_size

    if current_size > size:
        
        tmp_dir = f"./.tmp/{filename}"
        shutil.copy(file_path, tmp_dir) 
        image = Image.open(tmp_dir)
        image = image.convert("RGB", colors=8)
        size = image.size ##turubdalej
        quality = 80 #not the best value as this usually increases size

        current_size = os.stat(file_path).st_size
        print(current_size)
        
        while current_size > size or quality == 0:
            if quality == 0:
                #os.remove(save_path)
                print("Error: File cannot be compressed below this size")
                break

            compress_pic(file_path, quality, save_path)
            current_size = os.stat(save_path).st_size
            print(current_size)
            quality -= 5
    else: 
        shutil.copy(file_path, save_path)

         


def compress_pic(file_path, qual, save_path):
    '''File path is a string to the file to be compressed and
    quality is the quality to be compressed down to'''
    picture = Image.open(file_path)
    dim = picture.size

    picture.save(save_path,"JPEG", optimize=True, quality=qual) 

    processed_size = os.stat(save_path).st_size

    return processed_size

def main() -> None:
	directory = os.fsencode("./do_zmniejszenia")
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		compress_under_size(800000, f"./do_zmniejszenia/{filename}", f"./pomniejszone/{filename}", filename)
			


if __name__ == '__main__':
    main()
