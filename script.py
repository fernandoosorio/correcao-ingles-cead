import os

def ler_arquivo_linhas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()  # Ignora a primeira linha
            nome_aluno = linhas[0].strip() if linhas else None  # Salva o nome do aluno
            return nome_aluno, linhas[1:]  # Começa a partir do segundo elemento
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None


def calcular_nota(respostas_aluno, respostas_corretas,mostrar_erros):
    nota = 0
    for questao, resposta_aluno in respostas_aluno.items():
        if questao in respostas_corretas and resposta_aluno.lower() == respostas_corretas[questao].lower():
            nota += 1
        else:
             if mostrar_erros:
                print(f"Errou questão '{questao}' - '{resposta_aluno}' gabarito era '{respostas_corretas[questao]}'.")
    return nota

def main():
    respostas_corretas = {
        '1':'b','2':'a','3':'c','4':'a','5':'c','6':'b','7':'d','8':'c','9':'c','10':'a','11':'b','12':'a','13':'d','14':'c','15':'a',
        '16':'d','17':'d','18':'d','19':'b','20':'e','21':'d','22':'b','23':'a','24':'d','25':'a','26':'c','27':'c','28':'e','29':'b',
        '30':'d','31':'e','32':'b','33':'a','34':'c','35':'d','36':'b','37':'d','38':'d','39':'e','40':'a','41':'a','42':'d','43':'b',
        '44':'a','45':'a','46':'c','47':'a','48':'c','49':'d','50':'c'
    }
    
    diretorio_atual = os.getcwd()
    arquivos_txt = [arquivo for arquivo in os.listdir(diretorio_atual) if arquivo.endswith('.txt')]

    mostrar_erros = input("Deseja mostrar os erros? (S/N): ").lower() == 's'

    for nome_arquivo in arquivos_txt:
        print(f"Lendo o arquivo: {nome_arquivo}")
        nome_aluno, linhas = ler_arquivo_linhas(nome_arquivo)
    
        respostas_aluno = {}

        for linha in linhas:
            questao, resposta = linha.split()
            respostas_aluno[questao] = resposta

        
        nota_total = calcular_nota(respostas_aluno, respostas_corretas, mostrar_erros)
        total_questoes = len(respostas_corretas)
        
        print(f"A nota do aluno {nome_aluno} é: {nota_total}/{total_questoes}")
        print('------------    Fim Execução para aluno  -------------------')
        print('\n')

if __name__ == "__main__":
    main()

