from PIL import Image 
import pathlib

BASE_PATH = pathlib.Path().absolute()

def generate_thumbnails(file_name, file_path):
	im = Image.open(file_path)
	thumbnail_size = (140, 140)
	thumbnail = im.resize(thumbnail_size)
	thumbnail.save("resized_"+file_name)

generate_thumbnails("ads1.jpg", str(BASE_PATH)+'/'+"ads1.jpg");
generate_thumbnails("ads2.jpg", str(BASE_PATH)+'/'+"ads2.jpg");
generate_thumbnails("ads3.jpg", str(BASE_PATH)+'/'+"ads3.jpg");
generate_thumbnails("ads4.jpg", str(BASE_PATH)+'/'+"ads4.jpg");
generate_thumbnails("ads5.jpg", str(BASE_PATH)+'/'+"ads5.jpg");
generate_thumbnails("ads6.jpg", str(BASE_PATH)+'/'+"ads6.jpg");
generate_thumbnails("ads7.jpg", str(BASE_PATH)+'/'+"ads7.jpg");
generate_thumbnails("ads8.jpg", str(BASE_PATH)+'/'+"ads8.jpg");
generate_thumbnails("ads9.jpg", str(BASE_PATH)+'/'+"ads9.jpg");