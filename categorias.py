import json

# Defina os ranges de categorias
categorias = {
    "A00-A09": "Doenças infecciosas intestinais",
    "A15-A19": "Tuberculose",
    "A20-A28": "Algumas doenças bacterianas zoonóticas",
    "A30-A49": "Outras doenças bacterianas",
    "A50-A64": "Infecções de transmissão predominantemente sexual",
    "A65-A69": "Outras doenças por espiroquetas",
    "A70-A74": "Outras doenças causadas por clamídias",
    "A75-A79": "Rickettsioses",
    "A80-A89": "Infecções virais do sistema nervoso central",
    "A90-A99": "Febres por arbovírus e febres hemorrágicas virais",
    "B00-B09": "Infecções virais caracterizadas por lesões de pele e mucosas",
    "B15-B19": "Hepatite viral",
    "B20-B24": "Doença pelo vírus da imunodeficiência humana [HIV]",
    "B25-B34": "Outras doenças por vírus",
    "B35-B49": "Micoses",
    "B50-B64": "Doenças devidas a protozoários",
    "B65-B83": "Helmintíases",
    "B85-B89": "Pediculose, acaríase e outras infestações",
    "B90-B94": "Seqüelas de doenças infecciosas e parasitárias",
    "B95-B97": "Agentes de infecções bacterianas, virais e outros agentes infecciosos",
    "B99-B99": "Outras doenças infecciosas",
    "C00-C97": "Neoplasias [tumores] malignas(os)",
    "C00-C75": "Neoplasias [tumores] malignas(os), declaradas ou presumidas como primárias, de localizações especificadas, exceto dos tecidos linfático, hematopoético e tecidos correlatos",
    "C00-C14": "Neoplasias malignas do lábio, cavidade oral e faringe",
    "C15-C26": "Neoplasias malignas dos órgãos digestivos",
    "C30-C39": "Neoplasias malignas do aparelho respiratório e dos órgãos intratorácicos",
    "C40-C41": "Neoplasias malignas dos ossos e das cartilagens articulares",
    "C43-C44": "Melanoma e outras(os) neoplasias malignas da pele",
    "C45-C49": "Neoplasias malignas do tecido mesotelial e tecidos moles",
    "C50-C50": "Neoplasias malignas da mama",
    "C51-C58": "Neoplasias malignas dos órgãos genitais femininos",
    "C60-C63": "Neoplasias malignas dos órgãos genitais masculinos",
    "C64-C68": "Neoplasias malignas do trato urinário",
    "C69-C72": "Neoplasias malignas dos olhos, do encéfalo e de outras partes do sistema nervoso central",
    "C73-C75": "Neoplasias malignas da tireóide e de outras glândulas endócrinas",
    "C76-C80": "Neoplasias malignas de localizações mal definidas, secundárias e de localizações não especificadas",
    "C81-C96": "Neoplasias [tumores] malignas(os), declaradas ou presumidas como primárias, dos tecidos linfático, hematopoético e tecidos correlatos",
    "C97-C97": "Neoplasias malignas de localizações múltiplas independentes (primárias)",
    "D00-D09": "Neoplasias [tumores] in situ",
    "D10-D36": "Neoplasias [tumores] benignas(os)",
    "D37-D48": "Neoplasias [tumores] de comportamento incerto ou desconhecido"
}

def determinar_categoria(codigo):
    """
    Determina a categoria de um código CID baseado no range.
    """
    for range_cid, categoria in categorias.items():
        inicio, fim = range_cid.split("-")
        if inicio <= codigo <= fim:
            return categoria
    return "Categoria desconhecida"

def adicionar_categorias(arquivo_entrada, arquivo_saida):
    """
    Lê um JSON com códigos CID e adiciona as categorias correspondentes.
    """
    with open(arquivo_entrada, 'r', encoding='utf-8') as file:
        dados = json.load(file)

    for item in dados:
        codigo = item.get("codigo", "")
        item["categoria"] = determinar_categoria(codigo)

    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

# Caminho dos arquivos
arquivo_entrada = 'cid10.json'  # Substitua pelo seu arquivo de entrada
arquivo_saida = 'cids_com_categorias.json'

# Executa o script
adicionar_categorias(arquivo_entrada, arquivo_saida)
