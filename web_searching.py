from requests_html import HTMLSession
import json  # rodzaj zapisu danych
"""
    It works from the command line.
"""

session = HTMLSession()  #  obiekt klasy HTMLSession
r = session.get('https://www.pracuj.pl/praca/python;kw?rd=30')  # kod do strony z wynikami pracy
r.html.render()  # wbudowana funkcja - otwiera / tworzy / renderuje stronę

jobs = r.html.find('span.results-header__offer-count-text-number')[0]  # nazwa zmiennej, która szukamy na stronie;
# wybierz indeks 0 - liczbę wybierze; w bloku span w kodzie
print('Python jobs', jobs.text)
