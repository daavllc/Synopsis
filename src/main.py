import argparse
import sys

import conf.config as config

def main():
    print("   _____                              _     ")
    print("  / ___/__  ______  ____  ____  _____(_)____")
    print("  \__ \/ / / / __ \/ __ \/ __ \/ ___/ / ___/")
    print(" ___/ / /_/ / / / / /_/ / /_/ (__  ) (__  ) ")
    print("/____/\__, /_/ /_/\____/ .___/____/_/____/  ")
    print("     /____/           /_/                   ")
    print(f" Copyright ©2022 DAAV, LLC - Version {config.VERSION}")
    print(f" Licensed under the MIT license. See LICENSE for details.\n")
    sys.exit(0)

if __name__ == "__main__":
    main()