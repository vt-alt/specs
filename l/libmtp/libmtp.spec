%def_disable static
%define sover 9

Name: libmtp
Version: 1.1.17
Release: alt1
Packager: Dmitriy Khanzhin <jinn@altlinux.org>

Summary: a library for accessing Media Transfer Protocol devices

License: LGPLv2.1+
Group: System/Libraries
Url: http://libmtp.sourceforge.net/

Source: %name-%version.tar

# Automatically added by buildreq on Sat Apr 18 2009
BuildRequires: libusb-devel libgcrypt-devel

%package -n %name%sover
Summary: a library for accessing Media Transfer Protocol devices
Group: System/Libraries
Provides: %name = %version-%release
Obsoletes: %{name}7
Obsoletes: %name < %version-%release

%package -n %name-devel
Summary: %name development environment
Group: Development/C
Requires: %name = %version-%release

%package -n %name-devel-static
Summary: %name static development environment
Group: Development/C
Requires: %name-devel = %version-%release

%package -n %name-examples
Summary: %name usage examples
Group: Sound
Requires: %name = %version-%release

%description
Libmtp is a LGPL library implementation of the Media Transfer Protocol (MTP),
a superset of the Picture Transfer Protocol (PTP).

%description -n %name%sover
Libmtp is a LGPL library implementation of the Media Transfer Protocol (MTP),
a superset of the Picture Transfer Protocol (PTP).

%description -n %name-devel
This package contains all files which are needs to compile programs using
the %name library.

%description -n %name-devel-static
This package contains libraries which are needs to compile programs statically
linked against %name library.

%description -n %name-examples
This package contains example programs for communicating with MTP devices.

%prep
%setup

%build
touch config.rpath
%autoreconf
%configure \
	%{subst_enable static} \
	--with-udev=/lib/udev \
	--with-udev-group=audio \
	--with-udev-mode=0660

%make_build

%install
%make DESTDIR=%buildroot install

# Replace links with relative links
rm -f %buildroot%_bindir/mtp-{delfile,getfile,newfolder,sendfile,sendtr}
pushd %buildroot%_bindir
ln -sf mtp-connect mtp-delfile
ln -sf mtp-connect mtp-getfile
ln -sf mtp-connect mtp-newfolder
ln -sf mtp-connect mtp-sendfile
ln -sf mtp-connect mtp-sendtr
popd

rm -rf %buildroot%_docdir/%name-%version/html

%files -n %name%sover
%_libdir/*.so.*
/lib/udev/hwdb.d/*
/lib/udev/rules.d/*
/lib/udev/mtp-probe
%doc AUTHORS README TODO

%files -n %name-devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/*.so

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%endif

%files -n %name-examples
%_bindir/*

%changelog
* Tue Feb 04 2020 Dmitriy Khanzhin <jinn@altlinux.org> 1.1.17-alt1
- 1.1.17
- enabled mtpz

* Sun Oct 28 2018 Dmitriy Khanzhin <jinn@altlinux.org> 1.1.16-alt1
- 1.1.16
- removed unneeded patch

* Sat Mar 31 2018 Dmitriy Khanzhin <jinn@altlinux.org> 1.1.15-alt1
- 1.1.15

* Sun Mar 11 2018 Dmitriy Khanzhin <jinn@altlinux.org> 1.1.14-alt1
- 1.1.14

* Sun Apr 09 2017 Dmitriy Khanzhin <jinn@altlinux.org> 1.1.13-alt1
- 1.1.13

* Sun Dec 18 2016 Dmitriy Khanzhin <jinn@altlinux.org> 1.1.12-alt1
- 1.1.12

* Tue Mar 15 2016 Dmitriy Khanzhin <jinn@altlinux.org> 1.1.11-alt1
- 1.1.11

* Thu Sep 25 2014 Alexey Shabalin <shaba@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Mon Jul 01 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.6-alt2
- build with --with-udev-group=audio and --with-udev-mode=0660

* Fri Jun 07 2013 Alexey Shabalin <shaba@altlinux.ru> 1.1.6-alt1
- 1.1.6
- drop create group camera in pre
- drop hal support
- drop libmtp-1.1.3-alt-udev-rules.patch

* Mon Nov 19 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Sun May 20 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 1.1.3-alt1
- 1.1.3
- replaced libusb-compat-devel to libusb-devel in BuildRequires

* Sat Jan 21 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Tue Oct 12 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Mon Mar 22 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0.2-alt1
- 1.0.2
- disabled unneeded patch
- disabled packaging html docs

* Sat Sep 12 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sun Aug 16 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sat Apr 18 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.7-alt1
- 0.3.7
- updated build requires

* Wed Dec 24 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.4-alt2
- binary package renamed to %%name%%soversion

* Thu Dec 18 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.4-alt1
- 0.3.4
- removed obsolete patch3

* Sat Dec 13 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.2.6.1-alt3
- removed obsolete post{,un}_ldconfig calls

* Sat May 24 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.2.6.1-alt2
- moved HAL support into %name, %name-hal has removed

* Thu May 22 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.2.6.1-alt1
- 0.2.6.1
- corrected wrong location of hal device information file
- disabled build devel-static package by default
- supported hal >= 0.5.11

* Mon Mar 10 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.2.6-alt1
- updated to 0.2.6
- created %name-hal binary package

* Wed Jun 06 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 0.1.5-alt0.2
- usage examples moved into %name-examples package
- udev rules adapted for udev >= 098,
  for access to device user must be added into group "camera"

* Wed Apr 04 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 0.1.5-alt0.1
- initial build
