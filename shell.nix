{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    go-task
    python3
    uv
    black
  ];

  shellHook = ''
    if [ ! -d ".venv" ]; then
      echo "Creating uv virtual environment..."
      uv venv
    fi

    source .venv/bin/activate

    if [ ! -f ".venv/installed" ]; then
      echo "Installing Python dependencies..."
      uv pip install black circuitpython-stubs
      touch .venv/installed
    fi

    echo "Python environment ready!"
    echo "Available commands:"
    echo "  task firmware:setup  - Complete firmware setup"
    echo "  task firmware:flash  - Flash firmware to device"
    echo "  black firmware/      - Format firmware code"
  '';
}
