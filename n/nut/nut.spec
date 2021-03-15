# -*- rpm-spec -*-
%define _unpackaged_files_terminate_build 1

%def_with python2

Name: nut
Version: 2.7.4
Release: alt4

Summary: Network UPS Tools
License: GPL
Group: System/Servers
Url: http://networkupstools.org

%define srcname nut-%version
# https://github.com/networkupstools/nut
Source: nut-%version.tar
Source1: upsdrv.init
Source2: upsd.init
Source3: upsmon.init
Source4: upsd.sysconfig

Source104: libs.sh

Patch4: nut-2.6.0-alt-chroot.patch
Patch5: nut-2.6.0-alt-upsdrvctl-list.patch
Patch6: nut-2.6.0-alt-upsstats.patch
Patch7: nut-2.6.0-alt-drivers.patch
Patch10: nut-2.6.0-alt-usb.patch
Patch20: nut-2.6.2-snmp-noAES.patch
Patch21: nut-2.6.0-upsd-listen.patch
Patch22: nut-2.6.0-usb_submit_urb.patch
Patch23: nut-2.6.5-alt-systemd.patch
Patch24: nut-2.6.5-bcmxcp.patch
Patch25: nut-2.7.4-alt-gdlib.patch
Patch26: nut-2.7.4-alt-linking.patch
Patch27: nut-2.7.4-github-504-openssl.patch
Patch28: nut-2.7.4-man-parralel-build.patch
Patch29: nut-2.7.4-alt-python-compat.patch
Patch30: nut-2.7.4-alt-dont-autoreconf.patch
Patch31: nut-2.7.4-alt-fix-strip.patch

# Fedora patches
Patch103: nut-2.6.5-quickfix.patch
Patch105: nut-2.6.5-dlfix.patch
Patch107: nut-2.6.5-foreground.patch
Patch108: nut-2.6.5-unreachable.patch
Patch109: nut-2.6.5-rmpidf.patch

%def_with ssl
%def_with cgi
%def_with snmp
%def_with usb
%def_with avahi
%def_with freeipmi
%def_with systemd

%define docdir %_docdir/%name-%version
%define cgidocdir %_docdir/%name-cgi-%version
%define confdir %_sysconfdir/%name
%define drvdir /lib/%name
%define cgidir /var/www/cgi-bin
%define htmldir /var/www/html/%name
%define runas upsmon
%define ROOT %_localstatedir/%name
%define fdi_hal %_datadir/hal/fdi/information/20thirdparty

PreReq: shadow-utils
PreReq: libupsclient = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: pkgconfig libtool-common
BuildRequires: libltdl-devel
BuildRequires: asciidoc-a2x
%{?_with_systemd:BuildRequires: systemd-devel}

%if_with ssl
BuildRequires: libssl-devel
%endif

%if_with cgi
BuildRequires: fontconfig-devel freetype2-devel libgd2-devel libjpeg-devel libpng-devel
%endif

%if_with snmp
BuildRequires: libnet-snmp-devel python-modules
%endif

%if_with avahi
BuildRequires: libavahi-devel
%endif

%if_with freeipmi
BuildRequires: libfreeipmi-devel
%endif

%if_with usb
%define libusb libusb-compat-devel
%endif

%add_findreq_skiplist /lib/systemd/system-shutdown/nutshutdown

BuildRequires: %libusb

BuildRequires: libdbus-devel
BuildRequires: libdbus-glib-devel

%package server
Summary: The UPS information server
Group: System/Servers
Requires: shadow-utils
Requires: libnutscan = %EVR
Requires: libupsclient = %EVR
Provides: %name-driver = %EVR
Obsoletes: %name-driver < %EVR
Provides: %name-driver-usb = %EVR
Obsoletes: %name-driver-usb < %EVR

%package driver-snmp
Summary: Multi-MIB Driver for SNMP UPS equipment
Group: System/Servers
Requires: %name-server = %EVR

%package driver-ipmi
Summary: Multi-HID Driver for IPMI UPS equipment
Group: System/Servers
Requires: %name-server = %EVR

%package cgi
Summary: CGI utilities for the Network UPS Tools
Group: System/Servers
Requires: webserver
Requires: libupsclient = %EVR

%package -n libupsclient
Summary: Shared library libupsclient of nut
Group: Development/C
Conflicts: nut-devel

%package -n libnutscan
Summary: Shared library libnutscan of nut
Group: Development/C

%package -n libnutclient
Summary: Shared library libnutclient of nut
Group: Development/C

%package -n libupsclient-devel
Summary: Header files and C programming manuals for nut
Group: Development/C
Conflicts: nut-devel
Requires: libupsclient = %EVR
Requires: libnutscan = %EVR

%description
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package includes the client utilities that are required to monitor a
UPS that the client host is powered from - either connected directly via
a serial port (in which case the %name-server package needs to be installed on
this machine) or across the network (where another host on the network
monitors the UPS via serial cable and runs the upsd from %name-server package
to allow clients to see the information).

%description server
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package contains the UPS information server and per-UPS-model drivers which talk to the UPSes.

%description driver-snmp
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package contains somewhat experimental support of a wide range
of SNMP-aware UPS devices, including MGE and APC, for details
see snmp-ups(8).

%description driver-ipmi
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package contains somewhat experimental support of IPMI UPS devices,
for details see nut-ipmipsu(8).

%description cgi
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package includes CGI programs for accessing UPS status via a web
browser and can be installed on a separate machine to the rest of the
%name packages.


%description -n libupsclient
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package includes shared library of NUT project.

%description -n libnutscan
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package includes shared library of NUT project.

%description -n libnutclient
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package includes shared library of NUT project.

%description -n libupsclient-devel
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package includes header files and C programming manuals for nut.

%if_with python2
%package client
Summary: The UPS information GUI client
Group: System/Servers
BuildArch: noarch
Requires: python-module-%name = %EVR
%py_requires gtk.glade
%py_requires pynotify

%description client
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package contains the UPS information GUI client.

%package -n python-module-%name
Summary: Python bindings for NUT
Group: Development/Python
Requires: %name = %EVR

%description -n python-module-%name
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package contains python bindings for NUT.
%endif

%package -n python3-module-%name
Summary: Python bindings for NUT
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%name
These programs are part of a developing project to monitor the assortment 
of UPSes that are found out there in the field.  Many models have serial 
serial ports of some kind that allow some form of state checking.  This
capability has been harnessed where possible to allow for safe shutdowns, 
live status tracking on web pages, and more.

This package contains python bindings for NUT.

%prep
%setup
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch10 -p2
%patch21 -p1
%patch24 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1

%patch103 -p1 -b .quickfix
%patch105 -p1 -b .dlfix
%patch107 -p1 -b .foreground
%patch108 -p1 -b .unreachable
%patch109 -p1 -b .rmpidf

%patch23 -p2
%patch25 -p2
%patch26 -p2

# fix cgi path in html links for current %%cgidir
sed -i 's@/cgi-bin/nut/@/cgi-bin/@g' data/html/header.html.in

# fixes for nut client
sed -i 's|=NUT-Monitor|=nut-monitor|'  scripts/python/app/nut-monitor.desktop
sed -i "s|sys.argv\[0\]|'%_datadir/nut/nut-monitor/nut-monitor'|" scripts/python/app/NUT-Monitor

%build
%define snmp_opts --with-snmp
./autogen.sh
%autoreconf
%configure \
	--disable-static \
	--sysconfdir=%confdir --datadir=%confdir \
	--includedir=%_includedir/%name \
	--with-pkgconfig-dir=%_pkgconfigdir \
	%{subst_with cgi} --with-cgipath=%cgidir \
	--with-htmlpath=%htmldir \
	%{subst_with ssl} \
	--with-drvpath=%drvdir \
	--with-statepath=%_localstatedir/upsd \
	%{subst_with usb} \
	--with-udev-dir=/lib/udev \
	%{subst_with snmp} %snmp_opts \
	--with-pkgconfig-dir=%_pkgconfigdir \
	--with-dev \
	--with-user=%runas \
	--with-group=%runas \
	--enable-strip=no \
	%nil

sh %SOURCE104 >>include/config.h

%make_build

%install
%makeinstall_std

# Provide %drvdir/newapc for compatibility with nut-1.4.x
ln -s apcsmart %buildroot%drvdir/newapc

# Provide %drvdir/powermust for compatibility with nut-2.0.4
ln -s blazer_ser %buildroot%drvdir/powermust
ln -s blazer_ser %buildroot%drvdir/megatec

# Install start/stop scripts.
install -pD -m755 %SOURCE1 %buildroot%_initdir/upsdrv
install -pD -m755 %SOURCE2 %buildroot%_initdir/upsd
install -pD -m755 %SOURCE3 %buildroot%_initdir/upsmon
install -pD -m644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/upsd

# SSL infrastucture.
mkdir -p %buildroot%confdir/certs
touch %buildroot%confdir/upsd.pem
# Copy *.conf.sample files to *.conf
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
mkdir -p %buildroot%cgidocdir
for f in %buildroot%confdir/*.sample ; do
    f=`basename $f`
    cp -p %buildroot%confdir/$f %buildroot%confdir/"${f/.sample/}"
done
mv %buildroot%confdir/*.sample %buildroot%docdir/
# Prepare chroot jail for upsd/upsdrv.
mkdir -p %buildroot%ROOT{/dev,%confdir,%_localstatedir/upsd}
ln -s %name%_localstatedir/upsd %buildroot%_localstatedir/
pushd %buildroot
cp -p .%confdir/ups.conf .%ROOT%confdir/
for f in upsd.conf upsd.users upsd.pem cmdvartab; do
	mv .%confdir/$f .%ROOT%confdir/$f
	ln -s `relative %ROOT%confdir/$f %confdir/` .%confdir/
done
popd

# Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature.
mksock %buildroot%ROOT/dev/log
mkdir -p %buildroot%_sysconfdir/syslog.d
ln -s %ROOT/dev/log %buildroot%_sysconfdir/syslog.d/%name


# Rename udev rules file
%if_with usb
mv %buildroot/lib/udev/rules.d/62-nut-usbups.rules %buildroot/lib/udev/rules.d/98-nut-usbups.rules
%endif
%if_with freeipmi
mv %buildroot/lib/udev/rules.d/52-nut-ipmipsu.rules %buildroot/lib/udev/rules.d/98-nut-ipmipsu.rules
%endif

%if_with systemd
# Add symlink for SysV compatibility
ln -s nut-monitor.service %buildroot%_unitdir/upsmon.service
ln -s nut-driver.service %buildroot%_unitdir/upsdrv.service
ln -s nut-server.service %buildroot%_unitdir/upsd.service
%endif

# install PyNUT
install -p -D -m 644 scripts/python/module/PyNUT.py %buildroot%python3_sitelibdir/PyNUT.py

# install nut-monitor
%if_with python2
install -p -D -m 644 scripts/python/module/PyNUT.py %buildroot%python_sitelibdir/PyNUT.py

mkdir -p %buildroot%_datadir/nut/nut-monitor/pixmaps
install -p -m 755 scripts/python/app/NUT-Monitor %buildroot%_datadir/nut/nut-monitor/nut-monitor
install -p -m 644 scripts/python/app/gui-1.3.glade %buildroot%_datadir/nut/nut-monitor
install -p -m 644 scripts/python/app/pixmaps/* %buildroot%_datadir/nut/nut-monitor/pixmaps/
install -p -D scripts/python/app/nut-monitor.png %buildroot%_pixmapsdir/nut-monitor.png
install -p -D -m 644 scripts/python/app/nut-monitor.desktop %buildroot%_desktopdir/nut-monitor.desktop
ln -sr %buildroot%_datadir/nut/nut-monitor/nut-monitor %buildroot%_bindir/nut-monitor
%endif

# remove unpackaged files
rm -f %buildroot%_libdir/*.a

%pre
if [ $1 -gt 1 -a -x /sbin/upsmon -a ! -d /etc/nut/certs ]; then
	echo "Upgrading from incompatible nut < 1.4.1-alt2" >&2
	[ -x %_initdir/upsmon ] && service upsmon condstop ||:
	[ -x %_initdir/upsd ] && service upsd condstop ||:
	if [ ! -d "%confdir" -o -e "%confdir".bak ] ||
	   ! mv -v "%confdir" "%confdir".bak; then
		echo "Automatic upgrade failed." >&2
		exit 1
	fi
	echo "Please update config files manually." >&2
fi
/usr/sbin/groupadd -r -f %runas
/usr/sbin/useradd -r -g %runas -d / -s /dev/null \
	-c "NUT monitoring daemon" -n %runas >/dev/null 2>&1 ||:

%post
%post_service upsmon

%preun
%preun_service upsmon

%pre server
/usr/sbin/groupadd -r -f upsdrv
/usr/sbin/useradd -r -g upsdrv -G uucp -d %ROOT -s /dev/null \
	-c "NUT drivers" -n upsdrv >/dev/null 2>&1 ||:

/usr/sbin/groupadd -r -f upsd
/usr/sbin/useradd -r -g upsd -G upsdrv -d %ROOT -s /dev/null \
	-c "NUT information server" -n upsd >/dev/null 2>&1 ||:

%post server
%post_service upsdrv
%post_service upsd

%preun server
%preun_service upsd
%preun_service upsdrv


%files
%doc COPYING MAINTAINERS NEWS README UPGRADING docs/*.txt conf/upsmon.conf.sample conf/upssched.conf.sample conf/nut.conf.sample
%dir %confdir
%dir %attr(710,root,%runas) %confdir/certs
%config(noreplace) %attr(640,root,%runas) %confdir/upsmon.conf
%config(noreplace) %attr(640,root,%runas) %confdir/upssched.conf
%_initdir/upsmon
%if_with systemd
%_unitdir/nut-monitor.service
%_unitdir/upsmon.service
/lib/systemd/system-shutdown/nutshutdown
%endif

%_bindir/upsc
%_bindir/upscmd
%_bindir/upslog
%_bindir/upsrw
%_bindir/upssched-cmd
%_sbindir/upsmon
%_sbindir/upssched

%_man5dir/nut.conf.*
%_man5dir/upsmon.conf.*
%_man5dir/upssched.conf.*
%_man8dir/upsc.*
%_man8dir/upscmd.*
%_man8dir/upslog.*
%_man8dir/upsmon.*
%_man8dir/upsrw.*
%_man8dir/upssched.*

%files server
%doc conf/upsd.conf.sample conf/upsd.users.sample conf/ups.conf.sample docs/cables
%_sbindir/upsd
%_bindir/nut-scanner
%_sbindir/upsdrvctl

%_initdir/upsd
%_initdir/upsdrv
%if_with systemd
%_unitdir/nut-server.service
%_unitdir/upsd.service
%_unitdir/nut-driver.service
%_unitdir/upsdrv.service
%endif
%dir %confdir

%config(noreplace) %_sysconfdir/sysconfig/upsd

%confdir/cmdvartab
%confdir/nut.conf
%confdir/upsd.conf
%confdir/upsd.users
%confdir/upsd.pem
%config(noreplace) %attr(640,root,upsdrv) %confdir/ups.conf

%_man5dir/upsd.conf.*
%_man5dir/upsd.users.*

%_sysconfdir/syslog.d/*
%dir %attr(0710,root,upsdrv) %ROOT
%dir %attr(0710,root,upsdrv) %ROOT/dev
%ghost %attr(666,root,root) %ROOT/dev/*
%dir %attr(0710,root,upsdrv) %ROOT/var
%dir %attr(0710,root,upsdrv) %ROOT%_localstatedir
%dir %attr(1730,root,upsdrv) %ROOT%_localstatedir/upsd
%dir %attr(0710,root,upsdrv) %ROOT%_sysconfdir
%dir %attr(0710,root,upsdrv) %ROOT%confdir
%config(noreplace) %attr(640,root,upsd) %ROOT%confdir/cmdvartab
%config(noreplace) %attr(640,root,upsd) %ROOT%confdir/upsd.conf
%config(noreplace) %attr(640,root,upsd) %ROOT%confdir/upsd.users
%config(noreplace) %attr(640,root,upsd) %ROOT%confdir/upsd.pem
%attr(640,root,upsdrv) %ROOT%confdir/ups.conf

%_localstatedir/upsd

%config %confdir/driver.list
%if_with usb
%attr(644,root,root) /lib/udev/rules.d/98-nut-usbups.rules
%endif

%drvdir
%if_with snmp
%exclude %drvdir/snmp-ups
%endif # with_snmp
%if_with freeipmi
%exclude %drvdir/nut-ipmipsu
%endif # with_freeipmi

%_man5dir/ups.conf.*
%_man8dir/*
%exclude %_man8dir/upsc.*
%exclude %_man8dir/upscmd.*
%exclude %_man8dir/upslog.*
%exclude %_man8dir/upsmon.*
%exclude %_man8dir/upsrw.*
%exclude %_man8dir/upssched.*
%if_with cgi
%exclude %_man8dir/upsimage.cgi.*
%exclude %_man8dir/upsset.cgi.*
%exclude %_man8dir/upsstats.cgi.*
%endif # with_cgi
%if_with snmp
%exclude %_man8dir/snmp-ups.*
%endif # with_snmp
%if_with freeipmi
%exclude %_man8dir/nut-ipmipsu.*
%endif # with_freeipmi

%if_with snmp
%files driver-snmp
%dir %drvdir
%drvdir/snmp-ups
%_man8dir/snmp-ups.*
%endif # with_snmp

%if_with freeipmi
%files driver-ipmi
%drvdir/nut-ipmipsu
%attr(644,root,root) /lib/udev/rules.d/98-nut-ipmipsu.rules
%_man8dir/nut-ipmipsu.*
%endif # with_freeipmi

%if_with cgi
%files cgi
%doc conf/hosts.conf.sample conf/upsset.conf.sample  conf/upsstats.html.sample conf/upsstats-single.html.sample data/html/README
%dir %confdir
%config(noreplace) %confdir/hosts.conf
%config(noreplace) %confdir/upsset.conf
%config(noreplace) %confdir/upsstats.html
%config(noreplace) %confdir/upsstats-single.html
%cgidir/upsimage.cgi
%cgidir/upsset.cgi
%cgidir/upsstats.cgi
%htmldir
%_man5dir/hosts.conf.*
%_man5dir/upsset.conf.*
%_man5dir/upsstats.html.*
%_man8dir/upsimage.cgi.*
%_man8dir/upsset.cgi.*
%_man8dir/upsstats.cgi.*
%endif # with_cgi

%files -n libupsclient
%_libdir/libupsclient.so.*

%files -n libnutscan
%_libdir/libnutscan.so.*

%files -n libnutclient
%_libdir/libnutclient.so.*

%files -n libupsclient-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_man3dir/*

%if_with python2
%files client
%_bindir/nut-monitor
%_pixmapsdir/nut-monitor.png
%_desktopdir/nut-monitor.desktop
%_datadir/nut

%files -n python-module-%name
%python_sitelibdir/PyNUT.py*
%endif

%files -n python3-module-%name
%python3_sitelibdir/PyNUT.py
%python3_sitelibdir/__pycache__/PyNUT.*

%changelog
* Wed Feb 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.4-alt4
- Packaged PyNUT GUI into nut-client package (Closes: #39720).
- Disabled stripping debuginfo.

* Mon Mar 11 2019 Anton Farygin <rider@altlinux.ru> 2.7.4-alt3
- cleanup build requires for fix FTBFS (closes: #36253)

* Wed Oct 03 2018 Anton Farygin <rider@altlinux.ru> 2.7.4-alt2
- added patch for build with openssl-1.1
- build from upstream git
- cleaned specfile from old master-2.4 knobs

* Tue May 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.4-alt1
- Updated to upstream version 2.7.4.

* Tue Aug 22 2017 Anton Farygin <rider@altlinux.ru> 2.6.5-alt10
- rebuilt for freeipmi

* Thu Aug 17 2017 Michael Shigorin <mike@altlinux.org> 2.6.5-alt9
- BOOTSTRAP: introduce systemd knob (on by default)

* Thu Jun 16 2016 Anton Farygin <rider@altlinux.ru> 2.6.5-alt8
- rebuild with new freeipmi

* Fri May 02 2014 Michael Shigorin <mike@altlinux.org> 2.6.5-alt7
- skip findreq upon that helper script (closes: #30053)

* Wed Apr 23 2014 Michael Shigorin <mike@altlinux.org> 2.6.5-alt6
- packaged systemd shutdown helper script

* Wed Apr 23 2014 Michael Shigorin <mike@altlinux.org> 2.6.5-alt5
- added bcmxcp patch by Alex Moskalenko (closes: #29847)

* Tue Mar 25 2014 Anton Farygin <rider@altlinux.ru> 2.6.5-alt4
- rebuild with new freeipmi

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 2.6.5-alt3
- rebuild with new freeipmi

* Mon Jul 15 2013 Anton Farygin <rider@altlinux.ru> 2.6.5-alt2
- rebuild with new freeipmi

* Tue Nov 20 2012 Alexey Shabalin <shaba@altlinux.ru> 2.6.5-alt1
- 2.6.5
- add fedora patches (fixed nut-scanner, foreground start daemons for systemd)
- enabled avahi support
- enabled freeipmi support
- enabled systemd support
- add libupsclient package
- merge driver, driver-usb, server packages to server package

* Thu May 31 2012 Michael Shigorin <mike@altlinux.org> 2.6.3-alt2
- applied upstream patch to fix CVE-2012-2944 (closes: #27386)
  + thanks ldv@ for heads-up

* Sun Feb 12 2012 Yura Kalinichenko <yuk@altlinux.org> 2.6.3-alt1
- 2.6.3
- Michael Shigorin <mike@altlinux.org> 2.6.3-alt1.M51.1
  built for M51
- nut & nut-driver depends on current version of libupsclient
- nut-snmp depends on python-modules
- backport to ALT Master 2.4 & ALT branch 4.1
- fix runlevels:
    upsdrv :
     # chkconfig: 2345 51 89
    upsd :
     # chkconfig: 2345 52 88
    upsmon :
     # chkconfig: 2345 53 87
- applied nut-2.6.0-upsd-listen.patch from Sergey Vlasov <vsu@>

* Wed Jan 18 2012 Michael Shigorin <mike@altlinux.org> 2.2.2-alt1.1.1
- reenabled service enabling scripts (except for hal)
  + thanks Vladimir Karpinsky and snejok@ (closes: #26832)

* Wed Dec 22 2010 Michael Shigorin <mike@altlinux.org> 2.2.2-alt1.1
- rebuilt for Sisyphus as my 2.4.3 is not production ready

* Mon Feb 09 2009 Aleksey Avdeev <solo@altlinux.ru> 2.2.2-alt1.1
- NMU

* Fri Sep 12 2008 Mikhail Pluzhnikov <amike@altlinux.ru> 2.2.2-alt1
- New version 2.2.2
  + Updated alt-chroot, alt-drivers, alt-makefile(rewritten from scratch), alt-megatec-shutdown, 
    alt-upsdrvctl-list, alt-upsstats patches for 2.2.2.
  + New patches from alexsid@: alt-man, alt-powercom (update powercom driver).
  + Patch from ab@ for fix usb support.
  + alt-timehead and alt-driverlist patches remove, because merged by upstream.
  + In %name-drives-usb package replace hidups and newhidups by one driver - usbhid-ups(8),
    add new USB driver - megatec_usb(8).
  + Cleaned up specfile.
  + Build %name-drivers-snmp on default again.
  + New sub-package: nut-hal, see info on this package.
  + New two packages libupsclient (provides shared library) and libupsclient-devel
    (provides man(3) pages, headers and configure for pkgconfig).
  + Remove nut-devel package, replace with libupsclient-devel.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.5-alt3.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun Jul 29 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.5-alt3
- Merged changes made by Sergey Vlasov:
  + Updated alt-chroot, alt-upsdrvctl-list, alt-drivers, alt-driverlist patches
    for 2.0.5.
  + Updated alt-makefile patch for 2.0.5, fixed man pages installation
    (gamatronic(8) and rhino(8) man pages were not installed).
  + Moved new bcmxcp_usb and tripplite_usb drivers to the %name-driver-usb
    subpackage.
  + Added HTML pages with references to CGI scripts to the %name-cgi subpackage.
  + driver: Provide %drvdir/powermust symlink for compatibility.
  + Added alt-megatec-shutdown patch: Fix megatec shutdown to use "ondelay" and
    "offdelay" from config.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.5-alt2
- Cleaned up specfile.

* Sun Mar 25 2007 Ilya Evseev <evseev@altlinux.ru> 2.0.5-alt1
- updated to latest version 2.0.5
- added notes for building under Master 2.4

* Wed Feb 07 2007 Stanislav Ievlev <inger@altlinux.org> 2.0.2-alt4
- upsd.sysconfig (upsd_configured): Fixed regexp (ldv, #9907).
- Fixed driver.list file (#10778)

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.2-alt3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Wed May 24 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0.2-alt3
- Do not build snmp driver by default.

* Fri Mar 10 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0.2-alt2
- Fixed pkgconfig files packaging.
- Fixed build with --as-needed.

* Fri Dec 02 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.2-alt1.1
- rebuild with libnetsnmp.so.9 .

* Mon Oct 10 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.2-alt1
- Updated to 2.0.2 release.
- In startup scripts, changed chkconfig priorities
  to start later and stop earler (see #5211).

* Thu Mar 17 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt2
- %_initdir/upsdrv: fixed find warning.

* Sat Mar 05 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt1
- Updated to 2.0.1 release.
- Updated patches.
- Fixed segfault in upsstats.cgi (#5946).

* Thu Sep 30 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt0.1
- Updated to 2.0.1-pre4 (release candidate).
- Format fixes merged upstream, thanks to Russell Kroll
  for understanding the problem.

* Thu Aug 05 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.0-alt2
- Fixed format issues.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.0-alt1.1
- Rebuilt with openssl-0.9.7d.

* Mon Apr 05 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.0-alt1
- Updated to 2.0.0, updated patches.
- driver: Provide %drvdir/newapc symlink for compatibility.
- devel: Packaged libupsclient.pc and libupsclient-config.
- Use /etc/syslog.d/ feature.
- Implemented partial upgrade support from older releases.

* Sun Mar 14 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt2
- Updated to 1.4.2-pre2.
- Implemented "upsdrvctl list" extention.
- Rewritten alt-chroot patch, dropped no longer needed
  chroot.d stuff.
- Relocated drivers from /sbin/ to /lib/nut/, to avoid
  unnecessary namespace pollution.
- Relocated daemons from /sbin/ to /usr/sbin/, since
  there are no need to keep them in /sbin/.
- Relocated upsd configs from %confdir/ to %ROOT%confdir/,
  to avoid unnecessary configs duplication.
- Changed pseudousers layout:
  + upsdrvctl: u=upsdrv, g=upsdrv, G=uucp;
  + upsd: u=upsd, g=upsd, G=upsdrv;
  + upsmon, upslog: u=upsmon, g=upsmon.
- Reworked start/stop scripts.
- Packaged drivers separately.
- Packaged usb drivers separately from other drivers.
- Packaged SSL infrastructure.
- Updated URLs, summaries and descriptions.

* Sat Dec  6 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1
- built and subpackaged experimental snmp-ups driver
- upsd and drivers now are chrooted

* Sat Aug  9 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.4.0-alt1
- 1.4.0
- drivers relocated to /sbin
- initscripts migrated to startup

* Thu Apr 24 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.2.2-alt1
- 1.2.2

* Sat Mar 15 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.2.1-alt1
- 1.2.1

* Wed Jan 29 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.0.0-alt2
- initscripts fixed a bit

* Sat Sep 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.0.0-alt1
- 1.0.0

* Mon Jul 22 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.5.0-alt1
- first build for ALT Linux distribution
