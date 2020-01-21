Name: altsp-test-scripts
Version: 1.1
Release: alt4

Summary: Test scripts for SPT7 distro
License: GPL
Group: System/Configuration/Other
Source: %name-%version.tar
Provides: spt7-test-scripts
Obsoletes: spt7-test-scripts

%description
Test scripts for SPT7 distro

%prep
%setup

%build
make -C src test_access
make -C src test_clearmem

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libexecdir/%name/
install -pm755 scripts/* %buildroot%_bindir/
install -pm755 src/test_access %buildroot%_bindir/
install -pm755 src/test_clearmem %buildroot%_bindir/
cp -a setup-tests/ %buildroot%_libexecdir/%name/
cp -a tests/ %buildroot%_libexecdir/%name/
mkdir -p %buildroot/etc/sysconfig
cp sysconfig-s_rm %buildroot/etc/sysconfig/s_rm

%files
%_bindir/*
%_libexecdir/%name/
/etc/sysconfig/*

%changelog
* Mon Jul 29 2019 Denis Medvedev <nbr@altlinux.org> 1.1-alt4
- tests moved to /opt

* Fri Jul 26 2019 Denis Medvedev <nbr@altlinux.org> 1.1-alt3
- s_rm calls s_fill now to prevent remans of dirs in inodes.

* Thu Jun 20 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.1-alt2
- -r option added to s_rm

* Wed May 22 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.1-alt1
- s_rm and s_fill packaged

* Wed May 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0-alt1
- package rename

* Fri Dec 23 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.4-alt1
- test_clearmem programm added

* Thu Apr 02 2015 Mikhail Efremov <sem@altlinux.org> 1.3-alt1
- Fix p4_6_2_3 test (by azol@).

* Fri Mar 20 2015 Mikhail Efremov <sem@altlinux.org> 1.2-alt1
- Add tests.

* Fri Feb 27 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt1
- test_access programm added

* Tue Feb 24 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt1
- first build

