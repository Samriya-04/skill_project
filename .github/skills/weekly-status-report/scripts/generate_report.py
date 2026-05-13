import sys, json, os, subprocess
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)

# ===== Microsoft-style colors =====
MS_BLUE = colors.HexColor("#0078D4")
MS_DARK = colors.HexColor("#201F1E")
MS_GRAY = colors.HexColor("#605E5C")
MS_LIGHT = colors.HexColor("#F3F2F1")


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="MSTitle",
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=28,
        textColor=MS_BLUE,
        spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name="MSSubtitle",
        fontName="Helvetica",
        fontSize=11,
        leading=14,
        textColor=MS_GRAY,
        spaceAfter=18,
    ))
    styles.add(ParagraphStyle(
        name="MSHeader",
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=MS_DARK,
        spaceBefore=14,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="MSBullet",
        fontName="Helvetica",
        fontSize=11,
        leading=16,
        textColor=MS_DARK,
        leftIndent=14,
        bulletIndent=0,
        spaceAfter=2,
    ))
    # Box header style (white text on colored header)
    styles.add(ParagraphStyle(
        name="BoxHeader",
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=14,
        textColor=colors.white,
        leftIndent=0,
        spaceAfter=0,
    ))
    styles.add(ParagraphStyle(
        name="BoxContent",
        fontName="Helvetica",
        fontSize=11,
        leading=16,
        textColor=MS_DARK,
        leftIndent=0,
        spaceAfter=0,
    ))
    return styles


def add_section(elements, styles, title, items):
    # Build a boxed section with a colored header and light background content
    if items is None:
        items = []
    header_para = Paragraph(title, styles["BoxHeader"])
    if not items:
        content_html = "• N/A"
    else:
        content_html = "<br/>".join([f"• {item}" for item in items])
    content_para = Paragraph(content_html, styles["BoxContent"]) 
    tbl = Table([[header_para], [content_para]], colWidths=[17 * cm])
    tbl.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, MS_BLUE),
        ("BACKGROUND", (0, 0), (-1, 0), MS_BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("BACKGROUND", (0, 1), (-1, 1), MS_LIGHT),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(Spacer(1, 8))
    elements.append(tbl)
    elements.append(Spacer(1, 8))


def main():
    if len(sys.argv) < 2:
        print("❌ Provide JSON input file")
        return

    arg = sys.argv[1]
    try:
        with open(arg, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = json.loads(arg)

    today = datetime.now().strftime("%Y-%m-%d")
    title = data.get("title", f"Weekly Status Report")
    author = data.get("author", "Aman Samriya")

    pdf_name = f"WeeklyStatusReport_{today}.pdf"
    output_path = os.path.join(os.getcwd(), pdf_name)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
        title=title,
        author=author,
    )

    styles = build_styles()
    elements = []

    # Header
    elements.append(Paragraph(title, styles["MSTitle"]))
    elements.append(Paragraph(
        f"Prepared by <b>{author}</b> &nbsp;|&nbsp; {today}",
        styles["MSSubtitle"]
    ))

    # Accent divider
    divider = Table([[""]], colWidths=[17 * cm], rowHeights=[2])
    divider.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), MS_BLUE),
    ]))
    elements.append(divider)
    elements.append(Spacer(1, 12))

    # Sections
    add_section(elements, styles, "Highlights", data.get("highlights", []))
    add_section(elements, styles, "Progress", data.get("progress", []))
    add_section(elements, styles, "Blockers / Risks", data.get("blockers", []))
    add_section(elements, styles, "Next Week Plan", data.get("next_week", []))
    add_section(elements, styles, "Asks / Help Needed", data.get("asks", []))

    # Footer style
    elements.append(Spacer(1, 24))
    footer = Table([[""]], colWidths=[17 * cm], rowHeights=[1])
    footer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), MS_LIGHT),
    ]))
    elements.append(footer)
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(
        "Generated using Copilot CLI Skill • Microsoft Style",
        ParagraphStyle(
            "footer",
            fontName="Helvetica-Oblique",
            fontSize=9,
            textColor=MS_GRAY,
            alignment=1,
        )
    ))

    doc.build(elements)

    print(f"✅ PDF created: {output_path}")

    # Auto open PDF
    try:
        os.startfile(output_path)
    except Exception as e:
        print(f"⚠️ Could not auto-open: {e}")


if __name__ == "__main__":
    main()