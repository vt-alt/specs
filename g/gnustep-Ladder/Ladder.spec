%set_verify_elf_method unresolved=strict

Name: gnustep-Ladder
Version: 1.0
Release: alt6
Summary: Ladder is a graphically pleasing implementation of Go
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/gap/ladder/index.html
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnugo
Requires: gnustep-back

%description
Ladder is a graphically pleasing implementation of Go. It uses gnugo as
it's engine and you must have a recent version of gnugo installed in
order to run it.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ANNOUNCE README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 1.0-alt6
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 1.0-alt5
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.0-alt4.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Built with clang

* Mon Feb 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

