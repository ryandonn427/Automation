from PyPDF2 import PdfFileReader

file = open('document-1.pdf','rb')
document = PdfFileReader(file)

print(document.numPages)
print(document.isEncrypted)
print(document.documentInfo)

print(document.pages[1].extractText())
file.close()

file = open('document-2.pdf','rb')
document = PdfFileReader(file)
document.decrypt('automate')
print(document.pages[0].extractText())
file.close()

