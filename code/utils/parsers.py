from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from pathlib import Path

arg_parser = ArgumentParser()
arg_parser.add_argument(
    'exampleFileList',
    help='list of files containing ellipsis patterns',
    type=FileType('r'),
)
arg_parser.add_argument(
    'model',
    help='GPT model to test',
    choices=[
        "text-davinci-003",
        "text-davinci-002", 
        "text-ada-001", 
        "text-curie-001", 
        "text-babbage-001"
    ],
)
arg_parser.add_argument(
    'sampleSize',
    help='number of examples to test',
    type=int,
    choices=[1, 10, 50, 100, 500],
)

arg_parser.add_argument(
    "iterations",
    help="number of iterations",
    type=int,
    choices=[1, 2, 3, 5, 10, 50],
    default=1
)    

ARGS = arg_parser.parse_args()

# check that exampleFileList is not empty
files = ARGS.exampleFileList.readlines()
if not files:
    raise ValueError('exampleFileList is empty')

# check that all files in exampleFileList exist and are json files
data_files = Path("data").glob("*.json")
EXAMPLE_FILES = [p for p in data_files if p.name in [f.strip("\n") for f in files]]
if len(EXAMPLE_FILES) != len(files):
    raise ValueError('exampleFileList contains invalid/missing file(s)')


config_parser = ConfigParser()
config_parser.read('config.cfg')
if not config_parser.get('DEFAULT', 'API_KEY'):
    raise ValueError('API_KEY not set in config.cfg')