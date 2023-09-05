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
        if "section" in section:
            story.append(
                Paragraph(section["section"]["heading"], stylesheet["Title"]))
            for subsection in section["section"]["content"]:
                if "subsection" in subsection:
                    story.append(
                        Paragraph(subsection["subsection"]["heading"], stylesheet["BodyText"]))
                    story.append(
                        Paragraph(subsection["subsection"]["paragraph"], stylesheet["BodyText"]))
                story.append(Spacer(1, 25))
        story.append(Spacer(1, 25))

    doc.build(story)


def main():
    yaml_file = "test.yaml"
    output_pdf = "output.pdf"

    data = parse_yaml(yaml_file)
    create_pdf(data, output_pdf)


if __name__ == "__main__":
    main()
