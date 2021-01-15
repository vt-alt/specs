%define soversion 11

Name: libmirage
Version: 3.2.4
Release: alt1

Summary: A CD-ROM image access library
License: GPLv2+
Group: System/Libraries

URL: http://cdemu.sourceforge.net
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2

BuildRequires: bzlib-devel
BuildRequires: cmake
BuildRequires: glib-networking
BuildRequires: glibc-kernheaders-generic
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: libGConf
BuildRequires: liblzma-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: time
BuildRequires: zlib-devel

%description
This is libMirage library, a CD-ROM image access library, and part of the 
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

The aim of libMirage is to provide uniform access to the data stored in 
different image formats, by creating a representation of disc stored in image 
file, which is based on GObjects.

%package -n %name%soversion
Summary: A CD-ROM image access library
Group: System/Libraries
Provides: %name = %version
Obsoletes: %name
Conflicts: %{name}10

%description -n %name%soversion
This is libMirage library, a CD-ROM image access library, and part of the 
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

The aim of libMirage is to provide uniform access to the data stored in 
different image formats, by creating a representation of disc stored in image 
file, which is based on GObjects.

%package devel
Summary: A CD-ROM image access library
Group: Development/C
Requires: glib2-devel

%description devel
This is libMirage library, a CD-ROM image access library, and part of the 
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux. It is
written in C and based on GLib.

This package contains files needed to develop with libMirage.

%prep
%setup -q

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
         -DCMAKE_INSTALL_PREFIX:PATH="%prefix" \
         -DCMAKE_C_FLAGS:STRING="%optflags" \
         -DCMAKE_BUILD_TYPE:STRING="Release"
         
popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%find_lang %name

%files -n %name%soversion -f %name.lang
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_libdir/libmirage.so.*
%dir %_libdir/libmirage-3.2
%_libdir/libmirage-3.2/*.so
%_datadir/mime/packages/*.xml

%files devel
%_libdir/libmirage.so
%_libdir/girepository-1.0/*
%_pkgconfigdir/%name.pc
%dir %_includedir/%name-3.2
%dir %_includedir/%name-3.2/mirage
%_includedir/%name-3.2/mirage/*.h
%_datadir/gir-1.0/*
%dir %_datadir/gtk-doc
%dir %_datadir/gtk-doc/html
%doc %_datadir/gtk-doc/html/%name

%changelog
* Mon Nov 02 2020 Nazarov Denis <nenderus@altlinux.org> 3.2.4-alt1
- Version 3.2.4 (ALT #39133)

* Mon Jun 17 2019 Nazarov Denis <nenderus@altlinux.org> 3.2.2-alt1
- Version 3.2.2

* Sat Jan 26 2019 Nazarov Denis <nenderus@altlinux.org> 3.2.0-alt2
- Remove %ubt macro

* Fri Jul 27 2018 Nazarov Denis <nenderus@altlinux.org> 3.2.0-alt1%ubt
- Version 3.2.0

* Thu Aug 03 2017 Nazarov Denis <nenderus@altlinux.org> 3.1.0-alt2%ubt
- Add conflicts on libmirage10 (ALT #33724)

* Wed Aug 02 2017 Nazarov Denis <nenderus@altlinux.org> 3.1.0-alt1%ubt
- Version 3.1.0

* Sat Oct 15 2016 Nazarov Denis <nenderus@altlinux.org> 3.0.5-alt2
- Add provides/obsoletes on libmirage (ALT #32614)

* Thu Oct 13 2016 Nazarov Denis <nenderus@altlinux.org> 3.0.5-alt1
- Version 3.0.5

* Mon Jan 11 2016 Nazarov Denis <nenderus@altlinux.org> 3.0.4-alt1
- Version 3.0.4

* Sun Nov 30 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Fri Oct 10 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.2-alt0.M70T.1
- Build for branch t7

* Tue Oct 07 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.2-alt1
- Version 3.0.2

* Thu Aug 07 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt0.M70T.1
- Build for branch t7

* Wed Aug 06 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt1
- Version 3.0.1

* Sun Jul 20 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt0.M70P.1
- Build for branch p7

* Fri Jul 04 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt0.M70T.1
- Build for branch t7

* Thu Jul 03 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt1
- Version 3.0.0

* Mon Feb 10 2014 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt0.M70P.1
- Build for branch p7

* Sun Feb 09 2014 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt0.M70T.1
- Build for branch t7

* Sat Sep 21 2013 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Sun Jun 09 2013 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Tue Dec 25 2012 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt2
- Fix post-install unowned files

* Tue Dec 25 2012 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Tue Jan 24 2012 Nazarov Denis <nenderus@altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Tue Sep 20 2011 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt2
- Fix buildrequires

* Sun Sep 18 2011 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Jan 25 2011 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt2
- Fix shared-mime-info

* Thu Nov 11 2010 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmirage
  * postun_ldconfig for libmirage
  * shared-mime-info for libmirage
  * postclean-05-filetriggers for spec file

* Fri Nov 14 2008 Nick S. Grechukh <gns@altlinux.org> 1.1.0-alt1
- first build for ALT Linux

* Sat Jun 28 2008 Rok Mandeljc <rok.mandeljc@email.si> - 1.1.0-1
- Updated to 1.1.0

* Thu Dec 20 2007 Rok Mandeljc <rok.mandeljc@email.si> - 1.0.0-1
- Initial RPM release.
