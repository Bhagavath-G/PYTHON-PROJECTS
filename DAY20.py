'''PROJECT 20'''

import qrcode

data = input("ENTER TEXT OR LINK :")

img = qrcode.make(data)

img.save("img.png")

img.show()

print("QR-CODE GENERATED !!!")
