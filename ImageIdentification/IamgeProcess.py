# encoding=utf-8
from PIL import Image,ImageFilter
def process():
    file_path='./cache/yzm.png'
    split_lines = [5,17,29,41,53]
    img=Image.open(file_path)
    img = img.convert('RGB')
    r, g, b = img.split()
    image_b_median = b.filter(ImageFilter.MedianFilter())
    image_b_median_binary = image_b_median.point(lambda i: i > 160, mode='1')
    c = 1
    for x_min, x_max in zip(split_lines[:-1], split_lines[1:]):
        image_b_median_binary.crop([x_min, 0, x_max, 22]).save('./cache/yzm-{}.png'.format(c))
        c = c + 1
    print(u"图片处理完成")
