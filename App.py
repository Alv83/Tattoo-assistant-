from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configura tu clave de OpenAI aquí
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")

    if not incoming_msg:
        return "No message received", 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente para un estudio de tatuajes. Ayudas a los clientes a resolver dudas y agendar citas."},
                {"role": "user", "content": incoming_msg}
            ]
        )
        reply = response.choices[0].message["content"]
    except Exception as e:
        reply = "Lo siento, hubo un error al procesar tu mensaje."

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
