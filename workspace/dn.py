import json
import urllib2
import time
from xml.etree import ElementTree as ET

# Take from
def get_items(uri):
    items = []
    data = json.loads(urllib2.urlopen(uri).read())
    for item in data['stories']:
        result = parse_item(item)
        items.append(result)

    xml = generate_xml(items)
    return xml


def generate_xml(items):
    xml_items = ET.Element('items')
    for item in items:
        xml_item = ET.SubElement(xml_items, 'item')
        for key in item.keys():
            if key is 'uid' or key is 'arg':
                xml_item.set(key, item[key])
            else:
                child = ET.SubElement(xml_item, key)
                child.text = item[key]
    print ET.tostring(xml_items)


def parse_item(item):
    return {
        'uid': '%s%s' % (item['id'], time.time()),
        'arg': item['url'],
        'title': item['title'],
        'subtitle': str(item['vote_count']) +' Votes  ' + str(item['num_comments']) + ' Comments',
        'icon': 'icon.png'
    }
