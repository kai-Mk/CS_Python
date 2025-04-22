from PIL import Image, ImageFilter

before = Image.open("../images/sample_image1.png")
after = before.filter(ImageFilter.BoxBlur(1))
after.save("out.png")