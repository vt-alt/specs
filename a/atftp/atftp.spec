%define _unpackaged_files_terminate_build 1

Name: atftp
Version: 0.7.2
Release: alt2

URL: https://sourceforge.net/projects/atftp
Summary: Advanced Trivial File Transfer Protocol
License: GPLv2+
Group: System/Servers
Conflicts: tftpd

Source: %name-%version.tar

Source1: atftpd.init
Source2: atftpd.sysconfig
Source3: atftpd.tmpfiles.conf

Patch1: %name-%version-alt.patch

%description
atftp stands for Advanced Trivial File Transfer Protocol. It is called
"advanced", by contrast to others TFTP servers, for two reasons.
Firstly, it is intended to be fully compliant with all related
RFCs. This include RFC1350, RFC2090, RFC2347, RFC2348 and RFC2349.
To my knowledge, there is no TFTP server currently available in the
public domain that fulfills this requirement. Secondly, atftp is
intended for serving boot files to large clusters. It is
multi-threaded and support multicast (RFC2090 and PXE), allowing
faster boot of hundreds of machine simultaneously.

%prep
%setup
%patch1 -p1

%build
%configure --disable-libpcre
make

%install
%makeinstall
install -pm0755 -D %SOURCE1 %buildroot%_initdir/atftpd
install -pm0644 -D %SOURCE2 %buildroot%_sysconfdir/sysconfig/atftpd
install -pm0644 -D %SOURCE3 %buildroot%_tmpfilesdir/atftpd.tmpfiles.conf
mkdir -p %buildroot%_localstatedir/tftpboot
mkdir -pm0770 %buildroot%_logdir/atftpd
touch %buildroot%_sysconfdir/mtftp.conf
 
%pre
%_sbindir/groupadd -r -f _atftpd &> /dev/null
%_sbindir/useradd -r -g _atftpd -d /dev/null -s /dev/null -c 'ATFTP Service User' -n _atftpd &> /dev/null ||:

%post
%post_service atftpd

%preun
%preun_service atftpd

%files
%doc Changelog BUGS FAQ INSTALL LICENSE README README.CVS 
%doc README.MCAST README.PCRE TODO docs test/mtftp.conf

%config(noreplace) %_sysconfdir/sysconfig/atftpd
%ghost %config(noreplace) %_sysconfdir/mtftp.conf

%_tmpfilesdir/atftpd.tmpfiles.conf

%_initdir/atftpd

%_bindir/atftp
%_sbindir/atftpd
%_sbindir/in.tftpd

%_man1dir/atftp.1*
%_man8dir/atftpd.8*
%_man8dir/in.tftpd.8*

%dir %_localstatedir/tftpboot
%dir %attr(0770,root,_atftpd) %_logdir/atftpd

%changelog
* Wed Oct 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.2-alt2
- Create runtime directory via tmpfiles (Closes: #39157).

* Tue Oct 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.2-alt1
- Updated to upstream version 0.7.2 (Fixes: CVE-2019-11365, CVE-2019-11366).

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1.qa1
- NMU: added URL:

* Mon Aug 03 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.1-alt1
- 0.7.1 released

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Oct 15 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt1
- built for ALTLinux

* Mon Aug 10 2009 Douglas E. Warner <silfreed@silfreed.net> 0.7-6
- fixing typo in service scripts

* Tue Jan 15 2007 Douglas E. Warner <silfreed@silfreed.net> 0.7-5
- fixing typos in sysconfig
- fixing dir creation
- adding chkconfig for init script

* Tue Jan 15 2007 Douglas E. Warner <silfreed@silfreed.net> 0.7-4
- adding user/group
- adding log dir
- updating sysconfig to set user, group, and log dir

* Tue Jan 15 2007 Douglas E. Warner <silfreed@silfreed.net> 0.7-3
- updated license to GPLv2+
- added init script and sysconfig

* Tue Jan 15 2007 Douglas E. Warner <silfreed@silfreed.net> 0.7-2
- adding patches from Dag's SRPM
- updating format to Fedora guidelines

* Mon Jun 06 2005 Douglas E. Warner <silfreed@silfreed.net> 0.7-1
- Initial RPM release.

