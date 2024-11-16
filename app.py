from flask import Flask, request
import requests

app = Flask(__name__)

# Вставьте сюда ваш токен
TELEGRAM_TOKEN = "7774866777:AAHIzKvY-uRoE-0-owX8Mj5KwvhdyCUFCsw"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Telegram Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # Проверяем, есть ли сообщение
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_message = data["message"]["text"]

        # Простое ответное сообщение
        response_message = f"Вы сказали: {user_message}"

        # Отправляем ответ пользователю
        send_message(chat_id, response_message)

    return "ok", 200

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
