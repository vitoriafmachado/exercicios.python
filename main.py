class Prato:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self):
        self.pratos = []  # Lista para armazenar os pratos
        self.total = 0.0  # Total do pedido

    def adicionar_prato(self, prato):
        self.pratos.append(prato)  # Adiciona o prato na lista de pratos
        self.total += prato.preco  # Atualiza o total do pedido com o preço do prato

    def mostrar_pedido(self):
        for prato in self.pratos:
            print(f"{prato.nome} - R$ {prato.preco:.2f}")
        print(f"Total: R$ {self.total:.2f}")

# Criando os pratos
prato1 = Prato("Pizza", 20.00)
prato2 = Prato("Sopa", 12.00)
prato3 = Prato("Sorvete", 6.00)

# Criando um pedido
pedido = Pedido()

# Adicionando pratos ao pedido
pedido.adicionar_prato(prato1)
pedido.adicionar_prato(prato2)
pedido.adicionar_prato(prato3)

# Mostrar o pedido atualizado
pedido.mostrar_pedido()
