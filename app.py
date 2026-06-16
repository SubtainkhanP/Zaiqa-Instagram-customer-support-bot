import os
import json
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from responses import get_response

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Credentials
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
IG_USER_ID = os.getenv("IG_USER_ID")

# Instagram Messaging API
GRAPH_API_URL = f"https://graph.facebook.com/v18.0/{IG_USER_ID}/messages"

# Store processed message IDs to avoid duplicate replies
processed_messages = set()


def send_message(recipient_id, message_text):
    """Send message to Instagram user"""

    payload = {
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    }

    params = {
        "access_token": ACCESS_TOKEN
    }

    try:
        response = requests.post(
            GRAPH_API_URL,
            params=params,
            json=payload,
            timeout=10
        )

        print("\n===== META RESPONSE =====")
        print("Status:", response.status_code)
        print("Response:", response.text)
        print("=========================\n")

        return response.status_code == 200

    except Exception as e:
        print("Send Message Error:", e)
        return False


@app.route("/", methods=["GET"])
def home():
    return "Instagram Bot is Running!", 200


@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    # Webhook Verification
    if request.method == "GET":

        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        print("Verification Request Received")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("Webhook verified successfully")
            return challenge, 200

        print("Verification failed")
        return "Verification failed", 403

    # Incoming Messages
    body = request.get_json()

    # print("\n===== WEBHOOK RECEIVED =====")
    # print(json.dumps(body, indent=2))
    # print("============================\n")

    if body.get("object") == "instagram":

        for entry in body.get("entry", []):

            for messaging in entry.get("messaging", []):

                # Ignore events without message object
                if "message" not in messaging:
                    continue

                message = messaging["message"]

                # Ignore bot echoes
                if message.get("is_echo"):
                    # print("Echo ignored")
                    continue

                message_id = message.get("mid")

                # Ignore duplicate messages
                if message_id in processed_messages:
                    # print(f"Duplicate ignored: {message_id}")
                    continue

                processed_messages.add(message_id)

                sender_id = messaging.get("sender", {}).get("id")
                recipient_id = messaging.get("recipient", {}).get("id")
                message_text = message.get("text")

                if not sender_id or not message_text:
                    continue

                # print("\n===== NEW MESSAGE =====")
                # print("Message ID:", message_id)
                # print("Sender:", sender_id)
                # print("Recipient:", recipient_id)
                # print("Text:", message_text)
                print("=======================\n")

                # Generate reply
                reply_text = get_response(message_text)

                print("Reply:", reply_text)

                # Send reply
                send_message(
                    recipient_id=sender_id,
                    message_text=reply_text
                )

    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":

    # print("\n===== CONFIG =====")
    # print("IG_USER_ID:", IG_USER_ID)
    # print("VERIFY_TOKEN:", VERIFY_TOKEN)
    # print("ACCESS_TOKEN LOADED:", ACCESS_TOKEN is not None)
    # print("==================\n")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )