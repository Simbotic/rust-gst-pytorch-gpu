# Pytorch - VSCode Devcontainer

## Contains
- Rust
- GStreamer
- Pytorch 1.3.1
- CUDA 10.2
- cuDNN 7.x

## Setup

- Run the initialization script: `./setup.sh`
- Install the VSCode extension [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- Press <kbd>F1</kbd> to bring up the Command Palette and type in *remote-containers* for a full list of commands
- Run the `Remote-Containers: Reopen in Container` command or run `Remote-Containers: Open Folder in Container...` command and select the local folder

## Test the installation
execute `python src/test/test.py`
