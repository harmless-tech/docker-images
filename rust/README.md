# [harmless/rust](https://hub.docker.com/r/harmlesstech/rust)
[Repo](https://github.com/harmless-tech/docker-images) <br><br>
Rust images with additional tools installed.

## Tags
- [alpine-latest](), [alpine-3.15](), [alpine-3.14]()
- [debian-latest](), [debian-bullseye-slim](), [debian-buster](), [debian-buster-slim]()
<br>
<br>
*You can also append a rust version to the front of any tag. (EX: 1.64.0-debian-latest)*

## What's installed?
- Rustup
  - Latest stable toolchain
  - Latest nightly toolchain (Image is rebuilt about once a week)
  - Cargo, RustFmt, Clippy
- Cargo Tools
  - [cargo-edit](https://github.com/killercup/cargo-edit)
  - [cargo-generate](https://github.com/cargo-generate/cargo-generate)
  - [wasm-pack](https://github.com/rustwasm/wasm-pack)
  - [trunk](https://github.com/thedodd/trunk)
  - [bacon](https://github.com/Canop/bacon)
  - [just](https://github.com/casey/just)
