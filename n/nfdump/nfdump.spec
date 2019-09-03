# https://bugzilla.altlinux.org/36391
%def_without	devel

Name: nfdump
Version: 1.6.18
Release: alt1
Summary: collect and process netflow data

Group: Monitoring
License: %bsd
#Url: http://sourceforge.net/projects/nfdump/
Url: https://github.com/phaag/nfdump/releases

Source: %name-%version.tar
Source2: nfcapd.init
Source3: nfcapd.sysconfig
Source4: nfcapd.service
Source5: %name.tmpfiles
Source6: sfcapd.init
Source7: sfcapd.sysconfig
Source8: sfcapd.service

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: rpm-build-licenses

BuildRequires: librrd-devel libpcap-devel flex bison zlib-devel bzlib-devel

%description
Nfdump is a set of tools to collect and process netflow data.
It's fast and has a powerful filter pcap like syntax. Nfdump
supports netflow versions v5, v7, v9 and IPFIX as well as a
limited set of sflow and is IPv6 compatible.

%package nfprofile
Summary: nfprofile - netflow profiler
Group: Monitoring

%description nfprofile
nfprofile is the netflow profiler program for NfSen. It reads
the netflow data from the files stored by nfcapd and creates
the corresponding output files for every channel required.
This program is run only by NfSen.

%package nftrack
Summary: nftrack - Port tracking decoder for NfSen plugin PortTracker.
Group: Monitoring

%description nftrack
nftrack - Port tracking decoder for NfSen plugin PortTracker.

%package -n libnfdump
Summary: nfdump shared library
Group: System/Libraries

%description -n libnfdump
nfdump shared library

%if_with devel
%package -n libnfdump-devel
Summary: nfdump development files
Group: Development/C

%description -n libnfdump-devel
nfdump development files
%endif

%prep
%setup -q

%build
%autoreconf
%configure \
	--disable-static \
	--enable-nfprofile \
	--enable-nftrack \
	--enable-sflow \
	--enable-readpcap \
	--enable-nfpcapd \
	--enable-nsel

%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_cachedir/{nfcapd,sfcapd},%_sysconfdir/sysconfig,%_initdir,%_unitdir,%_tmpfilesdir,%_runtimedir/{nfcapd,sfcapd}}

install -m0755 %SOURCE2 %buildroot%_initdir/nfcapd
install -m0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/nfcapd
install -m0644 %SOURCE4 %buildroot%_unitdir/nfcapd.service
install -m0644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf
install -m0755 %SOURCE6 %buildroot%_initdir/sfcapd
install -m0644 %SOURCE7 %buildroot%_sysconfdir/sysconfig/sfcapd
install -m0644 %SOURCE8 %buildroot%_unitdir/sfcapd.service

%if_without devel
rm %buildroot%_libdir/libnfdump.so
%endif

%pre
%_sbindir/groupadd -r -f nfcapd
%_sbindir/useradd -r -n -g nfcapd -d %_cachedir/nfcapd -s /bin/false nfcapd >/dev/null 2>&1 ||:

%_sbindir/groupadd -r -f sfcapd
%_sbindir/useradd -r -n -g sfcapd -d %_cachedir/sfcapd -s /bin/false sfcapd >/dev/null 2>&1 ||:

%post
%post_service nfcapd
%post_service sfcapd

%preun
%preun_service nfcapd
%preun_service sfcapd

%files
%exclude %_bindir/nfprofile
%exclude %_man1dir/nfprofile.1.*
%exclude %_bindir/nftrack
%_bindir/*
%_man1dir/*
%_initdir/*
%_unitdir/*
%_tmpfilesdir/*
%config(noreplace) %_sysconfdir/sysconfig/*
%attr(770,root,nfcapd) %dir %_cachedir/nfcapd
%attr(775,root,nfcapd) %dir %_runtimedir/nfcapd
%attr(770,root,sfcapd) %dir %_cachedir/sfcapd
%attr(775,root,sfcapd) %dir %_runtimedir/sfcapd
%doc README NEWS AUTHORS ChangeLog COPYING

%files nfprofile
%_bindir/nfprofile
%_man1dir/nfprofile.1.*

%files nftrack
%_bindir/nftrack

%files -n libnfdump
%_libdir/libnfdump-%version.so

%if_with devel
%files -n libnfdump-devel
%_libdir/libnfdump.so
%endif

%changelog
* Sun Sep 01 2019 Sergey Y. Afonin <asy@altlinux.org> 1.6.18-alt1
- 1.6.18 (removed 1.5 compat code)
- built without --enable-compat15
- don't packed devel subpackage (ALT #36391)

* Fri Jun 22 2018 Sergey Y. Afonin <asy@altlinux.ru> 1.6.17-alt1
- 1.6.17
- changed Url

* Tue Oct 31 2017 Sergey Y. Afonin <asy@altlinux.ru> 1.6.15-alt2
- rebuilt with librrd8

* Sat Jul 09 2016 Sergey Y. Afonin <asy@altlinux.ru> 1.6.15-alt1
- 1.6.15 (Security update)
- added libnfdump and libnfdump-devel packages

* Thu Jul 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.13-alt3
- fixed init and unit names

* Fri Jul 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.13-alt2
- add nftrack package

* Thu Jul 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.13-alt1
- 1.6.13
- add --enable-nsel configure options
- add sfcapd init script
- add systemd unit and tmpfiles files

* Wed May 07 2014 Sergey Y. Afonin <asy@altlinux.ru> 1.6.12-alt1
- New version 1.6.12

* Sat Dec 07 2013 Sergey Y. Afonin <asy@altlinux.ru> 1.6.11-alt1
- New version 1.6.11

* Sat Apr 06 2013 Sergey Y. Afonin <asy@altlinux.ru> 1.6.9-alt1
- New version 1.6.9

* Wed Apr 11 2012 Sergey Y. Afonin <asy@altlinux.ru> 1.6.6-alt2
- added %%post_service/%%preun_service
- fixed line for chkconfig in init script
- added lsb init header in init script

* Fri Mar 30 2012 Sergey Y. Afonin <asy@altlinux.ru> 1.6.6-alt1
- New version 1.6.6
- moved nfprofile to separated subpackage

* Tue Nov 08 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.6.4-alt2
- enabled compatibility with data of nfdump 1.5

* Mon Sep 19 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.6.4-alt1
- New version 1.6.4 (ALT #25699)

* Sat Feb 12 2011 Vladimir Lettiev <crux@altlinux.ru> 1.6.3-alt1
- New version 1.6.3

* Sun Sep 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1.6.2-alt1
- New version 1.6.2

* Thu Jun 10 2010 Vladimir Lettiev <crux@altlinux.ru> 1.6.1-alt1
- initial build

