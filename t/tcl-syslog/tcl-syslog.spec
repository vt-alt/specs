Name: tcl-syslog
Version: 2.0
Release: alt5.1.qa2

Summary: Syslog tcl lib
Group: Development/Tcl
License: BSD
Url: http://www.45.free.net/tcl/tclsyslog.html

Packager: Denis Smirnov <mithraen@altlinux.ru>

Conflicts: scotty

Source: %name-%version.tar.gz

Patch1: %name.Makefile.patch

# Automatically added by buildreq on Sun Sep 25 2005
BuildRequires: tcl-devel >= 8.6.7-alt2

%description
Writing to syslog from tcl scripts

%prep
%setup -q -c
%patch1 -p1

%build
%make

%install
export PREFIX=%buildroot/usr
sed -i '/PREFIX=/d' Makefile
%makeinstall
rm -rf %buildroot%_datadir/tcl/syslog/
mkdir -p %buildroot%_libdir/tcl/syslog/
cat <<EOF > %buildroot%_libdir/tcl/syslog/pkgIndex.tcl
package ifneeded Syslog 2.0 [list load [file join \$dir .. libsyslog.so.2.0] Syslog]
EOF

mkdir -p %buildroot%_libdir/tcl/
%if "%_libdir" != "/usr/lib"
mv %buildroot/usr/lib/tcl/*.so.* %buildroot%_libdir/tcl/
%endif

%files
%_mandir/mann/*
%_libdir/tcl/*.so.*
%_libdir/tcl/syslog

%changelog
* Mon Jul 15 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0-alt5.1.qa2
- Fixed build on architectuires where %%_libdir != /usr/lib .

* Tue Feb 27 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.0-alt5.1.qa1.1
- NMU:
  + fixed FTBFS: built against Tcl 8.6
  + fixed runtime: made extension loadable via package(n) facility
  + adapted for new Tcl/Tk extenstion packaging policy

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0-alt5.1.qa1
- NMU: rebuilt for debuginfo.

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt5.1
- rebuild (with the help of girar-nmu utility)

* Sun Dec 14 2008 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt5
- add conflicts to scotty

* Wed Dec 03 2008 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt4
- fixed build on x86_64

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt3
- cleanup spec

* Sun Dec 30 2007 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt2
- Build with tcl 8.5

* Sun Sep 25 2005 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt1
- first build for Sisyphus

