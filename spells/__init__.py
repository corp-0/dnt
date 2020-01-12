"""
Classes of the spells in the game.

Base class is spells.Spell()
"""

from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

print("Importing spells...")
count = 0
for element in __all__:
    count+=1
    print(f"{count}. {element} loaded!")

print("__________________________________________")