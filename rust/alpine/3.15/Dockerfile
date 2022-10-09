#TAG: alpine-3.15
FROM rust:alpine as builder

# Image updates
RUN apk update
RUN apk upgrade
RUN apk add git build-base openssl-dev pkgconf perl ca-certificates curl

# Build Cargo Bins
RUN ARCH=$(apk --print-arch); \
    case $ARCH in \
    aarch64) export CFLAGS='-mno-outline-atomics';; \
    esac; \
    cargo install cargo-edit cargo-generate wasm-pack trunk bacon just

FROM alpine:3.15

# Image updates
RUN apk update
RUN apk upgrade
RUN apk add git build-base openssl-dev pkgconf perl ca-certificates curl

# Env
ENV RUSTUP_HOME=/usr/local/rustup
ENV CARGO_HOME=/usr/local/cargo
ENV PATH=/usr/local/cargo/bin:$PATH

# Rust
RUN ARCH=$(apk --print-arch); \
    case $ARCH in \
    x86_64) RUST_TARGET='x86_64-unknown-linux-musl';; \
    aarch64) RUST_TARGET='aarch64-unknown-linux-musl';; \
    *) echo "Arch not supported!"; exit 1;; \
    esac; \
    mkdir -p target/$RUST_TARGET/release; \
    curl -sSf https://static.rust-lang.org/rustup/dist/$RUST_TARGET/rustup-init -o target/$RUST_TARGET/release/rustup-init; \
    curl -sSf https://static.rust-lang.org/rustup/dist/$RUST_TARGET/rustup-init.sha256 | sha256sum -c; \
    chmod +x target/$RUST_TARGET/release/rustup-init; \
    ./target/$RUST_TARGET/release/rustup-init -y --no-modify-path; \
    rm -rf target
RUN rustup toolchain install nightly
RUN rustup target add wasm32-unknown-unknown

# Copy Cargo Bins
COPY --from=builder /usr/local/cargo/bin /usr/local/cargo/bin
