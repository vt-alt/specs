%define _unpackaged_files_terminate_build 1
%define dovecot_version 2.3

Name: dovecot-pigeonhole
Version: 0.5.7.1
Epoch: 1
Release: alt1
Summary: Sieve language and the ManageSieve protocol for the Dovecot Secure IMAP Server
Group: System/Servers
License: LGPL v2.1
Source: dovecot-2.3-pigeonhole-%version.tar.gz
Source1: postfix+sieve.patch
Url: http://pigeonhole.dovecot.org/

Requires: dovecot >= %dovecot_version

BuildRequires: dovecot-devel >= %dovecot_version

%description
This package is part of the Pigeonhole project
(http://pigeonhole.dovecot.org). It adds support for the Sieve language
(RFC 5228) and the ManageSieve protocol (RFC 5804) to the Dovecot Secure
IMAP Server. In the literal sense, a pigeonhole is a a hole or recess
inside a dovecot for pigeons to nest in. It is, however, also the name
for one of a series of small, open compartments in a cabinet used for
filing or sorting mail. As a verb, it describes the act of putting an
item into one of those pigeonholes. The name `Pigeonhole' therefore well
describes an important part of the functionality that this project adds
to Dovecot: sorting and filing e-mail messages.

This package provides Sieve support as a plugin to Dovecot's Local
Delivery Agent (LDA) and Dovecot's LMTP service. The ManageSieve
protocol is provided is an additional service, next to Dovecot's own
POP3 and IMAP services.

%package devel
Group: Development/C
Summary: Development file for %name, %summary
%description devel
Development file for %name, %summary

%prep
%setup -n dovecot-%dovecot_version-pigeonhole-%version
cp %SOURCE1 .

%build
export ACLOCAL='aclocal -I .'
%autoreconf
%configure --with-dovecot=%_libdir/dovecot --disable-static
%make_build

%check
make test

%install
make DESTDIR=%buildroot install dovecot_docdir=%_defaultdocdir/dovecot-%dovecot_version
install -pD -m 644 %buildroot/%_defaultdocdir/dovecot-%dovecot_version/example-config/conf.d/20-managesieve.conf %buildroot/%_sysconfdir/dovecot/conf.d/20-managesieve.conf
install -pD -m 644 %buildroot/%_defaultdocdir/dovecot-%dovecot_version/example-config/conf.d/90-sieve.conf %buildroot/%_sysconfdir/dovecot/conf.d/90-sieve.conf

# XXX behold, verifyelf
( cd %buildroot/%_libdir; ln -s dovecot/lib*.so.* . )

%files
%doc README AUTHORS NEWS TODO *.patch examples
%doc %_defaultdocdir/dovecot-%dovecot_version/
%doc %_defaultdocdir/dovecot-%dovecot_version/example-config/
%doc %_defaultdocdir/dovecot-%dovecot_version/example-config/*
%doc %_defaultdocdir/dovecot-%dovecot_version/sieve
%doc %_defaultdocdir/dovecot-%dovecot_version/*
%exclude %_libdir/dovecot/*.la
%exclude %_libdir/dovecot/modules/*.la
%_bindir/*
%prefix/libexec/*
%_mandir/*/*
# XXX behold, verifyelf
%_libdir/lib*.so.*
%_libdir/dovecot/lib*.so.*
%_libdir/dovecot/modules/doveadm/lib*_doveadm_sieve_plugin.*
%_libdir/dovecot/modules/lib*_sieve*
%_libdir/dovecot/modules/sieve
%_libdir/dovecot/modules/settings
%_libdir/dovecot/modules/settings/lib*

%config(noreplace) %_sysconfdir/dovecot/conf.d/20-managesieve.conf
%config(noreplace) %_sysconfdir/dovecot/conf.d/90-sieve.conf

%files devel
%dir %_includedir/dovecot/sieve
%_includedir/dovecot/sieve/*
%_includedir/dovecot/
%_includedir/dovecot/*
%_libdir/dovecot/lib*.so
%_aclocaldir/dovecot-pigeonhole.m4

%changelog
* Fri Aug 23 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:0.5.7.1-alt1
- Updated to 0.5.7.1.

* Mon Mar 25 2019 Fr. Br. George <george@altlinux.ru> 1:0.5.5-alt1
- Autobuild version bump to 0.5.5

* Fri Jul 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:0.5.2-alt1
- Update version to 0.5.2 from src

* Fri Jul 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:0.4.24-alt1
- Update version to 0.4.24 from src

* Thu Jan 18 2018 Fr. Br. George <george@altlinux.ru> 1:0.4.21-alt1
- Autobuild version bump to 0.4.21

* Wed Jun 07 2017 Fr. Br. George <george@altlinux.ru> 1:0.4.18-alt2
- Build with new dovecot

* Wed Apr 26 2017 Fr. Br. George <george@altlinux.ru> 1:0.4.18-alt1
- Autobuild version bump to 0.4.18
- Build with new dovecot

* Wed Mar 15 2017 Fr. Br. George <george@altlinux.ru> 1:0.4.17-alt1
- Autobuild version bump to 0.4.17

* Tue Dec 27 2016 Fr. Br. George <george@altlinux.ru> 1:0.4.16-alt1
- Autobuild version bump to 0.4.16 (closes: 32947)

* Mon Jan 25 2016 Fr. Br. George <george@altlinux.ru> 1:0.4.11-alt1
- Autobuild version bump to 0.4.11

* Wed Oct 14 2015 Fr. Br. George <george@altlinux.ru> 1:0.4.9-alt1
- Autobuild version bump to 0.4.9

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 1:0.4.8-alt1
- Autobuild version bump to 0.4.8
- Build with new dovecot

* Tue Apr 21 2015 Fr. Br. George <george@altlinux.ru> 1:0.4.7-alt1
- Autobuild version bump to 0.4.7

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 1:0.4.6-alt1
- Autobuild version bump to 0.4.6

* Tue Oct 28 2014 Fr. Br. George <george@altlinux.ru> 1:0.4.4-alt1
- Autobuild version bump to 0.4.4
- Build with new dovecot

* Tue May 13 2014 Fr. Br. George <george@altlinux.ru> 1:0.4.3-alt1
- Autobuild version bump to 0.4.3
- Build with new dovecot

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 1:0.4.2-alt4
- Build with new dovecot

* Mon Jan 13 2014 Fr. Br. George <george@altlinux.ru> 1:0.4.2-alt3
- Build with new dovecot

* Thu Nov 28 2013 Fr. Br. George <george@altlinux.ru> 1:0.4.2-alt2
- Build with new dovecot

* Tue Oct 15 2013 Fr. Br. George <george@altlinux.ru> 1:0.4.2-alt1
- Autobuild version bump to 0.4.2
- Dovecot minor version bump

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 1:0.4.1-alt1
- Autobuild version bump to 0.4.1
- Dovecot submajor version bump

* Tue May 21 2013 Fr. Br. George <george@altlinux.ru> 1:0.4.0-alt1
- Autobuild version bump to 0.4.0
- Dovecot submajor version bump

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 1:0.3.3-alt3
- Rebuild with dovecot 2.1.15

* Mon Dec 17 2012 Fr. Br. George <george@altlinux.ru> 1:0.3.3-alt2
- Rebuild with dovecot 2.1.12

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 1:0.3.3-alt1
- Autobuild version bump to 0.3.3

* Tue Aug 21 2012 Fr. Br. George <george@altlinux.ru> 1:0.3.1-alt3
- Rebuild with dovecot 2.1.9

* Thu Aug 02 2012 Fr. Br. George <george@altlinux.ru> 1:0.3.1-alt2
- Rebuild with dovecot 2.1.8

* Tue Jun 05 2012 Fr. Br. George <george@altlinux.ru> 1:0.3.1-alt1
- Autobuild version bump to 0.3.1
- Add patchfile as a documentation

* Mon May 14 2012 Fr. Br. George <george@altlinux.ru> 1:0.3.0-alt1
- Initial separate build for ALT

