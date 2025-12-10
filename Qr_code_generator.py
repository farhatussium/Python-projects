import qrcode#pip install qrcode[pil]
link = input("Enter the link/URL: ")#Generate QR code for the provided link
qr = qrcode.make(link)#store the QR code as an image file
qr.save("qrcode.png")#show the QR code
print("QR Code saved as qrcode.png")#to display the QR code image
qr.show()#opens the default image viewer to display the QR code