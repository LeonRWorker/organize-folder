# Importar bibliotecas
import os
import shutil
# Importando variáveis "directory" e "extensions" do arquivo formats.py
from formats import directory , extensions

# Subdiretórios ou arquivos
subdirect = os.listdir(directory)

# Automação de Organização de Arquivos e Pastas
class Organize:

    # Construtor inicial
    def __init__(self, message):
        # Mensagem atribuída no projeto
        self.message = message
    # Função de listagem de arquivos e pastas do diretório principal
    def Search(self):
        # Liste os arquivos e pastas
        for document in subdirect:
            # Chamar função de verificação
            self.Format(document)

    # Função de verificação do formato
    def Format(self, archive):
        # Separar texto
        split = archive.split('.')
        # Pegar última palavra
        ext = len(split) - 1
        # Percorrer lista de tipos
        for extension in extensions:
            # Entensões
            formats = extension[1]
            # Pasta
            folder = extension[0][0]
            # Verificar se o arquivo extensão do arquivo faz parte da lista de extensões da posicial atual
            if formats.count(f'.{split[ext]}') >= 1:
                # Se existir a pasta 
                if os.path.isdir(directory + '\\' + folder):
                    # Chamar função de redirecionamento de pastas
                    self.Move(archive, folder)
                # Se não existir
                else:
                    # Chamar função de criação de pastas
                    self.Folder(archive, folder)


    # Função de criação de pastas
    def Folder(self, archive, folder):
        # Criar pasta do tipo em questão
        os.mkdir(directory + '\\' + folder)
        # Chamar função de redirecionamento das pastas e arquivos
        self.Move(archive, folder)
        
    # Função de redirecionamento das pastas e arquivos - mover pastas ou arquivos
    def Move(self, archive, folder):
        # Mover arquivo para pasta em questão
        shutil.move(directory + '\\' + archive, directory + '\\' + folder)

        
# Oranizador
OrganizeBot = Organize('Automatizando Processo de Organização')
OrganizeBot.Search()