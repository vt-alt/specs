Name: tinycompress
Version: 1.2.4
Release: alt1

Summary: Userspace Interface to Kernel ALSA Compressed Audio APIs
License: LGPLv2.1+ or BSD
Group: Sound

Url: http://git.alsa-project.org/?p=tinycompress.git
Source: %name-%version.tar

BuildRequires: libalsa-devel
BuildRequires: glibc-kernheaders

%description
This package contains cplay and crecord command line utilities which
demonstrate the usage of ALSA Compressed Audio API via tinycompress.

%package -n lib%name
Summary: Userspace Interface to Kernel ALSA Compressed Audio APIs
Group: System/Libraries

%description -n lib%name
Userspace library for anyone who wants to use the ALSA compressed APIs
introduced in Linux 3.3

This library provides the APIs to open a ALSA compressed device
and read/write compressed data like MP3 etc to it.

%package -n lib%name-devel
Summary: Headers and libraries for %name development
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for %name.

%prep
%setup
rm -r include/sound
ln -s %_includedir/sound include/

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%doc README
%_includedir/%name
%_libdir/lib%name.so

%changelog
* Wed Oct 21 2020 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4

* Wed Jun 10 2020 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3

* Thu Feb 20 2020 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Jan 24 2019 Michael Shigorin <mike@altlinux.org> 1.1.8-alt1
- 1.1.8

* Wed Oct 17 2018 Michael Shigorin <mike@altlinux.org> 1.1.7-alt1
- 1.1.7

* Wed Apr 04 2018 Michael Shigorin <mike@altlinux.org> 1.1.6-alt1
- 1.1.6

* Wed Nov 22 2017 Michael Shigorin <mike@altlinux.org> 1.1.5-alt1
- 1.1.5

* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 1.1.4-alt1
- 1.1.4

* Thu Dec 22 2016 Michael Shigorin <mike@altlinux.org> 1.1.3-alt1
- 1.1.3

* Mon Jun 20 2016 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1
- 1.1.1

* Mon Nov 09 2015 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- built for ALT Linux (based on Mageia 0.2.0 package)

