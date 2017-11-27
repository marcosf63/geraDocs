#!/usr/bin/env python 

import os
import markdown

class mark2html:
  """
    Converte um arquivo em markdown em html
  """
  
  def __init__(self):
    pass

  @staticmethod
  def ler_markdown(nome_do_arquivo):
    """
      Ler um arquivo no formato markdown e devolve uma string
    """
    return open("teste.md").read()

  @staticmethod
  def gera_html(string_markdown):
    return markdown.markdown(string_markdown)
    

  @staticmethod
  def renderiza_template(template, html_gerado):
    with open(template) as template:
      t = template.read().format(html_gerado)
      with open('doc.html', 'w') as doc:
        doc.write(t)



 

