# azurelinux-sudo-rs
Memory safe sudo and su, packaged for Azurelinux

## Description

Ubuntu 25.10 will try to release with the version of sudo that has been built in rust, meaning higher security and way better perfomance. The reason behind this repo, is to test sudo-rs in AzureLinux 3, and if it works properly to suggest it for AzureLinux 4. Specially if used in conjunction with the "oxidizr" tool, made to replace the GNU Coreutils for the Rust Coreutils.

*Note*: This is a proposal for AzureLinux 4, which is why we are downloading a newer version of Rust, as part of the installation process that follows. This is only required for compiling the RPM, and no
t for running the rust-coreutils.

## Instructions

RPMs are being built and release using GitHub actions, so you only need to download the package and install it.

Start with a brand new AzureLinux 3 VM. Then, inside of it, run:

```
sudo tdnf -y update
sudo tdnf -y install cargo
sudo tdnf -y install https://github.com/fede2cr/azurelinux-sudo-rs/releases/download/v0.2.10/sudo-rs-0.2.10-2.azl3.$(uname -m).rpm
cargo install --git https://github.com/fede2cr/oxidizr --branch azurelinux
sudo .cargo/bin/oxidizr enable -e sudo-rs
ls -l $(which sudo)
sudo --version
sudo ls
```

Great. Now do your testing with some interesting sudoers config files.

