import qrcode

# URL cruda del archivo HTML en GitHub
pagina_url = "https://github.com/arirodriguez001/young/raw/main/pagina.html"

# Crear el código QR con la URL del archivo HTML
qr = qrcode.make(pagina_url)

# Guardar el QR como imagen
qr.save("qr_code.png")

print("Código QR generado exitosamente como 'qr_code.png'.")


