%define _name flare

Name: %_name-game
Version: 1.11
Release: alt1

Summary: Fantasy action RPG using the FLARE engine
# All of Flare's art and data files are released under CC-BY-SA 3.0.
# Later versions are permitted.
# The Liberation Sans fonts version 2 are released under the SIL Open
# Font License, Version 1.1.
License: %ccbysa30+, SIL Open Font License 1.1
Group: Games/Adventure

URL: http://flarerpg.org/
# https://github.com/flareteam/flare-game.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses rpm-macros-cmake
BuildRequires: gcc-c++ cmake

Requires: %_name-engine >= %version

Obsoletes: flare < %version-%release
Provides: flare = %version-%release
Obsoletes: flare-data < %version-%release
Provides: flare-data = %version-%release

%define _unpackaged_files_terminate_build 1

%description
The Empyrean Campaign is a single-player 2D action RPG with fast-paced action
and a dark fantasy style.
It is built on the FLARE engine (Free/Libre Action Roleplaying Engine).

%prep
%setup
#patch -p1

%build
%cmake -DBINDIR=bin -DDATADIR=share/flare
cd BUILD
%make_build
cd -

%install
cd BUILD
%makeinstall_std
cd -
%find_lang %_name

%files -f %_name.lang
%_datadir/%_name/*
%_datadir/metainfo/*.xml

%changelog
* Thu Aug 08 2019 Mikhail Efremov <sem@altlinux.org> 1.11-alt1
- Updated to 1.11.

* Tue May 21 2019 Mikhail Efremov <sem@altlinux.org> 1.10-alt1
- Fix license.
- Updated to 1.10.

* Fri Dec 14 2018 Mikhail Efremov <sem@altlinux.org> 1.09.01-alt1
- Updated to 1.09.01.

* Mon Dec 10 2018 Mikhail Efremov <sem@altlinux.org> 1.09-alt1
- Updated to 1.09.

* Tue Sep 18 2018 Mikhail Efremov <sem@altlinux.org> 1.08-alt1
- Updated to 1.08.

* Wed Sep 05 2018 Mikhail Efremov <sem@altlinux.org> 1.07-alt1
- Updated to 1.07.

* Tue May 29 2018 Mikhail Efremov <sem@altlinux.org> 1.06-alt1
- Updated to 1.06.

* Thu May 03 2018 Mikhail Efremov <sem@altlinux.org> 1.05-alt1
- Updated to 1.05.

* Wed Apr 18 2018 Mikhail Efremov <sem@altlinux.org> 1.03-alt1
- Updated to 1.03.

* Wed Mar 14 2018 Mikhail Efremov <sem@altlinux.org> 1.0-alt1
- Updated description.
- Updated URL.
- Updated to 1.0.

* Sat Aug 30 2014 Mikhail Efremov <sem@altlinux.org> 0.19-alt1
- Updated to 0.19.

* Fri Jan 06 2012 Mikhail Efremov <sem@altlinux.org> 0.15-alt1
- Initial build.

