import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ExifTags
from PIL.ExifTags import TAGS
from datetime import datetime

class Timestamp():
    def __init__(self, original_path, destination_path):
        self.original_path = original_path
        self.destination_path = destination_path

    def place_timestamp(self):
        data_folder = os.path.abspath(Path(self.original_path))
        destination_folder = os.path.abspath(Path(self.destination_path))

        file_list = os.listdir(data_folder)

        for file in file_list:
            photo = Image.open(data_folder / Path(file))
            exif = {
                TAGS[k]:v 
                for k, v in photo._getexif().items()
                if k in TAGS
                }

            dateTimeOriginal = exif['DateTimeOriginal']
            dateTime_obj = datetime.strptime(dateTimeOriginal, '%Y:%m:%d %H:%M:%S')
            date_time = dateTime_obj.strftime("%Y/%m/%d %H:%M:%S")
            image_data = photo._getexif()
            print(dateTimeOriginal)
            copy_photo = photo.copy()
            width, height = copy_photo.size
            print(f'{width}x{height}')
            new_file_name = 'timestamp-' + file
            draw = ImageDraw.Draw(copy_photo)
            fontsFolder = 'C:\Windows\Fonts'
            font_size = round(170/2256*height)
            arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'),font_size)
            if width >= height:
                draw.text((0.42*width ,0.9*height), date_time, fill='yellow',stroke_width=4, stroke_fill='black', font=arialFont)
            else:
                draw.text((0.05*width ,0.85*height), date_time, fill='yellow',stroke_width=4, stroke_fill='black', font=arialFont)
            copy_photo.save(destination_folder / Path(new_file_name))

        return len(file_list)