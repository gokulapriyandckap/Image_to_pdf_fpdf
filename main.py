from fpdf import FPDF

fpdf = FPDF()

images = ["Understand The Background of Python Programming - MindxMaster.jpeg","pythondatastructuresmin.png"]

for image in images:
    fpdf.add_page()
    fpdf.set_auto_page_break(auto=True, margin=0)
    fpdf.image(image, x=0, y=0, w=fpdf.w, h=fpdf.h)
fpdf.output("file.pdf", "F")
