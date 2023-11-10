import streamlit as st 
pip install qrcode[pil]
import qrcode

# Create an instance of the QRCode class
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
data = "Hello, QR Code!"
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save or display the image
img.save("my_qrcode.png")
img.show()
