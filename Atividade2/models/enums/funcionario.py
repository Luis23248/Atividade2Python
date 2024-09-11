from Atividade2.models.enums.Setor import Setor
from Atividade2.models.enums.Sexo import Sexo


class Funcionario:

    def __init__(self, id: int, nome:str, cpf:str, rg:str, matricula:str, data_nascimento: str, sexo: Sexo, setor: Setor, salario:float, telefone:str,email:str,endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.setor = setor
        self.salario = salario
        self.telefone = telefone
        self.email = email
        self.endereco = endereco



    def __str__(self) -> str:
        return(
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatricula: {self.matricula}"
            f"\nData de nascimento: {self.data_nascimento}"
            f"\nSexo: {self.sexo}"
            f"\nSetor: {self.setor}"
            f"\nSalário: {self.salario}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nEndereço: {self.endereco}) 
        
