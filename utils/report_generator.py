from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(report_text, filename="resume_analysis_report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []


    title = Paragraph(
        "AI Resume Analyzer Report",
        styles["Title"]
    )

    story.append(title)
    story.append(Spacer(1, 20))


    lines = report_text.split("\n")


    for line in lines:

        if line.strip():

            paragraph = Paragraph(
                line,
                styles["BodyText"]
            )

            story.append(paragraph)
            story.append(Spacer(1, 8))


    doc.build(story)


    return filename