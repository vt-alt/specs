%define _unpackaged_files_terminate_build 1

Name: ipsumdump
Version: 1.86
Release: alt3
Group: Networking/Other
Summary: Summarizes TCP/IP dump files into a self-describing ASCII format easily readable by humans and programs
License: %bsd
Url: http://www.read.seas.harvard.edu/~kohler/ipsumdump/

# https://github.com/kohler/ipsumdump.git
Source: %name-%version.tar
Patch1: %name-%version-alt-gcc8.patch
Patch2: %name-%version-alt-glibc.patch

BuildRequires: rpm-build-licenses
BuildRequires: perl-podlators
BuildRequires: gcc-c++

%description
Ipsumdump reads IP packets from tcpdump(1) files, or network interfaces,
and summarizes their contents in an ASCII file.
Ipsumdump can read packets from network interfaces, from tcpdump files, and
from existing ipsumdump files.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%configure
%make_build

%install
%makeinstall

%files
%doc NEWS.md README.md
%_bindir/ipsumdump
%_bindir/ipaggcreate
%_bindir/ipaggmanip
%_man1dir/ipsumdump.1*
%_man1dir/ipaggcreate.1*
%_man1dir/ipaggmanip.1*

%changelog
* Tue Jul 09 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.86-alt3
- Fixed build.

* Mon Feb 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.86-alt2
- Fixed build with gcc-8.

* Tue Nov 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.86-alt1
- Updated to upstream version 1.86.

* Mon Dec 29 2014 Andriy Stepanov <stanv@altlinux.ru> 1.84-alt2
- Update BuildRequires

* Mon Dec 29 2014 Andriy Stepanov <stanv@altlinux.ru> 1.84-alt1
- ALTLinux build
