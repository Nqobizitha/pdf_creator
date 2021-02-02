from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER


canvas = Canvas('second.pdf')

canvas.drawString (10, 10, "This is my first pdf created using python and i am quiet fascinated about it")

canvas.save()

canvas = Canvas("second.pdf", pagesize=(612.0, 792.0))





