from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs = ['1st.pdf', '2nd.pdf','3.pdf','4.pdf', '5.pdf', '6.pdf', '7.pdf', '8.pdf', '9.pdf', '10.pdf', '11.pdf']

for pdf in pdfs:
    merger.append(pdf)

merger.write("combined.pdf")
merger.close()