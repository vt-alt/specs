%define module_name rtl8723de
%define module_version 5.1.1.8

%define module_source %module_name.tar

Name: kernel-source-%module_name-4.11up
Version: %module_version
Release: alt6

Group: Development/Kernel
Summary: Linux %module_name modules sources
License: GPL
URL: https://github.com/smlinux/rtl8723de
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

BuildArch: noarch
Conflicts: kernel-source-%module_name

Source: %name-%version.tar
Patch1: alt-build-time.patch

BuildRequires: kernel-build-tools

%description
%module_name modules sources for RTL8723DE Linux kernel driver

%prep
%setup -c -q
pushd %name-%version
%patch1 -p1
popd

%install
mkdir -p %kernel_srcdir
mv %name-%version kernel-source-%module_name-%version
tar -cjf %kernel_srcdir/kernel-source-%module_name-%version.tar.bz2 kernel-source-%module_name-%version

%files
%_usrsrc/*

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 5.1.1.8-alt6
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 5.1.1.8-alt5
- NMU: remove %ubt from release

* Tue Sep 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt4%ubt
- initial build
