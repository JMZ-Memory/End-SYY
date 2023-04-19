import random
from Users.mixins import code

from django.test import TestCase

# Create your tests here.
test = {'account': '1097741077', 'password': '123'}
print(test)
test['password'] = '45'
print(test)

a = "1097741099@qq.com"

if "@" in a:
    print('是邮箱')

b = "f2d74b3e-f6d9-43b2-be65-07d8975ad2ee"
c = b.replace('-', '')
print(c)

a = 0
b = 2
c = 3
if a == 1:
    print('1')
elif b == 2:
    print('2')
elif c == 3:
    pass
else:
    print('3')

a = 4
print(a)

# code = []
# for i in range(5):
#     num = str(random.randint(0, 9))
#     code.append(num)
# code = "".join(code)
#
# message = """
#         '【验证码】:{},思叶云用户验证,请勿随意转发，验证码仅在三分钟内有效，请用户及时操作'，
#         """.format(code)
# print(message)
#
# o = 'null'
# print(o)
# if o:
#     print('abc')


from PIL import Image, ImageDraw, ImageFont, ImageFilter

def check_code(width=120, height=130, char_length=5, font_file='STKAITI.TTF', font_size=20):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')


    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        h = 1
        draw.text([i * width / char_length, h], '好', font=font, fill=(0,0,0))





    # img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img

print(check_code().show())
