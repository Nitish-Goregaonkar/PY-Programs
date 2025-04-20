from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs = ['file1.pdf', 'file2.pdf', ..., 'file10.pdf']

for pdf in pdfs:
    merger.append(pdf)

merger.write("combined.pdf")
merger.close()
