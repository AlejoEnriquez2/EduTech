import urllib.request

pdf_path = ""

def descargar_archivo(url, nombre):
    response = urllib.request.urlopen(url)
    file = open(nombre + ".pdf", "wb")
    file.write(response.read())
    file.close()

enlaces = ['https://dspace.ups.edu.ec/bitstream/123456789/13/5/Tesis.pdf', 'https://dspace.ups.edu.ec/bitstream/123456789/10175/1/UPS%20-%20ST001817.pdf', 'https://dspace.ups.edu.ec/bitstream/123456789/10184/1/UPS%20-%20ST001835.pdf', 'https://dspace.ups.edu.ec/bitstream/123456789/14191/1/UPS-GT001882.pdf', 'https://dspace.ups.edu.ec/bitstream/123456789/10177/1/UPS%20-%20ST001821.pdf', 'https://dspace.ups.edu.ec/bitstream/123456789/7455/1/UPS-CT004404.pdf', 'https://dspace.ups.edu.ec/bitstream/123456789/3280/1/UPS-CT002536.pdf', 'https://dspace.ups.edu.ec/bitstream/123456789/10378/1/UPS-GT001402.pdf', 'https://dspace.ups.edu.ec/bitstream/123456789/10376/1/UPS-GT001398.pdf', 'https://dspace.ups.edu.ec/bitstream/123456789/10375/1/UPS-GT001396.pdf']

for i in range (len(enlaces)):
    descargar_archivo(enlaces[0], str(i))