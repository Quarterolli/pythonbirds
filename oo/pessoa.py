class Pessoa:
    olhos = 2

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
    ivana.olhos = 1
    del ivana.olhos
    print(ighor.__dict__)
    print(ivana.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(ivana.olhos)
    print(ighor.olhos)
    print(id(Pessoa.olhos), id(ivana.olhos), id(ighor.olhos))

