Python Brasileirão
==================
 Simples crawler que resgata informações sobre o campeonato brasileiro
 serie A.

Instalação
----------
    pip install git+https://github.com/pyanderson/python-brasileirao

Uso
---

    >>> import brasileirao
    >>> campeonato = brasileirao.get()
    >>> campeonato.get_jogos_rodada()
    [Clube Atlético Paranaense x São Paulo Futebol Clube,
	Clube Atlético Mineiro x Sport Club do Recife...
    >>> campeonato.get_jogos_rodada('1')
	[Sport Club Corinthians Paulista x Associação Chapecoense de Futebol,
	Associação Atlética Ponte Preta x Sport Club do Recife...
    >>> campeonato.rodada.atual
    '9'
    >>> campeonato.classificacao
	[Sport Club Corinthians Paulista, Grêmio Foot-Ball Porto-Alegrense...
    >>> campeonato.classificacao[0].gp.total
    '17'

 Mais em [USAGE.md](../master/USAGE.md)

Requisitos
----------
    requests>=2.10.0
    inflection>=0.3.1
