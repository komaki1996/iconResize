from PIL import Image

input_view = Image.open("icon.png")
Size = [20,29,40,58,60,76,80,87,120,152,167,180]

for size in Size:
    icon = input_view.resize((size,size))
    icon.save("icon_x" + str(size) + ".png")