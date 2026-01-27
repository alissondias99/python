# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b',
    '--basic',
    help = 'Mostra um mensagem',
    type = str,
    metavar = 'STRING',
    default = "Mensagem padão",
    required = False)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou argumentos')
else:
    print('Basic:', args.basic)