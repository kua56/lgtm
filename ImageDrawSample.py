from PIL import Image, ImageDraw

file_path = './neko.jpg'

image = Image.open(file_path)
draw = ImageDraw.Draw(image)

draw.text((0,0), 'LGTM')
image.save('output.png', 'PNG')
