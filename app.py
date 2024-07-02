from flask import Flask, request, render_template, send_file, redirect, url_for
from werkzeug.utils import secure_filename
import os
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def create_watermark(watermark_text):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 36)
    can.setFillAlpha(0.1)

    # Rotacionar o texto em 45 graus
    can.saveState()
    can.translate(100, 300)
    can.rotate(45)
    can.drawString(0, 0, watermark_text)
    can.restoreState()

    # Rotacionar o texto em -45 graus
    can.saveState()
    can.translate(10, 260)
    can.rotate(-45)
    can.drawString(0, 0, watermark_text)
    can.restoreState()

    can.save()
    packet.seek(0)
    return packet

def add_watermark(input_pdf, watermark_text):
    watermark = create_watermark(watermark_text)
    watermark_pdf = PdfReader(watermark)
    output_pdf = PdfWriter()

    input_pdf = PdfReader(open(input_pdf, "rb"))

    for i in range(len(input_pdf.pages)):
        page = input_pdf.pages[i]
        page.merge_page(watermark_pdf.pages[0])
        output_pdf.add_page(page)

    output_filename = os.path.join(app.config['UPLOAD_FOLDER'], "watermarked.pdf")
    with open(output_filename, "wb") as outputStream:
        output_pdf.write(outputStream)

    return output_filename

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files or 'watermark_text' not in request.form:
            return redirect(request.url)
        file = request.files['file']
        watermark_text = request.form['watermark_text']
        if file.filename == '' or not allowed_file(file.filename):
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            watermarked_file_path = add_watermark(file_path, watermark_text)
            return send_file(watermarked_file_path, as_attachment=True, download_name="watermarked.pdf")
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True, host="0.0.0.0", port=8080)
