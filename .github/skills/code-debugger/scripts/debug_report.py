import sys, os, json
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted
)

MS_BLUE = colors.HexColor("#0078D4")
MS_DARK = colors.HexColor("#201F1E")
MS_GRAY = colors.HexColor("#605E5C")
MS_LIGHT = colors.HexColor("#F3F2F1")
MS_CODEBG = colors.HexColor("#F5F5F5")


def build_styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="MSTitle", fontName="Helvetica-Bold",
                         fontSize=22, leading=28, textColor=MS_BLUE, spaceAfter=10))
    s.add(ParagraphStyle(name="MSSubtitle", fontName="Helvetica",
                         fontSize=11, leading=14, textColor=MS_GRAY, spaceAfter=18))
    s.add(ParagraphStyle(name="MSHeader", fontName="Helvetica-Bold",
                         fontSize=14, leading=18, textColor=MS_DARK,
                         spaceBefore=14, spaceAfter=6))
    s.add(ParagraphStyle(name="MSBody", fontName="Helvetica",
                         fontSize=11, leading=16, textColor=MS_DARK,
                         spaceAfter=6))
    s.add(ParagraphStyle(name="MSBullet", fontName="Helvetica",
                         fontSize=11, leading=16, textColor=MS_DARK,
                         leftIndent=14, spaceAfter=2))
    s.add(ParagraphStyle(name="MSCode", fontName="Courier",
                         fontSize=9, leading=12, textColor=MS_DARK,
                         backColor=MS_CODEBG, leftIndent=6, rightIndent=6))
    return s


def section_header(elements, styles, text):
    elements.append(Paragraph(text, styles["MSHeader"]))


def bullets(elements, styles, items):
    if not items:
        elements.append(Paragraph("• N/A", styles["MSBullet"]))
        return
    for i in items:
        elements.append(Paragraph(f"• {i}", styles["MSBullet"]))


def code_block(elements, styles, code):
    if not code:
        code = "# (no code provided)"
    elements.append(Preformatted(code, styles["MSCode"]))
    elements.append(Spacer(1, 6))


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
    title = data.get("title", "Debug Report")
    author = data.get("author", "Aman Samriya")

    # Folder
    out_dir = os.path.join(os.getcwd(), "DebugReports")
    os.makedirs(out_dir, exist_ok=True)
    safe_title = "".join(c if c.isalnum() else "_" for c in title)[:40]
    output_path = os.path.join(out_dir, f"DebugReport_{today}_{safe_title}.pdf")

    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.8*cm, bottomMargin=1.8*cm,
        title=title, author=author
    )

    styles = build_styles()
    elements = []

    # Title block
    elements.append(Paragraph(f"🛠️ {title}", styles["MSTitle"]))
    elements.append(Paragraph(
        f"Prepared by <b>{author}</b> &nbsp;|&nbsp; {today}",
        styles["MSSubtitle"]
    ))

    # Divider
    divider = Table([[""]], colWidths=[17*cm], rowHeights=[2])
    divider.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), MS_BLUE)]))
    elements.append(divider)
    elements.append(Spacer(1, 14))

    # Symptom
    section_header(elements, styles, "🩺 Symptom")
    elements.append(Paragraph(data.get("symptom", "N/A"), styles["MSBody"]))

    # Root cause
    section_header(elements, styles, "🔬 Likely Root Cause")
    elements.append(Paragraph(data.get("root_cause", "N/A"), styles["MSBody"]))

    # Reasoning
    section_header(elements, styles, "🧠 Reasoning")
    bullets(elements, styles, data.get("reasoning", []))

    # Code Before
    section_header(elements, styles, "❌ Code Before")
    code_block(elements, styles, data.get("code_before", ""))

    # Code After
    section_header(elements, styles, "✅ Suggested Fix")
    code_block(elements, styles, data.get("code_after", ""))

    # Tests
    section_header(elements, styles, "🧪 Test To Prevent Recurrence")
    code_block(elements, styles, data.get("tests", ""))

    # Prevention
    section_header(elements, styles, "🚀 Prevention Tips")
    bullets(elements, styles, data.get("prevention", []))

    # Severity table
    section_header(elements, styles, "📊 Severity & Priority")
    sev_data = [
        ["Field", "Value"],
        ["Severity", data.get("severity", "N/A")],
        ["Impact", data.get("impact", "N/A")],
        ["Fix Complexity", data.get("fix_complexity", "N/A")],
        ["Priority", data.get("priority", "N/A")],
    ]
    tbl = Table(sev_data, colWidths=[5*cm, 12*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), MS_BLUE),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, MS_LIGHT]),
        ("GRID", (0,0), (-1,-1), 0.4, MS_GRAY),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(tbl)
    elements.append(Spacer(1, 14))

    # Summary
    section_header(elements, styles, "🏁 Summary")
    elements.append(Paragraph(data.get("summary", "N/A"), styles["MSBody"]))

    # Footer
    elements.append(Spacer(1, 24))
    footer = Table([[""]], colWidths=[17*cm], rowHeights=[1])
    footer.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), MS_LIGHT)]))
    elements.append(footer)
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(
        "Generated using Copilot CLI Skill • Microsoft Style",
        ParagraphStyle("footer", fontName="Helvetica-Oblique",
                       fontSize=9, textColor=MS_GRAY, alignment=1)
    ))

    doc.build(elements)
    print(f"✅ Debug report created: {output_path}")

    # Auto open
    try:
        os.startfile(output_path)
    except Exception as e:
        print(f"⚠️ Could not auto-open: {e}")


if __name__ == "__main__":
    main()