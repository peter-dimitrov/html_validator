#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    s = []
    tags = _extract_tags(html)
    balanced = True
    for tag in tags:
        if tag[1] != '/':
            s.append(tag)
        else:
            if s == []:
                balanced = False
            else:
                top = s.pop()
                if tag != top[0] + '/' + top[1::]:
                    balanced = False
    if balanced and s == []:
        return True
    else:
        return False

def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.
'''
    L = []
    for x in range(len(html)):
        tag = ''
        if html[x] == '<':
            y = x
            while y < len(html):
                tag = tag + html[y]
                if html[y] == '>':
                    break
                else:
                    y = y + 1
            L.append(tag)
    return L
