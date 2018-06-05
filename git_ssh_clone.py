#!/usr/bin/env python3
"""Convert an HTTP url to the SSH equivalent and clone the repo."""

import sys
import subprocess


def is_ssh(uri):
    """Check if URI is a git SSH URI."""
    return uri.split('@')[-1] == 'git'


def to_ssh(uri):
    """convert a URI to an SSH URI."""
    ssh_uri = uri.split('://')[-1].split('/')
    ssh_uri = f'git@{ssh_uri[0]}:{"/".join(ssh_uri[1:])}'
    return ssh_uri


def main(args):
    """Entry point."""
    if len(args) < 2:
        return 1
    uri = args[-1]
    if not is_ssh(uri):
        uri = to_ssh(uri)
    cmd = ['git', 'clone']
    cmd += args[1:-1]
    cmd.append(uri)
    subproc = subprocess.run(cmd)
    return subproc.returncode


if __name__ == '__main__':
    sys.exit(main(sys.argv))
