import sys
import os
import json
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

MS_BLUE = colors.HexColor("#0078D4")
MS_GRAY = colors.HexColor("#605E5C")
MS_DARK = colors.HexColor("#201F1E")
MS_LIGHT = colors.HexColor("#F3F2F1")


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="MS_Title",
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=28,
        textColor=MS_BLUE,
        spaceAfter=10,
    ))

    styles.add(ParagraphStyle(
        name="MS_Subtitle",
        fontName="Helvetica",
        fontSize=11,
        leading=14,
        textColor=MS_GRAY,
        spaceAfter=16,
    ))

    styles.add(ParagraphStyle(
        name="MS_Header",
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=MS_DARK,
        spaceBefore=12,
        spaceAfter=6,
    ))

    styles.add(ParagraphStyle(
        name="MS_Body",
        fontName="Helvetica",
        fontSize=11,
        leading=16,
        textColor=MS_DARK,
        spaceAfter=4,
    ))

    styles.add(ParagraphStyle(
        name="MS_Bullet",
        fontName="Helvetica",
        fontSize=11,
        leading=16,
        textColor=MS_DARK,
        leftIndent=14,
        spaceAfter=2,
    ))

    styles.add(ParagraphStyle(
        name="MS_Footer",
        fontName="Helvetica-Oblique",
        fontSize=9,
        leading=12,
        textColor=MS_GRAY,
        alignment=1,
    ))

    return styles


def add_section(elements, styles, title, content):
    elements.append(Paragraph(title, styles["MS_Header"]))

    if isinstance(content, list):
        if content:
            for item in content:
                elements.append(Paragraph(f"• {item}", styles["MS_Bullet"]))
        else:
            elements.append(Paragraph("• N/A", styles["MS_Bullet"]))
    else:
        if str(content).strip():
            elements.append(Paragraph(str(content), styles["MS_Body"]))
        else:
            elements.append(Paragraph("N/A", styles["MS_Body"]))

    elements.append(Spacer(1, 8))


def create_divider(width_cm=17):
    divider = Table([[""]], colWidths=[width_cm * cm], rowHeights=[2])
    divider.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), MS_BLUE),
    ]))
    return divider


def main():
    if len(sys.argv) < 2:
        print("❌ Provide JSON input file")
        print("Usage: python analyze.py analysis_input.json")
        return

    input_arg = sys.argv[1]

    try:
        with open(input_arg, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {input_arg}")
        return
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return

    title = data.get("title", "Deep Analysis Report")
    author = data.get("author", "Aman Samriya")
    today = datetime.now().strftime("%Y-%m-%d")

    output_dir = os.path.join(os.getcwd(), "DeepAnalysis")
    os.makedirs(output_dir, exist_ok=True)

    safe_title = "".join(c if c.isalnum() else "_" for c in title)[:50]
    output_path = os.path.join(output_dir, f"Analysis_{today}_{safe_title}.pdf")

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

    # Title
    elements.append(Paragraph(title, styles["MS_Title"]))
    elements.append(Paragraph(
        f"Prepared by <b>{author}</b> &nbsp;|&nbsp; {today}",
        styles["MS_Subtitle"]
    ))
    elements.append(create_divider())
    elements.append(Spacer(1, 14))

    # Sections
    add_section(elements, styles, "💡 What it does", data.get("what_it_does", ""))
    add_section(elements, styles, "🎯 Why it exists", data.get("why_it_exists", ""))
    add_section(elements, styles, "✅ Strengths", data.get("strengths", []))
    add_section(elements, styles, "⚠️ Weaknesses", data.get("weaknesses", []))
    add_section(elements, styles, "🧠 Hidden Issues", data.get("hidden_issues", []))
    add_section(elements, styles, "🚨 Risks", data.get("risks", []))
    add_section(elements, styles, "📈 Scalability", data.get("scalability", ""))
    add_section(elements, styles, "❗ Edge Cases", data.get("edge_cases", []))
    add_section(elements, styles, "🛠 Improvements", data.get("improvements", []))
    add_section(elements, styles, "📊 PM Insights", data.get("pm_insights", []))
    add_section(elements, styles, "🏁 Summary", data.get("summary", ""))

    # Footer
    elements.append(Spacer(1, 18))
    elements.append(create_divider())
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(
        "Generated using Copilot CLI Skill • Microsoft Style",
        styles["MS_Footer"]
    ))

    doc.build(elements)

    print(f"✅ PDF created: {output_path}")

    # Auto-open on Windows
    try:
        os.startfile(output_path)
    except Exception as e:
        print(f"⚠️ Could not auto-open PDF: {e}")


if __name__ == "__main__":
    main()