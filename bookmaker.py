from PyPDF2 import PdfReader, PdfWriter
import sys

path = sys.argv[1]
pdf = PdfReader(path)
pages = pdf.pages
N = len(pages)

out = PdfWriter()

for i in range(N//2):
    if i%2 == 0:
        out.add_page(pages[i])
        out.add_page(pages[N - i - 1])
    else:
        out.add_page(pages[N - i - 1])
        out.add_page(pages[i])

out.write(open('a.pdf','wb'))

print('Done!')
