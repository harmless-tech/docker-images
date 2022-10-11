#!/usr/bin/python3

import sys, os


def main(version):
    version = version.strip()

    # Get version from cache
    if not os.path.exists("vstore.cache"):
        with open("vstore.cache", "w"):
            pass

    with open("vstore.cache", "r") as file:
        cached = file.read().strip()

    if cached != version:
        with open("vstore.cache", "w") as file:
            file.write(version)
        print("::set-output name=build::true")
    else:
        print("::set-output name=build::false")

    print("::set-output name=version::" + version)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1])
