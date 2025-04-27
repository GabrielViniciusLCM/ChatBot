from flask import Flask, request, jsonify
from flask_cors import CORS
from models import Session, Time, Jogador

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    session = Session()

    response = "Desculpe, não entendi sua pergunta."

    if "time" in user_message.lower():
        time = session.query(Time).first()
        if time:
            response = f"O time é '{time.nome}' e joga '{time.jogo_principal}'."
        else:
            response = "Não há times cadastrados ainda."
    elif "jogadores" in user_message.lower():
        jogadores = session.query(Jogador).all()
        if jogadores:
            response = "Jogadores: " + ", ".join([j.nome for j in jogadores])
        else:
            response = "Nenhum jogador cadastrado."
    elif "jogo" in user_message.lower():
        times = session.query(Time).all()
        if times:
            jogos = ", ".join(set([t.jogo_principal for t in times]))
            response = "Jogos principais: " + jogos
        else:
            response = "Nenhum jogo cadastrado."

    session.close()
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
