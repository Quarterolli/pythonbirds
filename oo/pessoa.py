class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    ighor = Pessoa(nome='Ighor')
    ivana = Pessoa(ighor, nome='Ivana')
    print(Pessoa.cumprimentar(ivana))
    print(id(ivana))
    print(ivana.cumprimentar())
    print(ivana.nome)
    print(ivana.idade)
    for filho in ivana.filhos:
        print(filho.nome)
    ivana.sobrenome = 'Quarterolli'
    del ivana.filhos
    print(ivana.__dict__)
    print(ighor.__dict__)
