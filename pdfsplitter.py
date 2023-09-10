from PyPDF2 import PdfWriter,PdfReader

def cropper(start,end,file):
    inputPdf = PdfReader(open(file,"rb"))
    outPdf = PdfWriter()
    with open(file.split(".")[0]+"cropped"+".pdf","wb") as ostream:
        for page in range(start, end + 1):
          outPdf.add_page(inputPdf.pages[start])
          outPdf.write(ostream)


