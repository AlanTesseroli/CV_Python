def notas(*n, sit=False):
    """"
        AJUDA - NOTAS
    -> n = notas do aluno
    -> sit (opcional) = classifica a situação do aluno
    -> return = dicionário com as informações
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if True:
        if r['média'] >= 9:
            r['situação'] = 'ÓTIMO'
        if r['média'] >= 8 and r['média'] < 9:
            r['situação'] = 'BOA'
        if r['média'] >= 7 and r['média'] < 8:
            r['situação'] = 'RAZOÁVEL'
        if r['média'] <= 6:
            r['situação'] = 'RUIM'
    return r


rest = notas(6,7,5,4,sit=False)
print(rest)
help(notas)