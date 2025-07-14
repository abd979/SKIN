from flask import Flask, render_template, request, redirect, send_from_directory
import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from datetime import datetime
from prescriptions import prescription_data
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from werkzeug.utils import secure_filename

# === Flask Setup ===
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
PDF_FOLDER = 'static/pdfs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PDF_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# === Model Setup ===
device = torch.device("cpu")
class_names = list(prescription_data.keys())
num_classes = len(class_names)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

model = models.resnet34(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model.load_state_dict(torch.load("best_model.pth", map_location=device))
model.eval()

# === Predict Image Function ===
def predict_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image.to(device))
        _, predicted = torch.max(outputs, 1)
    return class_names[predicted.item()]

# === Generate PDF Report ===
def generate_pdf(filename, disease, treatments, prevention, name, age, phone):
    filepath = os.path.join(PDF_FOLDER, filename)
    doc = SimpleDocTemplate(filepath, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("AI Skin Disease Diagnosis Report", styles['Title']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"<b>Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    elements.append(Paragraph(f"<b>Name:</b> {name} | <b>Age:</b> {age} | <b>Phone:</b> {phone}", styles['Normal']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"<b>Disease Detected:</b> <font color='red'>{disease}</font>", styles['Heading2']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Recommended Treatments:</b>", styles['Heading3']))
    data = [["Type", "Form", "Name", "Instructions"]]
    for t in treatments:
        data.append([t['type'], t['form'], t['name'], t['instructions']])

    table = Table(data, colWidths=[70, 70, 100, 250])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#00796b")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Prevention Tips:</b>", styles['Heading3']))
    for line in prevention.split('. '):
        if line.strip():
            elements.append(Paragraph(f"• {line.strip()}.", styles['Normal']))

    doc.build(elements)
    return filename

# === Routes ===
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    name = request.form.get('name')
    age = request.form.get('age')
    phone = request.form.get('phone')

    if file.filename == '' or not name or not age or not phone:
        return redirect(request.url)

    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    result = predict_image(path)
    data = prescription_data[result]
    treatments = data["treatments"]
    prevention = data["prevention"]

    pdf_filename = f"diagnosis_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    generate_pdf(pdf_filename, result, treatments, prevention, name, age, phone)

    return render_template("result.html",
                           image=filename,
                           result=result,
                           treatments=treatments,
                           prevention=prevention,
                           pdf_filename=pdf_filename)

@app.route('/download/<filename>')
def download(filename):
    import time
    start = time.time()
    response = send_from_directory(PDF_FOLDER, filename, as_attachment=True)
    print(f"📥 PDF sent in {time.time() - start:.3f} sec")
    return response

# === Run App ===
if __name__ == '__main__':
    app.run(debug=True)
