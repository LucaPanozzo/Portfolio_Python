class Dipendente:

    def __init__(self, nome):
        self.nome = nome
        self.attivita = 0
        print(self.nome, "creato")

    def lavora(self):
        self.attivita = self.attivita + 1
        print(self.nome, "attività completate:", self.attivita)


class Sviluppatore(Dipendente):

    def __init__(self, nome, linguaggio):
        
        super().__init__(nome)
        
        self.linguaggio = linguaggio
        self.progetti = 0

    def completa_progetto(self):
        self.progetti = self.progetti + 1
        self.lavora()
        print(self.nome, "progetti completati:", self.progetti)
        print("Linguaggio principale:", self.linguaggio)


dipendente = Dipendente("Anna")
dipendente.lavora()

sviluppatore = Sviluppatore("Marco", "Python")
sviluppatore.lavora()
sviluppatore.completa_progetto()

print(dir(sviluppatore))
