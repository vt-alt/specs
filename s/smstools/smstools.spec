Name: smstools
Version: 3.1.21
Release: alt1

Summary: SMS Gateway software which can send and receive short messages through GSM modems and mobile phones
License: GPLv2+
Group: Communications

Url: http://smstools3.kekekasvi.com
Source0: http://smstools3.kekekasvi.com/packages/smstools3-%version.tar.gz
Source1: smsd.init
Source2: smsd.logrotate
Source3: smsd.conf

BuildRequires: libmm-devel

%description
%summary

%prep
%setup -q

# build with debug info
subst '/ggdb/ s/^#//' src/Makefile
# build with statistics
subst '/^CFLAGS.*NOSTATS/d' src/Makefile 
# correct mode for html docs
find doc -type f -exec chmod 644 {} \;

%build
%make_build

%install
mkdir -p %buildroot%_spooldir/sms/{checked,failed,incoming,outgoing,sent}
mkdir -p %buildroot%_logdir/smsd/smsd_stats
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_logrotatedir
cp %SOURCE1 %buildroot%_initdir/smsd
cp %SOURCE2 %buildroot%_logrotatedir/smsd
cp %SOURCE3 %buildroot%_sysconfdir
cp src/smsd %buildroot%_sbindir

%pre
/usr/sbin/groupadd -r -f smsd
/usr/sbin/useradd -r -n -g smsd -d /dev/null -s /dev/null -c SMSd -G uucp,smsd smsd >/dev/null 2>&1 ||:

%post
%post_service smsd

%preun
%preun_service smsd

%files
%attr(0640,root,smsd) %config(noreplace) %_sysconfdir/smsd.conf
%attr(0640,root,root) %config(noreplace) %_logrotatedir/smsd
%attr(0755,root,root) %_initdir/smsd
%attr(0755,root,root) %_sbindir/smsd
%dir %attr(770,root,smsd) %_spooldir/sms
%dir %attr(770,root,smsd) %_spooldir/sms/checked
%dir %attr(770,root,smsd) %_spooldir/sms/failed
%dir %attr(770,root,smsd) %_spooldir/sms/incoming
%dir %attr(770,root,smsd) %_spooldir/sms/outgoing
%dir %attr(770,root,smsd) %_spooldir/sms/sent
%dir %attr(770,root,smsd) %_logdir/smsd
%dir %attr(770,root,smsd) %_logdir/smsd/smsd_stats
%doc README LICENSE examples doc

%changelog
* Mon Jul 01 2019 Andrey Cherepanov <cas@altlinux.org> 3.1.21-alt1
- New version (ALT #36961).
- Enable statistics.

* Tue Oct 02 2012 Vladimir Lettiev <crux@altlinux.ru> 3.1.14-alt1
- initial build
