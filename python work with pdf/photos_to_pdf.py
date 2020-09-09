from PIL import Image

img1 = Image.open('1.jpg')
img2 = Image.open('2.jpg')

img1.save('p.pdf', 'PDF', resolution=100.0, save_all=True, append_images = [img2])