"""
Resolução do desafio: 
Crie uma classe ContaBancaria com métodos para depositar, sacar e verificar saldo. 
Adicione tratamento de exceções para saques que excedam o saldo disponível.

Desafio referente aos meus estudos de Objetos em Python.
"""

# Criar exceção
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_disponivel, valor_saque):
        super().__init__(f"Saldo insuficiente para sacar {valor_saque}. Saldo disponível: {saldo_disponivel}")
        self.saldo_disponivel = saldo_disponivel
        self.valor_saque = valor_saque

# Criação da classe e seus métodos
class ContaBancaria():
  def __init__(self, id, saldo):
    self.id = id
    self.saldo = saldo

  def verificarSaldo(self):
    return f'O saldo da conta {self.id} é de: R${self.saldo}'

  def depositar(self, valor):
      self.saldo += valor
      return f'Depósito de R${valor} realizado'

  def sacar(self, valor):
      try:
          if valor <= self.saldo:
              self.saldo -= valor
              return f'Saque de R${valor} realizado'
          else:
              raise SaldoInsuficienteError(self.saldo, valor)
      except SaldoInsuficienteError as e:
          return str(e)


conta = ContaBancaria(1, 1000)
print(conta.verificarSaldo())
print(conta.depositar(500))
print(conta.verificarSaldo())
print(conta.sacar(1600))
print(conta.sacar(1200))
print(conta.verificarSaldo())