Name: btcat
Version: 0.2
Release: alt1

Summary: Btcat is a torrent command line tool
License: GPL-3.0-or-later
Group: Networking/WWW
Url: https://github.com/glebfm/btcat

BuildArch: noarch

Source: btcat

BuildRequires: rpm-build-python3

%description
btcat is a command line tool that downloads a file using the bittorrent
protocol and outputs its contents to the standard output. btcat streams
the data sequentially, which allows processing the file in a pipeline
before the whole transfer has been completed. It is possible, for
instance, to reproduce a media file while it's still downloading.

%prep
%setup -c -T
cp %_sourcedir/btcat .

%install
mkdir -p %buildroot/%_bindir
install -m755 btcat %buildroot%_bindir/

%files
%_bindir/btcat

%changelog
* Fri Mar 27 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2-alt1
- Updated to v0.2.

* Fri Dec 11 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt2
- Fixed program permissions.

* Fri Feb 01 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Initial build
