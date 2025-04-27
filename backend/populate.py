from models import Session, Time, Jogador

# Criar sessão
session = Session()

# Criar time
time = Time(nome="Dragões da Areia", jogo_principal="Valorant")
session.add(time)
session.commit()

# Criar jogadores
jogadores = [
    Jogador(nome="Ana", posicao="Atiradora", time_id=time.id),
    Jogador(nome="Bruno", posicao="Suporte", time_id=time.id),
    Jogador(nome="Carlos", posicao="Tank", time_id=time.id),
    Jogador(nome="Daniela", posicao="Assassina", time_id=time.id)
]

session.add_all(jogadores)
session.commit()
session.close()

print("Banco de dados populado com sucesso!")
