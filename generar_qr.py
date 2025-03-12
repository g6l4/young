import qrcode

# URL cruda del archivo HTML en GitHub
pagina_url = "https://g6l4.github.io/young/pagina.html"

# Crear el código QR con la URL del archivo HTML
qr = qrcode.make(pagina_url)

# Guardar el QR como imagen
qr.save("qr_code.png")

print("Código QR generado exitosamente como 'qr_code.png'.")


