#!/usr/bin/python3

import datetime
import os
import shutil
import subprocess
import sys


def install_dot(src_path, dst_dir="~"):
    print(f"\nInstalling {src_path} to {dst_dir}")

    dst_dir = os.path.expanduser(dst_dir)
    dst_path = os.path.join(dst_dir, src_path)
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)

    if os.path.exists(dst_path):
        with open(src_path) as src_file:
            src_content = src_file.read()
        with open(dst_path) as dst_file:
            dst_content = dst_file.read()

        if src_content == dst_content:
            print(f"  {dst_path} is identical to {src_path}, skipping")
            return

        print("  diff:")
        os.system(f"diff --color -u {dst_path} {src_path}")
        print("")

        backup_path = (
            f"{dst_path}.bak.{datetime.datetime.now().isoformat(timespec='seconds')}"
        )
        print(f"  Backup {dst_path} to {backup_path}")
        shutil.copy(dst_path, backup_path)

    print(f"  Copy {src_path} to {dst_path}")
    shutil.copy(src_path, dst_path)


def main():
    install_dot(".zshrc")
    install_dot(".vimrc")
    install_dot(".tmux.conf")
    install_dot(".config/nvim/init.vim")
    install_dot(".config/nvim/coc-settings.json")
    install_dot(".gitconfig")
    install_dot(".gitignore_global")


if __name__ == "__main__":
    sys.exit(main())
