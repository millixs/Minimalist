import qrcode

url = input("Enter the URL: ").strip()
# Add your file path where you want the qr code image to be stored.
file_path = "C:\\Users\\HP\\Downloads\\qrcode.jpg"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated")
