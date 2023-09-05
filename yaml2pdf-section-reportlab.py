import yaml
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

# Load the YAML file
with open('control_catalog.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# Create a new PDF document
pdf = SimpleDocTemplate("control_catalog.pdf", pagesize=letter)
content = []

# Extract data and create a structured PDF
styles = getSampleStyleSheet()
metadata = data["catalog"]["metadata"]

# Adding metadata details
content.append(Paragraph("Security Control Catalog", styles['Title']))
content.append(Paragraph(f'Title: {metadata["title"]}', styles['BodyText']))
content.append(
    Paragraph(f'Version: {metadata["version"]}', styles['BodyText']))
content.append(
    Paragraph(f'Published Date: {metadata["published"]}', styles['BodyText']))
content.append(
    Paragraph(f'Last Modified: {metadata["last-modified"]}', styles['BodyText']))
content.append(
    Paragraph(f'OSCAL Version: {metadata["oscal-version"]}', styles['BodyText']))
content.append(Spacer(1, 12))

# Adding control group details
for control_group in data["catalog"]["groups"]:
    content.append(
        Paragraph(f'Control Group ID: {control_group["id"]}', styles['Heading2']))
    content.append(Paragraph(
        f'Control Group Title: {control_group["title"]}', styles['BodyText']))
    content.append(Spacer(1, 12))

    # Adding individual control details
    for control in control_group["controls"]:
        content.append(
            Paragraph(f'Control ID: {control["id"]}', styles['Heading3']))
        content.append(
            Paragraph(f'Control Title: {control["title"]}', styles['BodyText']))
        content.append(
            Paragraph(f'Priority: {control["priority"]}', styles['BodyText']))
        content.append(Paragraph("Description", styles['Heading4']))
        content.append(
            Paragraph(control["statements"]["description"], styles['BodyText']))
        content.append(Paragraph("Guidance", styles['Heading4']))
        content.append(
            Paragraph(control["statements"]["guidance"], styles['BodyText']))
        content.append(Paragraph("References", styles['Heading4']))
        content.append(
            Paragraph(", ".join(control["properties"][0]["values"]), styles['BodyText']))
        content.append(Spacer(1, 12))

    content.append(PageBreak())

# Build the PDF with the content list
pdf.build(content)
