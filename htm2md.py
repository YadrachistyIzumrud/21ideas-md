import sys
import html2markdown
from pathlib import Path
import re




#s=sys.stdin.read()
#print (html2markdown.convert(s))


for f in Path().rglob('*.html'):
  html=open(f).read()
  article_start=html.find("<article>")
  if article_start > 0:
    article_end=html.find("</article>")
    if article_end > 0:
      article=html[article_start+10:article_end]
      md=html2markdown.convert(article)
      open(str(f)+'.md','w').write(md)
      print(f)
