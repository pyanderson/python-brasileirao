Python Brasileirão
==================
 Simples crawler que resgata informações sobre o campeonato brasileiro
 serie A.
 
Instalação
----------
    pip install git+https://github.com/TheKiller666/python-brasileirao

Uso
---
    >>> import brasileirao
    >>> campeonato = brasileirao.get()
    >>> campeonato.get_jogos_rodada()
    [Fluminense Football Club x Botafogo de Futebol e Regatas, 
    São Paulo Futebol Clube x Sociedade Esportiva Palmeiras, Cruzeiro...
    >>> campeonato.get_jogos_rodada('1')
    [Santa Cruz Futebol Clube x Esporte Clube Vitória, Coritiba Football
    Club x Cruzeiro Esporte Clube, Sport Club Internacional x Associa...
    >>> campeonato.rodada.atual
    '4'
    >>> campeonato.classificacao
    [Grêmio Foot-Ball Porto-Alegrense, Spot Club Internacional, Santa
    Cruz Futebol Clube, Sport Club Corinthians Paulista, Clube de Reg...
    >>> campeonato.classificacao[0].gp.total
    '6'
 Mais em [USAGE.md](../master/USAGE.md)
    

Requisitos
----------
    requests>=2.10.0
    inflection>=0.3.1

Licença
-------
 The MIT License
 
 Copyright (c) 2016 Anderson Lima anderson.sl93@hotmail.com

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
