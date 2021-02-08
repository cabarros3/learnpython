# projeto - bola mágica. Consiste em fazer uma pergunta a bola e ela vai mostrar uma respota aleatória

respostas = ['Sim', 'Não', 'Talvez', 'Com certeza', 'Espero que não', 'Foi com Deus']

pergunta = str(input('Faça uma pergunta --> '))
mostrar_resposta = random.choice(respostas)


print(f'A bola mágica prevê --> {mostrar_resposta}')
