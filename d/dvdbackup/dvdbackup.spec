Name: dvdbackup
Version: 0.4.2
Release: alt3

Summary: DVD-copy tool
License: GPL
Group: Archiving/Cd burning

Url: http://dvdbackup.sourceforge.net
Source0: %name-%version.tar
Source1: http://ftp.debian.org/debian/pool/main/d/dvdbackup/dvdbackup_0.4.2-4.debian.tar.gz
Packager: Vlasenko Igor <viy@altlinux.ru>
BuildRequires: libdvdread-devel >= 0.9.6

Summary(ru_RU.UTF-8): Утилита для копирования содержимого DVD на жесткий диск

%description
Copy DVD-content on hard disc.

%description -l ru_RU.UTF-8
Утилита копирования содержимого DVD диска на жесткий диск.
Поддерживает как выборочное копирование, так и полное.

%prep
%setup -a1
for patch in `cat debian/patches/series`; do
    patch -p1 < debian/patches/$patch
done
cp -at . -- /usr/share/gnu-config/config.sub /usr/share/gnu-config/config.guess

%build
%configure 
%make_build

%install
%makeinstall_std
%find_lang %name
rm -rf %buildroot%_defaultdocdir/%name

%files -f %name.lang
%doc README INSTALL
%_bindir/%name
%_man1dir/%name.*

%changelog
* Wed Apr 22 2020 Anton Farygin <rider@altlinux.ru> 0.4.2-alt3
- update from debian to fix build with libdvdread 6.1.1

* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 0.4.2-alt2
- fixed build on new arches
- spec fixup/cleanup

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1
- new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Sep 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- new version from http://dvdbackup.sourceforge.net

* Sun Jan 21 2007 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2
- removed static linkage with legacy version 0.9.4 of libdvdread
- (debian patch, thanks to thresh@ for hint)

* Wed Jan 17 2007 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1
- new version;
- resurrected from orphaned;
- note: starting from 0.9.7, libdvdread no more provide
  UDFFindFile symbol. so we statically link dvdbackup
  with legacy version 0.9.4 of libdvdread.

* Wed Jan 17 2007 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt0.M30.1
- backport for M30

* Tue Oct 05 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.1-alt1.1
- Rebuilt with libdvdread.so.3.

* Sun May 18 2003 Gerasimov Dmitry <dmitryg@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Team
