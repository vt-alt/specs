%define _localstatedir %_var
%define _enable_debug_packages %nil
%define debug_package %nil
%global _davsvn 2891

%ifarch %ix86
%global davarch x86
%endif
%ifarch x86_64
%global davarch x86_64
%endif

Name:     davmail
Version:  5.3.1
Release:  alt1
Summary:  POP/IMAP/SMTP/Caldav/Carddav/LDAP gateway for Microsoft Exchange
URL:      http://davmail.sourceforge.net/
Group:    Networking/Other
License:  GPLv2+

BuildArch: noarch

Source0:  %name-%version.tar
Source1:  %name.desktop

Requires: java
Requires: javapackages-tools
Requires: swig

BuildRequires: java-devel-default /proc
BuildRequires: ant
BuildRequires: desktop-file-utils 
BuildRequires: xml-commons-apis

%description
DavMail is a POP/IMAP/SMTP/Caldav/Carddav/LDAP Exchange gateway allowing
users to use any mail/calendar client with an Exchange server, even from
the internet or behind a firewall through Outlook Web Access. DavMail
now includes an LDAP gateway to Exchange global address book and user
personal contacts to allow recipient address completion in mail compose
window and full calendar support with attendees free/busy display.

%prep
%setup

%build
sed -i '/class-path/I d' build.xml
ANT_OPTS="-Dfile.encoding=UTF-8" ant

%install
install -p -Dm755 src/bin/%name %buildroot%_bindir/%name

install -p -Dm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -p -Dm644 src/java/tray2.png %buildroot%_datadir/icons/hicolor/16x16/apps/%name.png
install -p -Dm644 src/java/tray32.png %buildroot%_datadir/icons/hicolor/32x32/apps/%name.png
install -p -Dm644 src/java/tray48.png %buildroot%_datadir/icons/hicolor/48x48/apps/%name.png

rm -f dist/lib/*win32*.jar
mkdir -p %buildroot%_datadir/%name/lib/
install -p -m664 dist/lib/*.jar %buildroot%_datadir/%name/lib/
rm -f dist/lib/*x86*.jar
install -p -m664 dist/lib/* %buildroot%_datadir/%name/lib/
install -p -m664 dist/*.jar %buildroot%_datadir/%name/
install -p -Dm644 src/etc/%name.properties %buildroot%_sysconfdir/%name/%name.properties

sed -i 's/\r//' releaseguide.txt

%files
%doc releaseguide.txt
%_sysconfdir/%name/
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Mon Sep 16 2019 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version.

* Wed Aug 07 2019 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version.

* Mon Apr 08 2019 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Mon Jan 28 2019 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version.

* Thu Dec 13 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Thu Oct 18 2018 Andrey Cherepanov <cas@altlinux.org> 4.9.0-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.5-alt1
- New version.

* Mon Apr 09 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.4-alt1
- New version.
- Spec cleanup.

* Wed Apr 04 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.3-alt2
- Increase release number for correct update from Autoimports.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.3-alt1
- Build from Autoimports to Sisyphus (ALT #34759).

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 4.8.3-alt1_1
- new version

