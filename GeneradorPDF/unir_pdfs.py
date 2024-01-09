import PyPDF2

#Nombre de los archivos PDFs (El Orden importa)
archivos = ["p5_1.pdf",
            "p5_2.pdf",
            "p5_3.pdf"]

nombre_salida = "Practica5_Ecuaciones.pdf"

pdf_final = PyPDF2.PdfMerger()

for nombre_archivo in archivos:
    pdf_final.append(nombre_archivo)

pdf_final.write(nombre_salida)
pdf_final.close()