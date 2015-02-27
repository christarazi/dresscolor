from PIL import Image, ImageDraw

im = Image.open("a.jpg")
im = im.resize((150,150))
result = im.convert('P', palette=Image.ADAPTIVE, colors=8)
result.putalpha(0)
colors = result.getcolors(150*150)

newimg = Image.new('RGB', (64*8, 64))
draw = ImageDraw.Draw(newimg)

posx = 0
for row, col in colors:
	draw.rectangle([posx, 0, posx+64, 64], fill=col)
	posx = posx + 64

del draw
newimg.save("swatch", "JPEG")
