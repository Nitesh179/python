import PyPDF2


readFile=PyPDF2.PdfReader('pyquest.pdf')
# print(len(readFile.pages))
# print(readFile.pages[3].extract_text())

for i in range(len(readFile.pages)):
    print(readFile.pages[i].extract_text())