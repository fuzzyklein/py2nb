from pathlib import Path
import pdb
import site
import sys
from traceback import print_exc
from warnings import warn

# site.addsitedir(str(Path(__file__).parent))
# pdb.set_trace()
from py2nb.py2nb import Py32JNb

def main():
    """ main()

        Call the `run` method of a class descended from `py.Program`.
    """
    # print("Hello, World!")
    try:
        Py32JNb().run()
    except:
        print_exc()
        exit(1)

if __name__ == "__main__":
    main()
