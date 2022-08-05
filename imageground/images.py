from PIL import Image,ImageFilter
img=Image.open('./pokedex/pikachu.jpg')
filter=img.convert('L')
filter.save('grey.png','png')