# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%add_verify_elf_skiplist %python3_sitelibdir/gns3server/compute/docker/resources/bin/busybox
%add_findreq_skiplist %python3_sitelibdir/gns3server/compute/docker/*

Name: gns3-server
Version: 2.2.11
Release: alt1

Summary: GNS3 server manages emulators such as Dynamips, VirtualBox or Qemu/KVM
License: GPLv3
Group: File tools
Url: https://github.com/GNS3/gns3-server

Buildarch: noarch

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: python3-devel python3-module-setuptools
BuildRequires(pre): rpm-build-python3 rpm-build-gir
Requires: cpulimit
Requires: dynamips >= 0.2.11
Requires: python3-module-yarl >= 1.3
Requires: python3-module-aiohttp >= 3.5.0
Requires: python3-module-aiohttp-cors >= 0.7.0
Requires: python3-module-jinja2 >= 2.7.3 
Requires: python3-module-aiohttp >= 3.5.4
Requires: python3-module-aiofiles >= 0.4.0
Requires: python3-module-async_generator >= 1.10
Requires: python3-module-async-timeout >= 3.0.1
Requires: python3-module-jsonschema >= 2.6.0
Requires: python3-module-raven >= 5.23.0
Requires: python3-module-psutil >= 5.6.6
Requires: iouyap
Requires: ubridge
Requires: vpcs
Conflicts: gns3 < 1.0.0

%description
The GNS3 server manages emulators such as Dynamips, VirtualBox or Qemu/KVM.
Clients like the GNS3 GUI controls the server using a HTTP REST API.

%prep
%setup
echo '' > requirements.txt

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS LICENSE README.rst
%_bindir/*
%python3_sitelibdir/gns3server
%python3_sitelibdir/gns3_server-*.egg-info
%exclude %python3_sitelibdir/tests/controller

%changelog
* Fri Jul 10 2020 Anton Midyukov <antohami@altlinux.org> 2.2.11-alt1
- new version 2.2.11

* Thu Jun 04 2020 Anton Midyukov <antohami@altlinux.org> 2.2.9-alt1
- new version 2.2.9

* Sun May 10 2020 Anton Midyukov <antohami@altlinux.org> 2.2.8-alt1
- new version 2.2.8

* Sun Apr 12 2020 Anton Midyukov <antohami@altlinux.org> 2.2.7-alt1
- new version 2.2.7

* Tue Jan 14 2020 Anton Midyukov <antohami@altlinux.org> 2.2.5-alt1
- new version 2.2.5

* Fri Nov 08 2019 Anton Midyukov <antohami@altlinux.org> 2.2.2-alt1
- new version 2.2.2

* Thu Oct 03 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt5
- New release 2.2.0

* Tue Sep 03 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt4.rc4
- New release candidate 2.2.0rc4

* Wed Jul 31 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt3.b4
- New beta release 2.2.0b4

* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt2.b2
- New beta release 2.2.0b2

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt1.a4
- New alpha release 2.2.0a4

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 2.1.12-alt1.1
- Update Requires

* Mon Feb 25 2019 Anton Midyukov <antohami@altlinux.org> 2.1.12-alt1
- new version 2.1.12

* Tue Jan 29 2019 Anton Midyukov <antohami@altlinux.org> 2.1.11-alt2
- drop requires python3(typing), not needed for python3 >= 3.5

* Wed Oct 17 2018 Anton Midyukov <antohami@altlinux.org> 2.1.11-alt1
- new version 2.1.11

* Sun May 13 2018 Anton Midyukov <antohami@altlinux.org> 2.1.5-alt1
- new version 2.1.5

* Mon Mar 26 2018 Anton Midyukov <antohami@altlinux.org> 2.1.4-alt1
- new version 2.1.4
- disable requires qemu and wireshark

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 24 2018 Anton Midyukov <antohami@altlinux.org> 2.1.3-alt1
- new version 2.1.3

* Sat Nov 18 2017 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- new version 2.1.0

* Tue May 23 2017 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Mon May 08 2017 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0

* Tue Aug 30 2016 Anton Midyukov <antohami@altlinux.org> 1.5.2-alt1
- New version 1.5.2

* Thu Aug 04 2016 Anton Midyukov <antohami@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux Sisyphus.
