{
  pkgs ? import <nixpkgs> {
    config.allowUnsupportedSystem = true;
  },
}:

pkgs.mkShell {
  buildInputs = with pkgs; [
    qmk

    gcc-arm-embedded
    (if stdenv.isDarwin then pkgsCross.avr.buildPackages.gcc else avr-gcc)
    (if stdenv.isDarwin then pkgsCross.avr.avrlibc else avrlibc)
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
    echo "qmk --version: $(qmk --version)"
    echo "avr-gcc --version: $(avr-gcc --version | head -1)"
    echo "arm-none-eabi-gcc --version: $(arm-none-eabi-gcc --version | head -1)"
  '';

  QMK_HOME = "$PWD/qmk_firmware";
  PYTHONPATH = "$QMK_HOME/lib/python";
  QMK_CONFIG = "$PWD/qmk_config";
}
