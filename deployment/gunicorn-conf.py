import multiprocessing
from pathlib import Path

# Dynamically computed values
base_dir = str(Path(__file__).parent.parent.resolve().joinpath('src'))
worker_nodes = multiprocessing.cpu_count() * 2 + 1

chdir = base_dir
bind = "127.0.0.1:5000"
workers = worker_nodes
accesslog = 'logs/access.log'
errorlog =  'logs/debug.log'
loglevel  = 'DEBUG'