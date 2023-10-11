import qrcode

def generate_qrcode(data, output_file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="white", back_color="black")
    qr_img.save(output_file_path)

if __name__ == "__main__":
    # Replace this variable with the data you want to encode in the QR code
    data_to_encode = "https://github.com/afrozkhan12?tab=repositories"

    # Replace this variable with the output file path for the final QR code
    # output_file_path = "past your path here and give name for saving qrcode picture." #example:"C:\practice\qrcodegenerator/qrcode.png"
    output_file_path = output_file_path = "E:/py-practice/New folder/Projects/qr-code-generator/coded.jpeg"
    generate_qrcode(data_to_encode, output_file_path)
