from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

pdf_file = "C:\\Users\\user\\Desktop\\Laby\\PDFfile.pdf"
watermark = "C:\\Users\\user\\Desktop\\Laby\\watermarkkk.jpg"
#merged = "C:/Users/11359023/Desktop/merged.pdf"

with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
    input_pdf = PdfFileReader(input_file)
    watermark_pdf = PdfFileReader(watermark_file)
    watermark_page = watermark_pdf.getPage(0)

    output = PdfFileWriter()

    for i in range(input_pdf.getNumPages()):
        pdf_page = input_pdf.getPage(i)
        pdf_page.mergePage(watermark_page)
        output.addPage(pdf_page)

##    with open(merged, "wb") as merged_file:
#       output.write(merged_file)