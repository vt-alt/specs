Name: thinksaber
Version: 0.4
Release: alt3

Summary: Turn your HDAPS-enabled Thinkpad into Jedi's Lightsabre
License: GPL-2.0
Group: Toys

Url: http://elfsternberg.com/projects/thinksaber/
Source0: %url/%name-%version.tar.gz
Source1: thinksaber.sh
Source2: thinksaber.sysconfig
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%define tsdir %_datadir/%name

%description
Thinksaber is obviously inspired by the program MacSaber, and I'm
grateful to the MacSaber people for assembling the Star Wars sound
effects collection needed to make it so successful.

Thinksaber uses a motion-detection algorithm derived from the one
written by Tatsuhiko Miyagawa (miyagawa at gmail.com) for his own
thinkpad-saber program, which ran only under Perl for Windows.
Obviously, I think mine's better.

%prep
%setup

%install
mkdir -p %buildroot%tsdir
cp -a *.wav %buildroot%tsdir
install -pDm755 %name.py %buildroot%_bindir/%name.py
install -pDm755 %SOURCE1 %buildroot%_bindir/%name
install -pDm644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

# TODO:
# - something regarding the udev rule needed (js input)

# !TODO:
# - _don't_ add desktop file, Jedi will know better. :)

%files
%_bindir/*
%tsdir
%_sysconfdir/sysconfig/%name
%doc AUTHORS ChangeLog README

%changelog
* Wed May 12 2021 Grigory Ustinov <grenka@altlinux.org> 0.4-alt3
- Fixed FTBFS.

* Fri Jan 10 2020 Grigory Ustinov <grenka@altlinux.org> 0.4-alt2
- Transferred to python3.
- Fixed license.

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.1
- Rebuilt with python 2.6

* Fri Apr 03 2009 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- use the... er, equipped ALT Linux with this one
- lowered default acceleration thresholds:
  prefer wisdom to brute force
- introduced universe-wide and per-jedi configs
- added README.ALT until udev rules get settled
