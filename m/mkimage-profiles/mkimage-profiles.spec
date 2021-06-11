Name: mkimage-profiles
Version: 1.4.13
Release: alt1

Summary: ALT based distribution metaprofile
License: GPLv2+
Group: Development/Other

Url: http://altlinux.org/m-p
Source: %name-%version.tar
Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch
BuildRequires: rsync

Requires: rsync git-core
Requires: time schedutils sfdisk
Requires: mkimage >= 0.2.5
Requires: mkimage-preinstall

# Recommends: graphviz qemu-img

%define mpdir %_datadir/%name
%add_findreq_skiplist %mpdir/*.in/*

%def_with doc
%define docs $HOME/docs

Summary(ru_RU.UTF-8): метапрофиль дистрибутивов на базе Альт

%description
mkimage-profiles is a collection of bits and pieces useful for
distributions construction: it contains package lists, features,
and whole subprofiles (like "rescue" building block) for you
to choose from, and some ready-made image recipes as well.

Make no mistake: constructing distributions isn't just fun, it takes
a lot of passion and knowledge to produce a non-trivial one.  So m-p
(the short alias for mkimage-profiles) is complex too.  If you need
-- or want -- to make a few tweaks to an existing recipe, it might
be easier to comprehend the generated profile (aka builddir) which
contains only the needed subprofiles, script hooks and package lists
and is way more compact.

The main deliverable form for x86 is a (hybrid) ISO; virtual environment
template caches (OpenVZ/LXC) can be made either as well as VM disk images.

In short, setup hasher (http://en.altlinux.org/hasher) and here we go:
  cd %mpdir
  head README
  make syslinux.iso

But if you're into regular distro hacking and are not afraid of make
and modest metaprogramming (some code generation and introspection),
welcome to the metaprofile itself; read the docs and get the git:
%url (NB: these are mostly in Russian with translation on demand).

%description -l ru_RU.UTF-8
mkimage-profiles является собранием всего необходимого для
построения дистрибутивов и содержит списки пакетов, особенности
и целые субпрофили (вроде "кирпичика" rescue), из которых можно
выбирать требуемое; также включены и описания готовых образов.

Поймите правильно: создание дистрибутивов является занятием
не только интересным, но и требующим вдохновения и знаний
для получения нетривиального результата.  Если хочется или же
необходимо чуток поправить уже существующий "рецепт", может
быть проще разобраться в сгенерированном профиле (builddir),
который содержит только необходимые субпрофили, скрипты
и списки пакетов, являясь намного более компактным.

Основной формой результата на x86 является (гибридный) ISO-образ;
также возможно создавать шаблоны контейнеров OpenVZ/LXC и образы
дисков виртуальных машин.

Короче говоря, настройте hasher (http://altlinux.org/hasher) и:
  cd %mpdir
  head README
  make syslinux.iso

Но если разработка дистрибутивов становится обыденным делом
и не страшитесь make и чуточки метапрограммирования (немного
генерирования кода и интроспекции), добро пожаловать в сам
метапрофиль; гляньте документацию и забирайте git:
%url

%package doc
Summary: %name documentation
Group: Development/Documentation
%{?_with_doc:BuildRequires: java /proc}
%{?_with_doc:BuildRequires: asciidoc-a2x fop fonts-ttf-dejavu}
Summary(ru_RU.UTF-8): документация %name

%description doc
This package holds developer docs for %name
as a book in HTML and PDF formats.

%description -l ru_RU.UTF-8 doc
Этот пакет содержит документацию разработчика
для %name в форме книжки (HTML, PDF).

%prep
%setup

%build
%if_with doc
make BUILDDIR=%docs docs
%endif

%install
mkdir -p %buildroot{%mpdir,%_man7dir}
cp -a * %buildroot%mpdir
%if_with doc
mv %buildroot%mpdir/doc/mkimage-profiles.7 %buildroot%_man7dir/
%endif

%files
%mpdir/
%if_with doc
%_man7dir/*
%endif

%if_with doc
%files doc
%doc README
%doc QUICKSTART
%doc %docs/*
%endif

%changelog
* Mon Jun 07 2021 Anton Midyukov <antohami@altlinux.org> 1.4.13-alt1
- add parametr's BRANCH, NO_SYMLINK
- fix usage AUTOCLEAN parameter with DEBUG
- use variable REPORT from ~/.mkimage/profiles.mk
- move logs to reports directory, if enable REPORT
- fix build pdf documentation after clean
- update documetation
- build starterkits from regular.mk profile
- cnc-rt: uses lxqt DE instead of lxde
- cnc-rt: Not add efi=runtime to EFI_BOOTARGS
- kernel: add missing virtio kernel modules to VM_INITRDMODULES
- server-v: 9.2 beta
- workstation: 9.2 beta
- education: added last commits

* Fri May 21 2021 Anton Midyukov <antohami@altlinux.org> 1.4.12-alt1
- fix VM_SAVE_TARBALL parameter support
- grub: save ang read default menu item (thanks jqt4@, sin@)

* Mon May 17 2021 Anton Midyukov <antohami@altlinux.org> 1.4.11-alt1
- build-vm: Add ability to build .img.xz (thanks sem@)
- reports.mk: optimiztion for generate rpm and srpms lists (thanks mike@)
- reports.mk: generate targets.svgz instead targets.png
- add VM_SAVE_TARBALL parameter
- add MKIMAGE_PREFIX parameter
- kernel: optimization use/kernel/initrd-setup
- set STAGE1_INITRD_BOOTARGS in initrd-propagator
- slinux 9.1
- education 9.2

* Mon Apr 26 2021 Anton Midyukov <antohami@altlinux.org> 1.4.10-alt1
- build propagator and copy kernel in mkimage-profiles
- copy kernel to boot/ directory on iso image
- multiple kernels support for iso with grub
- add support initrd.img instead full.cz in stage1 with grub, syslinux
- use method:cdrom,fuid instead method:disk,uuid in uuid-iso feature
  (thanks jqt4@)
- vmguest: Drop virtualbox-addition kernel modules
- fix make distclean
- reports.mk: Generate rpm and srpms lists
- add hdt for grub-pc (floppy disk image)
- add items boot with local drive for grub-pc (iso)
- oem: use/deflogin/root
- add switch sddm|lightdm for kde5
- education 9.2 beta

* Mon Apr 05 2021 Anton Midyukov <antohami@altlinux.org> 1.4.9-alt1
- build-distro: BOOT_TYPE = BOOTLOADER
- Add the ability to override BOOTLOADER
- grub: restrict graphics mode to architectures i586, x86_64, aarch64
- Add grub-efi support for riscv64 (thanks arei@)
- New feature uuid-iso for create UUID for ISO image (thanks jqt4@)
- Disable sort subprofiles (build stage1 first)
- fonts: Set SYSTEM_FONTS for use/fonts/install2 again
- stage2: Add cmac.ko for use SMB2 and newer
- live.mk: Add distro/grub, fix allowed targets for architectures
- init: Add mount-efivars for sysvinit
- alt-server: fix missing packages in p9
- education: pull new commits

* Mon Mar 15 2021 Anton Midyukov <antohami@altlinux.org> 1.4.8-alt1
- Set BOOT_TYPE, BOOTLOADER to efiboot for aarch64
- 'Simply Linux 9.1 (beta)' commits contained (Thanks sem@)
- mipsel-bfk3: Switch to 5.4 kernel, other changes (Thanks iv@)
- oem: Add use/oem/distro
- uboot: Drop BOOTARGS cma=192M
- net: Added switch between NetworkManager (etcnet) and NetworkManager (native)
  Assigned by default NetworkManager (etcnet)
- x11: Not add use/drm to use/x11
- efi: Add check EFIVAR_FS option
- sound/base: Add test-audio
- armh-mcom02: set screen resolution 1366x768
- realtime.mk: Refactoring, drop live with session support
- engineering.mk: Switch to MATE
- x11: Reduce size of kde5
- regular-vm.mk: Set as default un-def kernel flavour, drop lts kernel flavour

* Mon Feb 15 2021 Anton Midyukov <antohami@altlinux.org> 1.4.7-alt1
- Add kernel modules for support Raspberry Pi 4 (mainline kernel)
- grub: Markup configuration files for translation (thanks Ivan Razzhivin)
- grub: Use META_VOL_ID for @distro@ instead RELNAME if available
  (ALT bug 39611, 39612)
- tar2fs: Enable secure-boot support for x86_64, add riscv64 support
- Add initrd features for rootfs: kbd rdshell rootfs
- desktop+mate: list is fixed,  as removed metapackage mate-default
- grub: use single boot/grub/grub.cfg in ISO
- Add support grub-pc for bootloading ISO (experimentall)
- Removed kernel modules that haven't been built for a long time

* Mon Jan 25 2021 Anton Midyukov <antohami@altlinux.org> 1.4.6-alt1
- deepin: add Network Manager applet
- engineering: initial as distributiv
- efi: fixed check modules for kernel-image >= 5.10
- oem: fixed calculation of required free space for installing additional
  packages
- oem: not use git in 60-oem-install.mk
- regular: do not default to mounting anything found (thanks mike@)
- rescue: added save session mode support for efi
- tar2fs: Disable os-probe at the time of grub installation
- xfce-sysv: add gnome-disks (suggested by Speccyfighter)

* Mon Dec 07 2020 Anton Midyukov <antohami@altlinux.org> 1.4.5-alt1
- Initial feature drm, added Nvidia proprietary driver support
- Adapted use/repo/main for vm/ targets
- oem: Added ability to set alterator-setup steps
- oem: Added use/oem/install target
- wireless: Update kernel modules for wi-fi
- armh-skit: Initial feature
- grub: Drop multiple kernel support
- stage1: Also add STAGE1_KMODULES
- bootloader, plymouth: Add splash to BASE_BOOTARGS only when using
  the plymouth feature
- tar2fs: Not add EFI partition for all aarch64, armh, but only for
  those with grub-efi bootloader or VM_BOOTTYPE variable set
- regular.mk, x11: Initial regular-deepin.iso
- arm-rpi4: Cleanup
- grub: Added EFI_BOOTARGS into BOOT/EFI/grub.cfg

* Mon Oct 26 2020 Anton Midyukov <antohami@altlinux.org> 1.4.4-alt1
- apply server-v 9.1 release patches (thanks shaba@)
- apply e2k patches (mike@)
- mipsel-bfk3: Fix /etc/fstab generation (thanks iv@)
- Rename all RPMs to canonical names before genbasedir (thanks boyars@)
- gnustep: Fix build
- oem: Add use/oem/no-cleanup
- deflogin: Now you can add a user with specific uid, gid and so on

* Fri Sep 25 2020 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt1
- education: added commits skipped when rebase was done
- wireless: added rtl8812au driver
- partially added commits from the kworkstation
- added e2k patches (mike@)
- tar2fs: set UUID in extlinux.conf, if exist
- vm.mk: simplified conditions for choosing a bootloader depending on arch
- added a couple of commits (obirvalger@)
- added commits for mipsel support (iv@)
- added the ability to override fonts (needed kworkstation)
- added target use/live/no-cleanup which is needed to disable cleanup
  documentation and rpmdb; is needed for live kworkstation without
  livecd-install
- fixed adding empty variable in "use/efi"
- don't cleanup dri modules from install2 (needed for support glamore)
- metadata/lib/50-metadata.mk: space-prefixed strings handling fixed (boyarsh@)

* Tue Sep 01 2020 Anton Midyukov <antohami@altlinux.org> 1.4.2-alt1
- x11: Added missing xorg-dri-armsoc for armh
- oem: Added rootfs-installer-features
- server-v: Added more commits by andy@, shaba@
- Set default timeout 60 seconds for syslinux and grub
- Set default item to install2 for syslinux and grub
- main.mk: Added vm/, ve/ targets into everything target
- Extended e2k support in distributions (thanks mike@)
- education: fix build and install

* Mon Aug 17 2020 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- Revert commit for support multiple kernel in iso image.

* Mon Aug 17 2020 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- New official maintainer antohami@ (blessed by mike@)
- Added grub config file generator for iso images
  (thanks shaba@)
- Expanded support for USB controllers and SD card readers
- Added support for booting on single-board Raspberry Pi 3 and 4
  in EFI mode (u-boot or edk2)
- Added grub-efi bootloader support for rootfs images
- Merged with branches for Workstation, Education,
  Simply Linux, Server, Server-V distributions
- Added a starterkit build profile with a real-time kernel (live)
- Added riscv64 platform support (thanks arei@)
- rootfs: support headless boot via alterator-setup-vnc (thanks arei@)

* Mon Nov 18 2019 Michael Shigorin <mike@altlinux.org> 1.3.15-alt1
- autoinstall fix (sin@)
- Baikal-M support, @ARM, elogind removal, other tweaks (antohami@)
- factored out archdep-filter, pulled in check-pkg-list (me)

* Mon Oct 21 2019 Michael Shigorin <mike@altlinux.org> 1.3.14-alt1
- make bails out on single image build error, see also make -k (iv@)
- mipsel support (iv@, antohami@)
- regular-vm.mk, refactoring, cleanups (antohami@)

* Mon Sep 16 2019 Michael Shigorin <mike@altlinux.org> 1.3.13-alt1
- recovery.tar support (iv@)
- mixin/mixin deps, aarch64 EFI, mcom02 & jetson nano support,
  multikernel & portability fixes, refactoring & cleanups (antohami@)
- document STAGE1_MODLISTS (me)

* Mon Aug 19 2019 Michael Shigorin <mike@altlinux.org> 1.3.12-alt1
- ppc64le support (glebfm@)
- build-vm hacked to build tarballs too (iv@ et al)
- p8.mk: dropped; along with other cleanups/fixups (antohami@)

* Tue Jul 09 2019 Michael Shigorin <mike@altlinux.org> 1.3.11.1-alt1
- x11: reverted vulkan changes (need more testing)

* Mon Jul 08 2019 Michael Shigorin <mike@altlinux.org> 1.3.11-alt1
- pkg.in/profiles subdirs support (shaba@)
- repo fixup regarding target arch (obirvalger@)
- switch back to yandex mirror by default,
  portability fixes, refactoring, cleanups (antohami@)
- x11 amdgpu/radeon and dm fixups, vmguest refactoring (me)

* Mon Jun 17 2019 Michael Shigorin <mike@altlinux.org> 1.3.10-alt1
- add server-v profile, drop groups/openstack (shaba@)

* Mon Jun 10 2019 Michael Shigorin <mike@altlinux.org> 1.3.9-alt1
- uboot feature, bootloader refactoring, etc (antohami@)
- cleanlog factored out from reports.mk (me)

* Mon Jun 03 2019 Michael Shigorin <mike@altlinux.org> 1.3.8-alt1
- p9.mk, office feature and other enhancements/fixes (antohami@)
- education (cas@)
- simply (sem@)
- minor tidbits and major merge-up (me)

* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 1.3.7-alt1
- docker, vm, browser fixups (obirvalger@)
- elogind support, refactoring, cleanups (antohami@)
- a couple more improvements (me)

* Mon Apr 01 2019 Michael Shigorin <mike@altlinux.org> 1.3.6-alt1
- no joke!

* Mon Mar 04 2019 Michael Shigorin <mike@altlinux.org> 1.3.5-alt1
- Spring 2019 patch queue cleanup
  + antohami@, jqt4@, iv@, obirvalger@, zerg@, me
  + tar2fs fixes for mipsel, qemu etc
  + lots of pkglist updates

* Mon Jan 14 2019 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- new 2019 year release ;-)
- tar2fs related security fix (iv@) iff sudo's been configured
- use/x11/dm rework (antohami@)
- archfixes (antohami@, iv@)
- pre-p8 bits cleanup (me)

* Mon Dec 24 2018 Michael Shigorin <mike@altlinux.org> 1.3.3-alt1
- aarch64/armh portability fixups (antohami@)
- grub-based vm images (shaba@)
- even smaller images (glebfm@)
- lxc/lxd lists/feature/image (dans@)
- updated robotics lists/image (dd@)
- e2k: 801/101/jeos tweaks (me)

* Mon Dec 10 2018 Michael Shigorin <mike@altlinux.org> 1.3.2-alt1
- sisyphus drops

* Mon Nov 05 2018 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- current fixes and tweaks

* Mon Oct 15 2018 Michael Shigorin <mike@altlinux.org> 1.3.0-alt1
- pre-p9 sisyphus: fixes, drops and just two kludges

* Mon Aug 13 2018 Michael Shigorin <mike@altlinux.org> 1.2.21-alt1
- volumes feature; fixups

* Mon Aug 06 2018 Michael Shigorin <mike@altlinux.org> 1.2.20-alt1
- isoboot/isodata; apt-conf feature; dual-seat e801

* Mon Jul 23 2018 Michael Shigorin <mike@altlinux.org> 1.2.19-alt1
- alt-workstation: x86 (sem@), e2k (me)

* Mon Jul 16 2018 Michael Shigorin <mike@altlinux.org> 1.2.18-alt1
- ldm feature (lakostis@)

* Mon Jun 25 2018 Michael Shigorin <mike@altlinux.org> 1.2.17-alt1
- e2k & profiles

* Mon Jun 11 2018 Michael Shigorin <mike@altlinux.org> 1.2.16-alt1
- starterkits-20180612

* Mon May 28 2018 Michael Shigorin <mike@altlinux.org> 1.2.15-alt1
- fixup release

* Mon May 21 2018 Michael Shigorin <mike@altlinux.org> 1.2.14-alt1
- pkgpriorities feature (manowar@)
- extended e2k support

* Mon Apr 23 2018 Michael Shigorin <mike@altlinux.org> 1.2.13-alt1
- antohami@'s improvements

* Mon Mar 19 2018 Michael Shigorin <mike@altlinux.org> 1.2.12-alt1
- @IA32, @X86

* Mon Mar 12 2018 Michael Shigorin <mike@altlinux.org> 1.2.11-alt1
- starterkits-20180312

* Mon Feb 19 2018 Michael Shigorin <mike@altlinux.org> 1.2.10-alt1
- antohami@'s fixups

* Mon Feb 12 2018 Michael Shigorin <mike@altlinux.org> 1.2.9-alt1
- antohami@'s release

* Mon Feb 05 2018 Michael Shigorin <mike@altlinux.org> 1.2.8-alt1
- regular fixes

* Mon Jan 22 2018 Michael Shigorin <mike@altlinux.org> 1.2.7-alt1
- 2018: better sound feature (antohami@)

* Mon Dec 11 2017 Michael Shigorin <mike@altlinux.org> 1.2.6-alt1
- starterkits-20171212

* Mon Dec 04 2017 Michael Shigorin <mike@altlinux.org> 1.2.5-alt1
- qcow2c

* Mon Nov 20 2017 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- opennebula-systemd

* Mon Sep 25 2017 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- p8+

* Mon Sep 11 2017 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- regular-engineering

* Mon Aug 21 2017 Michael Shigorin <mike@altlinux.org> 1.2.1-alt1
- seven years ago...

* Mon Aug 07 2017 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- e2k

* Mon Jul 31 2017 Michael Shigorin <mike@altlinux.org> 1.1.110-alt1
- lxde-sysv

* Mon Jun 12 2017 Michael Shigorin <mike@altlinux.org> 1.1.109-alt1
- starterkits-20170612

* Mon Apr 24 2017 Michael Shigorin <mike@altlinux.org> 1.1.108-alt1
- yandex.mirror

* Mon Apr 03 2017 Michael Shigorin <mike@altlinux.org> 1.1.107-alt1
- serial improvements

* Mon Mar 13 2017 Michael Shigorin <mike@altlinux.org> 1.1.106-alt1
- starterkits-20170312

* Mon Feb 27 2017 Michael Shigorin <mike@altlinux.org> 1.1.105-alt1
- disable git hooks (glebfm@)

* Mon Feb 06 2017 Michael Shigorin <mike@altlinux.org> 1.1.104-alt1
- [[vncinst]] fixed

* Mon Jan 30 2017 Michael Shigorin <mike@altlinux.org> 1.1.103-alt1
- rescue -= bootsplash

* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 1.1.102-alt1
- 2017

* Mon Dec 12 2016 Michael Shigorin <mike@altlinux.org> 1.1.101-alt1
- starterkits-20161212

* Mon Dec 05 2016 Michael Shigorin <mike@altlinux.org> 1.1.100-alt1
- preparing for starterkits

* Mon Nov 14 2016 Michael Shigorin <mike@altlinux.org> 1.1.99-alt1
- xfce-sysv
- preparing...

* Mon Oct 31 2016 Michael Shigorin <mike@altlinux.org> 1.1.98-alt1
- preparing for workstation 8.1

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 1.1.97-alt1
- regular tweaks

* Mon Sep 12 2016 Michael Shigorin <mike@altlinux.org> 1.1.96-alt1
- starterkits-20160912

* Mon Aug 15 2016 Michael Shigorin <mike@altlinux.org> 1.1.95-alt1
- s/basealt/alt/g

* Mon Jun 27 2016 Michael Shigorin <mike@altlinux.org> 1.1.94-alt1
- workstation

* Mon Jun 13 2016 Michael Shigorin <mike@altlinux.org> 1.1.93-alt1
- starterkits-20160612

* Mon May 30 2016 Michael Shigorin <mike@altlinux.org> 1.1.92-alt1
- server-openstack

* Mon May 23 2016 Michael Shigorin <mike@altlinux.org> 1.1.91-alt1
- nvidia/nouveau rehash
- overlayfs support (lakostis@)

* Tue May 03 2016 Michael Shigorin <mike@altlinux.org> 1.1.90-alt1
- starterkits-20160429

* Mon Apr 25 2016 Michael Shigorin <mike@altlinux.org> 1.1.89-alt1
- preparing for p8 starterkits

* Mon Apr 11 2016 Michael Shigorin <mike@altlinux.org> 1.1.88-alt1
- pkg.in/profiles

* Mon Mar 14 2016 Michael Shigorin <mike@altlinux.org> 1.1.87-alt1
- starterkits-20160312

* Mon Feb 29 2016 Michael Shigorin <mike@altlinux.org> 1.1.86-alt1
- junior

* Mon Feb 15 2016 Michael Shigorin <mike@altlinux.org> 1.1.85-alt1
- regular-jeos-ovz

* Mon Feb 08 2016 Michael Shigorin <mike@altlinux.org> 1.1.84-alt1
- %name(7) :)

* Mon Jan 25 2016 Michael Shigorin <mike@altlinux.org> 1.1.83-alt1
- openssh 7.x (see also #31716)

* Mon Jan 11 2016 Michael Shigorin <mike@altlinux.org> 1.1.82-alt1
- firmwarez

* Mon Dec 07 2015 Michael Shigorin <mike@altlinux.org> 1.1.81-alt1
- regular fixes

* Mon Nov 30 2015 Michael Shigorin <mike@altlinux.org> 1.1.80-alt1
- pre-starterkit cleanups

* Mon Nov 16 2015 Michael Shigorin <mike@altlinux.org> 1.1.79-alt1
- faked workaround

* Mon Nov 09 2015 Michael Shigorin <mike@altlinux.org> 1.1.78-alt1
- regular-enlightenment

* Mon Oct 19 2015 Michael Shigorin <mike@altlinux.org> 1.1.77-alt1
- webkiosk improvements

* Mon Oct 12 2015 Michael Shigorin <mike@altlinux.org> 1.1.76-alt1
- no more GREP_OPTIONS

* Mon Sep 28 2015 Michael Shigorin <mike@altlinux.org> 1.1.75-alt1
- systemd-specific hook for installer (solo@)

* Mon Sep 14 2015 Michael Shigorin <mike@altlinux.org> 1.1.74-alt1
- starterkits-20150912

* Mon Sep 07 2015 Michael Shigorin <mike@altlinux.org> 1.1.73-alt1
- im feature

* Mon Aug 31 2015 Michael Shigorin <mike@altlinux.org> 1.1.72-alt1
- starterkits alpha

* Mon Aug 10 2015 Michael Shigorin <mike@altlinux.org> 1.1.71-alt1
- docs feature

* Mon Jul 20 2015 Michael Shigorin <mike@altlinux.org> 1.1.70-alt1
- check KFLAVOURS

* Mon Jun 29 2015 Michael Shigorin <mike@altlinux.org> 1.1.69-alt1
- yet another systemd- tweak

* Mon Jun 22 2015 Michael Shigorin <mike@altlinux.org> 1.1.68-alt1
- LIVE_CLEANUP_KDRIVERS actually works

* Mon Jun 08 2015 Michael Shigorin <mike@altlinux.org> 1.1.67-alt1
- minor post-tweaks

* Mon Jun 01 2015 Michael Shigorin <mike@altlinux.org> 1.1.66-alt1
- remote rescue

* Mon May 04 2015 Michael Shigorin <mike@altlinux.org> 1.1.65-alt1
- archdep pkglists

* Mon Apr 20 2015 Michael Shigorin <mike@altlinux.org> 1.1.64-alt1
- modularized stage1 modules list

* Mon Mar 30 2015 Michael Shigorin <mike@altlinux.org> 1.1.63-alt1
- support USB3, ACPI suspend

* Mon Mar 16 2015 Michael Shigorin <mike@altlinux.org> 1.1.62-alt1
- starterkits-20150312

* Mon Mar 09 2015 Michael Shigorin <mike@altlinux.org> 1.1.61-alt1
- EFI_BOOTARGS

* Mon Mar 02 2015 Michael Shigorin <mike@altlinux.org> 1.1.60-alt1
- vmguest, install2: refactoring

* Mon Feb 23 2015 Michael Shigorin <mike@altlinux.org> 1.1.59-alt1
- regular rebase

* Mon Feb 16 2015 Michael Shigorin <mike@altlinux.org> 1.1.58-alt1
- vagrant feature (closes: #28553)

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 1.1.57-alt1
- fix the lists copying fix

* Mon Feb 02 2015 Michael Shigorin <mike@altlinux.org> 1.1.56-alt1
- fix lilo check for vm images

* Mon Jan 26 2015 Michael Shigorin <mike@altlinux.org> 1.1.55-alt1
- lists copying fixed

* Mon Jan 05 2015 Michael Shigorin <mike@altlinux.org> 1.1.54-alt1
- live: don't force localboot

* Mon Dec 15 2014 Michael Shigorin <mike@altlinux.org> 1.1.53-alt1
- starterkits-20141212

* Mon Nov 17 2014 Michael Shigorin <mike@altlinux.org> 1.1.52-alt1
- docs: "7.0+" (closes: #30474)
- l10n feature

* Mon Nov 10 2014 Michael Shigorin <mike@altlinux.org> 1.1.51-alt1
- current updates

* Mon Oct 27 2014 Michael Shigorin <mike@altlinux.org> 1.1.50-alt1
- minor tweaks

* Mon Oct 13 2014 Michael Shigorin <mike@altlinux.org> 1.1.49-alt1
- pkglist updates

* Mon Sep 29 2014 Michael Shigorin <mike@altlinux.org> 1.1.48-alt1
- (sysv)init: exclude systemd explicitly

* Mon Sep 22 2014 Michael Shigorin <mike@altlinux.org> 1.1.47-alt1
- kpackages() argswap

* Mon Sep 15 2014 Michael Shigorin <mike@altlinux.org> 1.1.46-alt1
- regular fixes

* Mon Sep 01 2014 Michael Shigorin <mike@altlinux.org> 1.1.45-alt1
- starterkits alpha

* Mon Aug 18 2014 Michael Shigorin <mike@altlinux.org> 1.1.44-alt1
- connman fixup

* Mon Aug 04 2014 Michael Shigorin <mike@altlinux.org> 1.1.43-alt1
- fixed package build

* Mon Jul 28 2014 Michael Shigorin <mike@altlinux.org> 1.1.42-alt1
- current bits

* Mon Jul 07 2014 Michael Shigorin <mike@altlinux.org> 1.1.41-alt1
- post-214 fixups

* Mon Jun 30 2014 Michael Shigorin <mike@altlinux.org> 1.1.40-alt1
- systemd-214

* Mon Jun 16 2014 Michael Shigorin <mike@altlinux.org> 1.1.39-alt1
- starterkits-20140612

* Mon Jun 02 2014 Michael Shigorin <mike@altlinux.org> 1.1.38-alt1
- mksquashfs 4.3 support

* Mon May 26 2014 Michael Shigorin <mike@altlinux.org> 1.1.37-alt1
- use/browser

* Mon May 19 2014 Michael Shigorin <mike@altlinux.org> 1.1.36-alt1
- regular-lxqt

* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 1.1.35-alt1
- yet another rescue week

* Mon May 05 2014 Michael Shigorin <mike@altlinux.org> 1.1.34-alt1
- remember Odessa

* Mon Apr 28 2014 Michael Shigorin <mike@altlinux.org> 1.1.33-alt1
- net-eth tweaks

* Mon Apr 21 2014 Michael Shigorin <mike@altlinux.org> 1.1.32-alt1
- regular-rescue week

* Mon Apr 14 2014 Michael Shigorin <mike@altlinux.org> 1.1.31-alt1
- live: refactoring
- forensics mode

* Mon Apr 07 2014 Michael Shigorin <mike@altlinux.org> 1.1.30-alt1
- robotics support

* Mon Mar 31 2014 Michael Shigorin <mike@altlinux.org> 1.1.29-alt1
- mediacheck feature

* Mon Mar 24 2014 Michael Shigorin <mike@altlinux.org> 1.1.28-alt1
- install2: more cleanups

* Mon Mar 17 2014 Michael Shigorin <mike@altlinux.org> 1.1.27-alt1
- don't insist on k-m-r8168
- codebase deduplication

* Mon Mar 10 2014 Michael Shigorin <mike@altlinux.org> 1.1.26-alt1
- docs week
- deflogin: empty ROOTPW explicitly ignored (potential security fix)

* Mon Mar 03 2014 Michael Shigorin <mike@altlinux.org> 1.1.25-alt1
- regular updates

* Mon Feb 10 2014 Michael Shigorin <mike@altlinux.org> 1.1.24-alt1
- service bridge

* Mon Feb 03 2014 Michael Shigorin <mike@altlinux.org> 1.1.23-alt1
- live, net*, syslinux fixes (see also #26608)

* Mon Jan 27 2014 Michael Shigorin <mike@altlinux.org> 1.1.22-alt1
- ahci kludge (see #29705) :(

* Mon Jan 20 2014 Michael Shigorin <mike@altlinux.org> 1.1.21-alt1
- rescue tweaks

* Mon Jan 13 2014 Michael Shigorin <mike@altlinux.org> 1.1.20-alt1
- support for CIFS installation method (sin@)
- glibc-locales for regular images (closes: #29693)

* Mon Dec 30 2013 Michael Shigorin <mike@altlinux.org> 1.1.19-alt1
- regular fixes

* Mon Dec 23 2013 Michael Shigorin <mike@altlinux.org> 1.1.18-alt1
- efi updates

* Mon Dec 16 2013 Michael Shigorin <mike@altlinux.org> 1.1.17-alt1
- refind branding

* Mon Dec 09 2013 Michael Shigorin <mike@altlinux.org> 1.1.16-alt1
- e18

* Mon Dec 02 2013 Michael Shigorin <mike@altlinux.org> 1.1.15-alt1
- regular fixups

* Mon Nov 25 2013 Michael Shigorin <mike@altlinux.org> 1.1.14-alt1
- important bugfix: THE_PACKAGES weren't getting through to .base
- regular-sysv-tde related churn

* Mon Nov 04 2013 Michael Shigorin <mike@altlinux.org> 1.1.13-alt1
- rescue friday

* Mon Oct 21 2013 Michael Shigorin <mike@altlinux.org> 1.1.12-alt1
- live-builder update

* Mon Oct 14 2013 Michael Shigorin <mike@altlinux.org> 1.1.11-alt1
- luks better

* Mon Sep 30 2013 Michael Shigorin <mike@altlinux.org> 1.1.10-alt1
- regular tweaks

* Mon Sep 23 2013 Michael Shigorin <mike@altlinux.org> 1.1.9-alt1
- regular fixes

* Mon Sep 16 2013 Michael Shigorin <mike@altlinux.org> 1.1.8-alt1
- armh/p7/ve fixes

* Mon Aug 26 2013 Michael Shigorin <mike@altlinux.org> 1.1.7-alt1
- minor fixes

* Mon Aug 12 2013 Michael Shigorin <mike@altlinux.org> 1.1.6-alt1
- vm-net retired

* Mon Aug 05 2013 Michael Shigorin <mike@altlinux.org> 1.1.5-alt1
- armh related fixes

* Mon Jul 29 2013 Michael Shigorin <mike@altlinux.org> 1.1.4-alt1
- assorted fixups

* Mon Jul 22 2013 Michael Shigorin <mike@altlinux.org> 1.1.3-alt1
- armh fixes and tweaks

* Mon Jul 15 2013 Michael Shigorin <mike@altlinux.org> 1.1.2-alt1
- control and sound features

* Mon Jul 01 2013 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1
- cuboxism

* Mon Jun 17 2013 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- 1.1.x branch: public alpha development status
  + new subprofile: rootfs
  + new features: armh*, deflogin, init, services
  + refactored features: build-*, efi, fonts, live, x11*
  + tar2vm got rewritten as tar2fs, gained ARM support
- minor spec metadata update

* Mon Jun 17 2013 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0

* Mon Jun 10 2013 Michael Shigorin <mike@altlinux.org> 0.9.16-alt1
- 1.0pre

* Mon May 27 2013 Michael Shigorin <mike@altlinux.org> 0.9.15-alt1
- +installer

* Mon May 20 2013 Michael Shigorin <mike@altlinux.org> 0.9.14-alt1
- more regular fixes

* Mon May 13 2013 Michael Shigorin <mike@altlinux.org> 0.9.13-alt1
- regular fixes

* Mon Apr 22 2013 Michael Shigorin <mike@altlinux.org> 0.9.12-alt1
- four weeks later...

* Mon Mar 25 2013 Michael Shigorin <mike@altlinux.org> 0.9.11-alt1
- persistent icewm

* Mon Mar 18 2013 Michael Shigorin <mike@altlinux.org> 0.9.10-alt1
- fonts: axios!

* Tue Feb 26 2013 Michael Shigorin <mike@altlinux.org> 0.9.9-alt1
- regular refactoring

* Tue Feb 19 2013 Michael Shigorin <mike@altlinux.org> 0.9.8.1-alt1
- works with make-initrd 0.8.1+ (see #28578)

* Mon Feb 18 2013 Michael Shigorin <mike@altlinux.org> 0.9.8-alt1
- live fixes/tweaks galore

* Mon Feb 11 2013 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- going nightly

* Mon Feb 04 2013 Michael Shigorin <mike@altlinux.org> 0.9.6-alt1
- assorted fixes

* Mon Jan 21 2013 Michael Shigorin <mike@altlinux.org> 0.9.5-alt1
- homeros

* Mon Jan 14 2013 Michael Shigorin <mike@altlinux.org> 0.9.4-alt1
- restricted boot

* Mon Dec 31 2012 Michael Shigorin <mike@altlinux.org> 0.9.3-alt1
- regular images

* Mon Dec 17 2012 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- enhanced uefi support

* Mon Dec 03 2012 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1
- initial kde4 support

* Mon Nov 19 2012 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- initial uefi, luks, armh support
- enhanced arm, gnome3/systemd, vm support

* Sun Nov 11 2012 Michael Shigorin <mike@altlinux.org> 0.8.7-alt1
- regressions--

* Mon Nov 05 2012 Michael Shigorin <mike@altlinux.org> 0.8.6-alt1
- docs subpackage (HTML/PDF book)

* Mon Oct 29 2012 Michael Shigorin <mike@altlinux.org> 0.8.5-alt1
- diffable logs
- AMD APU support

* Tue Oct 16 2012 Michael Shigorin <mike@altlinux.org> 0.8.4-alt1
- worked around enhancements in current make-initrd-propagator
  (thus fixed live image boot, finally)

* Mon Oct 15 2012 Michael Shigorin <mike@altlinux.org> 0.8.3-alt1
- make-3.82 support
- fixed live image boot to some extent (see #27640, #27852)

* Mon Sep 24 2012 Michael Shigorin <mike@altlinux.org> 0.8.2-alt1
- fixed build with recent make-initrd-propagator

* Mon Sep 03 2012 Michael Shigorin <mike@altlinux.org> 0.8.1-alt1
- misc fixes

* Mon Aug 13 2012 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- stage2@live

* Mon Aug 06 2012 Michael Shigorin <mike@altlinux.org> 0.7.6-alt1
- minor improvements

* Mon Jul 30 2012 Michael Shigorin <mike@altlinux.org> 0.7.5-alt1
- a bunch of fixups and cleanups

* Mon Jul 16 2012 Michael Shigorin <mike@altlinux.org> 0.7.4-alt1
- ppc builds

* Mon Jul 09 2012 Michael Shigorin <mike@altlinux.org> 0.7.3-alt1
- arm builds

* Mon Jul 02 2012 Michael Shigorin <mike@altlinux.org> 0.7.2-alt1
- simply fixes

* Mon Jun 25 2012 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- vm improvements and assorted tweaks/fixes

* Mon Jun 18 2012 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- new features:
  + initial build-vm
  + plymouth

* Mon May 28 2012 Michael Shigorin <mike@altlinux.org> 0.6.8-alt1
- minor bugfixes

* Mon May 21 2012 Michael Shigorin <mike@altlinux.org> 0.6.7-alt1
- docs updates

* Mon May 14 2012 Michael Shigorin <mike@altlinux.org> 0.6.6-alt1
- build helpers refactored
- initial frontend support

* Mon May 07 2012 Michael Shigorin <mike@altlinux.org> 0.6.5-alt1
- branding feature

* Mon Apr 23 2012 Michael Shigorin <mike@altlinux.org> 0.6.4-alt1
- simply better (tm)

* Mon Apr 09 2012 Michael Shigorin <mike@altlinux.org> 0.6.3-alt1
- massive squashfs tuning

* Mon Apr 02 2012 Michael Shigorin <mike@altlinux.org> 0.6.2-alt1
- better live-webkiosk and initial live-flightgear
- cleanup, syslinux, xorg feature tweaks

* Mon Mar 26 2012 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- ISO9660 metadata support
- initial alien VE image

* Mon Mar 19 2012 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- reports (targets graph)

* Mon Mar 12 2012 Michael Shigorin <mike@altlinux.org> 0.5.7-alt1
- distro tweaks

* Mon Feb 20 2012 Michael Shigorin <mike@altlinux.org> 0.5.6-alt1
- minor fixups

* Mon Feb 06 2012 Michael Shigorin <mike@altlinux.org> 0.5.5-alt1
- live-related tweaks (including live.hooks support)
- terminal server and webkiosk images

* Mon Jan 16 2012 Michael Shigorin <mike@altlinux.org> 0.5.4-alt1
- better diags for initial deployment

* Mon Jan 02 2012 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- multi-target, multi-arch, single-job builds

* Mon Dec 19 2011 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- THE_{KMODULES,PACKAGES,LISTS,GROUPS}
- incremental development, refactoring and bugfixing

* Fri Dec 02 2011 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- generic VE archive type (added cpio and xz either)
- minor additions/fixes

* Mon Nov 21 2011 Michael Shigorin <mike@altlinux.org> 0.5.0-alt1
- add_feature for autoregistration (simple but invasive)
- added features: isomd5sum, repo, systemd
- changed features: powerbutton -> power

* Tue Nov 08 2011 Michael Shigorin <mike@altlinux.org> 0.4.3.2-alt1
- mkimage version required/checked

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.4.3.1-alt1
- CLEAN by default unless DEBUG

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.4.3-alt2
- include %mpdir/ itself as well

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.4.3-alt1
- enhancements to logging
- NICE variable: employ nice(1) and ionice(1) if available
- features.in/syslinux: banner tweaked to include target name
- features.in/live: set up unicode locale/consolefont

* Wed Nov 02 2011 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- initial package
