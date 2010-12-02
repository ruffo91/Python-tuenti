#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2010 David Francos Cuartero (XayOn)
# Copyright (C) 2010 Rubén López Angós (Ruffo)
from BeautifulSoup import BeautifulSoup, SoupStrainer
import mechanize, urllib, re, os, sys, thread
from tuenti.login import TuentiLogger
from tuenti.profile_images import TuentiProfileImageDownloader

urls = {'start' : 'http://m.tuenti.com/?m=login',
        'login' : 'http://m.tuenti.com/?m=login&func=process_login',
        'profile' : 'http://m.tuenti.com/?m=profile&user_id=%s'}

if __name__ == "__main__":
    log=TuentiLogger(sys.argv[1],sys.argv[2])
    for i in range(int(sys.argv[3]),int(sys.argv[4])):
        TuentiProfileImageDownloader(log, i)
