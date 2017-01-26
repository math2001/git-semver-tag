# -*- encoding: utf-8 -*-

from __future__ import print_function
import argparse
import subprocess
import re
import webbrowser

FRIST_TAG = [0, 1, 0]

def confirm(question):
    yes = ['yes', 'y']
    no = ['no', 'n']
    ans = ''
    while ans not in yes + no:
        ans = input(question + ' (y/n)? ')
        if ans in yes:
            return True
        elif ans in no:
            return False

def tag(v, major, minor, patch, args):
    tag = '{}{}.{}.{}'.format(v or '', major, minor, patch)
    if args.sure or confirm('Tag {}'.format(tag)):
        subprocess.Popen(['git', 'tag', tag])
        if not args.quiet:
            # CSW: ignore
            print('Created tag {}'.format(tag))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--docs', action='store_true', help='Open the docs and exit')
    type_ = parser.add_mutually_exclusive_group(required=False)
    type_.add_argument('-M', '--major', action="store_true", help='Increment the major')
    type_.add_argument('-m', '--minor', action="store_true", help='Increment the minor')
    type_.add_argument('-p', '--patch', action="store_true", help='Increment the patch')
    parser.add_argument('-s', '--sure', action='store_true', help="Do not ask any confirmation")
    parser.add_argument('-q', '--quiet', action='store_true', help='Quiet mode')
    args = parser.parse_args()

    if args.docs:
        webbrowser.open_new_tab('https://math2001.github.io/git-semver-tag')
        exit(0)

    # http://stackoverflow.com/a/7261049/6164984
    cmd = subprocess.Popen(['git', 'describe', '--abbrev=0', '--tags'],
                           stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    last_tag = cmd.stdout.read().decode() or cmd.stderr.read().decode()
    last_tag = last_tag.strip()
    matchobj = re.match(r'^(?P<v>v)?(?P<major>\d)\.(?P<minor>\d)\.(?P<patch>\d)$', last_tag)
    if matchobj is not None:
        if args.patch:
            tag(matchobj.group('v'), matchobj.group('major'), matchobj.group('minor'),
                int(matchobj.group('patch')) + 1, args)
        elif args.minor:
            tag(matchobj.group('v'), matchobj.group('major'), int(matchobj.group('minor')) + 1, 0,
                args)
        elif args.major:
            tag(matchobj.group('v'), int(matchobj.group('major')) + 1, 0, 0, args)
        else:
            # CSW: ignore
            print("You need to specify -m, -p or -M since it's not the first tag")
            parser.print_help()
            exit(1)
    elif last_tag.strip() == 'fatal: No names found, cannot describe anything.':
        if not args.quiet:
            # CSW: ignore
            print('Creating first tag:')
        tag('v' if confirm("Add 'v' prefix") else None, *FRIST_TAG, args=args)
    elif last_tag.startswith('fatal'):
        # CSW: ignore
        print(last_tag.strip())
        exit(1)
    else:
        # CSW: ignore
        print("invalid tag:", repr(last_tag))
        exit(1)

if __name__ == '__main__':
    main()
