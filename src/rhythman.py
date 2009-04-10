#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../lib/BeautifulSoup')
sys.path.append('../lib')
from BeautifulSoup import BeautifulSoup as Soup
import urllib
from podsafe import PodsafeSite

def get_chosen(opts):
    for opt, i in zip(opts, range(len(opts))):
        print i,
        print '-', opt['artist']
        print ' '*(len(str(i))+2), opt['song']

    return raw_input('Separe as musicas escolhidas com espaço. Digite -1 para pegar todas.\n>> ')


def main(argv):
    if len(argv) != 2:
        query = raw_input("What should I aim for? >> ")
    else:
        query = argv[1].lower()

    query = '+'.join(query.split(' '))

    site = PodsafeSite(query)
    opts = site.parse()

    musics = get_chosen(opts)

    return site.download(musics, opts)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
