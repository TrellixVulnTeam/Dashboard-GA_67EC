#!c:\users\nmi\appdata\local\programs\python\python35-32\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rsa==3.4.2','console_scripts','pyrsa-priv2pub'
__requires__ = 'rsa==3.4.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('rsa==3.4.2', 'console_scripts', 'pyrsa-priv2pub')()
    )
