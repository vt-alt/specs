Name: tutka
Version: 1.1.3
Release: alt3

Summary: tracker style MIDI sequencer
License: %gpl2plus
Group: Sound
Url: http://www.nongnu.org/tutka/

Source: %name-%version.tar.bz2

Patch1: tutka-1.1.3-disable-werror.patch
Patch2: tutka-1.1.3-fix-build-with-Qt5-5.13.patch

BuildPreReq: rpm-build-licenses
BuildRequires: gcc-c++ libalsa-devel libgtk+2-devel libgnomeui-devel libxml2-devel libglade-devel
BuildRequires: qt5-base-devel qt5-tools-devel

%description
Tutka is a free (as in freedom) tracker style MIDI sequencer for GNU/Linux (and
other systems; only GNU/Linux is supported at this time though). It is similar
to programs like SoundTracker, ProTracker and FastTracker except that it does
not support samples and is meant for MIDI use only. Tutka is licensed under the
GNU GPL.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
qmake-qt5
# Wno-error=type-limits for aarch64, due it use unsigned char
%ifnarch aarch64
%make_build
%else
%make_build CXXFLAGS="$CXXFLAGS -Wno-error=type-limits"
%endif

%install
%makeinstall_std INSTALL_ROOT=%buildroot
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README TODO
%_bindir/*
%_desktopdir/*
%_liconsdir/*
%_iconsdir/hicolor/512x512/apps/%name.png

%changelog
* Tue Sep 08 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt3
- Fixed segfault. [thx to zerg@] (Closes: #38894).

* Thu Aug 27 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt2
- Fixed FTBFS.

* Thu Aug 08 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt1
- Build new version.

* Mon Jun 18 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt1
- Build new version.

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 0.12.5-alt1
- New version 0.12.5
- Remove deprecated function g_thread*

* Sun Sep 13 2009 Timur Batyrshin <erthad@altlinux.org> 0.12.4-alt1
- initial build for sisyphus

