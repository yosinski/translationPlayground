#!/usr/bin/env python

# JBY modified from https://github.com/mouuff/Google-Translate-API/blob/master/gtranslate.py

import sys
import urllib2



def translate(text, fromLang = 'auto', toLang = 'auto'):
	'''Return the translation using google translate
	you must shortcut the fromLang you define (French = fr, English = en, Spanish = es, etc...)
	if you dont define anything it will detect it or use english by default
	Example:
	print(translate('salut tu vas bien?', 'en'))
	hello you alright?'''
    
	agents = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)'}
	before_trans = 'class="t0">'
	link = 'http://translate.google.com/m?hl=%s&sl=%s&q=%s' % (toLang, fromLang, text.replace(' ', '+'))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split('<')[0]
	return result



def getLanguages():
    '''Returns a dictionary of available languages'''
    langs = {}
    with open('languages.txt') as ff:
        for line in ff:
            descrip, code = line.strip().rsplit(None, 1)
            langs[code] = descrip
    return langs



def main():
    lang1 = sys.argv[1]
    lang2 = sys.argv[2]
    text = ' '.join(sys.argv[3:])

	#to_translate = 'Hola como estas?'
    print 'original', lang1, '\t', text
    current = text
    
    for ii in range(4):
        current = translate(current, lang1, lang2)
        print '%s -> %s \t%s' % (lang1, lang2, current)
        current = translate(current, lang2, lang1)
        print '%s -> %s \t%s' % (lang2, lang1, current)



if __name__ == '__main__':
    main()
