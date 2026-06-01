class Aluno:
    def __init__(self):
        self.notas = []

    def cadastrar_nota(self, nota):
        """Cadastra uma nota válida (0 a 10)"""
        if not isinstance(nota, (int, float)) or nota < 0 or nota > 10:
            raise ValueError("Nota inválida. Deve ser um número entre 0 e 10.")
        self.notas.append(nota)
        return True

    def calcular_media(self):
        """Calcula a média das notas cadastradas"""
        if not self.notas:
            return 0.0
        return round(sum(self.notas) / len(self.notas), 2)

    def verificar_situacao(self):
        """Retorna a situação do aluno conforme as regras"""
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"