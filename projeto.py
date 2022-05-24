import pdfkit
import zipfile

pdfkit.from_url('www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf', 'anexo1.pdf')
pdfkit.from_url('www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.xlsx', 'anexo1.xlsx')
pdfkit.from_url('www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf', 'anexo2.pdf')
pdfkit.from_url('www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf', 'anexo3.pdf')
pdfkit.from_url('www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf', 'anexo4.pdf')

with zipfile.ZipFile("projeto.zip", "w") as myzip:
  myzip.write("anexo1.pdf")
  myzip.write("anexo2.pdf")
  myzip.write("anexo3.pdf")
  myzip.write("anexo4.pdf")
  myzip.write("anexo1.xlsx")