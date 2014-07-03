Name: retroshare
Version: 0.5.5
Release: 1
Source0: http://downloads.sourceforge.net/project/retroshare/RetroShare/0.5.5c/retroshare_%{version}-0.7068.tar.gz
Patch0: retroshare-0.5.5-compile.patch
Summary: Secure decentralised communication platform
URL: http://retroshare.sf.net/
License: GPL
Group: Networking/File transfer
BuildRequires: pkgconfig(QtGui) < 5.0.0
BuildRequires: pkgconfig(libssh)
BuildRequires: pkgconfig(libupnp)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(protobuf)
BuildRequires: pkgconfig(speex)

%description
RetroShare is a Open Source cross-platform, Friend-2-Friend and secure
decentralised communication platform.

It lets you to securely chat and share files with your friends and
family, using a web-of-trust to authenticate peers and OpenSSL to
encrypt all communication.

RetroShare provides filesharing, chat, messages, forums and channels

%package nogui
Summary: Non-GUI version of RetroShare
Group: Networking/File transfer

%description nogui
Non-GUI version of RetroShare

%prep
%setup -q
%apply_patches
cd src
qmake *.pro

%build
cd src
# As of 0.5.5, not ready for real SMP build
%make || make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 src/retroshare-gui/src/RetroShare %{buildroot}%{_bindir}/
install -m 755 src/retroshare-nogui/src/retroshare-nogui %{buildroot}%{_bindir}/

%files
%{_bindir}/RetroShare

%files nogui
%{_bindir}/retroshare-nogui
