ARG UBUNTU_VERSION=18.04

FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu${UBUNTU_VERSION} as base
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES},display

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
        mesa-utils \
        build-essential \
        sudo \
        cmake \
        libgtk2.0-dev \
        libgtk-3-dev \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        libfreetype6-dev \
        libhdf5-serial-dev \
        unzip \
        zip \
        libzmq3-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libeigen3-dev \
        libdc1394-22-dev \
        pkg-config \
        software-properties-common \
        unzip \
        zip \
        wget \
        git \
        vim \
        curl \
        libssl-dev \
        lldb \
        procps \
        lsb-release \
        x11-xserver-utils \
        libmagick++-dev \
        python3-dev

# I'm not sure about --allow-change-held-packages
RUN apt install -y --allow-change-held-packages libnccl2 \
        libnccl-dev \ 
        libyaml-dev

# GStreamer

RUN apt-get install -y --no-install-recommends \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libgstreamer-plugins-good1.0-dev \
    libgstreamer-plugins-bad1.0-dev \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    libgstrtspserver-1.0-dev \
    libgstreamer1.0-0 \
    gstreamer1.0-libav \
    gstreamer1.0-doc \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 \
    gstreamer1.0-pulseaudio \
    gtk-doc-tools
    
ARG USERNAME=sim
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Non-root user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && mkdir -p /home/$USERNAME/.vscode-server /home/$USERNAME/.vscode-server-insiders \
    && chown ${USER_UID}:${USER_GID} /home/$USERNAME/.vscode-server* \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && usermod -a -G audio,video $USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER $USERNAME
ENV HOME /home/$USERNAME
WORKDIR $HOME

# # Latest Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain stable -y
ENV PATH=$HOME/.cargo/bin:$PATH
RUN rustup component add rls rust-analysis rust-src rustfmt clippy
RUN cargo install fd-find ripgrep

# Pip from installation script to install the lastest version
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN sudo python3 get-pip.py

#        python3-numpy \
#        python3-pip \
#        python3-tk \

#Pytorch
RUN sudo pip install torch torchvision

# Remember de Pillow version 7.0.0 bug