#!/bin/sh

# configure dnf
sudo echo 'max_parallel_downloads=6' | sudo tee -a /etc/dnf/dnf.conf &&
sudo echo 'deltarpm=True' | sudo tee -a /etc/dnf/dnf.conf &&
sudo echo 'install_weak_deps=False' | sudo tee -a /etc/dnf/dnf.conf &&
sudo echo 'defaultyes=True' | sudo tee -a /etc/dnf/dnf.conf &&

# enable auto trim
sudo systemctl enable fstrim.timer &&

# enable rpm fusion free and non-free
sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm &&
sudo dnf upgrade --refresh &&

# enable flathub
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
sudo flatpak update &&

# install nvidia
sudo dnf install -y akmod-nvidia &&
sudo dnf install -y xorg-x11-drv-nvidia-cuda &&
sudo dnf install -y vdpauinfo libva-vdpau-driver libva-utils vulkan &&

# install general softwares
sudo dnf install -y alacritty btop deluge-gtk deadbeef deadbeef-plugins deadbeef-mpris2-plugin discord dunst ffmpegthumbnailer fish flameshot mediainfo mpv neofetch neovim pcmanfm picom qalculate-gtk rofi starship sxiv xed zathura &&
sudo flatpak install flathub com.bitwarden.desktop com.vscodium.codium &&
sudo dnf install -y unzip p7zip p7zip-plugins unrar &&
sudo dnf install -y gimp gimpfx-foundry gmic-gimp gimp-paint-studio krita libreoffice-calc libreoffice-draw libreoffice-langpack-hu libreoffice-writer thunderbird &&

# install codecs
sudo dnf install -y gstreamer1-plugins-{bad-*,good-*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel &&
sudo dnf install -y lame* --exclude=lame-devel &&
sudo dnf group upgrade -y --with-optional Multimedia &&

# for gaming
sudo dnf install wine lutris steam &&
sudo flatpak install flathub net.davidotek.pupgui2 com.heroicgameslauncher.hgl &&

# kvm virtualization setup
sudo dnf install -y bridge-utils libvirt virt-install qemu-kvm &&
sudo dnf install -y libvirt-devel virt-top libguestfs-tools guestfs-tools &&
sudo systemctl enable libvirtd &&
sudo dnf install -y virt-manager &&

# qtile from source
sudo dnf install -y python3-pip python3-cffi python3-xcffib pango wlroots-devel &&
sudo dnf install -y python3-cairocffi &&
sudo pip install --no-input qtile &&
sudo echo '[Desktop Entry]' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
sudo echo 'Name=Qtile' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
sudo echo 'Comment=Qtile Session' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
sudo echo 'Exec=qtile start' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
sudo echo 'Type=Application' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
sudo echo 'Keywords=wm;tiling' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
sudo chmod +x /usr/share/xsessions/qtile.desktop
