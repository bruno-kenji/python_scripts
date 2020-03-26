from cpf_cnpj import Cpf, Cnpj

def format_cpf_or_cnpj(cpf_or_cnpj):
  cpf = Cpf()
  cnpj = Cnpj()

  if cpf.validate(cpf_or_cnpj):
    try:
      return cpf.format(cpf_or_cnpj)
    except Exception as e:
      print(f'Error when formatting cpf: {e}')
      return cpf_or_cnpj

  if cnpj.validate(cpf_or_cnpj):
    try:
      return cnpj.format(cpf_or_cnpj)
    except Exception as e:
      print(f'Error when formatting cnpj: {e}')
      return cpf_or_cnpj

  raise ValueError(f'Invalid cpf or cnpj: {cpf_or_cnpj}.')
