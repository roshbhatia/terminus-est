{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  buildInputs = with pkgs; [
    qmk

    gcc-arm-embedded
    avr-gcc
    avr-binutils
    avr-libc
    avrlibc
    avrdude

    gnumake
    cmake
    ninja

    dfu-programmer
    dfu-util
    teensy-loader-cli

    python3
    python3Packages.pip
    python3Packages.setuptools
    python3Packages.wheel
  ];

  shellHook = ''
    echo "QMK development environment loaded!"
    echo "Available tools:"
    echo "  qmk --version: $(qmk --version)"
    echo "  avr-gcc --version: $(avr-gcc --version | head -1)"
    echo "  arm-none-eabi-gcc --version: $(arm-none-eabi-gcc --version | head -1)"
    echo ""
    echo "To set up QMK in this directory:"
    echo "  qmk setup -H ."
    echo ""
    echo "To initialize submodules if you have an existing QMK repo:"
    echo "  git submodule update --init --recursive"
  '';

  QMK_HOME = "$PWD";
  PYTHONPATH = "$PWD/lib/python";
}
