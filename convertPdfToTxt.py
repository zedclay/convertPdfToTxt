# import PyPDF2

# pdfFileObj=open('cover letter.pdf','rb')

# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# x = pdfReader.numberPages
# pageObj = pdfReader.getPage(x-1)
# text = pageObj.extractText()
# file1 = open(r"C:\Users\zedclay","a")
# file1.writeLines(text)
# file1.close()
import PyPDF2

pdf_file_path = input("Enter the name of the PDF file (including the extension): ")

with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    number_of_pages = len(pdf_reader.pages)
    last_page = pdf_reader.pages[number_of_pages - 1]
    text = last_page.extract_text()

    output_file_name = input("Enter the name of the output text file (including the extension): ")
    output_file_path = r"C:\Users\zedclay\Desktop\{}".format(output_file_name)

    with open(output_file_path, "a") as output_file:
        output_file.write(text)

print("Text extracted from the last page and saved to {}.".format(output_file_path))