#define status beta
Name: rosegarden
Version: 20.06
Release: alt1

Summary: MIDI and audio sequencer and musical notation editor
License: GPL
Group: Sound

Url: http://www.rosegardenmusic.com
Source: %name-%version.tar

Requires: libsndfile-utils
Obsoletes: rosegarden-alsa rosegarden-arts rosegarden-common librosegarden-alsa librosegarden-arts

# Automatically added by buildreq on Mon Jul 31 2017
# optimized out: cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 ladspa_sdk libEGL-devel libGL-devel libICE-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libalsa-devel libqt5-core libqt5-gui libqt5-network libqt5-printsupport libqt5-test libqt5-widgets libqt5-xml libstdc++-devel pkg-config python-base python-modules qt5-base-common qt5-base-devel qt5-tools raptor2-devel shared-mime-info xorg-kbproto-devel xorg-xproto-devel
BuildRequires: cmake dssi-devel libSM-devel libXcursor-devel libXinerama-devel libXrandr-devel libXtst-devel libXv-devel libfftw3-devel libjack-devel liblirc-devel liblo-devel liblrdf-devel libsamplerate-devel libsndfile-devel qt5-tools-devel zlib-devel

%description
Rosegarden is a professional audio and MIDI sequencer, score editor, and
general-purpose music composition and editing environement.

Rosegarden is an easy-to-learn, attractive application that runs on
Linux, ideal for composers, musicians, music students, and small studio
or home recording environments.

%prep
%setup
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.20
sed -i "1 i\set (CMAKE_CXX_STANDARD 11)" CMakeLists.txt
# strip UTF-8 BOM for lcc < 1.24
find -type f -print0 -name '*.cpp' -o -name '*.h' |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
%find_lang --with-kde %name

%check
# doesn't work yet
#make test -C BUILD

%files -f %name.lang
%doc AUTHORS CONTRIBUTING README
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/*/*
%_datadir/metainfo/%name.*
%_datadir/mime/packages/*

%changelog
* Mon Sep 07 2020 Vitaly Lipatov <lav@altlinux.ru> 20.06-alt1
- new version 20.06

* Sun Mar 08 2020 Vitaly Lipatov <lav@altlinux.ru> 19.12-alt1
- NMU: new version 19.12 (ALT bug 38088)

* Sat Oct 05 2019 Michael Shigorin <mike@altlinux.org> 17.12-alt2
- E2K: explicit -std=c++11; strip UTF-8 BOM for lcc < 1.24

* Fri Feb 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.12-alt1
- Updated to upstream version 17.12.

* Mon Jul 31 2017 Ildar Mulyukov <ildar@altlinux.ru> 17.04-alt1
- new version 17.04

* Thu Jun 20 2013 Andrey Cherepanov <cas@altlinux.org> 13.02-alt1.1
- Rebuild with new version liblo

* Mon Feb 25 2013 Alex Karpov <karpov@altlinux.ru> 13.02-alt1
- new version

* Wed Jan 09 2013 Alex Karpov <karpov@altlinux.ru> 12.12.25-alt1
- new version

* Thu May 17 2012 Alex Karpov <karpov@altlinux.ru> 12.04-alt1
- new version

* Tue Dec 13 2011 Alex Karpov <karpov@altlinux.ru> 11.11.42-alt1
- new version

* Thu Nov 10 2011 Alex Karpov <karpov@altlinux.ru> 11.11.1-alt1
- new version

* Thu Aug 25 2011 Alex Karpov <karpov@altlinux.ru> 11.06-alt1
- new version

* Mon Feb 07 2011 Alex Karpov <karpov@altlinux.ru> 11.02-alt1
- new version

* Fri Nov 05 2010 Alex Karpov <karpov@altlinux.ru> 10.10-alt1
- new version

* Wed May 05 2010 Alex Karpov <karpov@altlinux.ru> 10.04.2-alt1
- quick bugfix release

* Mon Apr 26 2010 Alex Karpov <karpov@altlinux.ru> 10.04.1-alt1
- new version

* Wed Mar 10 2010 Alex Karpov <karpov@altlinux.ru> 10.02.1-alt1.1
- fixed configure parameters and filelist

* Thu Mar 04 2010 Alex Karpov <karpov@altlinux.ru> 10.02.1-alt1
- new version
    + minor spec cleanup
    + removed obsoleted patches

* Wed Feb 04 2009 Alex Karpov <karpov@altlinux.ru> 1.7.3-alt1
- 1.7.3
    + removed obsoleted stuff

* Wed Sep 24 2008 Alex Karpov <karpov@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Mon Aug 18 2008 Alex Karpov <karpov@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Sun May 11 2008 Alex Karpov <karpov@altlinux.ru> 1.7.0-alt1
- 1.7.0 release

* Thu Mar 27 2008 Alex Karpov <karpov@altlinux.ru> 1.6.1-alt1.1
- added desktopdb and mimedb macros with new build requirements

* Fri Dec 21 2007 Alex Karpov <karpov@altlinux.ru> 1.6.1-alt1
- 1.6.1 bugfix release

* Fri Dec 07 2007 Alex Karpov <karpov@altlinux.ru> 1.6.0-alt1
- 1.6.0 release

* Fri Nov 30 2007 Alex Karpov <karpov@altlinux.ru> 1.6.0-alt0.pre2
- 1.6.0 prerelease 2

* Fri Oct 19 2007 Alex Karpov <karpov@altlinux.ru> 1.5.1-alt1.1
- rebuild with filesystem-2.3.3-alt1

* Tue Apr 10 2007 Alex Karpov <karpov@altlinux.ru> 1.5.1-alt1
- 1.5.1 upstream bugfix release

* Sun Feb 11 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt4
- updated patch

* Fri Feb 09 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt3
- added libsndfile-utils to requirements

* Wed Feb 07 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt2
- rebuild

* Tue Feb 06 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt1
- 1.5.0 release

* Wed Jan 10 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt0.2svn
- rebuild

* Tue Jan 09 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt0.1svn
- added patch for working --as-needed flag

* Sun Jan 07 2007 Alex Karpov <karpov@altlinux.ru> 1.5.0-alt0.svn
- new version from SVN


* Wed Oct 04 2006 Alex Karpov <karpov@altlinux.ru> 1.4.0-alt0.1
- new version

* Mon Sep 25 2006 Michael Shigorin <mike@altlinux.org> 1.4.0-alt0
- add_changelog
- test build in hasher on behalf of Alex Karpov <karpov@>
  + spec based on old rosegarden-1.0-alt1 spec by Yuri N. Sedunov <aris@>
    and klear-0.5.4-alt2 spec by Igor Zubkov <icesik@>

