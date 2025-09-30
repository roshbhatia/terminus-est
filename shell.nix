{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  name = "terminus-est";

  buildInputs = with pkgs; [
    qmk
  ];

  shellHook = ''
    qmk setup
  '';
}
