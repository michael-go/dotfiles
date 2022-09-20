# Dont forget to install:
* git
* zsh
* tmux
* neovim
* fzf
* bat
* node (https://github.com/Schniz/fnm)

# Extra steps
## vim
### neoclide/coc.nvim
```
:CocInstall coc-json
```
for C/C++ support
```
:CocInstall coc-clangd
```
this requries `clangd` to be installed. some options:
* on Ubuntu: `sudo apt install clangd`
* or try via the plugin: `:CocCommand clangd.install`
