%define module_name	virtualbox-addition
%define module_version  6.1.8
%define module_release	alt1

%define flavour		un-def
%define karch x86_64 %ix86
BuildRequires(pre): rpm-build-kernel >= 0.100-alt1
BuildRequires(pre): kernel-headers-modules-un-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

%define guest_module_name	vboxguest
%define vfs_module_name		vboxsf
%define video_module_name	vboxvideo

Summary: VirtualBox modules
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
Url: http://www.virtualbox.org/

Patch0: vboxcommon-5.4.patch

BuildPreReq: gcc-c++
BuildRequires: perl
BuildRequires: rpm >= 4.0.2-75
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%guest_module_name = %module_version
BuildRequires: kernel-source-%vfs_module_name = %module_version
BuildRequires: kernel-source-%video_module_name = %module_version

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Provides: kernel-modules-%vfs_module_name-%kversion-%flavour-%krelease = %version-%release
Provides: kernel-modules-%vfs_module_name-%flavour = %version-%release
Obsoletes: kernel-modules-%vfs_module_name-%flavour < %version-%release

# Don't use requires_kimage macros due it clean from requires
Requires: %kimage
ExclusiveArch: %karch

Requires: virtualbox-guest-common = %module_version
Requires: kernel-modules-%module_name-video-%flavour = %version-%release
Requires: kernel-modules-%module_name-guest-%flavour = %version-%release

%description
This package contains VirtualBox addition modules (vboxguest, vboxsf)
that are needed for additonal guests support for VirtualBox.


%package -n kernel-modules-%module_name-video-%flavour
Summary: VirtualBox video modules
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
%requires_kimage
License: GPLv2
Group: System/Kernel and hardware

Provides: kernel-modules-%module_name-video-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-video-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-video-%kversion-%flavour-%krelease > %version-%release

Provides: kernel-modules-%video_module_name-%kversion-%flavour-%krelease = %version-%release
Provides: kernel-modules-%video_module_name-%flavour = %version-%release

Requires: virtualbox-guest-common-vboxvideo = %module_version

%description -n kernel-modules-%module_name-video-%flavour
This package contains VirtualBox addition vboxvideo module
that are needed for additonal guests support for VirtualBox.
You can also use vboxvideo module from staging subpackage of
your kernel.


%package -n kernel-modules-%module_name-guest-%flavour
Summary: VirtualBox guest modules
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
%requires_kimage
License: GPLv2
Group: System/Kernel and hardware

Provides: kernel-modules-%module_name-guest-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-guest-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-guest-%kversion-%flavour-%krelease > %version-%release

Provides: kernel-modules-%guest_module_name-%kversion-%flavour-%krelease = %version-%release
Provides: kernel-modules-%guest_module_name-%flavour = %version-%release

Requires: virtualbox-guest-common-vboxguest = %module_version

%description -n kernel-modules-%module_name-guest-%flavour
This package contains VirtualBox addition vboxvideo module
that are needed for additonal guests support for VirtualBox.
You can also use vboxvideo module from staging subpackage of
your kernel.


%prep
%setup -T -c -n kernel-source-%module_name-%module_version
tar jxvf %kernel_src/kernel-source-%guest_module_name-%module_version.tar.bz2
pushd kernel-source-%guest_module_name-%module_version
%patch0 -p1
popd
tar jxvf %kernel_src/kernel-source-%vfs_module_name-%module_version.tar.bz2
pushd kernel-source-%vfs_module_name-%module_version
%patch0 -p1
popd
tar jxvf %kernel_src/kernel-source-%video_module_name-%module_version.tar.bz2

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
%make -C kernel-source-%guest_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/ KERN_VER=%kversion
%make -C kernel-source-%vfs_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/ KERN_VER=%kversion \
    KBUILD_EXTRA_SYMBOLS=%_builddir/kernel-source-%module_name-%module_version/kernel-source-%guest_module_name-%module_version/Module.symvers
%make -C kernel-source-%video_module_name-%module_version \
    KERN_DIR=%_usrsrc/linux-%kversion-%flavour/ KERN_VER=%kversion

%install
mkdir -p %buildroot/%module_dir
install -pD -m644 kernel-source-%guest_module_name-%module_version/vboxguest.ko \
    %buildroot%module_dir/vboxguestvbox.ko
install -pD -m644 kernel-source-%vfs_module_name-%module_version/vboxsf.ko \
    %buildroot%module_dir/
install -pD -m644 kernel-source-%video_module_name-%module_version/vboxvideo.ko \
    %buildroot%module_dir/vboxvideovbox.ko

%files
%defattr(644,root,root,755)
%module_dir
%exclude %module_dir/vboxvideovbox.ko
%exclude %module_dir/vboxguestvbox.ko

%files -n kernel-modules-%module_name-guest-%flavour
%module_dir/vboxguestvbox.ko

%files -n kernel-modules-%module_name-video-%flavour
%module_dir/vboxvideovbox.ko

%changelog
* %(LC_TIME=C date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Thu May 21 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.8-alt1
- Updated template for virtualbox 6.1.8

* Wed Apr 15 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.6-alt1
- Updated template for virtualbox 6.1.6

* Sat Mar 14 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt7
- Fix provides and conflicts for vboxvideo and vboxguest

* Tue Mar 04 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt6
- Add separated modprobe and load module rules for vboxvideo and vboxguest

* Tue Mar 04 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt5
- Revert separated modules for compatibility with update-kernel:
 + kernel-modules-virtualbox-addtition-video-FLAVOUR
 + kernel-modules-virtualbox-addtition-guest-FLAVOUR

* Tue Mar 04 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt4
- Fix obsoletes own provides without version

* Tue Mar 04 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt3
- Added provides for obsoletes separated packages:
 + kernel-modules-virtualbox-addtition-video-FLAVOUR
 + kernel-modules-virtualbox-addtition-guest-FLAVOUR

* Tue Feb 25 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt2
- Fixed build with kernel-5.5 using KBUILD_EXTRA_SYMBOLS environment variable
  instead of copy Module.symvers into dependend modules source directory.

* Thu Feb 20 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt1
- Updated template for virtualbox 6.1.4

* Wed Feb 05 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.2-alt2
- Rebuild with i586 support

* Wed Jan 22 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.2-alt1
- Updated template for virtualbox 6.1.2

* Fri Dec 27 2019 Valery Sinelnikov <greh@altlinux.org> 6.1.0-alt2
- Fixed build with un-def kernel-5.4 for virtualbox 6.1.0

* Fri Dec 20 2019 Valery Sinelnikov <greh@altlinux.org> 6.1.0-alt1
- Updated template for virtualbox 6.1.0

* Thu Dec 12 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.34-alt4
- Fixed build with un-def kernel-5.4
- Set license to GPLv2 instead of GPL with unknown version

* Wed Dec 04 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.34-alt3
- Fix dependency to virtualbox-guest-common package for modules configuration

* Tue Dec 03 2019 Valery Sinelnikov <greh@altlinux.org> 5.2.34-alt2
- Merge separated packages with conflicts modules
- Rename conflicts modules with suffix 'vbox'
- Place common install and blacklist rules to virtualbox-guest-utils package

* Mon Oct 21 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.34-alt1
- Updated template for virtualbox 5.2.34

* Tue Jun 09 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.30-alt1
- Updated template for virtualbox 5.2.30

* Thu Apr 04 2019 Ivan Zakharyaschev <imz@altlinux.org> 5.2.26-alt5
- (.spec) %%requires_kimage used
- checkinstall pkgs added to check that update-kernel sees our modules pkgs

* Fri Mar 29 2019 Anton V. Boyarshinov <boyarsh@altinux.org> 5.2.26-alt3
- No more outdated vboxvideo for kernels >= 5.0

* Fri Feb 08 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.26-alt1
- Updated template for virtualbox 5.2.26

* Wed Jan 16 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.24-alt1
- Updated template for virtualbox 5.2.24

* Fri Nov 30 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.22-alt1
- Updated template for virtualbox 5.2.22

* Fri Oct 19 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.20-alt1
- Updated template for virtualbox 5.2.20

* Mon Oct 15 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.18-alt1
- Updated template for virtualbox 5.2.18

* Thu Jul 20 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.16-alt1
- Updated template for virtualbox 5.2.16

* Tue Dec 26 2017 Denis Medvedev <nbr@altlinux.org> 5.1.30-alt2
- Fixed build for un-def

* Tue Nov 14 2017 Denis Medvedev <nbr@altlinux.org> 5.1.30-alt1
- Updated template for virtualbox 5.1.30

* Thu Jul 20 2017 Denis Medvedev <nbr@altlinux.org> 5.1.24-alt1
- Updated template for virtualbox 5.1.24

* Thu Mar 16 2017 Denis Medvedev <nbr@altlinux.org> 5.1.18-alt1
- Updated template for virtualbox 5.1.18

* Thu Mar 16 2017 Denis Medvedev <nbr@altlinux.org> 5.1.16-alt1
- Updated template for virtualbox 5.1.16

* Wed Jan 25 2017 Denis Medvedev <nbr@altlinux.org> 5.1.14-alt1
- Updated template for virtualbox 5.1.14

* Tue Nov 22 2016 Denis Medvedev <nbr@altlinux.org> 5.1.10-alt1
- Updated template for virtualbox 5.1.10

* Fri Oct 14 2016 Evgeny Sinelnikov <sin@altlinux.ru> 5.1.6-alt2
- Copy Module.symvers during video module building

* Thu Jul 28 2016 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.1.2-alt1
- Updated template for virtualbox 5.1.2

* Wed May 11 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.0.20-alt1
- Updated template for virtualbox 5.0.20.

* Wed Mar 16 2016 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.14-alt1
- new version

* Tue Oct  6 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.3.30-alt2
- build with kernel 4.2 fixed

* Mon Aug 31 2015 Aleksey Avdeev <solo@altlinux.org> 4.3.30-alt1
- Update template for virtualbox 4.3.30.

* Thu Jan 29 2015 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.20-alt1
- Update template for virtualbox 4.3.20

* Wed Sep 03 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.3.14-alt1
- Update template for virtualbox 4.3.14.

* Tue Mar 19 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.10-alt1
- Update to last stable version
- Support specsubst for kflavour

* Mon Dec 17 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.2.4-alt2
- new template

* Tue Nov 27 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.2.4-alt1
- 4.2.4

* Wed Aug 29 2012 Anton Protopopov <aspsk@altlinux.org> 4.1.20-alt2
- technical

* Wed Aug 22 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.20-alt1
- Update to new release

* Sun Jul 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.18-alt1
- 4.1.18

* Sun Apr 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.12-alt4
- 4.1.12

* Mon Mar 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.6-alt4
- fix to build with 3.3 kernel

* Sat Jan 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.6-alt3
- fix to build with 3.2 kernel

* Mon Dec 12 2011 Anton Protopopov <aspsk@altlinux.org> 4.1.6-alt2
- Fix build with latest el-smp

* Fri Dec 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.6-alt1
- Update to new release

* Tue Nov 01 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.4-alt1
- Update to new release

* Wed Sep 21 2011 Anton Protopopov <aspsk@altlinux.org> 4.0.12-alt2
- Technical

* Mon Jul 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.12-alt1
- 4.0.12

* Sun Feb 20 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt1
- Update to new release

* Thu Jan 06 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.12-alt1
- Update to new release

* Thu Jun 10 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.4-alt1
- Update to new release

* Tue May 11 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.8-alt1
- Update to new release

* Sun Apr 04 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.6-alt1
- Update to new release

* Thu Mar 11 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.4-alt1
- Update to new release

* Tue Nov 03 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.10-alt1
- Update to new release

* Wed Oct 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.8-alt1
- Update to new release

* Sun Sep 20 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.6-alt1
- Update to new release

* Tue Aug 11 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.4-alt1
- Update to new release

* Thu Jul 23 2009 Anton Protopopov <aspsk@altlinux.org> 3.0.2-alt2
- Merge with sin@ to enforce inheritance

* Mon Jul 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.2-alt1
- Update to new release

* Sun Jul 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt2
- Merge vboxvfs module into common virtualbox-addition
- Built new video module

* Wed Jul 08 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt1
- Update to new release

* Sun Jun 14 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.4-alt1
- Update to new release

* Tue May 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.2-alt1
- Update to new release

* Wed Feb 25 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt1
- Update to new release

* Fri Dec 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt1
- Update to new release

* Sat Nov 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.0.4-alt1
- Update to new release

* Thu Sep 04 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.6-alt1
- Update to last release

* Sun Aug 31 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.4-alt1
- Update to last release

* Sun Jun 08 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.2-alt1
- Update to last release

* Fri Mar 28 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt1
- Initial virtualbox addition modules build

