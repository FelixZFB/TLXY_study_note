# Tesseract OCR图像识别

import pytesseract as pt
from PIL import Image

# 生成图片案例
image = Image.open('D:\Hello World\python_work\TLXY_study_note\Spider\图像识别测试.png')

# 调用pytesseract将图像转换成文字
text = pt.image_to_string(image)
print(text)