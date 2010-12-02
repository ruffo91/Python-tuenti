#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2010 David Francos Cuartero (XayOn)
# Copyright (C) 2010 Rubén López Angós (Ruffo)
from BeautifulSoup import BeautifulSoup, SoupStrainer
import mechanize, urllib, re, os, sys, thread

urls = {'start' : 'http://m.tuenti.com/?m=login',
        'login' : 'http://m.tuenti.com/?m=login&func=process_login',
        'profile' : 'http://m.tuenti.com/?m=profile&user_id=%s'}

class TuentiProfileImageDownloader():
    def __init__(self, logged, id_):
        response=logged.get_profile(id_)
        if response:
            try:
                strainer=SoupStrainer('div', {"class" : "h"})
                name=unicode([tag for tag in BeautifulSoup(response, parseOnlyThese=strainer)][0].string).encode('utf-8')
                reg=re.search('http://perfiles(.*).tuenti.net/(.*)" alt', response)
                a=reg.group(2).split('/')
                url = "http://imagenes2.tuenti.net/%s/%s/%s/600/%s/%s/%s" %(a[1],a[2],a[3],a[5],a[6],a[7])
                thread.start_new_thread(os.system, ('wget -O "%s_%s.jpg " %s' %(name, id_, url),))
            except:
                pass
