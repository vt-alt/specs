%define ver_major 0.21
%define ver_minor 17

Name: gwc
Version: %ver_major.%ver_minor
Release: alt3

Summary: Gnome Wave Cleaner
License: GPLv2+
Group: Sound

Url: http://gwc.sourceforge.net/
Source: http://download.sourceforge.net/gwc/gwc-%ver_major-%ver_minor.tgz
Source1: gwc-48x48.xpm
Source2: gwc-32x32.xpm
Source3: gwc-16x16.xpm
Source4: gwc.desktop
Patch0: gwc-0.21.07-alt-makefile.patch
Patch1: gwc-0.21.19-debian-clang.patch
Patch2: gwc-0.21.17-make-gcc10-happy.patch

# Automatically added by buildreq on Sun Jun 19 2011
BuildRequires: libalsa-devel libfftw3-devel libgnomeui-devel libsndfile-devel

%description
Digital audio restoration of CD quality audio wavefiles. Dehiss, declick and
decrackle in a GUI environment.

%prep
%setup -n gwc-%ver_major-%ver_minor
%patch0 -p1
%patch1 -p1
%patch2 -p2
find -iname makefile.in | xargs sed -i 's/-O6/-O%_optlevel/g' --

%build
%configure --enable-alsa
%make_build

%install
%makeinstall_std

# desktop file
install -pD -m644 %_sourcedir/gwc.desktop %buildroot%_desktopdir/gwc.desktop

# icons
install -pD -m644 %SOURCE1 %buildroot%_liconsdir/gwc.xpm
install -pD -m644 %SOURCE2 %buildroot%_niconsdir/gwc.xpm
install -pD -m644 %SOURCE3 %buildroot%_miconsdir/gwc.xpm

%find_lang --with-gnome gnome_wave_cleaner

%files -f gnome_wave_cleaner.lang
%_bindir/*
%_desktopdir/*
%_niconsdir/*
%_miconsdir/*
%_liconsdir/*
%_pixmapsdir/*

%changelog
* Thu Apr 15 2021 Grigory Ustinov <grenka@altlinux.org> 0.21.17-alt3
- Fixed FTBFS.

* Fri Apr 17 2020 Michael Shigorin <mike@altlinux.org> 0.21.17-alt2
- E2K:
  + apply debian's clang patch (debian#750369)
  + fix superfluous optimization level (there's no -O6)

* Sun Apr 15 2012 Victor Forsiuk <force@altlinux.org> 0.21.17-alt1
- %ver_major.%ver_minor

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 0.21.16-alt1
- 0.21-16.

* Fri Oct 01 2010 Victor Forsiuk <force@altlinux.org> 0.21.11-alt1
- 0.21-11.

* Tue Mar 24 2009 Victor Forsyuk <force@altlinux.org> 0.21.10-alt1
- 0.21-10.

* Sat Jan 10 2009 Victor Forsyuk <force@altlinux.org> 0.21.08-alt3
- Remove obsolete install time scripts.

* Wed Jul 04 2007 Victor Forsyuk <force@altlinux.org> 0.21.08-alt2
- Update build requirements (libSM-devel now have to be listed explicitly).

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 0.21.08-alt1
- 0.21-08.

* Fri Jan 12 2007 Victor Forsyuk <force@altlinux.org> 0.21.07-alt1
- Initial build.
