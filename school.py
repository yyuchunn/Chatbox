import qrcode
codeText = "https://www.nuk.edu.tw/"
img = qrcode.make(codeText)
print("檔案格式", type(img))
img.save("nuk_qrcode.jpg")
