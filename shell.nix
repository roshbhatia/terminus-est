{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "zmk-dev-environment";

  buildInputs = with pkgs; [
    # ZMK development tools
    python3
    python3Packages.west
    python3Packages.pyelftools

    # Build tools
    gcc-arm-embedded
    cmake
    ninja
    dtc

    # Development utilities
    git
    go-task

    # Hardware debugging/flashing tools
    dfu-util
    picotool

    # Text processing and validation
    jq

    # Shell utilities
    which
  ];

  shellHook = ''
    echo "⚡ ZMK Development Environment for Terminus Est"
    echo ""
    echo "Available commands:"
    echo "  task firmware:setup     - Setup ZMK environment"
    echo "  task firmware:compile   - Compile firmware"
    echo "  task firmware:test      - Test firmware configuration"
    echo "  task firmware:clean     - Clean build artifacts"
    echo ""

    # Setup ZMK environment variables
    export ZMK_HOME=$(pwd)/firmware
    export ZEPHYR_TOOLCHAIN_VARIANT=gnuarmemb
    export GNUARMEMB_TOOLCHAIN_PATH=${pkgs.gcc-arm-embedded}

    echo "Environment variables set:"
    echo "  ZMK_HOME=$ZMK_HOME"
    echo "  ZEPHYR_TOOLCHAIN_VARIANT=$ZEPHYR_TOOLCHAIN_VARIANT"
    echo ""
  '';
}