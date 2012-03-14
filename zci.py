#!/usr/bin/env python
import os
import sys
import argparse
from StringIO import StringIO
import requests
import yaml


PKGLIST_URL = "https://raw.github.com/hhatto/zci/master/package.yaml"
DEFAULTS = {'install_path': '~/.zsh/completion/'}


class Command(object):

    @classmethod
    def search(self, opts):
        target_package = opts.target_package
        pkg = load_package()
        is_found = False
        for key in pkg.iterkeys():
            if target_package in key:
                print "%s - %s" % (key, pkg[key])
                is_found = True
        if not is_found:
            print "package not found."
            return -1
        return 0

    @classmethod
    def install(self, opts):
        target_package = opts.target_package
        pkg = load_package()
        url = pkg.get(target_package)
        if not url:
            print "%s not found" % target_package
            return -1

        zshfunc = get_zshcomp(target_package, url)
        _name = '_' + target_package
        path = os.path.join(os.path.expanduser(DEFAULTS['install_path']),
                            _name)
        zshfile = open(path, 'w+')
        zshfile.write(zshfunc)
        zshfile.close()
        print "'%s' zsh completion function install success." % target_package
        return 0


def load_package():
    f = requests.get(PKGLIST_URL)
    packages = yaml.load(StringIO(f.text))
    return packages


def get_zshcomp(name, url):
    f = requests.get(url)
    return f.text


def get_optionparser():
    parser = argparse.ArgumentParser(prog='zci')
    sub_commands = parser.add_subparsers(help='zci sub command help')

    install = sub_commands.add_parser('install', help='install package')
    install.add_argument('target_package', help='package name')
    install.set_defaults(func=Command.install)

    search = sub_commands.add_parser('search', help='search package')
    search.add_argument('target_package', help='package name')
    search.set_defaults(func=Command.search)

    sub_commands.add_parser('help', help='sub command help')

    return parser


def main():
    parser = get_optionparser()
    opts = parser.parse_args(sys.argv[1:])
    target_package = opts.target_package
    return opts.func(opts)

if __name__ == '__main__':
    sys.exit(main())
