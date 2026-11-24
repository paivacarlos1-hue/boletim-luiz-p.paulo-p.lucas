# Autor: Pedro Paulo dos Santos Batista Torres

def falta(m):
    """Devolve quantos pontos faltam para chegar a 60.
    Se a media ja e 60 ou mais, devolve 0.
    Ex.: falta(50) -> 10
    """
    # complete aqui: troque o return "?" pelo if
    if m >= 60:
        return 0
    else:
        return 60 - m
