# -*- coding: utf-8 -*-
#Author: Alexander Strom

def sort_photos_bydate(gallery_path):
    
    """
    Photos from different sources with different name structures are renamed systematically using the date of the respective photo taken.
    """
    
    import PIL.Image
    import os
    
    imgs = [f for f in os.listdir(gallery_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.JPG') or f.endswith('.JPEG')]
    
    date_phototaken = []
    
    for img_file in imgs:
    #    print(img_file)
        img_path = gallery_path+'/'+img_file
        img = PIL.Image.open(img_path)
        
        try:
            exif_data = img._getexif()
            date_phototaken = exif_data[306]
            
            year = date_phototaken[:4]
            month = date_phototaken[5:7]
            day = date_phototaken[8:10]
            hour = date_phototaken[11:13]
            minute = date_phototaken[14:16]
            second = date_phototaken[17:19]
            
            print(date_phototaken)
            print(year+month+day + "_" + hour+minute+second)
            
            new_img_path = gallery_path + '/' + 'IMG_'+year+month+day + "_" + hour+minute+second+'.jpg'
            
            print("Old name: " + img_path)
            print("New name: " + new_img_path)
            
            os.rename(img_path,new_img_path)
            
            print("")
        
        except:
            print('Fehler im Exif-Datenformat. {} nicht umbenannt.'.format(img_file))
            print("")
            continue