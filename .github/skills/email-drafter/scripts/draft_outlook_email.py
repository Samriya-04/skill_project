import sys
import json
import win32com.client

def create_outlook_draft(subject, body, to=""):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)  # 0 = MailItem

    mail.Subject = subject
    mail.HTMLBody = body.replace("\n", "<br>")
    
    if to:
        mail.To = to

    mail.Display(True)  # Opens draft window
    print("✅ Outlook draft created. Just review and click Send.")

def main():
    if len(sys.argv) < 2:
        print("❌ Provide JSON input")
        return

    arg = sys.argv[1]

    # Allow input as file or JSON string
    try:
        with open(arg, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = json.loads(arg)

    subject = data.get("subject", "Draft Email")
    body = data.get("body", "")
    to = data.get("to", "")

    create_outlook_draft(subject, body, to)

if __name__ == "__main__":
    main()