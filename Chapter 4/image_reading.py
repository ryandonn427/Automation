from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import xmltodict
from gps_conversion import exif_to_decimal,rdf_to_decimal

image1 = Image.open('./images/photo-dublin-a1.jpg')
print(image1.height)
print(image1.width)
print(image1.format)

