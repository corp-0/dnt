"""
Classes of the items in the game.

Base class is items.Base()
"""

from os.path import dirname, basename, isfile, join
import glob
import importlib

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
for element in __all__:
    module = importlib.import_module(f"items.{element}")
    globals().update(
    {n: getattr(module, n) for n in module.__all__} if hasattr(module, '__all__') 
    else 
    {k: v for (k, v) in module.__dict__.items() if not k.startswith('_')
        })

print("Importing items...")
count = 0
for element in __all__:
    count+=1
    print(f"{count}. {element} loaded!")

print("__________________________________________")