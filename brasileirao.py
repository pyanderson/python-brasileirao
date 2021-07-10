import json
import sys
import traceback

import requests
from inflection import underscore


def snake_string(string):
    if string:
        return ''.join(string).strip()
    return string


class Base:
    def __init__(self, obj=None):
        self.obj = obj
        if self.obj:
            self.__update__()

    def __update__(self):
        for k, v in self.obj.items():
            if isinstance(v, dict):
                setattr(self, underscore(snake_string(k)), Base(v))
            else:
                setattr(self, underscore(snake_string(k)), snake_string(v))


class Jogo:
    def __init__(self, obj=None, equipes=None):
        if not equipes:
            equipes = {}
        self.obj = obj
        if self.obj:
            self.__update__(equipes)

    def __update__(self, equipes=None):
        if not equipes:
            equipes = {}
        for k, v in self.obj.items():
            if isinstance(v, dict):
                setattr(self, underscore(snake_string(k)), Base(v))
            else:
                setattr(self, underscore(snake_string(k)), snake_string(v))
        time1 = self.obj['time1']
        time2 = self.obj['time2']
        if time1:
            self.time1 = equipes[time1]
        if time2:
            self.time2 = equipes[time2]

    def __repr__(self):
        return self.time1.__repr__() + ' x ' + self.time2.__repr__()


class Rodada(Base):
    def __repr__(self):
        return self.atual


class Equipe(Base):
    def __repr__(self):
        return self.nome


class Campeonato:
    URL = ('http://jsuol.com.br/c/monaco/utils/gestor/commons.js?callback='
           'simulador_dados_jsonp&file=commons.uol.com.br/sistemas/esporte'
           '/modalidades/futebol/campeonatos/dados/2021/30/dados.json')

    def __init__(self):
        self._response = None
        self._json = None
        self.nome_completo = ''
        self.equipes = {}
        self.classificacao = []
        self.rodada = None
        self.jogos = {}
        self.get()

    def get_jogos_rodada(self, rodada=None):
        if not rodada:
            rodada = self.rodada.atual
        jogos = []
        for _, v in self.jogos.items():
            if v.rodada == rodada:
                jogos.append(v)
        return jogos

    def get(self):
        try:
            self._response = requests.get(self.URL)
            self._json = json.loads(
                self._response.text[22:len(self._response.text)-3]
            )
            self.nome_completo = self._json['nome-completo']
            for k, v in self._json['equipes'].items():
                self.equipes[k] = Equipe(v)
            fases = self._json['fases']['3275']
            self.rodada = Rodada(fases['rodada'])
            for e, d in fases['classificacao']['equipe'].items():
                for k, v in d.items():
                    if isinstance(v, dict):
                        setattr(
                            self.equipes[e],
                            underscore(snake_string(k)),
                            Base(v)
                        )
                    else:
                        setattr(
                            self.equipes[e],
                            underscore(snake_string(k)),
                            snake_string(v)
                        )
            for k, v in fases['jogos']['id'].items():
                self.jogos[k] = Jogo(v, self.equipes)
            for v in fases['classificacao']['grupo'].values():
                for k in v:
                    self.classificacao.append(self.equipes[k])
        except Exception:
            traceback.print_exc(file=sys.stdout)


def get():
    return Campeonato()


if __name__ == '__main__':
    campeonato = get()
    print(campeonato.get_jogos_rodada())
