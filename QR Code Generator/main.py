# QR code generator in python using the qrcode library
# import the qrcode library
import qrcode

print('-'*100)
print('QR Code Generator'.center(100))
print('-'*100)

def generate_qr(data, file_name):
    # Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Adding the data to the QR code
    qr.add_data(data)
    # Generating the QR code
    qr.make(fit=True)

    # Creating an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    file_path = file_name + '.png'
    # Saving the image
    img.save(file_path)

    choice = input('Do you want to display the QR code? (y/n): ')
    
    if choice == 'y':
        # Displaying the image
        img.show()

# Data to be stored in the QR code
data = input('Enter the data to be stored in the QR code: ')

# File name for the QR code
file_name = input('Enter the file name for the QR code: ')

# Generating the QR code   
generate_qr(data, file_name)

