# Script: bin/log_formatter.py
import datetime
import random

logs = [
    "A água saiu da torneira com um atraso de 0.4s. O soluço não foi acústico, foi físico.",
    "O motor do portão girou em silêncio absoluto. A física da trava falhou no impacto.",
    "A madeira da baqueta perdeu o peso. A mecânica de percussão continua, mas o ébano não devolve som.",
    "As três colunas de números subiram. Exatas. Sem memória do rosto de quem as enviou.",
    "A lâmpada de sódio na esquina ilumina o ar, mas não o asfalto. O mundo parou de renderizar o chão.",
    "O cursor pisca na tela cinza. O arquivo não está travado, ele simplesmente deixou de ser lido.",
    "O atrito das roupas não produz som. O tecido desliza sobre a pele como gesso seco.",
    "A luz das telas não projeta sombra no chão do galpão. O Logos está perdendo a profundidade.",
    "O atraso entre o impacto da gota e o som é de exatamente 1.5s. A latência é o único parâmetro real.",
    "O relógio de pulso avança com precisão cirúrgica, enquanto o mundo lá fora desacelera.",
    "Senti o formigamento nas unhas. O cérebro inventa sinais onde a realidade não entrega input.",
    "O portão partido em elo liso. A matéria não rompeu, foi removida do inventário.",
    "O rádio chiando na estática. A falha é a única coisa que ainda possui textura.",
    "O café na cozinha não esfria, ele apenas perde o significado de temperatura.",
    "O nome da rua na placa. Li as letras, mas não reconheci o lugar. O endereço foi deletado."
]

def generate_log():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = random.choice(logs)
    
    formatted = f"--- REGISTRO DE DESALINHAMENTO ---\nID: {random.randint(1000, 9999)}\nDATA: {timestamp}\n{log_content}\n"
    return formatted

if __name__ == "__main__":
    print(generate_log())
