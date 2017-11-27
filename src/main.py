from mark2html import mark2html as mk

m = mk.ler_markdown('teste.md')
html = mk.gera_html(m)
mk.renderiza_template('template.html', html)
