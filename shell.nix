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
    export QMK_HOME="$(pwd)/qmk_firmware";
    export PYTHONPATH="$(pwd)/qmk_firmware/lib/python";
    export QMK_CONFIG="$(pwd)/qmk_config";
  '';

}
