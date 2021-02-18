%define _unpackaged_files_terminate_build 1

Name: clamsmtp
Version: 1.10
Release: alt4

Summary: SMTP virus-scanning proxy
License: BSD
Group: File tools

Url: http://thewalter.net/stef/software/clamsmtp/
Source0: %name-%version.tar.gz
Source1: %{name}d.init
Source2: %{name}d.conf
Source3: %name-README.ALT-ru_RU.UTF-8
Source4: %{name}d.service
Source5: %name.tmpfiles

Patch0: clamsmtp-1.9-alt-strncat-buffer-overflow.patch
Patch1: clamsmtp-1.10-alt-smtppass.patch

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: clamav

%description
ClamSMTP is an SMTP filter that allows you to check for viruses using the
ClamAV anti-virus software. It accepts SMTP connections and forwards the SMTP
commands and responses to another SMTP server. The 'DATA' email body is
intercepted and scanned before forwarding.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

install -pD -m755 %SOURCE1 %buildroot%_initdir/%{name}d
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/
install -pD -m644 %SOURCE4 %buildroot%_unitdir/%{name}d.service
install -pD -m644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf
install -m644 %SOURCE3 %_builddir/%name-%version/README.ALT-ru_RU.UTF-8

%post
%post_service %{name}d

%postun
%preun_service %{name}d

%files
%doc AUTHORS ChangeLog README README.ALT-ru_RU.*
%config(noreplace) %_sysconfdir/*.conf
%_initdir/*
%_unitdir/*
%_sbindir/*
%_tmpfilesdir/*
%_man5dir/*
%_man8dir/*

%changelog
* Thu Feb 11 2021 Alexey Shabalin <shaba@altlinux.org> 1.10-alt4
- NMU: add systemd unit and tmpfiles config

* Fri Oct 19 2018 Leontiy Volodin <lvol@altlinux.org> 1.10-alt3
- add clamsmtp-1.10-alt-smtppass.patch (thanks gentoo for this patch)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.10-alt2.qa1
- NMU: rebuilt for debuginfo.

* Mon May 31 2010 Mikhail Efremov <sem@altlinux.org> 1.10-alt2
- drop alt-mkstemp patch

* Sun Aug 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.10-alt1
- 1.10

* Wed Nov 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.9-alt2
- fix for buffer overflow in strncat

* Mon Jun 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.9-alt1
- 1.9

* Thu Jan 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.8-alt2
- updated options in default configuration file (fixed #10710)
- drop README.ALT-ru_RU.KOI8-R

* Fri Sep 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.8-alt1
- 1.8

* Mon Aug 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt1
- 1.7

* Tue Mar 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.6-alt1
- 1.6

* Thu Oct 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.5-alt1
- 1.5

* Mon Jun 13 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Thu Jan 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.3-alt1
- 1.3

* Sun Jan 09 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- initial release

