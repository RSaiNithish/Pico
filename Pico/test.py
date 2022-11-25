from PIL import Image

picture = Image.open('''compressed.png''')
picture=picture.resize((120,50))
picture.save('''compressed.png''')
