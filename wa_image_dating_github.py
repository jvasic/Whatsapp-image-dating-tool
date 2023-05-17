from datetime import datetime
import piexif
import os

path = 'C:/EXAMPLE_PATH' #COPY FOLDER PATH HERE
directory = os.fsencode(path)
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filepath = path+filename
    year = int(filename[4:8])
    month = int(filename[8:10])
    day = int(filename[10:12])

    hour = 20 
    minute = 0 
    second = 0 

    exif_dict = piexif.load(filepath)
    new_date = datetime(year, month, day, hour, minute, second).strftime("%Y:%m:%d %H:%M:%S")
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, filepath)

    print("Dated photo on date", str(day), str(month), str(year))
