# -*- coding: utf8 -*-
import json

import requests
import inflection


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
                setattr(self, inflection.underscore(snake_string(k)), Base(v))
            else:
                setattr(self, inflection.underscore(snake_string(k)), snake_string(v))


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
                setattr(self, inflection.underscore(snake_string(k)), Base(v))
            else:
                setattr(self, inflection.underscore(snake_string(k)), snake_string(v))
        time1 = self.obj.get('time1')
        time2 = self.obj.get('time2')
        if time1:
            self.time1 = equipes.get(time1)
        if time2:
            self.time2 = equipes.get(time2)

    def __repr__(self):
        return self.time1.__repr__() + ' x ' + self.time2.__repr__()


class Rodada(Base):
    def __repr__(self):
        return self.atual


class Equipe(Base):
    def __repr__(self):
        return self.nome


class Campeonato:
    URL = 'http://jsuol.com.br/c/monaco/utils/gestor/commons.js?callback=simulador_dados_jsonp&' \
          'file=commons.uol.com.br/sistemas/esporte/modalidades/futebol/campeonatos/dados/2017/30/dados.json'
    _response = None
    _json = None
    nome_completo = ''
    equipes = {}
    classificacao = []
    rodada = None
    jogos = {}

    def __init__(self):
        self.get()

    def get_jogos_rodada(self, rodada=None):
        if not rodada:
            rodada = self.rodada.atual
        jogos = []
        for k, v in self.jogos.items():
            if v.rodada == rodada:
                jogos.append(v)
        return jogos

    def get(self):
        try:
            self._response = requests.get(self.URL)
            self._json = json.loads(self._response.text[22:len(self._response.text)-3])
            self.nome_completo = self._json.get('nome-completo')
            for k, v in self._json.get('equipes').items():
                self.equipes[k] = Equipe(v)
            self.rodada = Rodada(self._json.get('fases').get('2528').get('rodada'))
            for e, d in self._json.get('fases').get('2528').get('classificacao').get('equipe').items():
                for k, v in d.items():
                    if isinstance(v, dict):
                        setattr(self.equipes[e], inflection.underscore(snake_string(k)), Base(v))
                    else:
                        setattr(self.equipes[e], inflection.underscore(snake_string(k)), snake_string(v))
            for k, v in self._json.get('fases').get('2528').get('jogos').get('id').items():
                self.jogos[k] = Jogo(v, self.equipes)
            for v in self._json.get('fases').get('2528').get('classificacao').get('grupo').values():
                for k in v:
                    self.classificacao.append(self.equipes[k])
        except Exception as inst:
            print(inst)
            print(inst.args)


def get():
    return Campeonato()
