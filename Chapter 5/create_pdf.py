import fpdf

document = fpdf.FPDF()

document.set_font('Times','B',14)
document.set_text_color(19,83,173)
document.add_page()

document.cell(0,5,'PDF test document')
document.ln()

document.set_font('Times', '', 12)
document.set_text_color(0)
document.multi_cell(0,5,'This is an example of a long paragraph.'*10)
document.ln()

document.multi_cell(0,5,'Another long paragraph. Lorem ipsum dolor sit amet, consectetur adipiscing elit.' *20)

document.output('report_pdf.pdf')