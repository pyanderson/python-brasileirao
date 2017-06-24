Uso
===

Basico
------

    >>> import brasileirao
    >>> campeonato = brasileirao.get()

Campeonato
----------

    >>> campeonato.classificacao
	[Sport Club Corinthians Paulista, Grêmio Foot-Ball Porto-Alegrense...
    >>> campeonato.equipes
	{'29': Avaí Futebol Clube, '695': Associação Chapecoense de Futebol,...
    >>> campeonato.rodada
    9
    >>> campeonato.rodada.atual
    '9'
    >>> campeonato.rodada.total
    '38'
    >>> campeonato.nome_completo
    'Campeonato Brasileiro'
    >>> campeonato.get_jogos_rodada()
    [Clube Atlético Paranaense x São Paulo Futebol Clube,
	Clube Atlético Mineiro x Sport Club do Recife...
    >>> campeonato.get_jogos_rodada('1')
	[Sport Club Corinthians Paulista x Associação Chapecoense de Futebol,
	Associação Atlética Ponte Preta x Sport Club do Recife...
    >>> campeonato.jogos
	{'97083': São Paulo Futebol Clube x Avaí Futebol Clube,
	'97443': Clube de Regatas do Flamengo x Sport Club Corinthians...

Equipe
------

    >>> equipe = campeonato.equipes.get('76')
    >>> equipe
    Sport Clube Recife
    >>> equipe = campeonato.classificacao[7]
    >>> equipe
    Clube de Regatas do Flamengo
    >>> equipe.nome_comum
    'Flamengo'
    >>> equipe.nome_slug
    'flamengo'
    >>> equipe.sigla
    'FLA'
    >>> equipe.uri
    'http://esporte.uol.com.br/futebol/clubes/flamengo'
    >>> equipe.brasao
    'http://e.imguol.com/futebol/brasoes/40x40/flamengo.png'
    >>> equipe.pos
    '6'
    >>> equipe.ganho_pos
    '3'
    >>> equipe.pg.total, equipe.pg.mandante, equipe.pg.visitante
	('14', '8', '6')
    >>> equipe.j.total, equipe.j.mandante, equipe.j.visitante
	('9', '4', '5')
    >>> equipe.v.total, equipe.v.mandante, equipe.v.visitante
	('3', '2', '1')
    >>> equipe.e.total, equipe.e.mandante, equipe.e.visitante
	('5', '2', '3')
    >>> equipe.d.total, equipe.d.mandante, equipe.d.visitante
	('1', '0', '1')
    >>> equipe.gp.total
    '15'
    >>> equipe.gc.total
    '8'
    >>> equipe.sg.total
    '7'

Legenda de Equipe
-----------------

    pg = Pontos Ganhos
    j = Jogos
    v = Vitorias
    e = Empates
    d = Derrotas
    gp = Gols Pró
    gc = Gols Contra
    sg = Saldo de Gols

Jogo
----

    >>> jogo = campeonato.get_jogos_rodada('9')[4]
    >>> jogo
    Clube de Regatas do Flamengo x Associação Chapecoense de Futebol
    >>> jogo.data
    '2017-06-22'
    >>> jogo.estadio
    'Luso Brasileiro'
    >>> jogo.horario
    '21h00'
    >>> jogo.local
    'Rio de Janeiro'
    >>> jogo.rodada
    '9'
    >>> jogo.placar1
    '5'
    >>> jogo.placar2
    '1'
    >>> jogo.time1
    Clube de Regatas do Flamengo
    >>> jogo.time2
    Associação Chapecoense de Futebol
    >>> jogo.url_posjogo
	'https://esporte.uol.com.br/futebol/campeonatos/brasileiro/serie-a/...'
