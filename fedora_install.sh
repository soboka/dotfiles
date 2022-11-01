#!/bin/sh

# Packages
PKGS='alacritty btop deluge-gtk deadbeef deadbeef-plugins deadbeef-mpris2-plugin discord dunst ffmpegthumbnailer fish flameshot mediainfo mpv neofetch neovim pcmanfm picom qalculate-gtk rofi starship sxiv xed zathura unzip p7zip p7zip-plugins unrar gimp gimpfx-foundry gmic-gimp gimp-paint-studio krita libreoffice-calc libreoffice-draw libreoffice-langpack-hu libreoffice-writer thunderbird vivaldi-stable'
NVD='akmod-nvidia xorg-x11-drv-nvidia-cuda vdpauinfo libva-vdpau-driver libva-utils vulkan'
GME='wine lutris steam'
VRT='bridge-utils libvirt virt-install qemu-kvm libvirt-devel virt-top libguestfs-tools guestfs-tools'
FLAT='com.bitwarden.desktop com.vscodium.codium com.github.tchx84.Flatseal org.gnome.FontManager net.davidotek.pupgui2 com.heroicgameslauncher.hgl'

# make dirs for my auto mounted storages and I am manualy edit fstab after this
sudo mkdir /mnt/BarrackHDD /mnt/BarrackHDD2 /mnt/BarrackSSD /mnt/BarrackSSD2 &&
echo "All storage dir created." &&

# configure dnf
sudo echo 'max_parallel_downloads=6' | sudo tee -a /etc/dnf/dnf.conf &&
sudo echo 'deltarpm=True' | sudo tee -a /etc/dnf/dnf.conf &&
sudo echo 'install_weak_deps=False' | sudo tee -a /etc/dnf/dnf.conf &&
sudo echo 'defaultyes=True' | sudo tee -a /etc/dnf/dnf.conf &&

# enable auto trim
sudo systemctl enable fstrim.timer &&
echo "Auto Trim Enabled." &&

# enable rpm fusion free and non-free and vivaldi browser repo
sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm &&
sudo dnf config-manager --add-repo https://repo.vivaldi.com/archive/vivaldi-fedora.repo &&
sudo dnf upgrade -y --refresh &&
echo "All repositories added." &&

# install nvidia
sudo dnf install -y $NVD &&
echo "Nvidia drivers installed." &&

# install general softwares
sudo dnf install -y $PKGS &&
# Somehow vivaldi make duplicate repo so we remove one
sudo rm /etc/yum.repos.d/vivaldi-fedora.repo &&
echo "All package installed." &&

# install codecs
sudo dnf install -y gstreamer1-plugins-{bad-*,good-*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel &&
sudo dnf install -y lame* --exclude=lame-devel &&
sudo dnf group upgrade -y --with-optional Multimedia &&
echo "All codecs installed." &&

# for gaming
sudo dnf install -y $GME &&
echo "All gaming stuff installed." &&

# kvm virtualization setup
sudo dnf install -y $VRT &&
sudo systemctl enable libvirtd &&
sudo dnf install -y virt-manager &&
echo "All virtualization stuff installed." &&

# enable flathub
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
sudo flatpak update &&

# softwares from flathub
sudo flatpak install -y flathub $FLAT && 
echo "Flathub enabled and all flatpak installed." &&

# qtile from source
#sudo dnf install -y python3-pip python3-cffi python3-xcffib pango wlroots-devel psutils python3-dbus-next python3-pyxdg &&
#sudo dnf install -y python3-cairocffi &&
#pip install --no-input qtile &&
#sudo echo '[Desktop Entry]' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
#sudo echo 'Name=Qtile' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
#sudo echo 'Comment=Qtile Session' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
#sudo echo 'Exec=qtile start' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
#sudo echo 'Type=Application' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
#sudo echo 'Keywords=wm;tiling' | sudo tee -a /usr/share/xsessions/qtile.desktop &&
#sudo chmod +x /usr/share/xsessions/qtile.desktop
sudo dnf copr enable frostyx/qtile &&
sudo dnf install qtile &&
sudo dnf install qtile-extras &&
echo "Qtile installed." &&

# Notification
notify-send "All Installation and configuration is done" && 
echo "All Installation and configuration is done"
