#!/usr/bin/env python

# JBY modified from https://github.com/mouuff/Google-Translate-API/blob/master/gtranslate.py

import sys
from translate_1 import translate, getLanguages


def main():
    lang1 = sys.argv[1]
    text = ' '.join(sys.argv[2:])

    langs = getLanguages()
    #langsToTest = sorted(langs.keys())[:2]
    langsToTest = sorted(langs.keys())

    print 'original %s: %s\n' % (lang1, text)
    for code in langsToTest:
        foreign = translate(text, lang1, code)
        back    = translate(foreign, code, lang1)
        langStr = '%-13s' % ('(%s):' % langs[code])
        print '-> %s %s %-35s \t-> %s: %s' % (code, langStr, foreign, lang1, back)



if __name__ == '__main__':
    main()
