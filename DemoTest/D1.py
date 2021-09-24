from Core.TicketEnum import TicketType
import pytesseract
from PIL import Image

pytesseract_path = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = pytesseract_path

image_url = r'D:\Documents\image\20190710210507857.jpg'
image_full = Image.open(image_url)

# screenshot_size_x = image_full.size[0]
# screenshot_size_y = image_full.size[1]
# print(screenshot_size_x)
# print(screenshot_size_y)

# 裁剪截图成验证码图片
box_1 = (
    300,
    145,
    680,
    180
)

box_2 = (
    550,
    145,
    680,
    180
)

# box = [i * 1.5 for i in box]

image_crop_1 = image_full.crop(box_1)
image_crop_1 = image_crop_1.convert('L')
# image_crop_1.save('./test_crop1.png')

image_crop_2 = image_full.crop(box_2)
image_crop_2 = image_crop_2.convert('L')
# image_crop_2.save('./test_crop2.png')


config_str = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
captcha_code = pytesseract.image_to_string(image_crop_1, lang='eng', config=config_str).strip()

captcha_code2 = pytesseract.image_to_string(image_crop_2, lang='eng', config=config_str).strip()

print(captcha_code)
print(captcha_code2)

