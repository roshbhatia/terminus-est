{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  name = "zmk-dev-environment";

  buildInputs = with pkgs; [
    cmake
    dfu-util
    dtc
    gcc-arm-embedded
    git
    go-task
    jq
    ninja
    picotool
    python3
    python3Packages.pyelftools
    python3Packages.west
    which
  ];

  shellHook = ''
    export ZMK_HOME=$(pwd)/firmware
    export ZEPHYR_TOOLCHAIN_VARIANT=gnuarmemb
    export GNUARMEMB_TOOLCHAIN_PATH=${pkgs.gcc-arm-embedded}

    if [ ! -d "$ZMK_HOME/.west" ]; then
      task firmware:setup
      echo ""
    fi
  '';
}
