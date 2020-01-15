from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import xmltodict
from gps_conversion import exif_to_decimal,rdf_to_decimal

image1 = Image.open('./images/photo-dublin-a1.jpg')
print(image1.height)
print(image1.width)
print(image1.format)

exif_info_1 = {TAGS.get(tag,tag):value 
              for tag,value in image1._getexif().items()}

print(exif_info_1['Model'])
print(exif_info_1['LensModel'])
print(exif_info_1['DateTimeOriginal'])

image2 = Image.open('./images/photo-dublin-a2.png')
print(image2.height)
print(image2.width)
print(image2.format)

print(image2.info)
#xmp_info = xmltodict.parse(image2.info['XML:com.adobe.xmp'])
