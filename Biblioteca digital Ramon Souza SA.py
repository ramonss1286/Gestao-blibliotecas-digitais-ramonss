import os
from typing import List, Dict, Any, Union

# --- Definição da Estrutura do Documento ---
# (Idealmente, isso estaria em um módulo 'models.py' no seu projeto)

class Documento:
def __init__(self, id: int, titulo: str, autor: str, ano_publicacao: int, tipo_arquivo: str, caminho_arquivo: str = ""):
self.id = id
self.titulo = titulo
self.autor = autor.strip() # Remove espaços em branco extras
self.ano_publicacao = ano_publicacao
self.tipo_arquivo = tipo_arquivo.lower() # Garante que o tipo seja minúsculo para padronização
self.caminho_arquivo = caminho_arquivo

def __repr__(self):
# Representação para depuração
return f"Documento(ID: {self.id}, Título: '{self.titulo}', Autor: '{self.autor}', Ano: {self.ano_publicacao}, Tipo: '{self.tipo_arquivo}')"

def to_dict(self):
# Converte o objeto Documento para um dicionário (útil para serialização/visualização)
 return {
"id": self.id,
"titulo": self.titulo,
"autor": self.autor,
"ano_publicacao": self.ano_publicacao,
"tipo_arquivo": self.tipo_arquivo,
"caminho_arquivo": self.caminho_arquivo
        }

# --- Funções de Listagem e Organização ---

def listar_documentos_organizados(documentos: List[Documento]) -> Dict[str, List[Documento]]:
documentos_por_tipo = {}

# Define os tipos de arquivo esperados para garantir consistência e ordenação
tipos_esperados = ['pdf', 'epub', 'docx', 'txt', 'mobi', 'azw']

# Inicializa o dicionário com todos os tipos esperados, garantindo que apareçam
# mesmo que não haja documentos para eles.
for tipo in tipos_esperados:
documentos_por_tipo[tipo] = []
# Agrupa os documentos pelo tipo de arquivo
for doc in documentos:
tipo = doc.tipo_arquivo
if tipo in tipos_esperados: # Certifica-se de que estamos lidando com tipos válidos
documentos_por_tipo[tipo].append(doc)
else:
# Opcional: tratar documentos com tipos inesperados, caso haja
print(f"Aviso: Documento '{doc.titulo}' tem um tipo de arquivo inesperado: '{tipo}'. Ignorando.")
# Ordena os documentos dentro de cada grupo de tipo
for tipo, lista_docs in documentos_por_tipo.items():
# Ordena por ano de publicação (crescente) e depois por autor (alfabético crescente)
lista_docs.sort(key=lambda doc: (doc.ano_publicacao, doc.autor))
return documentos_por_tipo

def exibir_documentos_formatado(documentos_organizados: Dict[str, List[Documento]]):
# Ordena os tipos de arquivo para uma exibição consistente
tipos_ordenados = sorted(documentos_organizados.keys())

for tipo in tipos_ordenados:
lista_docs = documentos_organizados[tipo]
if lista_docs: # Só exibe se houver documentos para este tipo
for doc in lista_docs:
print(f"  - Título: {doc.titulo}")
print(f"    Autor: {doc.autor}")
print(f"    Ano: {doc.ano_publicacao}")
print("-" * (25 + len(tipo) + 4 + len(str(len(lista_docs))))) # Linha para separar tipos
else:
print(f"\n--- Tipo de Arquivo: {tipo.upper()} (Nenhum Documento) ---")
print("-" * (25 + len(tipo)))


# --- Exemplo de Uso com 35 Documentos ---

if __name__ == "__main__":
    # Simulação de uma lista de 35 documentos digitais variados
    documentos_exemplo = [
        Documento(1, "A Era da Inteligência Artificial", "Maria Silva", 2023, "pdf", "/docs/ia/era_ia.pdf"),
        Documento(2, "Fundamentos de Estruturas de Dados", "João Santos", 2019, "epub", "/docs/cs/estruturas.epub"),
        Documento(3, "Guia Completo de Python", "Ana Paula", 2021, "pdf", "/docs/prog/python_guia.pdf"),
        Documento(4, "O Universo e suas Galáxias", "Carlos Almeida", 2018, "mobi", "/docs/astronomia/universo.mobi"),
        Documento(5, "História da Arte Moderna", "Laura Costa", 2015, "docx", "/docs/arte/moderna.docx"),
        Documento(6, "Introdução à Economia", "Pedro Souza", 2020, "pdf", "/docs/economia/intro_eco.pdf"),
        Documento(7, "Aventuras no Mundo Digital", "Julia Lima", 2022, "epub", "/docs/ficcao/aventuras_digital.epub"),
        Documento(8, "Receitas Culinárias Brasileiras", "Fernanda Braga", 2017, "txt", "/docs/culinaria/receitas.txt"),
        Documento(9, "Decifrando Algoritmos Complexos", "Maria Silva", 2023, "pdf", "/docs/ia/algoritmos_comp.pdf"), # Mesmo ano/autor
        Documento(10, "Psicologia Cognitiva", "Lucas Pereira", 2016, "azw", "/docs/psicologia/cognitiva.azw"),
        Documento(11, "Desenvolvimento Web com Flask", "Ana Paula", 2021, "pdf", "/docs/prog/flask_web.pdf"), # Mesmo ano/autor
        Documento(12, "Física Quântica para Leigos", "Marcos Nunes", 2019, "epub", "/docs/fisica/quantica.epub"),
        Documento(13, "Biologia Marinha: Ecossistemas", "Mariana Gomes", 2022, "docx", "/docs/biologia/marinha.docx"),
        Documento(14, "Geografia Política Atual", "Roberto Carlos", 2018, "pdf", "/docs/geografia/politica.pdf"),
        Documento(15, "Engenharia de Software Ágil", "João Santos", 2019, "epub", "/docs/cs/agil.epub"), # Mesmo ano/autor
        Documento(16, "Técnicas de Escrita Criativa", "Larissa Faria", 2020, "txt", "/docs/escrita/criativa.txt"),
        Documento(17, "Marketing Digital Estratégico", "Gabriela Neves", 2023, "pdf", "/docs/marketing/digital.pdf"),
        Documento(18, "O Essencial do Machine Learning", "Maria Silva", 2023, "epub", "/docs/ia/machine_learning.epub"), # Mesmo ano/autor
        Documento(19, "Direito Constitucional Brasileiro", "Ricardo Souza", 2017, "pdf", "/docs/direito/const.pdf"),
        Documento(20, "Química Orgânica Avançada", "Beatriz Castro", 2021, "mobi", "/docs/quimica/organica.mobi"),
        Documento(21, "Inteligência Emocional e Liderança", "Fernando Alves", 2022, "azw", "/docs/psicologia/emocional.azw"),
        Documento(22, "Criptografia e Segurança da Informação", "Carlos Almeida", 2018, "pdf", "/docs/seguranca/cripto.pdf"), # Mesmo ano/autor
        Documento(23, "Planejamento Financeiro Pessoal", "Patricia Mendes", 2020, "docx", "/docs/financas/pessoal.docx"),
        Documento(24, "Gestão de Projetos PMBOK", "Pedro Souza", 2020, "pdf", "/docs/gestao/pmbok.pdf"), # Mesmo ano/autor
        Documento(25, "Introdução à Robótica", "João Santos", 2023, "epub", "/docs/robotica/intro_robo.epub"),
        Documento(26, "Design Gráfico Moderno", "Julia Lima", 2022, "pdf", "/docs/design/grafico.pdf"), # Mesmo ano/autor
        Documento(27, "Blockchain e Criptomoedas", "Gustavo Rios", 2021, "txt", "/docs/blockchain/cripto.txt"),
        Documento(28, "Microbiologia e Saúde Pública", "Carolina Viana", 2019, "azw", "/docs/saude/microbiologia.azw"),
        Documento(29, "Metodologias Ágeis em TI", "João Santos", 2019, "pdf", "/docs/cs/metodologias.pdf"), # Mesmo ano/autor
        Documento(30, "Lógica de Programação com JavaScript", "Ana Paula", 2021, "epub", "/docs/prog/js_logica.epub"), # Mesmo ano/autor
        Documento(31, "Filosofia Contemporânea", "André Borges", 2016, "pdf", "/docs/filosofia/contemporanea.pdf"),
        Documento(32, "Geologia dos Solos", "Eduarda Pires", 2022, "docx", "/docs/geologia/solos.docx"),
        Documento(33, "Neurociência e Aprendizagem", "Lucas Pereira", 2016, "mobi", "/docs/psicologia/neuro_aprend.mobi"), # Mesmo ano/autor
        Documento(34, "Inteligência Artificial Aplicada", "Maria Silva", 2023, "pdf", "/docs/ia/ia_aplicada.pdf"), # Mesmo ano/autor
        Documento(35, "Direito Penal: Parte Geral", "Ricardo Souza", 2017, "epub", "/docs/direito/penal.epub") # Mesmo ano/autor
    ]

    print("Iniciando a organização e listagem de 35 documentos digitais...")
    documentos_organizados = listar_documentos_organizados(documentos_exemplo)
    exibir_documentos_formatado(documentos_organizados)

    print("\n" + "="*50)
    print("Teste com uma lista vazia para verificar o comportamento:")
    print("="*50)
    documentos_vazios = []
    documentos_organizados_vazios = listar_documentos_organizados(documentos_vazios)
    exibir_documentos_formatado(documentos_organizados_vazios)