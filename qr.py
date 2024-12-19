import qrcode

# Data to be encoded in the QR code
data = "www.google.com"


# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls error correction level
    box_size=10,  # Size of each box (pixels)
    border=4,  # Size of the border (boxes)
)
 
# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qrcode_example.png")

# Display the image
img.show()  







#pip install qrcode[pil]
#pip install pillow
# # Data to encode in QR code (Name, Age, Number)
# name = "Alice"
# age = 25
# number = "123-456-7890"

# # Combine the data into a formatted string