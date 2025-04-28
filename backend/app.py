from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Banco de informações fixas
elenco = [
    {'pseudonimo': 'yuurih', 'nome': 'Yuri Santos', 'nacionalidade': 'Brasil', 'posição': 'Rifler'},
    {'pseudonimo': 'KSCERATO', 'nome': 'Kaike Cerato', 'nacionalidade': 'Brasil', 'posição': 'Rifler'},
    {'pseudonimo': 'FalleN', 'nome': 'Gabriel Toledo', 'nacionalidade': 'Brasil', 'posição': 'Rifler'},
    {'pseudonimo': 'molodoy', 'nome': 'Danil Golubenko', 'nacionalidade': 'Cazaquistão', 'posição': 'AWPer'},
    {'pseudonimo': 'YEKINDAR', 'nome': 'Mareks Gaļinskis', 'nacionalidade': 'Letônia', 'posição': 'Rifler'},
    {'pseudonimo': 'sidde', 'nome': 'Sid Macedo', 'nacionalidade': 'Brasil', 'posição': 'Treinador'},
    {'pseudonimo': 'Hepa', 'nome': 'Juan Borges', 'nacionalidade': 'Espanha', 'posição': 'Treinador assistente'}
]

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '').lower()

    # Regras simples de interpretação
    if "time" in message or "equipe" in message:
        nomes = ", ".join(jogador['pseudonimo'] for jogador in elenco if "Treinador" not in jogador['posição'])
        return jsonify({'response': f"Os jogadores da FURIA CS2 são: {nomes}."})
    
    elif "treinador" in message:
        treinadores = ", ".join(jogador['pseudonimo'] for jogador in elenco if "Treinador" in jogador['posição'])
        return jsonify({'response': f"Os treinadores da FURIA são: {treinadores}."})
    
    elif "awper" in message:
        awper = next((j for j in elenco if j['posição'].lower() == 'awper'), None)
        if awper:
            return jsonify({'response': f"O AWPer da FURIA é {awper['pseudonimo']} ({awper['nome']})."})
    
    elif "capitão" in message:
        capitao = next((j for j in elenco if 'fallen' in j['pseudonimo'].lower()), None)
        if capitao:
            return jsonify({'response': f"O capitão da equipe de CS da FURIA é {capitao['pseudonimo']} ({capitao['nome']})."})
    
    elif "jogadores" in message:
        detalhes = ""
        for jogador in elenco:
            if "Treinador" not in jogador['posição']:
                detalhes += f"{jogador['pseudonimo']} ({jogador['nome']}), {jogador['posição']} - {jogador['nacionalidade']}\n"
        return jsonify({'response': detalhes})

    else:
        return jsonify({'response': 'Desculpe, não entendi sua pergunta sobre a FURIA. Pode reformular?'})

if __name__ == '__main__':
    app.run(debug=True)
