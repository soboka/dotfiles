#!/bin/sh

# It's a simple script to pre config a freshly installed fedora i3 distro with all my stuff and with my qtile wm.

# Colors
CL='\033[0;32m'
NCL='\033[0m'
UR='\033[0;31m'

# Packages
PKGS='alacritty btop deluge-gtk deadbeef deadbeef-plugins deadbeef-mpris2-plugin discord dunst exa ffmpegthumbnailer fish flameshot mediainfo mpv neofetch neovim pcmanfm picom qalculate-gtk rofi starship sxiv xed zathura zathura-pdf-poppler zathura-plugins-all unzip p7zip p7zip-plugins unrar gimp gimpfx-foundry gmic-gimp gimp-paint-studio krita libreoffice-calc libreoffice-draw libreoffice-langpack-hu libreoffice-writer thunderbird vivaldi-stable playerctl psutils'
NVD='akmod-nvidia xorg-x11-drv-nvidia-cuda vdpauinfo libva-vdpau-driver libva-utils vulkan'
GME='wine lutris steam'
VRT='bridge-utils libvirt virt-install qemu-kvm libvirt-devel virt-top libguestfs-tools guestfs-tools'
FLAT='com.bitwarden.desktop com.vscodium.codium com.github.tchx84.Flatseal org.gnome.FontManager net.davidotek.pupgui2 com.heroicgameslauncher.hgl'

# make dirs for my auto mounted storages and I am manualy edit fstab after this
sudo mkdir /mnt/BarrackHDD /mnt/BarrackHDD2 /mnt/BarrackSSD /mnt/BarrackSSD2 &&
echo -e "${CL}###### All storage directories created. ###### ${NCL}" &&

# configure dnf
sudo echo 'max_parallel_downloads=6' | sudo tee -a /etc/dnf/dnf.conf &&
sudo echo 'deltarpm=True' | sudo tee -a /etc/dnf/dnf.conf &&
sudo echo 'install_weak_deps=False' | sudo tee -a /etc/dnf/dnf.conf &&
sudo echo 'defaultyes=True' | sudo tee -a /etc/dnf/dnf.conf &&
echo -e "${CL}###### DNF configuration is finished. ######${NCL}" &&

# enable auto trim
sudo systemctl enable fstrim.timer &&
echo -e "${CL}###### Auto Trim Enabled. ######${NCL}" &&

# enable rpm fusion free and non-free and vivaldi browser repo
sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm &&
sudo dnf config-manager --add-repo https://repo.vivaldi.com/archive/vivaldi-fedora.repo &&
sudo dnf upgrade -y --refresh &&
echo -e "${CL}###### All repositories added. ######${NCL}" &&

# install nvidia
sudo dnf install -y $NVD &&
echo -e "${CL}###### Nvidia drivers installation finished. ######${NCL}" &&

# install general softwares
sudo dnf install -y $PKGS &&
# Somehow vivaldi make duplicate repo so we remove one
sudo rm /etc/yum.repos.d/vivaldi-fedora.repo &&
echo -e "${CL}###### All package installation finished. ######${NCL}" &&

# install codecs
sudo dnf install -y gstreamer1-plugins-{bad-*,good-*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel &&
sudo dnf install -y lame* --exclude=lame-devel &&
sudo dnf group upgrade -y --with-optional Multimedia &&
echo -e "${CL}###### All codecs installation finished. ######${NCL}" &&

# for gaming
sudo dnf install -y $GME &&
echo -e "${CL}###### All gaming stuff installation finished. ######${NCL}" &&

# kvm virtualization setup
sudo dnf install -y $VRT &&
sudo systemctl enable libvirtd &&
sudo dnf install -y virt-manager &&
echo -e "${CL}###### All virtualization stuff installation finished. ######${NCL}" &&

# pamixer from source
sudo dnf install -y meson clang cmake pulseaudio-libs-devel cxxopts-devel &&
cd ~/Git &&
git clone https://github.com/cdemoulins/pamixer.git &&
cd ~/Git/pamixer &&
meson setup build &&
meson compile -C build &&
sudo meson install -C build &&
cd ~ &&
echo -e "${CL}###### Pamixer compilation and installation finished. ######${NCL}" &&

# enable flathub
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
sudo flatpak update &&

# softwares from flathub
sudo flatpak install -y flathub $FLAT && 
echo -e "${CL}###### Flathub enabled and all flatpak installation finished. ######${NCL}" &&

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
sudo dnf copr enable -y frostyx/qtile &&
sudo dnf install -y qtile &&
sudo dnf install -y qtile-extras &&
echo -e "${CL}###### Qtile installation finished. ######${NCL}" &&

# END Notification
notify-send "All Installation and configuration is done." && 
echo -e "${CL}###### All Installation and configuration is done. ######" &&
echo -e "${UR}###### You need to REBOOT the computer. ######${NCL}"

