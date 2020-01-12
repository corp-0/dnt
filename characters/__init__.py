"""
Classes of the characters in the game.

Base class is characters.Base()
"""

from os.path import dirname, basename, isfile, join
import glob
import importlib

modules = glob.glob(join(dirname(__file__), "*.py"))
files = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
for element in files:
    module = importlib.import_module(f"characters.{element}")
    globals().update(
    {n: getattr(module, n) for n in module.__all__} if hasattr(module, '__all__') 
    else 
    {k: v for (k, v) in module.__dict__.items() if not k.startswith('_')
        })

print("Importing characters...")
count = 0
for element in files:
    count+=1
    print(f"{count}. {element} loaded!")

print("__________________________________________")

