import PyPDF2

archivos = ["p51.pdf",
            "p52.pdf",
            "p53.pdf"]

nombre_salida = "Practica5_Ecuaciones.pdf"

pdf_final = PyPDF2.PdfMerger()

for nombre_archivo in archivos:
    pdf_final.append(nombre_archivo)


pdf_final.write(nombre_salida)
pdf_final.close()
