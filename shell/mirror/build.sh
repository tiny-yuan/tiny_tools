#!/bin/bash
sudo cp *.deb /home/repos/jiasion -rf
cd /home/repos/jiasion
dpkg-scanpackages -m . > Packages
apt-ftparchive release . > Release
gpg --armor --detach-sign --sign -o Release.gpg Release
gpg --clearsign -o InRelease Release