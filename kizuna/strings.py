import random

HAI_DOMO = '\u306F\u3044\u3069\u3082\uFF01\u30AD\u30BA\u30CA\u30FB\u30A2\u30A4\u3067\u3059\uFF01'
KIZUNA = '\u30AD\u30BA\u30CA'
WAIT_A_SEC = '\u3061\u3087\u3063\u3068\u5F85\u3063\u3066\u304F\u3060\u3055\u3044'
JAP_DOT = '\u3002'
AHO = '\u3042\u307B'
BAKA = '\u3070\u304B'
INSULTS = [AHO, BAKA]


def random_insult():
    return random.choice(INSULTS)


YOSHI = '\u3088\u3057'

VERSION_UPDATE_TEMPLATE = '\u79C1\u306F{{VERSION}}\u306B\u66F4\u65B0\u3057\u307E\u3057\u305F'
VERSION_TRANSITION_TEMPLATE = '\u30D0\u30FC\u30B8\u30E7\u30F3{{FROM_VERSION}}\u304B\u3089\u30D0\u30FC\u30B8\u30E7' \
                              '\u30F3{{TO_VERSION}}\u306B\u66F4\u65B0\u3057\u307E\u3057\u305F '


LQUO = '\u300C'
RQUO = '\u300D'
