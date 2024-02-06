"""Send email server"""

import os
from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/emails", methods=["POST"])
def send_email():
    """send email API"""
    data = request.json
    to_email = data.get("to")
    subject = data.get("subject")
    body = data.get("body")

    if not to_email or not subject or not body:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = os.getenv("SENDER_ADDRESS")
        msg["To"] = to_email

        # setup the SMTP server
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = os.getenv("SMTP_PORT")
        smtp_username = os.getenv("SMTP_USERNAME")
        smtp_password = os.getenv("SMTP_PASSWORD")

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        return jsonify({"message": "Email sent successfully"}), 200

    except Exception as e:  # pylint: disable=broad-except
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
