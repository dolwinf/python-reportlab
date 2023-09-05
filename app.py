import yaml
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import styles


def parse_yaml(yaml_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    return data


def create_pdf(data, output_pdf):
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    story = []
    stylesheet = styles.getSampleStyleSheet()

    # Customizations
    stylesheet['Title'].alignment = 0
    stylesheet['Title'].fontSize = 12
    stylesheet['Title'].spaceAfter = 2
    stylesheet['BodyText'].spaceBefore = 2

    for section in data:
        if "heading" in section:
            story.append(Paragraph(section["heading"], stylesheet["Title"]))
        if "paragraph" in section:
            story.append(
                Paragraph(section["paragraph"], stylesheet["BodyText"]))
        story.append(Spacer(1, 25))  # Space between each set of data

    doc.build(story)


def main():
    yaml_file = "test.yaml"
    output_pdf = "output.pdf"

    data = parse_yaml(yaml_file)
    create_pdf(data, output_pdf)


if __name__ == "__main__":
    main()
