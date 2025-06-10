import os
from typing import List, Dict, Any, Union

# --- Definição da Estrutura do Documento ---
# (Manteremos a classe Documento do exemplo anterior)

class Documento:
    def __init__(self, id: int, titulo: str, autor: str, ano_publicacao: int, tipo_arquivo: str, caminho_arquivo: str = ""):
        self.id = id
        self.titulo = titulo
        self.autor = autor.strip()
        self.ano_publicacao = ano_publicacao
        self.tipo_arquivo = tipo_arquivo.lower()
        self.caminho_arquivo = caminho_arquivo

    def __repr__(self):
        return f"Documento(ID: {self.id}, Título: '{self.titulo}', Autor: '{self.autor}', Ano: {self.ano_publicacao}, Tipo: '{self.tipo_arquivo}')"

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano_publicacao": self.ano_publicacao,
            "tipo_arquivo": self.tipo_arquivo,
            "caminho_arquivo": self.caminho_arquivo
        }

# --- Simulação de Armazenamento de Dados (em memória) ---
# Em um sistema real, isso seria um banco de dados.
biblioteca_digital: List[Documento] = []
next_document_id = 1 # ID sequencial para novos documentos

# --- Funções de Gestão de Documentos (CRUD) ---

def _get_next_id():
    """Gera o próximo ID único para um novo documento."""
    global next_document_id
    current_id = next_document_id
    next_document_id += 1
    return current_id

def adicionar_documento_cli():
    """Permite ao bibliotecário adicionar um novo documento."""
    print("\n--- Adicionar Novo Documento ---")
    titulo = input("Título do Documento: ").strip()
    if not titulo:
        print("Título não pode ser vazio. Operação cancelada.")
        return

    autor = input("Autor do Documento: ").strip()
    if not autor:
        print("Autor não pode ser vazio. Operação cancelada.")
        return

    while True:
        try:
            ano_publicacao_str = input("Ano de Publicação (AAAA): ").strip()
            ano_publicacao = int(ano_publicacao_str)
            if not (1000 <= ano_publicacao <= 2100): # Ano razoável
                print("Ano de publicação inválido. Por favor, insira um ano entre 1000 e 2100.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro para o ano.")

    tipos_validos = ['pdf', 'epub', 'docx', 'txt', 'mobi', 'azw']
    while True:
        tipo_arquivo = input(f"Tipo de Arquivo ({', '.join(tipos_validos)}): ").strip().lower()
        if tipo_arquivo in tipos_validos:
            break
        else:
            print(f"Tipo de arquivo inválido. Por favor, escolha entre: {', '.join(tipos_validos)}.")

    # Em um sistema real, aqui você também teria um input para o caminho do arquivo
    # ou uma rotina para fazer o upload do arquivo físico.
    caminho_arquivo = f"path/to/documents/{titulo.replace(' ', '_').lower()}.{tipo_arquivo}"

    doc_id = _get_next_id()
    novo_documento = Documento(doc_id, titulo, autor, ano_publicacao, tipo_arquivo, caminho_arquivo)
    biblioteca_digital.append(novo_documento)
    print(f"\nDocumento '{titulo}' (ID: {doc_id}) adicionado com sucesso!")

def renomear_documento_cli():
    """Permite ao bibliotecário renomear o título de um documento existente."""
    print("\n--- Renomear Título de Documento ---")
    if not biblioteca_digital:
        print("Nenhum documento na biblioteca para renomear.")
        return

    # Opcional: listar documentos para facilitar a escolha
    print("\nDocumentos Atuais:")
    for doc in biblioteca_digital:
        print(f"  ID: {doc.id}, Título: '{doc.titulo}'")

    while True:
        try:
            doc_id_str = input("Digite o ID do documento que deseja renomear: ").strip()
            doc_id = int(doc_id_str)
            break
        except ValueError:
            print("ID inválido. Por favor, insira um número inteiro.")

    documento_encontrado = None
    for doc in biblioteca_digital:
        if doc.id == doc_id:
            documento_encontrado = doc
            break

    if documento_encontrado:
        print(f"Documento selecionado: '{documento_encontrado.titulo}' (Autor: {documento_encontrado.autor})")
        novo_titulo = input("Digite o novo título para o documento: ").strip()
        if novo_titulo and novo_titulo != documento_encontrado.titulo:
            documento_encontrado.titulo = novo_titulo
            print(f"Título do documento ID {doc_id} atualizado para '{novo_titulo}' com sucesso!")
        elif not novo_titulo:
            print("Novo título não pode ser vazio. Operação cancelada.")
        else:
            print("Novo título é o mesmo que o título atual. Nenhuma alteração feita.")
    else:
        print(f"Documento com ID {doc_id} não encontrado.")

def remover_documento_cli():
    """Permite ao bibliotecário remover um documento."""
    print("\n--- Remover Documento ---")
    if not biblioteca_digital:
        print("Nenhum documento na biblioteca para remover.")
        return

    # Opcional: listar documentos para facilitar a escolha
    print("\nDocumentos Atuais:")
    for doc in biblioteca_digital:
        print(f"  ID: {doc.id}, Título: '{doc.titulo}'")

    while True:
        try:
            doc_id_str = input("Digite o ID do documento que deseja remover: ").strip()
            doc_id = int(doc_id_str)
            break
        except ValueError:
            print("ID inválido. Por favor, insira um número inteiro.")

    documento_removido = False
    for i, doc in enumerate(biblioteca_digital):
        if doc.id == doc_id:
            confirmacao = input(f"Tem certeza que deseja remover '{doc.titulo}' (ID: {doc.id})? (s/n): ").lower().strip()
            if confirmacao == 's':
                biblioteca_digital.pop(i)
                # Em um sistema real, aqui você também excluiria o arquivo físico se ele foi gerenciado pelo sistema.
                print(f"Documento ID {doc_id} ('{doc.titulo}') removido com sucesso!")
            else:
                print("Remoção cancelada.")
            documento_removido = True
            break
    
    if not documento_removido:
        print(f"Documento com ID {doc_id} não encontrado.")

# --- Funções de Listagem e Organização (reaproveitadas) ---

def listar_documentos_organizados(documentos: List[Documento]) -> Dict[str, List[Documento]]:
    """
    Lista todos os documentos digitais organizados por tipo de arquivo,
    com classificação por ano de publicação e nome de autor em ordem alfabética.
    """
    documentos_por_tipo = {}
    tipos_esperados = ['pdf', 'epub', 'docx', 'txt', 'mobi', 'azw']

    for tipo in tipos_esperados:
        documentos_por_tipo[tipo] = []

    for doc in documentos:
        tipo = doc.tipo_arquivo
        if tipo in tipos_esperados:
            documentos_por_tipo[tipo].append(doc)
        # else: Tratamento de tipos inesperados já está na função de adicionar

    for tipo, lista_docs in documentos_por_tipo.items():
        lista_docs.sort(key=lambda doc: (doc.ano_publicacao, doc.autor))

    return documentos_por_tipo

def exibir_documentos_formatado(documentos_organizados: Dict[str, List[Documento]]):
    """
    Exibe os documentos organizados de forma legível no console.
    """
    if not any(documentos_organizados.values()): # Verifica se há algum documento em qualquer categoria
        print("\n--- A biblioteca está vazia. Não há documentos para exibir. ---")
        return

    tipos_ordenados = sorted(documentos_organizados.keys())

    for tipo in tipos_ordenados:
        lista_docs = documentos_organizados[tipo]
        if lista_docs:
            print(f"\n--- Tipo de Arquivo: {tipo.upper()} ({len(lista_docs)} Documentos) ---")
            for doc in lista_docs:
                print(f"  ID: {doc.id}")
                print(f"  Título: {doc.titulo}")
                print(f"    Autor: {doc.autor}")
                print(f"    Ano: {doc.ano_publicacao}")
            print("-" * (25 + len(tipo) + 4 + len(str(len(lista_docs)))))
        else:
            print(f"\n--- Tipo de Arquivo: {tipo.upper()} (Nenhum Documento) ---")
            print("-" * (25 + len(tipo)))

# --- Função Principal da CLI ---

def main_cli():
    """Função principal que executa a interface de linha de comando."""
    print("Bem-vindo ao Sistema de Gerenciamento de Biblioteca Digital!")

    while True:
        print("\n--- Menu Principal ---")
        print("1. Adicionar Documento")
        print("2. Renomear Título de Documento")
        print("3. Remover Documento")
        print("4. Listar Todos os Documentos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            adicionar_documento_cli()
        elif escolha == '2':
            renomear_documento_cli()
        elif escolha == '3':
            remover_documento_cli()
        elif escolha == '4':
            print("\n--- Listando Documentos ---")
            documentos_organizados = listar_documentos_organizados(biblioteca_digital)
            exibir_documentos_formatado(documentos_organizados)
        elif escolha == '5':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")

# --- Inicializa a CLI ---
if __name__ == "__main__":
    # Opcional: Adicionar alguns documentos iniciais para facilitar o teste
    # Se você quiser começar com uma biblioteca vazia, comente as linhas abaixo.
    biblioteca_digital.append(Documento(_get_next_id(), "Introdução a Redes", "Ana Paula", 2020, "pdf", "/docs/redes/intro.pdf"))
    biblioteca_digital.append(Documento(_get_next_id(), "O Poder do Hábito", "Charles Duhigg", 2012, "epub", "/docs/autoajuda/habito.epub"))
    biblioteca_digital.append(Documento(_get_next_id(), "Manual de Git e GitHub", "Carlos Lima", 2021, "pdf", "/docs/prog/git_manual.pdf"))
    biblioteca_digital.append(Documento(_get_next_id(), "A Arte da Guerra", "Sun Tzu", 1900, "txt", "/docs/historia/guerra.txt"))
    biblioteca_digital.append(Documento(_get_next_id(), "A Linguagem Python", "Guido van Rossum", 1991, "epub", "/docs/prog/python_linguagem.epub"))
    
    main_cli()