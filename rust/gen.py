#!/usr/bin/python3

import sys, os


rust_targets = {
    "alpine": {
        "amd64": "x86_64-unknown-linux-musl",
        "arm64": "aarch64-unknown-linux-musl",
        "riscv64": None,
        "ppc64le": None,
        "s390x": None,
        "386": None,
        "mips64le": None,
        "mips64": None,
        "arm/v7": None
    },
    "debian": {
        "amd64": "x86_64-unknown-linux-gnu",
        "arm64": "aarch64-unknown-linux-gnu",
        "riscv64": None,
        "ppc64le": "powerpc64le-unknown-linux-gnu",
        "s390x": "s390x-unknown-linux-gnu",
        "386": "i686-unknown-linux-gnu",
        "mips64le": "mips64el-unknown-linux-gnuabi64",
        "mips64": "mips64-unknown-linux-gnuabi64",
        "arm/v7": "armv7-unknown-linux-gnueabihf"
    }
}


# Creates Dockerfile and returns a CSV of tags
def main(arch, distro, img, version):
    arch = arch.strip()
    distro = distro.strip()

    distro_tags = distro.split(":")
    distro = distro_tags.pop(0)

    target = rust_targets[distro][arch]
    if target is None:
        print("None")
        return

    # Dockerfile
    with open("Dockerfile." + distro, "r") as file:
        dockerfile = file.read()

    dockerfile = dockerfile.replace("%%TAG%%", distro_tags[-1])
    dockerfile = dockerfile.replace("%%RUST_TARGET%%", target)
    dockerfile = dockerfile.replace("%%RUST_VERSION%%", version)

    with open("Dockerfile", "w") as file:
        file.write(dockerfile)

    # Tags
    tags = []
    for d in distro_tags:
        tags.append(distro + "-" + d)
        if d != "latest":
            tags.append(version + "-" + distro + "-" + d)
        else:
            tags.append(version + "-" + distro)

    tags = map(lambda x: img + ":" + x, tags)
    out = ",".join(tags)
    print(out)


if __name__ == "__main__":
    argv = sys.argv
    main(argv[1], argv[2], argv[3], argv[4])
