#!/bin/sh

# Fetch dependencies and tarball
apt-get install -y libtool pkg-config autoconf-archive python3-dev
apt-get install -y build-essential
wget https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-1.1.1.tar.gz
tar xvf libgpiod-1.1.1.tar.gz
cd libgpiod-1.1.1

# Set up
export PYTHON_VERSION=3
./autogen.sh --enable-tools=yes --enable-bindings-python --prefix=/usr/local

# Install libgpiod
make
make install
ldconfig

# Clean Up
rm -f libgpiod-1.1.1.tar.gz
rm -f libgpiod-1.1.1.tar.gz.1

