Uso
===

Basico
------
    >>> import brasileirao
    >>> campeonato = brasileirao.get()

Campeonato
----------
    >>> campeonato.classificacao
    [Grêmio Foot-Ball Porto-Alegrense, Spot Club Internacional, Santa
     Cruz Futebol Clube, Sport Club Corinthians Paulista, Clube de Re...
    >>> campeonato.equipes
    {u'11': Fluminense Football Club, u'10': Figueirense Futebol Clube,
     u'26': América Futebol Clube, u'15': Sport Club Internacional, u...
    >>> campeonato.rodada
    '4'
    >>> campeonato.rodada.atual
    '4'
    >>> campeonato.rodada.total
    '38'
    >>> campeonato.nome_completo
    u'Campeonato Brasileiro'
    >>> campeonato.get_jogos_rodada()
    [Fluminense Football Club x Botafogo de Futebol e Regatas, 
    São Paulo Futebol Clube x Sociedade Esportiva Palmeiras, Cruzeiro...
    >>> campeonato.get_jogos_rodada('1')
    [Santa Cruz Futebol Clube x Esporte Clube Vitória, Coritiba Football
    Club x Cruzeiro Esporte Clube, Sport Club Internacional x Associa...
    >>> campeonato.jogos
    {u'92396': Associação Atlética Ponte Preta x América Futebol Clube, 
    u'92397': Sport Club do Recife x Santa Cruz Futebol Clube, u'9239...
    
Equipe
------
    >>> equipe = campeonato.get('76')
    >>> equipe
    Sport Clube Recife
    >>> equipe = campeonato.classificacao[19]
    >>> equipe
    Sport Clube Recife
    >>> equipe.nome_comum
    'Sport'
    >>> equipe.nome_slug
    'sport'
    >>> equipe.sigla
    'SPT'
    >>> equipe.uri
    'http://esporte.uol.com.br/futebol/clubes/sport'
    >>> equipe.brasao
    'http://e.imguol.com/futebol/brasoes/40x40/sport.png'
    >>> equipe.pos
    '20'
    >>> equipe.ganho_pos
    '-3'
    >>> equipe.pg.total, equipe.pg.mandante, equipe.pg.visitante
    ('1', '1', '0')
    >>> equipe.j.total, equipe.j.mandante, equipe.j.visitante
    ('4', '2', '2')
    >>> equipe.v.total, equipe.v.mandante, equipe.v.visitante
    ('0', '0', '0')
    >>> equipe.e.total, equipe.e.mandante, equipe.e.visitante
    ('1', '1', '0')
    >>> equipe.d.total, equipe.d.mandante, equipe.d.visitante
    ('3', '1', '2')
    >>> equipe.gp.total
    '1'
    >>> equipe.gc.total
    '5'
    >>> equipe.sg.total
    '-4'

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
    >>> jogo = campeonato.get_jogos_rodada()[0]
    >>> jogo
    Fluminense Football Club x Botafogo de Futebol e Regatas
    >>> jogo.data
    '2016-05-09'
    >>> jogo.estadio
    'Raulino de Oliveira'
    >>> jogo.horario
    '16h00'
    >>> jogo.local
    'Volta Redonda'
    >>> jogo.rodada
    '4'
    >>> jogo.placar1
    '1'
    >>> jogo.placar2
    '0'
    >>> jogo.time1
    Fluminense Football Club
    >>> jogo.time2
    Botafogo de Futebol e Regatas
    >>> jogo.url_posjogo
    ''http://esporte.uol.com.br/futebol/campeonatos/brasileiro/serie-a/
    ultimas-noticias/2016/05/29/carrasco-fred-aproveita-vacilo-de-zag...
    
