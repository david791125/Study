import qrcode
img = qrcode.make("hello world!")
img.get_image().show()
img.save('hello.png')