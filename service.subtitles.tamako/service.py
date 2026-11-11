# -*- coding: utf-8 -*-
import sys
from urllib.parse import parse_qs, unquote
import xbmcgui
import xbmcplugin

ADDON_ID = 'service.subtitles.tamako'
BASE = 'https://raw.githubusercontent.com/ManjarosV/tamako/main/subtitles/'
SUBTITLES = [
    ('Episódio 03 — Tamako Market PT-BR', 'Tamako_Market_S01E03_PT-BR.ass'),
    ('Episódio 04 — Tamako Market PT-BR', 'Tamako_Market_S01E04_PT-BR.ass'),
    ('Episódio 05 — Tamako Market PT-BR', 'Tamako_Market_S01E05_PT-BR.ass'),
    ('Episódio 06 — Tamako Market PT-BR', 'Tamako_Market_S01E06_PT-BR.ass'),
    ('Episódio 07 — Tamako Market PT-BR', 'Tamako_Market_S01E07_PT-BR.ass'),
    ('Episódio 08 — Tamako Market PT-BR', 'Tamako_Market_S01E08_PT-BR.ass'),
    ('Episódio 09 — Tamako Market PT-BR', 'Tamako_Market_S01E09_PT-BR.ass'),
    ('Episódio 10 — Tamako Market PT-BR', 'Tamako_Market_S01E10_PT-BR.ass'),
    ('Episódio 11 — Tamako Market PT-BR', 'Tamako_Market_S01E11_PT-BR.ass'),
    ('Episódio 12 — Tamako Market PT-BR', 'Tamako_Market_S01E12_PT-BR.ass'),
]

def params():
    raw = sys.argv[2][1:] if len(sys.argv) > 2 else ''
    return {k: unquote(v[0]) for k, v in parse_qs(raw).items()}

def add_item(label, url):
    item = xbmcgui.ListItem(label=label)
    item.setProperty('sync', 'false')
    item.setProperty('hearing_imp', 'false')
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, item, False)

def search():
    for label, filename in SUBTITLES:
        remote = BASE + filename
        add_item(label, 'plugin://%s/?action=download&url=%s' % (ADDON_ID, remote))

def download(url):
    if url:
        item = xbmcgui.ListItem(label=url.rsplit('/', 1)[-1])
        xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, item, False)

p = params()
action = p.get('action', 'search')
if action in ('search', 'manualsearch'):
    search()
elif action == 'download':
    download(p.get('url', ''))
xbmcplugin.endOfDirectory(int(sys.argv[1]))
