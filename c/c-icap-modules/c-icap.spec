Name: 	 c-icap-modules
Version: 0.5.4
Release: alt1
Epoch:	 1
Packager: Andrey Cherepanov <cas@altlinux.org>

Summary: ICAP server modules
License: %gpl2only
Group: 	 System/Servers
Url: 	 http://c-icap.sourceforge.net/

Provides:  c-icap-clamav = %epoch:%version-%release
Obsoletes: c-icap-clamav < %epoch:%version-%release

Source0: c_icap_modules-%version.tar.gz

BuildRequires: rpm-build-licenses

BuildRequires: c-icap-devel libclamav-devel libdb4-devel zlib-devel bzlib-devel

%description
Modules for Internet Content Adaptation Protocol (ICAP) server.

%prep
%setup -n c_icap_modules-%version

%build
%autoreconf
%undefine _configure_gettext
%configure
%make_build

%install
mkdir -p %buildroot%_sysconfdir
%makeinstall_std

rm -f %buildroot%_libdir/c_icap/*.la

%files
%doc AUTHORS README NEWS SPONSORS
%_sysconfdir/*
%dir %_libdir/c_icap
%_libdir/c_icap/*.so
%dir %_datadir/c_icap
%_datadir/c_icap/templates
%_man8dir/c-icap*.8*
%_bindir/c-icap-mods-sguardDB

%changelog
* Mon Feb 17 2020 Sergey Y. Afonin <asy@altlinux.org> 1:0.5.4-alt1
- New version (with ClamAV 0.102 support)

* Fri Jan 18 2019 Sergey Y. Afonin <asy@altlinux.ru> 1:0.5.3-alt1
- New version (with ClamAV 0.101 support)

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.5.2-alt1
- New version

* Sun Oct 08 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.4.5-alt1
- New version

* Sat Mar 19 2016 Sergey Y. Afonin <asy@altlinux.ru> 1:0.4.2-alt3
- Updated BuildRequires (gear-buildreq output used)
- Packaged c-icap-mods-sguardDB binary

* Thu Mar 10 2016 Sergey Y. Afonin <asy@altlinux.ru> 1:0.4.2-alt2
- Removed gcc-c++ from BuildRequires

* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 1:0.4.2-alt1
- New version
