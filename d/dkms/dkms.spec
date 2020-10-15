# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

# Based on dkms.spec from the source.

Summary: Dynamic Kernel Module Support Framework
Name: dkms
Version: 2.8.3
Release: alt4
License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/dell/dkms
Vcs: https://github.com/dell/dkms.git
# PR: https://www.dell.com/downloads/global/power/1q04-ler.pdf

BuildArch: noarch
Source0: %name-%version.tar
BuildRequires(pre): lsb-release

%filter_from_requires /\(debconf\|python\|dpkg\|lsb\|systemd\|module-init-tools\|\/etc\/sysconfig\/kernel\)/d

%description
The framework for the Dynamic Kernel Module Support (DKMS) method
for installing module RPMS as originally developed by Dell.

%package checkinstall
Summary: Checkinstall for dkms
Group: Development/Other
BuildArch: noarch
Requires(pre): %name = %EVR
Requires: /proc
Requires: kernel > 5.7
Requires: kernel-headers-modules-un-def
Requires: rpm-build

%description checkinstall
Run checkinstall tests for dkms.

%prep
%setup

%build
echo "enable dkms.service" > dkms.preset

# Turn prerm into postrm, disabling call to depmod.
sed 's/dkms remove/& --no-depmod/' kernel_prerm.d_dkms > kernel_postrm.d_dkms

%install
# Install both service types.
make install-redhat-systemd \
     install-redhat-sysv \
    DESTDIR=%buildroot \
    BASHDIR=%buildroot%_sysconfdir/bash_completion.d \
        ETC=%buildroot%_sysconfdir/dkms \
     LIBDIR=%buildroot%_libexecdir/dkms \
        MAN=%buildroot%_man8dir \
       SBIN=%buildroot%_sbindir \
    SYSTEMD=%buildroot%_unitdir \
        VAR=%buildroot%_localstatedir/dkms \

# Install triggers.
rm -rf %buildroot%_sysconfdir/kernel
install -p -m755 kernel_postrm.d_dkms   %buildroot%_libexecdir/dkms/postrm
install -p -m755 kernel_postinst.d_dkms %buildroot%_libexecdir/dkms/postinst
# '9' to make it run before boot_kernel.filetrigger for prerm
install -p -m755 -D .gear/dkms.filetrigger %buildroot%_rpmlibdir/9dkms.filetrigger

# Do not support building RPMs.
rm %buildroot%_sysconfdir/dkms/template-*.spec

# Bundled (in 2009) lsb_release is too old for ALT.
install -p /usr/bin/lsb_release %buildroot%prefix/lib/dkms/

# Rename sysv service name for consistency, otherwise post_service,
# and preun_service will not work properly.
mv %buildroot%_initdir/dkms_autoinstaller %buildroot%_initdir/dkms

install -D -p -m644 dkms.preset %buildroot%_presetdir/30-dkms.preset

%post
%post_service dkms

%preun
%preun_service dkms

%pre checkinstall
set -e
PS4=$'\n+ '
khdr=$(rpm -q kernel-headers-modules-un-def | sort -V | tail -1)
khdr=${khdr#kernel-headers-modules-}
khdr=${khdr%%.*}
krel=${khdr##*-}
kver=${khdr%%-*}
kver=${kver##*-}
kflv=${khdr%%-*-*}
kver=$kver-$kflv-$krel

set -x
dkms add %_defaultdocdir/%name-%version/test/dkms_test-1.0/dkms.conf
    dkms status | grep added || exit 1
dkms build	 --verbose --kernelver=$kver dkms_test/1.0
    dkms status | grep built || exit 1
dkms install	 --verbose --kernelver=$kver dkms_test/1.0
    dkms status | grep installed || exit 1
    modinfo /lib/modules/$kver/kernel/extra/dkms_test.ko*
dkms uninstall	 --verbose --kernelver=$kver dkms_test/1.0
    ! test -e /lib/modules/$kver/kernel/extra/dkms_test.ko*
dkms unbuild	 --verbose --kernelver=$kver dkms_test/1.0

dkms autoinstall --verbose --kernelver=$kver dkms_test/1.0
    modinfo /lib/modules/$kver/kernel/extra/dkms_test.ko*
dkms remove	 --verbose --kernelver=$kver dkms_test/1.0
   dkms status | grep . && exit 1
   ! test -e /lib/modules/$kver/kernel/extra/dkms_test.ko*

rm -rf /usr/src/dkms_test-1.0

%files
%doc AUTHORS COPYING README.md test
%config(noreplace) %_sysconfdir/dkms
%_sbindir/dkms
%_initdir/dkms
%_unitdir/dkms.service
%_presetdir/*dkms.preset
%_libexecdir/dkms
%_rpmlibdir/*dkms.filetrigger
%_localstatedir/dkms
%_man8dir/dkms.8*
%_sysconfdir/bash_completion.d/dkms

%files checkinstall

%changelog
* Fri Oct 09 2020 Vitaly Chikunov <vt@altlinux.org> 2.8.3-alt4
- Optimize dkms.filetrigger un/install logic.

* Fri Oct 09 2020 Vitaly Chikunov <vt@altlinux.org> 2.8.3-alt3
- Make checkinstall work outside of hasher.
- Optimize dkms.filetrigger.

* Tue Sep 29 2020 Vitaly Chikunov <vt@altlinux.org> 2.8.3-alt2
- spec: Remove dependence on /etc/sysconfig/kernel.

* Wed Sep 02 2020 Vitaly Chikunov <vt@altlinux.org> 2.8.3-alt1
- First import to ALT.
