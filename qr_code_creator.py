import qrcode
import matplotlib.pyplot as plt

# Text or link, which should be presented
text = "https://example.com"

# QR-Code generieren
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)

# Render QR-Code as image
image = qr.make_image(fill_color="black", back_color="white")

# QR-Code anzeigen
plt.imshow(image)
plt.axis('off')
plt.show()