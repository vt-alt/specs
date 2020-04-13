Name:		cqrlog
Version:	2.4.0
Release:	alt1
Summary:	An amateur radio contact logging program

Group:		Communications
License:	GPLv2
URL:		http://www.cqrlog.com/
Source0:	%name-%version.tar
# VCS:		https://github.com/ok2cqr/cqrlog

Patch0:		cqrlog-install.patch

ExclusiveArch:  %ix86 x86_64

BuildRequires:	fpc >= 2.6.4
BuildRequires:	lazarus
BuildRequires:	hamlib-devel
BuildRequires:	libssl-devel
BuildRequires:	desktop-file-utils

Requires:	mariadb-server
Requires:	trustedqsl
Requires:       hamlib

%description
CQRLOG is an advanced ham radio logger based on MySQL database. Provides
radio control based on hamlib libraries (currently support of 140+ radio
types and models), DX cluster connection, QRZ callbook (web version), a
grayliner, internal QSL manager database support and a most accurate
country resolution algorithm based on country tables developed by OK1RR.
CQRLOG is intended for daily general logging of HF, CW & SSB contacts
and strongly focused on easy operation and maintenance.

%prep
%setup -q
%patch0 -p1

chmod -x src/*.pas \
         voice_keyer/voice_keyer.sh

%build
%make_build

%install
%makeinstall_std

find %buildroot%_datadir/%name -name \*.txt | xargs subst 's/\r//'
subst 's/\r//' %buildroot%_datadir/%name/ctyfiles/CountryDel.tab
subst 's/\r//' %buildroot%_datadir/%name/ctyfiles/MASTER.SCP

iconv -f iso8859-1 -t utf-8 %buildroot%_datadir/%name/ctyfiles/eqsl.txt > eqsl.txt.conv && /bin/mv -f eqsl.txt.conv %buildroot%_datadir/%name/ctyfiles/eqsl.txt

rm -rf %buildroot%_datadir/%name/cqrlog-apparmor-fix
# Move icons to appropriate places
for i in 32 48 64 128 256; do
	install -Dm 0644 %buildroot%_iconsdir/%name/${i}x${i}/%name.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/%name.png
done

rm -rf %buildroot%_iconsdir/%{name}*

%files
%doc README.md AUTHORS CHANGELOG
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/appdata/%name.appdata.xml
%_pixmapsdir/%name/
%_man1dir/%name.1.*
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Wed Jan 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.
- Package cqrlog.appdata.xml.

* Sun Aug 06 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version

* Mon Mar 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- New version

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- New version

* Fri Sep 02 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version

* Tue May 10 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version

* Wed Feb 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.1-alt1
- New version

* Thu Jan 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt4
- Fix build with fpc-3.0.0

* Thu Nov 19 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt3
- Add trustedqsl in requirements

* Mon Nov 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt2
- Add hamlib to requirements

* Thu Nov 12 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- Initial build in Sisyphus (thanks Fedora for spec)

