#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2010 David Francos Cuartero (XayOn)
# Copyright (C) 2010 Rubén López Angós (Ruffo)
from BeautifulSoup import BeautifulSoup, SoupStrainer
import mechanize, urllib, re, os, sys, thread

urls = {'start' : 'http://m.tuenti.com/?m=login',
        'login' : 'http://m.tuenti.com/?m=login&func=process_login',
        'profile' : 'http://m.tuenti.com/?m=profile&user_id=%s'}

class TuentiLogger():
    def __init__(self, email, password):
            self._br=mechanize.Browser()
            response=self._br.open(urls['start'])
            self.encoded_data=urllib.urlencode({'tuentiemail': email, 'password': password})
            response=self._br.open(urls['login'], self.encoded_data).read()

    def get_profile(self, id_):
        try:
            return self._br.open(urls['profile'] %id_).read()
        except:
            return
