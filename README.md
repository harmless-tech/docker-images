# HarmlessTech Docker Images
A bunch of docker images.

- [harmlesstech/rust](md/RUST.md)
- [harmlesstech/node](md/NODE.md)
- [harmlesstech/rustnode](md/RUSTNODE.md)

### How to build
./gen.py takes in the arguments below then uses a template Dockerfile to generate a Dockerfile and places it in
the current directory. It then outputs a CSV of generated tags.

- -i, --img (rust|node|rustnode) REQUIRED
- -a, --arch (arm64|amd64) REQUIRED
- -o, --os (See tags list on one of the above) REQUIRED
- -l, --lts (true|false) OPTIONAL

*gen.py requires python 3. (It has only been tested on python 3.8+)*
