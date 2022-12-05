import xml.etree.ElementTree as ET

langs = [('da','Danish'),
         ('de','German'),
         ('el','Greek'),
         ('en','English'),
         ('es','Spanish'),
         ('fr','French'),
         ('fi','Finnish'),
         ('it','Italian'),
         ('nl','Dutch'),
         ('pt','Portuguese'),
         ('sv','Swedish'),
        ]

for cd, lang in langs:
    parser = ET.XMLParser(encoding='utf-8')
    root = ET.fromstring(open(f'{lang}.xml').read(), parser=parser)
    with open(f'{cd}.txt', 'w', encoding='utf-8') as out:
        for n in root.iter('seg'):
            if n.text is not None:
                out.write(n.text.strip() + '\n')