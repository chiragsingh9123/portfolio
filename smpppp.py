"""
Portfolio Flask App — Chirag
Run: python app.py
"""

import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ── SMTP CONFIG ── fill in .env ──────────────
SMTP_HOST     = os.environ.get("SMTP_HOST",     "smtp.gmail.com")
SMTP_PORT     = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER     = os.environ.get("SMTP_USER",     "chiragsingh9123@gmail.com")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "ttwawqlouywqxvmq")
YOUR_NAME     = os.environ.get("YOUR_NAME",     "Chirag")
YOUR_EMAIL    = os.environ.get("YOUR_EMAIL",    "chiragsingh9123@gmail.com")

# ─────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index_light.html")


@app.route("/api/send-mail", methods=["POST"])
def send_mail():
    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"success": False, "error": "Invalid request"}), 400

        visitor_email = data.get("to", "").strip()

        # ── validation ──────────────────────────
        if not visitor_email:
            return jsonify({"success": False, "error": "Email address is required"}), 400
        if "@" not in visitor_email or "." not in visitor_email:
            return jsonify({"success": False, "error": "Invalid email address"}), 400

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ── plain text body ──────────────────────
        plain_body = f"""
Hey there!

Thanks for visiting my portfolio terminal. 
I got your email address ({visitor_email}) from the terminal command.

Feel free to reach out to me directly:

  Telegram : @
  Email    : {YOUR_EMAIL}
  GitHub   : github.com/chiragsingh9123

I'm currently open for backend projects, automation systems,
Telegram bots, VoIP integrations, and server management.

Looking forward to connecting!

— {YOUR_NAME}
  Backend Engineer & Server Architect
  Meerut, Uttar Pradesh, India

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sent at: {now}
This email was triggered from chirag.portfolio terminal
        """.strip()

        # ── HTML body ────────────────────────────
        html_body = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap');
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    background:#0a0c0a;
    font-family:'JetBrains Mono',monospace;
    padding:30px 20px;
    color:#c8e6c9;
  }}
  .wrap {{
    max-width:600px;
    margin:0 auto;
    background:#0d110d;
    border:1px solid #2a4a2a;
    border-radius:10px;
    overflow:hidden;
    box-shadow:0 0 40px rgba(0,255,136,0.08);
  }}
  .titlebar {{
    background:#111811;
    padding:12px 20px;
    border-bottom:1px solid #2a4a2a;
    display:flex;
    align-items:center;
    gap:8px;
  }}
  .dot {{ width:12px;height:12px;border-radius:50%;display:inline-block; }}
  .r{{background:#ff5f56;}} .y{{background:#ffbd2e;}} .g{{background:#27c93f;}}
  .ttl {{ color:#558855;font-size:11px;margin:0 auto;letter-spacing:1px; }}
  .body {{ padding:28px 32px; }}
  .prompt {{ color:#00ff88;font-size:13px;margin-bottom:20px; }}
  .prompt .at {{ color:#ffff00; }}
  .prompt .path {{ color:#00ffff; }}
  .greeting {{ font-size:22px;font-weight:700;color:#00ff88;letter-spacing:2px;
    text-shadow:0 0 20px rgba(0,255,136,0.4);margin-bottom:6px; }}
  .sub {{ font-size:12px;color:#558855;letter-spacing:3px;
    text-transform:uppercase;margin-bottom:24px; }}
  .sep {{ border:none;border-top:1px solid #2a4a2a;margin:20px 0; }}
  .msg {{ font-size:14px;color:#b8d8b8;line-height:2;margin-bottom:24px; }}
  .msg .hi {{ color:#e8f5e9;font-weight:600; }}
  .contact-row {{ display:flex;align-items:center;gap:12px;
    padding:10px 0;border-bottom:1px solid #1a2e1a; }}
  .contact-row:last-child {{ border-bottom:none; }}
  .c-icon {{ font-size:16px;width:24px;text-align:center; }}
  .c-label {{ color:#558855;font-size:10px;letter-spacing:2px;
    text-transform:uppercase;width:80px; }}
  .c-val {{ color:#00ffff;font-size:13px; }}
  .badge {{
    display:inline-block;
    background:rgba(0,255,136,0.08);
    border:1px solid rgba(0,255,136,0.25);
    color:#00ff88;
    padding:4px 14px;
    border-radius:3px;
    font-size:11px;
    letter-spacing:1px;
    margin:4px 4px 4px 0;
  }}
  .footer {{
    background:#111811;
    border-top:1px solid #2a4a2a;
    padding:14px 32px;
    font-size:10px;
    color:#558855;
    letter-spacing:1px;
    line-height:1.8;
  }}
  .sig {{ color:#00ff88;font-weight:700;font-size:15px;
    letter-spacing:2px;margin-bottom:4px; }}
  .sig-role {{ color:#00ffff;font-size:11px;letter-spacing:2px;
    text-transform:uppercase;margin-bottom:16px; }}
</style>
</head>
<body>
<div class="wrap">

  <div class="titlebar">
    <span class="dot r"></span>
    <span class="dot y"></span>
    <span class="dot g"></span>
    <span class="ttl">chirag@portfolio — mail reply</span>
  </div>

  <div class="body">

    <div class="prompt">
      <span class="at">chirag</span>@<span class="path">portfolio</span>:~$
      mail {visitor_email}
    </div>

    <div class="greeting">Hey there! 👋</div>
    <div class="sub">Thanks for visiting my portfolio</div>

    <div class="msg">
      You just used the <span class="hi">mail</span> command in my portfolio terminal
      to reach out — that's awesome! I got your address
      <span class="hi">({visitor_email})</span> and wanted to reply right away.
      <br><br>
      I'm currently <span class="hi">open for new projects</span>.
      Feel free to reach out directly through any of the channels below.
    </div>

    <hr class="sep">

    <div style="margin-bottom:16px">
      <div class="contact-row">
        <span class="c-icon">✈️</span>
        <span class="c-label">Telegram</span>
        <span class="c-val">@chirag</span>
      </div>
      <div class="contact-row">
        <span class="c-icon">📧</span>
        <span class="c-label">Email</span>
        <span class="c-val">{YOUR_EMAIL}</span>
      </div>
      <div class="contact-row">
        <span class="c-icon">🐙</span>
        <span class="c-label">GitHub</span>
        <span class="c-val">github.com/chirag</span>
      </div>
      <div class="contact-row">
        <span class="c-icon">📍</span>
        <span class="c-label">Location</span>
        <span class="c-val">Meerut, Uttar Pradesh, India</span>
      </div>
    </div>

    <hr class="sep">

    <div style="margin-bottom:20px;font-size:11px;color:#558855;
      letter-spacing:1px;margin-bottom:8px;">// expertise</div>
    <div>
      <span class="badge">Python</span>
      <span class="badge">Flask</span>
      <span class="badge">Telegram Bot</span>
      <span class="badge">MySQL</span>
      <span class="badge">Linux/VPS</span>
      <span class="badge">Selenium</span>
      <span class="badge">Asterisk ARI</span>
      <span class="badge">Crypto Payments</span>
      <span class="badge">WebSockets</span>
      <span class="badge">Android Auto</span>
    </div>

    <hr class="sep">

    <div class="sig">— {YOUR_NAME}</div>
    <div class="sig-role">Backend Engineer &amp; Server Architect</div>

  </div>

  <div class="footer">
    Sent at {now} &nbsp;·&nbsp;
    Triggered via: chirag.portfolio terminal &nbsp;·&nbsp;
    cmd: mail {visitor_email}
  </div>

</div>
</body>
</html>""".strip()

        # ── build & send ─────────────────────────
        msg = MIMEMultipart("alternative")
        msg["From"]    = f"{YOUR_NAME} <{SMTP_USER}>"
        msg["To"]      = visitor_email
        msg["Subject"] = f"Hey! You reached out via my Portfolio Terminal 👋"
        msg["Reply-To"] = YOUR_EMAIL

        msg.attach(MIMEText(plain_body, "plain"))
        msg.attach(MIMEText(html_body,  "html"))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, visitor_email, msg.as_string())

        logger.info(f"[MAIL] ✓ Sent to {visitor_email} at {now}")
        return jsonify({"success": True})

    except smtplib.SMTPAuthenticationError:
        logger.error("[MAIL] ✗ SMTP auth failed")
        return jsonify({"success": False, "error": "SMTP authentication failed"}), 500

    except smtplib.SMTPRecipientsRefused:
        logger.error(f"[MAIL] ✗ Recipient refused: {visitor_email}")
        return jsonify({"success": False, "error": "Email address was refused by server"}), 500

    except smtplib.SMTPException as e:
        logger.error(f"[MAIL] ✗ SMTP error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

    except Exception as e:
        logger.error(f"[MAIL] ✗ Unexpected: {e}")
        return jsonify({"success": False, "error": "Internal server error"}), 500


@app.route("/health")
def health_check():
    return "OK", 200

import threading
import time
import requests

def keep_alive():
    while True:
        try:
            requests.get("https://chiragsingh.online/health")
            print("self ping")
        except:
            pass
        time.sleep(200)

threading.Thread(target=keep_alive, daemon=True).start()



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5500))
    app.run(host="0.0.0.0", port=port)