%add_python3_path /usr/share/lirc/python-pkg/
Name: lirc
Version: 0.10.1
Release: alt3

Summary: The Linux Infrared Remote Control package
License: GPL-2.0-or-later and MIT
Group: System/Base
Url: http://www.lirc.org

Source: %name-%version.tar
Source1: lircd
Source2: lircd.sysconfig
Source3: lircd.service
Source4: liblircclient0.pc
Source5: confs_by_driver.yaml

Patch1: lirc-0.10.1-disable-getconfig.patch
Patch2: lirc-0.10.1-alt-sysmacros.patch

Obsoletes: %name-remotes

BuildRequires: libX11-devel libalsa-devel python3-dev xsltproc gcc-c++
BuildRequires: python3-module-setuptools libsystemd-devel libportaudio2-devel
BuildRequires: python3-module-yaml
BuildRequires(pre): rpm-build-python3

Requires: liblirc = %version-%release

%description
LIRC is a package that allows you to decode and send infra-red signals
of many (but not all) commonly used remote controls.

%package -n liblirc
Summary: Client library for LIRC
Group: System/Libraries

%description -n liblirc
Libraries needed by programs, which uses LIRC

%package -n liblirc-devel
Summary: Development for LIRC
Group: Development/C
Requires: lib%name = %version-%release

%description -n liblirc-devel
Development library for LIRC

%package config
Summary: LIRC Configuration Tools and Data
Requires: lirc = %version-%release
Group: System/Base
Requires: python3-module-pygobject3-pygtkcompat
Requires: python3-module-yaml

%description config
The LIRC config package contains tools and data  to ease the
LIRC configuration process.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%add_optflags -I%_includedir/libftdi
cp %SOURCE5 configs/
%autoreconf
%configure  --disable-static --localstatedir=%_var \
	    --with-x --with-syslog --with-driver=userspace \
	    --enable-uinput --enable-devinput \
	    --with-port=0x3f8 --with-irq=4
make

%install
%makeinstall_std varrundir=%buildroot/%_runtimedir docdir=%_defaultdocdir/%name-%version
install -pm755 -D %SOURCE1 %buildroot%_initdir/lircd
install -pm644 -D %SOURCE2 %buildroot%_sysconfdir/sysconfig/lircd
install -pm644 -D %SOURCE4 %buildroot%_datadir/pkgconfig/liblircclient0.pc
mkdir -p %buildroot/%_runtimedir/lirc %buildroot%_tmpfilesdir
echo 'd /run/lirc 0755 root root' > %buildroot%_tmpfilesdir/lirc.conf
# relocate to docdir to avoid python deps
rm -f %buildroot%_bindir/pronto2lirc
rm -rf %buildroot%_datadir/lirc/contrib
mv %buildroot/%_libdir/pkgconfig/* %buildroot%_datadir/pkgconfig/
sed -i -e '/^plugindir/s|%buildroot||' %buildroot%_sysconfdir/lirc/lirc_options.conf
ln -sf `readlink %buildroot%_bindir/lirc-setup|sed 's,3\..,3,'` %buildroot%_bindir/lirc-setup
mkdir -p %buildroot%python3_sitelibdir/lirc
cp %buildroot%_datadir/lirc/python-pkg/config.py %buildroot%python3_sitelibdir/lirc



%triggerun -- lirc < 0.9.2
if [ $2 -gt 0 ] && [ $1 -gt 0 ] && [ -f /etc/lircd.conf ]; then
# This is upgrade.
	echo "Warning: configuration files from /etc/lirc.conf moved to /etc/lirc/lircd.conf.d/lircd-saved.conf"
	mkdir -p %_sysconfdir/lirc/lirc.conf.d >dev/null 2>&1 ||:
	mv /etc/lircd.conf /etc/lirc/lircd.conf.d/lircd-saved.conf ||:
	%post_service lircd
fi


%pre
/usr/sbin/groupadd -r -f %name &> /dev/null ||:

%post
%post_service lircd

%preun
%preun_service lircd

%files
%doc NEWS doc/irxevent.keys doc/html configs contrib
%config(noreplace) %_sysconfdir/sysconfig/lircd
%config(noreplace) %_sysconfdir/lirc/*
%dir %_sysconfdir/lirc
%systemd_unitdir/*.service
%systemd_unitdir/*.socket
%_initdir/*
%_bindir/*
%exclude %_bindir/irdb-get
%exclude %_bindir/lirc-config-tool
%exclude %_bindir/lirc-setup
%attr(2711,root,%name) %_sbindir/lircd
%_sbindir/lircmd
%_sbindir/lircd-uinput
%_sbindir/lirc-lsplugins
%_man1dir/*.1*
%exclude %_mandir/man1/irdb-get*
%exclude %_mandir/man1/lirc-config-tool*
%exclude %_mandir/man1/lirc-setup*
%_man5dir/*.5*
%_man8dir/*.8*
%_tmpfilesdir/lirc.conf
%_runtimedir/lirc

%files -n liblirc
%_libdir/liblirc_client.so.*
%_libdir/liblirc.so.*
%_libdir/libirrecord.so.*
%_libdir/liblirc_driver.so.*
%_libdir/lirc

%files -n liblirc-devel
%_libdir/*.so
%_includedir/*
%_datadir/pkgconfig/*

%files config
%_bindir/irdb-get
%_bindir/lirc-config-tool
%_bindir/lirc-setup
%_sbindir/lircd-setup
%_mandir/man1/irdb-get*
%_mandir/man1/lirc-config-tool*
%_mandir/man1/lirc-setup*
%_datadir/lirc/configs
%_datadir/lirc/lirc.hwdb
%_datadir/lirc/python-pkg
%python3_sitelibdir/lirc
%python3_sitelibdir/lirc-setup

%changelog
* Sun Mar 08 2020 Dmitry V. Levin <ldv@altlinux.org> 0.10.1-alt3
- Fixed FTBFS.

* Fri Apr 12 2019 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt2
- Adapted for python3.7.

* Mon Nov 19 2018 Anton Farygin <rider@altlinux.ru> 0.10.1-alt1
- 0.10.1
- enabled systemd support
- enabled portaudio
- enabled uinput and devinput
- disabled libusb and libftdi (closes: #32774)

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 0.10.0-alt1
- new version

* Thu May 11 2017 Anton Farygin <rider@altlinux.ru> 0.9.4d-alt1
- new version

* Thu Apr 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.9.3a-alt1.3
- build with libftdi1

* Wed May 11 2016 Michael Shigorin <mike@altlinux.org> 0.9.3a-alt1.2
- NMU: lirc(4) manpage dropped due to conflict with man-pages-4.06-alt1

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.3a-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.3a-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Oct 19 2015 Anton Farygin <rider@altlinux.ru> 0.9.3a-alt1
- new version

* Mon Feb 09 2015 Anton Farygin <rider@altlinux.ru> 0.9.2a-alt1
- new version

* Sun Mar 24 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt3
- systemd service file added for lircd

* Sat Mar 23 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt2
- tmpfiles.d entry added (closes: #28208)
- do not package ancient utilities, reducing dependencies

* Wed Jan 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1.2
- NMU: lirc database of remotes packaged as lirc-remotes subpackage

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.1
- Rebuild with Python-2.7

* Sat Oct 01 2011 Anton Farygin <rider@altlinux.ru> 0.9.0-alt1
- new version

* Tue Jul 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.7-alt2
- pkg-config from debain added

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.7-alt1.qa2
- Rebuilt for debuginfo
- Added svgalib-devel into BuildPreReq
- Fixed checking of ftdi.h

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.8.7-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Wed Sep 08 2010 Anton Farygin <rider@altlinux.ru> 0.8.7-alt1
- new version

* Mon Apr 12 2010 Anton Farygin <rider@altlinux.ru> 0.8.6-alt5
- Added driver for wb677 (Asrock ION330HT) receiver

* Thu Jan 14 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.6-alt4.2
- patched for 2.6.32 kernel compatibility

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt4.1
- Rebuilt with python 2.6

* Wed Sep 16 2009 Anton Farygin <rider@altlinux.ru> 0.8.6-alt4
- removed modutils and hal requires
- fixed hal fdi (altbug #21732)

* Wed Sep 16 2009 Anton Farygin <rider@altlinux.ru> 0.8.6-alt3
- fixed location of lirc daemon
- use /dev/lirc0 as default lirc device

* Wed Sep 16 2009 Anton Farygin <rider@altlinux.ru> 0.8.6-alt2
- added %_runtimedir/%name

* Tue Sep 15 2009 Anton Farygin <rider@altlinux.ru> 0.8.6-alt1
- new version
- added mode2 to lirc package
- add patches from RH for standardized remote keycodes

* Sun Jun 21 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.5-alt1
- new version.
- add requires to hal (as provides .fdi).

* Sat Dec 27 2008 L.A. Kostis <lakostis@altlinux.ru> 0.8.4-alt1.a
- New version.
- .spec cleanup.
- remove obsoleted patches.

* Thu Mar 13 2008 L.A. Kostis <lakostis@altlinux.ru> 0.8.3-alt1.cvs20080313
- 2008-03-13 CVS snapshot.
- remove commandir driver (already included).
- fix init script priority (start lircd before dm).

* Sun Nov 04 2007 L.A. Kostis <lakostis@altlinux.ru> 0.8.2-alt1
- 0.8.2.
- update commandir driver to 1.4.4 version.

* Sat May 19 2007 L.A. Kostis <lakostis@altlinux.ru> 0.8.1-alt2
- fix bogus font in xmode2 (ALT #9149).

* Sat Feb 17 2007 L.A. Kostis <lakostis@altlinux.ru> 0.8.1-alt1
- 0.8.1 version.
- remove obsoleted patches.
- update commandir driver to 1.4.2 version.
- update -alt-config patch.

* Wed May 10 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt4
- Some init.d script improvements (see #9454).

* Tue May 09 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt3.1
- Fixed typo in post (see #9534).

* Sat Apr 29 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt3
- Added sources:
  + commandir-1.4.1 - CommandIR Mini hardware driver.
- Added patches:
  + lirc-0.8.0-2-cmdir.patch - update cmdir patch from vendor.
  + commandir-1.4.1-cleanup.patch - update commandir kernel driver
    for 2.6.16+ kernel.
- Add post/preun service.

* Mon Apr 03 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt2
- Added patches:
  + lirc-drivers-cvs-update.patch - sync drivers changes
    for 2.6.16+ kernels.

* Tue Feb 14 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt1
- new version 0.8.0.
- update Makefile for kernel modules.

* Fri Jan 20 2006 LAKostis <lakostis at altlinux.ru> 0.8.0-alt1.pre4
- 0.8.0pre4.
- spec cleanup.
- update buildreq.
- disable static builds by default.

* Thu Nov 27 2003 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt4
- removed .la file

* Fri Oct 17 2003 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt3
- fix in start up script (--lock-file option replace with --lockfile, #3177)

* Tue Sep 23 2003 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt2
- kernel source makefile fix

* Fri Sep 19 2003 Kachalov Anton <mouse@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (from CVS)
- building kernel-source package

* Tue Oct 29 2002 Kachalov Anton <mouse@altlinux.ru> 0.6.6-alt1
- new version 0.6.6

* Mon Oct 28 2002 Kachalov Anton <mouse@altlinux.ru> 0.6.5-alt2
- remove smode2 from the package

* Tue Feb 26 2002 Kachalov Anton <mouse@altlinux.ru> alt1
- new version (0.6.5) build

* Mon Jan 21 2002 Kachalov Anton <mouse@altlinux.ru> alt3
- syncing with new dev package

* Fri Jan 11 2002 Kachalov Anton <mouse@altlinux.ru> alt2
- added group lirc
- configure with --localstatedir=/var
- startup script fix

* Wed Jan 09 2002 Kachalov Anton <mouse@altlinux.ru> alt1
- build for Sisyphus
