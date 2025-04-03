import json

# Defina os ranges de categorias
categorias = {
    "A00-A09": "Doencas infecciosas intestinais",
    "A15-A19": "Tuberculose",
    "A20-A28": "Algumas Doencas bacterianas zoonoticas",
    "A30-A49": "Outras Doencas bacterianas",
    "A50-A64": "Infecções de transmissao predominantemente sexual",
    "A65-A69": "Outras Doencas por espiroquetas",
    "A70-A74": "Outras Doencas causadas por clamidias",
    "A75-A79": "Rickettsioses",
    "A80-A89": "Infecções virais do sistema nervoso central",
    "A90-A99": "Febres por arbovirus e febres hemorragicas virais",
    "B00-B09": "Infecções virais caracterizadas por lesões de pele e mucosas",
    "B15-B19": "Hepatite viral",
    "B20-B24": "Doença pelo virus da imunodeficiencia humana [HIV]",
    "B25-B34": "Outras Doencas por virus",
    "B35-B49": "Micoses",
    "B50-B64": "Doencas devidas a protozoarios",
    "B65-B83": "Helmintiases",
    "B85-B89": "Pediculose, acariase e outras infestações",
    "B90-B94": "Seqüelas de Doencas infecciosas e parasitarias",
    "B95-B97": "Agentes de infecções bacterianas, virais e outros agentes infecciosos",
    "B99-B99": "Outras Doencas infecciosas",
    "C00-C97": "Neoplasias [tumores] malignas(os)",
    "C00-C75": "Neoplasias [tumores] malignas(os), declaradas ou presumidas como primarias, de localizações especificadas, exceto dos tecidos linfatico, hematopoético e tecidos correlatos",
    "C00-C14": "Neoplasias malignas do labio, cavidade oral e faringe",
    "C15-C26": "Neoplasias malignas dos orgaos digestivos",
    "C30-C39": "Neoplasias malignas do aparelho respiratorio e dos orgaos intratoracicos",
    "C40-C41": "Neoplasias malignas dos ossos e das cartilagens articulares",
    "C43-C44": "Melanoma e outras(os) neoplasias malignas da pele",
    "C45-C49": "Neoplasias malignas do tecido mesotelial e tecidos moles",
    "C50-C50": "Neoplasias malignas da mama",
    "C51-C58": "Neoplasias malignas dos orgaos genitais femininos",
    "C60-C63": "Neoplasias malignas dos orgaos genitais masculinos",
    "C64-C68": "Neoplasias malignas do trato urinario",
    "C69-C72": "Neoplasias malignas dos olhos, do encéfalo e de outras partes do sistema nervoso central",
    "C73-C75": "Neoplasias malignas da tireoide e de outras glândulas endocrinas",
    "C76-C80": "Neoplasias malignas de localizações mal definidas, secundarias e de localizações nao especificadas",
    "C81-C96": "Neoplasias [tumores] malignas(os), declaradas ou presumidas como primarias, dos tecidos linfatico, hematopoético e tecidos correlatos",
    "C97-C97": "Neoplasias malignas de localizações múltiplas independentes (primarias)",
    "D00-D09": "Neoplasias [tumores] in situ",
    "D10-D36": "Neoplasias [tumores] benignas(os)",
    "D37-D48": "Neoplasias [tumores] de comportamento incerto ou desconhecido",
    "D50-D53": "Anemias nutricionais",
    "D55-D59": "Anemias hemoliticas",
    "D60-D64": "Anemias aplasticas e outras anemias",
    "D65-D69": "Defeitos da coagulaçao, púrpura e outras afecções hemorragicas",
    "D70-D77": "Outras Doencas do sangue e dos orgaos hematopoéticos",
    "D80-D89": "Alguns transtornos que comprometem o mecanismo imunitario",
    "E00-E07": "Transtornos da glândula tireoide",
    "E10-E14": "Diabetes mellitus",
    "E15-E16": "Outros transtornos da regulaçao da glicose e da secreçao pancreatica interna",
    "E20-E35": "Transtornos de outras glândulas endocrinas",
    "E40-E46": "Desnutriçao",
    "E50-E64": "Outras deficiencias nutricionais",
    "E65-E68": "Obesidade e outras formas de hiperalimentaçao",
    "E70-E90": "Distúrbios metabolicos",
    "F00-F09": "Transtornos mentais orgânicos, inclusive os sintomaticos",
    "F10-F19": "Transtornos mentais e comportamentais devidos ao uso de substância psicoativa",
    "F20-F29": "Esquizofrenia, transtornos esquizotipicos e transtornos delirantes",
    "F30-F39": "Transtornos do humor [afetivos]",
    "F40-F48": "Transtornos neuroticos, transtornos relacionados com o 'stress' e transtornos somatoformes",
    "F50-F59": "Sindromes comportamentais associadas a disfunções fisiologicas e a fatores fisicos",
    "F60-F69": "Transtornos da personalidade e do comportamento do adulto",
    "F70-F79": "Retardo mental",
    "F80-F89": "Transtornos do desenvolvimento psicologico",
    "F90-F98": "Transtornos do comportamento e transtornos emocionais que aparecem habitualmente durante a infância ou a adolescencia",
    "F99-F99": "Transtorno mental nao especificado",
    "G00-G09": "Doencas inflamatorias do sistema nervoso central",
    "G10-G13": "Atrofias sistemicas que afetam primariamente o sistema nervoso central",
    "G20-G26": "Transtornos extrapiramidais e transtornos do movimento",
    "G30-G32": "Outras Doencas degenerativas do sistema nervoso",
    "G35-G37": "Doencas desmielinizantes do sistema nervoso central",
    "G40-G47": "Transtornos episodicos e paroxisticos",
    "G50-G59": "Transtornos de nervos, raizes nervosas e plexos nervosos",
    "G60-G64": "Polineuropatias e outros transtornos do sistema nervoso periférico",
    "G70-G73": "Doencas da junçao neuromuscular e Doencas musculares",
    "G80-G83": "Paralisias cerebrais e outras sindromes paraliticas",
    "G90-G99": "Outros transtornos do sistema nervoso",
    "H00-H06": "Doencas da palpebra, aparelho lacrimal e orbita",
    "H10-H13": "Doencas da conjuntiva",
    "H15-H22": "Transtornos da esclerotica, da cornea, da iris e do corpo ciliar",
    "H25-H28": "Doencas do cristalino",
    "H30-H36": "Doencas da coroide e da retina",
    "H40-H42": "Glaucoma",
    "H43-H45": "Doencas do corpo vitreo e do globo ocular",
    "H46-H48": "Doencas do nervo optico e vias opticas",
    "H49-H52": "Transtornos dos músculos oculares, dos movimentos binoculares, da acomodaçao e da refraçao",
    "H53-H54": "Transtornos da visao e cegueira",
    "H55-H59": "Outros transtornos do olho e anexos"
}

def determinar_categoria(codigo):
    """
    Determina a categoria de um codigo CID baseado no range.
    """
    for range_cid, categoria in categorias.items():
        inicio, fim = range_cid.split("-")
        if inicio <= codigo <= fim:
            return categoria
    return "Categoria desconhecida"

def adicionar_categorias(arquivo_entrada, arquivo_saida):
    """
    Le um JSON com codigos CID e adiciona as categorias correspondentes.
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
arquivo_saida = 'cid10_new.json'

# Executa o script
adicionar_categorias(arquivo_entrada, arquivo_saida)
