#TAG: ubuntu-focal
FROM rust:latest as builder

# Image updates
RUN apt update
RUN apt upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends tzdata
RUN apt install -y pkg-config
RUN apt install -y git curl build-essential libssl-dev

# Build Cargo Bins
RUN cargo install cargo-edit cargo-generate wasm-pack trunk bacon just

FROM ubuntu:focal

# Image updates
RUN apt update
RUN apt upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends tzdata
RUN apt install -y pkg-config
RUN apt install -y git curl build-essential libssl-dev

# Env
ENV RUSTUP_HOME=/usr/local/rustup
ENV CARGO_HOME=/usr/local/cargo
ENV PATH=/usr/local/cargo/bin:$PATH

# Rust
RUN ARCH=$(dpkg --print-architecture); \
    case $ARCH in \
    amd64) RUST_TARGET='x86_64-unknown-linux-gnu';; \
    arm64) RUST_TARGET='aarch64-unknown-linux-gnu';; \
    *) echo "Arch not supported!"; exit 1;; \
    esac; \
    mkdir -p target/$RUST_TARGET/release; \
    curl -sSf https://static.rust-lang.org/rustup/dist/$RUST_TARGET/rustup-init -o target/$RUST_TARGET/release/rustup-init; \
    curl -sSf https://static.rust-lang.org/rustup/dist/$RUST_TARGET/rustup-init.sha256 | sha256sum --check; \
    chmod +x target/$RUST_TARGET/release/rustup-init; \
    ./target/$RUST_TARGET/release/rustup-init -y --no-modify-path; \
    rm -rf target
RUN rustup toolchain install nightly
RUN rustup target add wasm32-unknown-unknown

# Copy Cargo Bins
COPY --from=builder /usr/local/cargo/bin /usr/local/cargo/bin
