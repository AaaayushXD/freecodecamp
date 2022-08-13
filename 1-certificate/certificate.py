
import qrcode
img = qrcode.make('https://www.freecodecamp.org/certification/Aayush2911/responsive-web-design')
type(img)  # qrcode.image.pil.PilImage
img.save("certificate-freecodecamp.png")