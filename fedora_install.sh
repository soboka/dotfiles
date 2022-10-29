#!/bin/sh

# configure dnf
sudo echo defaultyes=True \ndeltarpm=True \nmax_parallel_downloads=6 \ninstall_weak_deps=False /etc/dnf/dnf.conf &&

# enable rpm fusion free and non-free
sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm &&

# enable flathub
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
flatpak update &&

# install general softwares
sudo dnf install -y alacritty btop deluge-gtk deadbeef deadbeef-plugins deadbeef-mpris2-plugin discord dunst ffmpegthumbnailer fish flameshot krita mediainfo mpv neofetch neovim pcmanfm picom rofi starship sxiv xed zathura &&

# install nvidia
sudo dnf install -y akmod-nvidia &&
sudo dnf install -y xorg-x11-drv-nvidia-cuda &&
sudo dnf install -y vdpauinfo libva-vdpau-driver libva-utils vulkan &&

# install codecs
sudo dnf install -y gstreamer1-plugins-{bad-*,good-*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel &&
sudo dnf install -y lame* --exclude=lame-devel &&
sudo dnf group upgrade -y --with-optional Multimedia &&

# kvm virtualization setup
sudo dnf install -y bridge-utils libvirt virt-install qemu-kvm &&
sudo dnf install -y libvirt-devel virt-top libguestfs-tools guestfs-tools &&
sudo systemctl enable libvirtd &&
sudo dnf install -y virt-manager &&
