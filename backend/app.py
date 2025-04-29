from flask import Flask, request, jsonify
from flask_cors import CORS
from unidecode import unidecode

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
    message = unidecode(data.get('message', '').lower())

    # Saudação
    if message in ['oi', 'ola', 'bom dia', 'boa tarde', 'boa noite']:
        return jsonify({'response': (
            "Olá! 👋 Eu sou o bot da equipe FURIA CS. Aqui estão algumas coisas que posso te responder:\n"
            "- Quando é o próximo jogo?\n"
            "- Quem são os jogadores ou o treinador?\n"
            "- Quem é o capitão ou o AWPer?\n"
            "- Como funciona o plano Sócio Torcedor?\n"
            "- Onde comprar a camisa da equipe?\n"
            "- Quando será o próximo encontro com fãs?\n"
            "- Qual foi o último resultado?\n"
            "- Quem foi o MVP da última partida?\n"
            "- Qual a classificação da equipe?\n"
            "Mande sua pergunta!"
        )})

    if "time" in message or "equipe" in message:
        nomes = ", ".join(j['pseudonimo'] for j in elenco if "treinador" not in j['posição'].lower())
        return jsonify({'response': f"Os jogadores da FURIA CS2 são: {nomes}."})

    elif "treinador" in message:
        tecnicos = ", ".join(j['pseudonimo'] for j in elenco if "treinador" in j['posição'].lower())
        return jsonify({'response': f"Os treinadores da FURIA são: {tecnicos}."})

    elif "awper" in message:
        awper = next((j for j in elenco if j['posição'].lower() == 'awper'), None)
        if awper:
            return jsonify({'response': f"O AWPer da FURIA é {awper['pseudonimo']} ({awper['nome']})."})

    elif "capitao" in message:
        capitao = next((j for j in elenco if 'fallen' in j['pseudonimo'].lower()), None)
        if capitao:
            return jsonify({'response': f"O capitão da FURIA é {capitao['pseudonimo']} ({capitao['nome']})."})

    elif "jogadores" in message:
        detalhes = ""
        for j in elenco:
            if "treinador" not in j['posição'].lower():
                detalhes += f"{j['pseudonimo']} ({j['nome']}), {j['posição']} - {j['nacionalidade']}\n"
        return jsonify({'response': detalhes})

    elif "proximo jogo" in message:
        return jsonify({'response': "O próximo jogo da FURIA será no dia 05/05/2025 às 18h, com transmissão ao vivo no canal da Gaules na Twitch."})

    elif "socios" in message or "socio torcedor" in message or "vantagens" in message:
        return jsonify({'response': "O plano Sócio Torcedor da FURIA oferece acesso a conteúdos exclusivos, sorteios, desconto em produtos oficiais e prioridade em eventos presenciais. Mais detalhes em: https://furia.gg/sociotorcedor"})

    elif "camisa" in message or "comprar camisa" in message or "loja" in message:
        return jsonify({'response': "Você pode comprar a camisa oficial da FURIA na loja oficial: https://furia.gg/loja"})

    elif "encontro com fa" in message or "meet" in message or "fans" in message:
        return jsonify({'response': "O próximo encontro com fãs será em São Paulo, no dia 15/06/2025, no evento 'FURIA Fan Day'. Fique ligado nas redes sociais da FURIA para mais informações!"})

    elif "ultimo resultado" in message or "ultimo jogo" in message:
        return jsonify({'response': "No último jogo, a FURIA venceu a Natus Vincere por 2 mapas a 1. Mapas: Mirage (13-8), Inferno (6-13), Nuke (13-10)."})

    elif "classificacao" in message or "score" in message:
        return jsonify({'response': "A FURIA atualmente está na 5ª colocação do ranking mundial da HLTV."})

    elif "mvp" in message:
        return jsonify({'response': "O MVP da última partida foi o jogador KSCERATO, com 57 abates e 1.38 de rating."})

    else:
        return jsonify({'response': "Desculpe, não entendi sua pergunta sobre a FURIA. Você pode perguntar sobre o time, próximos jogos, resultados, sócio torcedor e muito mais!"})

if __name__ == '__main__':
    app.run(debug=True)
