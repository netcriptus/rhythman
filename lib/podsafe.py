import urllib
import sys
sys.path.append('../lib/BeautifulSoup')
sys.path.append('../lib')
from BeautifulSoup import BeautifulSoup as Soup


class PodsafeSite(object):
    def __init__(self, query = None):
        self.base_url = "http://music.podshow.com"
        self.search_prefix =  self.base_url +\
            "/music/listeners/searchResults.php?SearchString="
        self.url_sulfix = "&go2=Search+Keywords"
        self.html = self.search(query)

    def search(self, query):
        get_page = urllib.urlopen(self.search_prefix + query + self.url_sulfix)
        html = Soup(get_page)
        return html

    def parse(self):
        lst = self.html.findAll('tr', {'class': 'podcastListDescription'})
        opts = []
        for item in lst:
            params = item.findChildren('td')
            artist = params[0].contents[0].contents[0].strip()
            song = params[1].contents[0].strip()
            url = params[5].contents[0].contents[1].contents[1].attrs[1][1]
            url = url.split('=')[1].strip()
            info = {'artist': artist,
                    'song': song,
                    'url': url}
            opts.append(info)
        return opts


    def download(self, musics, opts):
        if not len(musics):
            return 1

        if '-1' in musics:
            musics = [i for i in range(len(opts))]
        else:
            musics = [int(i) for i in musics.split(' ')]

        for i in musics:
            music = opts[i]
            url = urllib.urlopen(self.base_url + music['url'])
            filename = music['artist'] + '-' + music['song'] + '.mp3'
            file = url.read()
            f_out = open(filename, 'wb')
            f_out.write(file)
            f_out.close()

        return 0
