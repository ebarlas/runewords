import xml.etree.ElementTree as ET
import json


def parse_runes(file):
    tree = ET.parse(file)
    root = tree.getroot()

    runes = {}
    for row in root.findall('./TABLE/TR'):
        name = row.findall('./TD[2]/font/span/b/font')[0].text
        level = row.findall('./TD[5]/font/span')[0].text
        runes[name] = 33 if level == '-' else int(level)

    return runes


def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()

    rws = []
    for row in root.findall('./TABLE/TR'):
        name = row.findall('./TD[1]/font/span/B')[0].text
        type = row.findall('./TD[2]/font/span')[0].text
        runes = row.findall('./TD[3]/font/span')[0].text.split(' + ')
        bonus = row.findall('./TD[4]/font/span/font')[0].text.strip().split('\n')

        split = type.split(' Socket ')
        sockets = int(split[0])
        item = split[1]

        rw = {
            'name': name,
            'item': item,
            'sockets': sockets,
            'runes': runes,
            'bonus': bonus,
        }
        rws.append(rw)

    return rws


def extend(rws, d):
    for rw in rws:
        rw.update(d)
    return rws


def add_level(rws, runes):
    for rw in rws:
        rw['level'] = max([runes[r] for r in rw['runes']])


def main():
    runes = parse_runes('xml/runes.xml')

    rws = []
    rws.extend(extend(parse_xml('xml/original.xml'), {'era': 'Original'}))
    rws.extend(extend(parse_xml('xml/110.xml'), {'era': '1.10'}))
    rws.extend(extend(parse_xml('xml/110_ladder.xml'), {'era': '1.10'}))
    rws.extend(extend(parse_xml('xml/111.xml'), {'era': '1.11'}))

    add_level(rws, runes)

    rws.sort(key=lambda rw: rw['level'])

    with open('runewords.json', 'w') as f:
        json.dump({'runewords': rws}, f)


if __name__ == '__main__':
    main()
