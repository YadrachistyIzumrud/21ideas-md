import sys
import html2markdown

s=sys.stdin.read()
print (html2markdown.convert(s))