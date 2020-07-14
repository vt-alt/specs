Name:           pcsc-tools
Version:        1.5.7
Release:        alt2
Summary:        Tools to be used with smart cards and PC/SC

Group:          System/Configuration/Hardware
License:        GPLv2+
URL:            http://ludovic.rousseau.free.fr/softwares/pcsc-tools/
Source0:        http://ludovic.rousseau.free.fr/softwares/pcsc-tools/%{name}-%{version}.tar.gz
Source1:	%name.watch

BuildRequires:  desktop-file-utils
BuildRequires:  libpcsclite-devel >= 1.2.9
BuildRequires:  perl-pcsc
BuildRequires:  perl-Gtk3
Requires:       pcsc-lite

%add_findreq_skiplist %_bindir/gscriptor

%description
The pcsc-tools package contains some useful tools for a PC/SC user:
pcsc_scan regularly scans connected PC/SC smart card readers and
prints detected events, ATR_analysis analyzes smart card ATRs (Anwser
To Reset), scriptor sends commands to a smart card.

%package gui
Summary:	GUI tool to be used with smart cards and PC/SC
Group:          System/Configuration/Hardware
Requires:	pcsc-tools = %version-%release
Requires:       perl-Gtk3

%description gui
The pcsc-tools-gui package contains gscriptor sends commands to a smart
card from a GTK user interface.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
desktop-file-install --mode=644 \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications gscriptor.desktop
# TODO: icon

%files
%doc Changelog README
%_bindir/*
%_datadir/pcsc/
%doc %_man1dir/*
%exclude %_bindir/gscriptor
%exclude %_man1dir/gscriptor.*

%files gui
%_bindir/gscriptor
%_desktopdir/gscriptor.desktop
%doc %_man1dir/gscriptor.*

%changelog
* Fri Jul 10 2020 Andrey Cherepanov <cas@altlinux.org> 1.5.7-alt2
- Remove strict requirements of python2-base.

* Thu Jul 09 2020 Andrey Cherepanov <cas@altlinux.org> 1.5.7-alt1
- New version.

* Tue Mar 10 2020 Andrey Cherepanov <cas@altlinux.org> 1.5.6-alt1
- New version.

* Mon Jan 06 2020 Andrey Cherepanov <cas@altlinux.org> 1.5.5-alt1
- New version.

* Fri Dec 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.4-alt1
- New version.

* Tue Apr 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.3-alt1
- New version.

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.2-alt1
- New version.

* Mon Jul 04 2016 Andrey Cherepanov <cas@altlinux.org> 1.4.27-alt1
- New version

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 1.4.26-alt1
- New version
- Add watch file

* Wed Sep 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.4.24-alt1
- New version

* Mon Feb 02 2015 Andrey Cherepanov <cas@altlinux.org> 1.4.23-alt1
- New version

* Wed Feb 12 2014 Andrey Cherepanov <cas@altlinux.org> 1.4.22-alt1
- Initial build for ALT Linux (thanks Fedora for spec)

