#Конвертер статей сайта 21ideas.org в формат md

##Работает так:

Скачиваем сайт:
wget --recursive   --page-requisites --domains 21ideas.org  https://www.21ideas.org

Устанавливаем библиотеку:
pip install html2markdown

cd www.21ideas.org
./article.md.sh