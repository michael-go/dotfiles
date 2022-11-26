if [ -d "/opt/homebrew/opt/fzf" ]; then
  fzf_root=/opt/homebrew/opt/fzf
else
  fzf_root=/usr/local/opt/fzf
fi

# Setup fzf
# ---------
if [[ ! "$PATH" == *${fzf_root}/bin* ]]; then
  PATH="${PATH:+${PATH}:}${fzf_root}/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "${fzf_root}/shell/completion.zsh" 2> /dev/null

# Key bindings
# ------------
source "${fzf_root}/shell/key-bindings.zsh"
