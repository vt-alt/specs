Name: pulseview
Version: 0.4.2
Release: alt2

Summary: sigrok -- signal analysis software suite
License: GPLv3
Group: Development/Other
Url: https://sigrok.org/

Requires: libqt5-svg

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake
BuildRequires: glib2-devel libglibmm-devel
BuildRequires: libsigrokcxx-devel >= 0.5.1 libsigrokdecode-devel >= 0.5.2
BuildRequires: boost-devel boost-filesystem-devel boost-multiprecision-devel
BuildRequires: qt5-base-devel qt5-svg-devel qt5-tools-devel

%description
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

PulseView is a Qt-based LA/scope/MSO GUI for sigrok.
Visit http://sigrok.org/wiki/PulseView for more.

%prep
%setup

%build
cmake . -DCMAKE_INSTALL_PREFIX=%prefix
%make_build

%install
%makeinstall_std

%files
%_bindir/pulseview
%_desktopdir/org.sigrok.PulseView.desktop
%_iconsdir/*/*/apps/pulseview.*
%_datadir/metainfo/*.appdata.xml
%_man1dir/pulseview.1*

%changelog
* Fri Aug 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt2
- fixed build with recent Qt5

* Wed Jul 15 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt1
- 0.4.2 released

* Tue Oct 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt1.1
- NMU: rebuilt with boost-1.67.0

* Mon Jun 19 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- initial
