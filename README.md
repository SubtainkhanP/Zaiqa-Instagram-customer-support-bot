# Zaiqa-Instagram-customer-support-bot
# Instagram DM Auto Reply Bot

An automated Instagram Direct Message chatbot built using **Python**, **Flask**, **Meta Webhooks**, and the **Instagram Messaging API**. The bot receives Instagram messages in real-time and responds automatically based on predefined rules.

---

## 🚀 Features

- Receive Instagram Direct Messages in real-time
- Automatic message replies
- Meta Webhook integration
- Flask-based backend server
- Environment variable support using `.env`
- Easy customization of bot responses
- Ngrok support for local development and testing
- Clean and beginner-friendly code structure

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Meta Graph API
- Instagram Messaging API
- Meta Webhooks
- Ngrok
- Requests
- Python Dotenv

---

## 📁 Project Structure

```text
Instagram-DM-Auto-Reply-Bot/
│
├── app.py
├── responses.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/instagram-dm-auto-reply-bot.git
cd instagram-dm-auto-reply-bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```env
ACCESS_TOKEN=YOUR_ACCESS_TOKEN
VERIFY_TOKEN=YOUR_VERIFY_TOKEN
IG_USER_ID=YOUR_INSTAGRAM_BUSINESS_ID
```

---

### 5. Start Flask Server

```bash
python app.py
```

Output:

```text
* Running on http://127.0.0.1:5000
```

---

### 6. Start Ngrok

```bash
ngrok http 5000
```

Copy the HTTPS URL:

```text
https://your-ngrok-url.ngrok-free.app
```

Webhook URL:

```text
https://your-ngrok-url.ngrok-free.app/webhook
```

---

## 🔄 How It Works

1. User sends a DM to Instagram Business Account.
2. Meta Webhook sends the event to Flask.
3. Flask processes the message.
4. `responses.py` generates a reply.
5. Bot sends a response through the Instagram Messaging API.

---

## 💬 Example Commands

### Greeting

**User**

```text
Hi
```

**Bot**

```text
👋 Welcome to ZAIQA Restaurant!

How can I help you today?

1️⃣ Menu
2️⃣ Location
3️⃣ Timings
4️⃣ Delivery
```

---

### Menu

**User**

```text
Menu
```

**Bot**

```text
🍽️ ZAIQA MENU

🍕 Pizza
🍔 Burger
🌯 Shawarma
🍗 BBQ
🥤 Drinks
```

---

### Location

**User**

```text
Location
```

**Bot**

```text
📍 ZAIQA Restaurant
Please visit our restaurant location.
```

---

### Timings

**User**

```text
Timings
```

**Bot**

```text
🕛 Opening Hours
12 PM - 12 AM
Open Daily
```

---

## 📸 Screenshots

### Webhook Verification

- Meta Webhooks connected successfully
- Instagram message events received

### Terminal Logs

```text
========== NEW MESSAGE ==========
Sender: 123456789
Message: Hi

Reply:
👋 Welcome to ZAIQA Restaurant!
```

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

## 👨‍💻 Author

**Subtain Khan**

Developed as a real-world Instagram automation project for restaurant customer support and messaging automation.
