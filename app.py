import yaml
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import styles, colors


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
    stylesheet['Title'].textColor = colors.blue

    stylesheet['Heading3'].textColor = colors.purple

    stylesheet['BodyText'].spaceBefore = 2

    for section in data:
        if "section" in section:
            story.append(
                Paragraph(section["section"]["heading"], stylesheet["Title"]))
            for subsection in section["section"]["content"]:
                if "subsection" in subsection:
                    story.append(
                        Paragraph(subsection["subsection"]["heading"], stylesheet["Heading3"]))
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


# Addition styling options:
# stylesheet['Title'].fontName = 'Helvetica'
# stylesheet['Title'].fontSize = 14
# stylesheet['Title'].leading = 18
# stylesheet['Title'].textColor = colors.blue
# stylesheet['Title'].backColor = colors.yellow
# stylesheet['Title'].borderColor = colors.red
# stylesheet['Title'].borderWidth = 1
# stylesheet['Title'].borderPadding = 5
# stylesheet['Title'].alignment = 1  # Center alignment

# Pre-defined styles:
# Normal: Basic style generally used for body text.
# BodyText: Also intended for body text with some customization options.
# Title: Intended for title text, usually larger and potentially bold compared to body text.
# Heading1, Heading2, ..., Heading6: These styles are for different levels of headings, with Heading1 being the highest level (usually used for main section titles) and Heading6 being the lowest level (used for subsections at several levels deep).
# Italic: A style where the text is italicized.
# Bold: A style where the text is bolded.
# Bullet: A style intended for bulleted lists.
# Definition: A style intended for definition lists.
# Code: A style intended for code snippets, often using a monospaced font.
