Name: stress-ng
Version: 0.09.60
Release: alt1
Summary: Stress test a computer system in various ways
Group: System/Kernel and hardware
License: GPLv2

Url: http://kernel.ubuntu.com/~cking/stress-ng/
#Git: git://kernel.ubuntu.com/cking/stress-ng.git
Source: %name-%version.tar

BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: libbsd-devel
BuildRequires: libcap-devel
BuildRequires: libgcrypt-devel
BuildRequires: libseccomp-devel
BuildRequires: libkeyutils-devel
BuildRequires: liblksctp-devel
BuildRequires: zlib-devel

%description
stress-ng will stress test a computer system in various selectable ways. It was
designed to exercise various physical subsystems of a computer as well as the
various operating system kernel interfaces.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%doc README
%_bindir/stress-ng
%_datadir/bash-completion/completions/stress-ng
%_datadir/stress-ng/
%_mandir/man1/stress-ng.1.*

%changelog
* Mon Jul 01 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.09.60-alt1
- New version
- Spec: cleanup

* Sat Aug 11 2018 Vitaly Chikunov <vt@altlinux.org> 0.09.36-alt2
- First package for ALT
