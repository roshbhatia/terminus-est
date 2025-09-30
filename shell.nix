{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  name = "terminus-est";

  buildInputs = with pkgs; [
    qmk
  ];

  shellHook = ''
    echo "Validating dependencies..."

    if ! qmk doctor >/dev/null 2>&1 || [ ! -d "./qmk_firmware" ]; then
      echo "Running qmk setup..."
      qmk setup
    fi
  '';
}
