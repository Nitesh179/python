import qrcode 

link="file:///home/dev52/Downloads/Python-Durga-Notes.pdf"
image=qrcode.make(link)
image.save("qrcode.jpg")
