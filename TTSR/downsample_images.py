from PIL import Image
import os

def downsample_image(filename_in, filename_ref):
    img_hr = Image.open(filename_in)

    # adjust to x4
    img_hr = img_hr.resize(
        (x - (x % 4) for x in img_hr.size), Image.BICUBIC)
    # input image
    img_lr = img_hr.resize(
        (x // 4 for x in img_hr.size), Image.BICUBIC)

    img_lr.save(filename_ref)

def upsample(filename_in, filename_ref):
    img_hr = Image.open(filename_in)

    # adjust to x4
    img_hr = img_hr.resize(
        (x * 4 for x in img_hr.size), Image.BICUBIC)

    img_hr.save(filename_ref)


if __name__ == '__main__':
    # folder
    folder = '/home/khiem/workspace/ilim-projects/super-resolution/TTSR/test/selfies'
    # loop over images
    files = os.listdir(folder)
    for file in files:
        if file.endswith('.jpg'):
            filename_in = os.path.join(folder, file)
            filename_small_png = os.path.join(folder, file.replace('.jpg', '_small.png'))
            downsample_image(filename_in, filename_small_png)

            filename_small_jpg = filename_small_png.replace('_small.png', '_small.jpg')
            downsample_image(filename_in, filename_small_jpg)

            filename_upsample_png = filename_small_png.replace('_small.png', '_small_upsampled.png')
            upsample(filename_small_png, filename_upsample_png)
