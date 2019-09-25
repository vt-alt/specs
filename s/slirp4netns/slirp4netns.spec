Name: slirp4netns
Version: 0.3.0
Release: alt1
Summary:  User-mode networking for unprivileged network namespaces 

Group: System/Configuration/Other
License: GPLv2
Url: https://github.com/rootless-containers/slirp4netns
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: libglib2-devel

%description
Starting with Linux 3.8, unprivileged users can create
network_namespaces(7) along with user_namespaces(7). However,
unprivileged network namespaces had not been very useful, because
creating veth(4) pairs across the host and network namespaces still
requires the root privileges. (i.e. No internet connection)

slirp4netns allows connecting a network namespace to the Internet in a
completely unprivileged way, by connecting a TAP device in a network
namespace to the usermode TCP/IP stack ("slirp").

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%doc README.md
%_man1dir/%name.*


%changelog
* Sat Jun  8 2019 Terechkov Evgenii <evg@altlinux.org> 0.3.0-alt1
- Initial build for ALT Linux Sisyphus
