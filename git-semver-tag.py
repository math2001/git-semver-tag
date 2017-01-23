# -*- encoding: utf-8 -*-

import argparse
import subprocess
import re

START = '0.1.0'


def main():
    valid = re.compile(r'')

    parser = argparse.ArgumentParser()
    type_ = parser.add_mutually_exclusive_group(required=True)
    type_.add_argument('-p', '--patch', action="store_true", help='Increment the path')
    type_.add_argument('-m', '--minor', action="store_true", help='Increment the minor')
    type_.add_argument('-M', '--major', action="store_true", help='Increment the major')
    args = parser.parse_args()

    # http://stackoverflow.com/a/7261049/6164984
    cmd = subprocess.Popen(['git', 'describe', '--abbrev=0', '--tags', '--dirty'],
                           stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    last_tag = cmd.stdout.read().decode() or cmd.stderr.read().decode()
    matchobj = re.match(r'^v?(?P<major>\d\.)(?P<minor>\d\.)(?P<patch>\d\.)$', last_tag)
    if matchobj is not None:
        if args.patch:
            # CSW: ignore
            print('new patch:', int(matchobj.group('patch')) + 1)
        elif args.minor:
            # CSW: ignore
            print('new minor:', int(matchobj.group('minor')) + 1)
        elif args.major:
            # CSW: ignore
            print('new major:', int(matchobj.group('major')) + 1)
        else:
            raise ValueError('Internal error')
    elif last_tag.startswith('fatal'):
        # CSW: ignore
        print(last_tag.strip())
    else:
        # CSW: ignore
        print("invalid tag:", repr(last_tag))

if __name__ == '__main__':
    main()
