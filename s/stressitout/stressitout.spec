%define		git 20150323

Name:		stressitout
Version:	0.2
Release:	alt1.%git.1
Summary:	StressItOut is a hardware stressing and testing program
License:	GPLv2+
Group:		Monitoring
Url:		http://jancoding.wordpress.com/stressitout/
Packager: 	Motsyo Gennadi <drool@altlinux.ru>

Source0:	%name-dev-master.tar.gz

BuildRequires: /usr/bin/convert libGLU-devel libsensors3-devel qt5-tools-devel

%description
StressItOut is a free (as in 'freedom') hardware stressing and testing program for GNU/Linux.

Its main purpose is to strain the computer to ensure the hardware is in good state. There are
several test modules: CPU load, memory test, 2D OpenGL painting, 3D OpenGL rendering, hard
drives, optical drives, serial ports transmission, and parallel ports. Support for lm-sensors
is in the works.

This software, when ready for release, will mainly be aimed at the QA departments of hardware-
manufacturing companies, who need to ensure their newly produced machines perform correctly
under heavy workloads, and that all their components work as expected.

%prep
%setup -n %name-dev

%build
lrelease-qt5 ./translations/*.ts
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" StressItOut.pro
%make_build

%install
install -Dp -m 0755 %name %buildroot%_bindir/%name
install -Dp -m 0644 %name.desktop %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 icon/64x64/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 icon/64x64/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 icon/64x64/%name.png %buildroot%_miconsdir/%name.png

%files
%doc README CHANGELOG
%_bindir/*
%_desktopdir/*.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Sun Apr 12 2020 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt1.20150323.1
- fix BuildRequires

* Sun Apr 12 2020 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt1.20150323
- 0.2-dev release
- build with Qt5

* Tue Jun 26 2012 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1.20120625
- 0.1 release

* Thu Jun 14 2012 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1.20120527.2
- added Russian and Ukrainian translations

* Mon Jun 11 2012 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1.20120527.1
- fix desktop-file

* Mon Jun 11 2012 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1.20120527
- initial build for ALT Linux
