%def_with sb_kern_signature_check_relaxed
%define efi_arches %ix86 x86_64 aarch64

Name: grub
Version: 2.02
Release: alt22

Summary: GRand Unified Bootloader
License: GPL-3
Group: System/Kernel and hardware

Url: http://www.gnu.org/software/grub

ExclusiveArch: %ix86 x86_64 aarch64 ppc64le

Source0: %name-%version.tar
Source1: grub2-sysconfig

Source3: 39_memtest
Source4: grub.filetrigger

Source5: grub-extras-%version.tar

Source6: grub-autoupdate

Source8: update-grub
Source9: update-grub.8

Source10: grub-efi-autoupdate
Source11: embedded_grub.cfg

Source12: grub-entries
Source13: grub-entries.8

Patch0: grub-2.02-os-alt.patch
Patch1: grub-2.00-sysconfig-path-alt.patch
Patch2: grub-2.02-altlinux-theme.patch
Patch3: grub-2.00-debian-uefi-os-prober.patch
Patch4: grub-2.02-os-alt-xen.patch
Patch5: grub-2.02-debian-disable_floppies.patch
Patch6: grub-2.02-add-fw_path-variable.patch
Patch7: grub-2.02-efibootmgr-check.patch
Patch8: grub-2.02-debian-install_signed.patch
Patch9: grub-2.00-fedora-unrestricted.patch
Patch10: grub2-stfu.patch
Patch11: grub-2.02-shift-interrupt-timeout.patch
Patch12: grub-2.02-ubuntu-efi-setup.patch
Patch13: grub-2.02-check_writes-alt.patch
Patch14: grub-2.02-alt-luks-use-uuid.patch
Patch15: grub-2.02-alt-fedora-linuxefi.patch
Patch16: grub-2.02-suse-fix-build-with-gcc8.patch
Patch17: grub-2.02-fix-binutils-break-grub-efi-build.patch
Patch18: grub-2.02-upstream-default-ptimer.patch
Patch19: grub-2.02-upstream-xfs-sparse-inodes.patch

# add a rhboot/grub-2.02-sb set of patches to ensure SecureBoot safe operation
# refer to url:  https://github.com/rhboot/grub2/commits/grub-2.02-sb
Patch101: grub-2.02-sb-0001-Use-linuxefi-and-initrdefi-where-appropriate.patch
Patch102: grub-2.02-sb-0002-Don-t-allow-insmod-when-secure-boot-is-enabled.patch
Patch103: grub-2.02-sb-0003-Load-arm-with-SB-enabled.patch
Patch104: grub-2.02-sb-0004-Use-linux16-when-appropriate-880840.patch
Patch105: grub-2.02-sb-0005-Make-10_linux-work-with-our-changes-for-linux16-and-.patch
Patch106: grub-2.02-sb-0006-Fix-race-in-EFI-validation.patch
Patch107: grub-2.02-sb-0007-Use-device-part-of-chainloader-target-if-present.patch
Patch108: grub-2.02-sb-0008-Add-secureboot-support-on-efi-chainloader.patch
Patch109: grub-2.02-sb-0009-Make-any-of-the-loaders-that-link-in-efi-mode-honor-.patch
Patch110: grub-2.02-sb-0010-Rework-linux-command.patch
Patch111: grub-2.02-sb-0011-Rework-linux16-command.patch
Patch112: grub-2.02-sb-0012-Re-work-some-intricacies-of-PE-loading.patch
Patch113: grub-2.02-sb-0013-Rework-even-more-of-efi-chainload-so-non-sb-cases-wo.patch
Patch114: grub-2.02-sb-0014-Add-some-grub_dprintf-in-the-linuxefi-path.patch
Patch115: grub-2.02-sb-0015-linuxefi-minor-cleanups.patch
Patch116: grub-2.02-sb-0016-Handle-multi-arch-64-on-32-boot-in-linuxefi-loader.patch
Patch117: grub-2.02-sb-0017-Clean-up-some-errors-in-the-linuxefi-loader.patch

Patch201: grub-2.02-alt-relaxed-kernel-sign-check.patch

BuildRequires(pre): rpm-macros-uefi
BuildRequires: flex fonts-bitmap-misc fonts-ttf-dejavu libfreetype-devel python-modules ruby autogen
BuildRequires: liblzma-devel help2man zlib-devel
BuildRequires: libdevmapper-devel
BuildRequires: texinfo

# fonts: choose one

## dejavu
#BuildRequires: fonts-ttf-dejavu
#define font /usr/share/fonts/ttf/dejavu/DejaVuSansMono.ttf

## terminus
#BuildRequires: fonts-bitmap-terminus
#define font /usr/share/fonts/bitmap/terminus/ter-x16n.pcf.gz

## univga
BuildRequires: fonts-bitmap-univga
%define font /usr/share/fonts/bitmap/univga/u_vga16_9.pcf.gz

## see also fonts-bitmap-ucs-miscfixed; efont-unicode doesn't fit

Requires: gettext

# NB: not a fashion but the critical need to fit into 62 sectors
%define _optlevel s

%ifarch %ix86
%global grubefiarch i386-efi
%global linux_module_name linux
%global efi_suff ia32
%endif
%ifarch x86_64
%global grubefiarch x86_64-efi
%global linux_module_name linuxefi
%global efi_suff x64
%endif
%ifarch aarch64
%global grubefiarch arm64-efi
%global linux_module_name linux
%global efi_suff x64
%endif

%package common
Summary: GRand Unified Bootloader (common part)
Group: System/Kernel and hardware
Provides: grub2-common = %EVR
Obsoletes: grub2-common < %EVR

%package pc
Summary: GRand Unified Bootloader (PC BIOS variant)
Group: System/Kernel and hardware
Requires: %name-common = %version-%release
%ifarch %ix86 x86_64
Provides: grub2 = %EVR
Provides: grub = %EVR
%endif
Provides: grub2-pc = %EVR
Obsoletes: grub2-pc < %EVR

%package ieee1275
Summary: GRand Unified Bootloader (IEEE1275 variant)
Group: System/Kernel and hardware
Requires: %name-common = %version-%release
%ifarch ppc64le
Requires: powerpc-utils
Provides: grub2 = %EVR
Provides: grub = %EVR
%endif

%package efi
Summary: GRand Unified Bootloader (UEFI variant)
Group: System/Kernel and hardware
Requires: %name-common = %EVR
Provides: grub2-efi = %EVR
Obsoletes: grub2-efi < %EVR
PreReq: efibootmgr >= 15
%ifarch aarch64
Provides: grub2 = %EVR
Provides: grub = %EVR
%endif

%define desc_generic \
GNU GRUB is a multiboot boot loader. It was derived from GRUB. It is an \
attempt to produce a boot loader for IBM PC-compatible machines that \
has both the ability to be friendly to beginning or otherwise \
nontechnically interested users and the flexibility to help experts in \
diverse environments. It is compatible with Free/Net/OpenBSD and Linux. \
It supports Win 9x/NT and OS/2 via chainloaders. It has a menu \
interface and a command line interface. \
It implements the Multiboot standard, which allows for flexible loading \
of multiple boot images (needed for modular kernels such as the GNU Hurd).

%description
%desc_generic

%description common
%desc_generic

This package carries the shared code and data.

%description pc
%desc_generic

This package provides PC BIOS support.

%description ieee1275
%desc_generic

This package provides Open Firmware (IEEE 1275) support.

%description efi
%desc_generic

This package provides UEFI systems support.

Please note that the official build is signed; this shouldn't
intervene in any way but rather provides means to cope with
UEFI SecureBoot (better described as Restricted Boot) firmware
when one can't disable it easily, doesn't want to, or needs not to.

%prep
%setup -b 5
%patch0 -p2
%patch1 -p1
%patch2 -p2
%patch3 -p1
%patch4 -p2
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p2
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p2
%patch14 -p2
%patch15 -p2
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p2

#SB patches
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch201 -p0

sed -i "/^AC_INIT(\[GRUB\]/ s/%version[^]]\+/%version-%release/" configure.ac
sed -i "s/PYTHON:=python/PYTHON:=python3/" autogen.sh

%build
./autogen.sh
build_grub() {
	local dir="$1"; shift
	mkdir -p "$dir"
	pushd "$dir"
	%define _configure_script ../configure
	%configure \
		TARGET_LDFLAGS=-static \
		--disable-werror \
		"$@"
	%make_build
	popd
}

build_efi_image() {
	local mkimage="$1"; shift
	local dir="$1"; shift
	local format="$1"; shift
	"$mkimage" -O "$format" -o "$dir"/grub.efi -d "$dir"/grub-core -p "" \
		part_gpt part_apple part_msdos hfsplus fat ext2 btrfs xfs \
		squash4 normal chain boot configfile diskfilter \
		minicmd reboot halt search search_fs_uuid search_fs_file \
		search_label sleep test syslinuxcfg all_video video font \
		gfxmenu gfxterm gfxterm_background lvm lsefi efifwsetup cat \
		gzio iso9660 loadenv loopback mdraid09 mdraid1x png jpeg \
		extcmd keystatus procfs cryptodisk gcry_rijndael gcry_sha1 \
		gcry_sha256 luks gcry_sha512 gcry_serpent gcry_twofish \
		"$@"
}

%ifarch %ix86 x86_64
build_grub build-pc \
	--with-platform=pc \
#
%endif

%ifarch ppc64le
build_grub build-ieee1275 \
	--with-platform=ieee1275 \
#
%endif

%ifarch %efi_arches
build_grub build-efi \
	--with-platform=efi \
#
build_efi_image build-efi/grub-mkimage build-efi %grubefiarch %linux_module_name

#add forced ia32 version build to be bundled with x86_64 EFI
%ifarch x86_64
build_grub build-efi-ia32 \
	--with-platform=efi \
	--target=i386 \
#
# use 64bit mkimage to build i386-efi image
build_efi_image build-efi/grub-mkimage build-efi-ia32 i386-efi linuxefi
%endif

%if_with sb_kern_signature_check_relaxed
# build grub efi binaries with relaxed kernel signature checks
# (see patch#201).
%ifarch %efi_arches
CFLAGS='%optflags -DRELAX_KERNEL_SIGNATURE_CHECK=1' \
	build_grub build-efi-relaxed \
	--with-platform=efi \
#
build_efi_image build-efi-relaxed/grub-mkimage build-efi-relaxed %grubefiarch %linux_module_name
%endif

%ifarch x86_64
CFLAGS='%optflags -DRELAX_KERNEL_SIGNATURE_CHECK=1' \
	build_grub build-efi-ia32-relaxed \
	--with-platform=efi \
	--target=i386 \
#
# use 64bit mkimage to build i386-efi image
build_efi_image build-efi-relaxed/grub-mkimage build-efi-ia32-relaxed i386-efi linuxefi
%endif
%endif
%endif

%install
%ifarch %ix86 x86_64
%makeinstall_std -C build-pc
%ifarch x86_64
#"cherry pick" only i386 executable
%if_with sb_kern_signature_check_relaxed
install -pDm644 build-efi-ia32/grub.efi %buildroot%_efi_bindir/grubia32sb.efi
install -pDm644 build-efi-ia32-relaxed/grub.efi %buildroot%_efi_bindir/grubia32.efi
%else
install -pDm644 build-efi-ia32/grub.efi %buildroot%_efi_bindir/grubia32.efi
%endif

#install ia32 version in parallel with x64 for x86_64 platforms with ia32 EFI
%makeinstall_std -C build-efi-ia32
%endif
%endif

%makeinstall_std -C \
%ifarch ppc64le
	build-ieee1275
%else
	build-efi
%endif

install -pDm644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/grub2

%find_lang grub

mkdir -p %buildroot/boot/grub/fonts

install -pD -m755 %SOURCE8 %buildroot%_sbindir/
install -pD -m644 %SOURCE9 %buildroot%_man8dir/update-grub.8
install -pD -m644 %SOURCE13 %buildroot%_man8dir/grub-entries.8

# TODO: drop the obsolete one (unifont.pf2)
%buildroot%_bindir/grub-mkfont -o %buildroot/boot/grub/unifont.pf2 %_datadir/fonts/bitmap/misc/8x13.pcf.gz
%buildroot%_bindir/grub-mkfont -o %buildroot/boot/grub/fonts/unicode.pf2 %font

mkdir -p %buildroot/boot/grub/themes

install -pDm755 %SOURCE3 %buildroot%_sysconfdir/grub.d/
sed -i 's,^libdir=,libdir=%_libdir,g' %buildroot%_sysconfdir/grub.d/39_memtest
sed -i 's,@LOCALEDIR@,%_datadir/locale,g' %buildroot%_sysconfdir/grub.d/*

install -pDm755 %SOURCE4  %buildroot%_rpmlibdir/grub.filetrigger
install -pDm755 %SOURCE6  %buildroot%_sbindir/grub-autoupdate
%ifarch %efi_arches
install -pDm755 %SOURCE10 %buildroot%_sbindir/grub-efi-autoupdate
%endif
install -pDm755 %SOURCE12 %buildroot%_sbindir/grub-entries

# Ghost config file
install -d %buildroot/boot/grub
touch %buildroot/boot/grub/grub.cfg
ln -s ../boot/grub/grub.cfg %buildroot%_sysconfdir/grub.cfg

# Docs/habits compat symlink
mkdir -p %buildroot%_sysconfdir/default
ln -s ../sysconfig/grub2 %buildroot%_sysconfdir/default/grub

%ifarch %efi_arches
%if_with sb_kern_signature_check_relaxed
install -pDm644 build-efi/grub.efi %buildroot%_efi_bindir/grub%{efi_suff}sb.efi
install -pDm644 build-efi-relaxed/grub.efi %buildroot%_efi_bindir/grub%{efi_suff}.efi
%else
install -pDm644 build-efi/grub.efi %buildroot%_efi_bindir/grub%{efi_suff}.efi
%endif

# Remove headers
rm -f %buildroot%_libdir/grub-efi/*/*.h
%endif
rm %buildroot%_sysconfdir/grub.d/README
rm %buildroot%_sysconfdir/grub.d/41_custom

%files common -f grub.lang
%dir %_sysconfdir/grub.d
%dir %_libdir/grub
%dir /boot/grub
/boot/grub/*.pf2
/boot/grub/fonts/
/boot/grub/themes/
%_sysconfdir/grub.d/00_header
%_sysconfdir/grub.d/05_altlinux_theme
%_sysconfdir/grub.d/10_linux
%_sysconfdir/grub.d/20_linux_xen
%_sysconfdir/grub.d/30_os-prober
%_sysconfdir/grub.d/30_uefi-firmware
%_sysconfdir/grub.d/39_memtest
%config(noreplace) %_sysconfdir/grub.d/40_custom
%config(noreplace) %_sysconfdir/sysconfig/grub2
%ghost %config(noreplace) /boot/grub/grub.cfg
%_sysconfdir/grub.cfg
%_sysconfdir/default/grub
%_sysconfdir/bash_completion.d/grub
%_rpmlibdir/%name.filetrigger
# these tools are only for efi and x86_64
%ifarch x86_64 ppc64le
%_bindir/grub-render-label
%_sbindir/grub-bios-setup
%_sbindir/grub-macbless
%endif
%_sbindir/grub-install
%_sbindir/grub-mkconfig
%_sbindir/grub-ofpathname
%_sbindir/grub-probe
%_sbindir/grub-reboot
%_sbindir/grub-set-default
%_sbindir/grub-sparc64-setup
%_sbindir/grub-entries
%_sbindir/update-grub
%_bindir/grub-editenv
%_bindir/grub-file
%_bindir/grub-fstest
%_bindir/grub-glue-efi
%_bindir/grub-kbdcomp
%_bindir/grub-menulst2cfg
%_bindir/grub-mknetdir
%_bindir/grub-mkstandalone
%_bindir/grub-mkfont
%_bindir/grub-mklayout
%_bindir/grub-mkimage
%_bindir/grub-mkpasswd-pbkdf2
%_bindir/grub-mkrelpath
%_bindir/grub-mkrescue
%_bindir/grub-script-check
%_bindir/grub-syslinux2cfg
%_datadir/grub/grub-mkconfig_lib
%_man1dir/*
%ifarch x86_64
%exclude %_man1dir/grub-render-label*
%exclude %_man8dir/grub-bios-setup*
%exclude %_man8dir/grub-macbless*
%endif
%_man8dir/*
%_infodir/grub.info.*
%_infodir/grub-dev.info.*

%ifarch %ix86 x86_64
%files pc
%_sbindir/grub-autoupdate
%_libdir/grub/*-pc/
%endif

%ifarch ppc64le
%files ieee1275
%_sbindir/grub-autoupdate
%_libdir/grub/*-ieee1275/
%endif

%ifarch %efi_arches
%files efi
%_efi_bindir/grub%{efi_suff}.efi
%if_with sb_kern_signature_check_relaxed
%_efi_bindir/grub%{efi_suff}sb.efi
%endif
%ifarch x86_64
%_efi_bindir/grubia32.efi
%if_with sb_kern_signature_check_relaxed
%_efi_bindir/grubia32sb.efi
%endif
%_libdir/grub/i386-efi
%endif
%_sbindir/grub-efi-autoupdate
%_libdir/grub/%grubefiarch
%endif

%ifarch %ix86 x86_64 ppc64le
%ifarch %ix86 x86_64
%post pc
%endif
%ifarch ppc64le
%post ieee1275
%endif
grub-autoupdate || {
	echo "** WARNING: grub-autoupdate failed, NEXT BOOT WILL LIKELY FAIL NOW"
	echo "** WARNING: please run it by hand, record the output offline,"
	echo "** WARNING: make sure you have bootable rescue CD/flash media handy"
	echo "** WARNING: and try \`grub-install /dev/sdX' manually"
} >&2
%endif

%post efi
modprobe efivars
grep -q '^GRUB_DISTRIBUTOR=' %_sysconfdir/sysconfig/grub2 ||
	echo 'GRUB_DISTRIBUTOR="ALT Linux"' >> %_sysconfdir/sysconfig/grub2

grep -q '^GRUB_BOOTLOADER_ID=' %_sysconfdir/sysconfig/grub2 ||
	echo 'GRUB_BOOTLOADER_ID="altlinux"' >> %_sysconfdir/sysconfig/grub2

grub-efi-autoupdate || {
	echo "** WARNING: grub-efi-autoupdate failed, NEXT BOOT WILL LIKELY FAIL NOW"
	echo "** WARNING: please run grub-efi-autoupdate by hand, record the output offline,"
	echo "** WARNING: make sure you have e.g. rEFInd bootable media handy."
} >&2

%changelog
* Thu Jan 23 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt22
- fix debian-install_signed patch (closes: #37664)
- spec: remove useless pesigning from install section
  + fix license
  + move rpm-macros-uefi to BR(pre):

* Mon Jan 20 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt21
- spec: add crypto modules into EFI binary images to support LUKS encrypted
  partition booting without dedicated unenctypted /boot partition alongside
  (closes: #37663)

* Fri Nov 29 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt20
- improve third-party customizer programs compatibility
  + grub2-sysconfig: add GRUB_BACKGROUND definition
  + rework altlinux-theme patch for conditional default colors application
- spec: sed autogen.sh to choose python3 interpreter explicitly

* Tue Oct 29 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt19
- grub-ieee1275: added R: powerpc-utils. (glebfm@)
- add xfs-sparse-inodes patch (closes: #37394)

* Tue Aug 13 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt18
- add extcmd and keystatus modules to EFI images (closes: #36722)

* Fri Jun 14 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.02-alt17
- Refactored %%build and %%install sections;
- Added grub-ieee1275 support for ppc64le architecture;
- %%ix86: renamed efi image files to grubia32{,sb}.efi ;
- spec:
  + removed unpackaged files;
  + added ExclusiveArch tag to skip build on unsupported architectures.

* Tue Mar 19 2019 Leonid Krivoshein <klark@altlinux.org> 2.02-alt16
- grub-entries script: variables initialization added

* Tue Feb 12 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt15
- add rhboot/grub2 SB patch set to prevent unauthorized code execution at boot time when SB is enabled
- add grub-entries script by klark@ for list grub menu (closes: #36048)
- add patch preventing boot failure for unsigned kernel in SB environment
  + add an optional patch application flag for convenience

* Mon Dec 10 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt14
- added patch from upstream with changes for default pit time source to ptimer

* Thu Nov 29 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt13
- fix FTBFS by adding suse-fix-build-with-gcc8 patch
- fix FTBFS by adding fix-binutils-break-grub-efi-build patch
- remove ubt

* Mon Jun 25 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.02-alt12
- add ia32 EFI binary to x86_64 package
- add a patch adopted from fedora one introducing linuxefi/initrdefi commands
- add ia32 grub modules to package
  + add embedded config into ia32 EFI coreimage
  + rename x64 EFI binary to grubx64.efi
  + add grub-efi-autoupdate ia32 EFI compatibility

* Wed May 30 2018 Oleg Solovyov <mcpain@altlinux.org> 2.02-alt11
- LVM+LUKS fixes:
  + write UUID to grub.cfg after installation
  + don't skip devices under /dev/mapper/

* Fri May 25 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt10
- removed xxd requires from efi firmware setup script

* Mon May 21 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt9
- fixed config generation errors on EFI platform (closes: #34852)

* Sun May 13 2018 Leonid Krivoshein <klark@altlinux.org> 2.02-alt8
- write to read-only grub device problem fixed.

* Mon Apr 16 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt7
- revert back the LVM+LUKS fixes from alt6

* Mon Apr 16 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt6
- add ubt for backporting

* Mon Apr 16 2018 Oleg Solovyov <mcpain@altlinux.org> 2.02-alt6
- LVM+LUKS fixes:
  + write UUID to grub.cfg after installation
  + fix empty root parameter after update-grub

* Thu Mar 29 2018 Anton Farygin <rider@altlinux.ru> 2.02-alt5
- more grub-efi modules enabled by default:
  part_apple part_msdos xfs squash4 search_fs_file search_label sleep  test syslinuxcfg video 
  gfxterm_background lvm lsefi efifwsetup cat gzio iso9660 loadenv loopback mdraid09 mdraid1x 
  png jpeg
- added patch from ubuntu for efi setup menu entry (closes: #34467)
- filetrigger and configs moved from pc/efi packages to common part

* Sat Dec 02 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt4
- interaction between the user and the shift key at boot time interrupts the grub wait timeout (closes: #33655)

* Thu Nov 30 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt3
- fixed sysconfig/grub2 usage in grub-efi post script (closes: #34258)
- fixed Xen menu entry  (closes: #32811)

* Tue Jul 18 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt2
- renamed from grub2 to grub
- added strong requires to efibootmgr >= 15

* Sat Jun 17 2017 Anton Farygin <rider@altlinux.ru> 2.02-alt1
- add ubt for backporting process

* Mon Jun 05 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.02-alt1
- 2.02 released

* Tue May 10 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.02-alt0.3
- 2.02 beta3

* Wed Dec 02 2015 Michael Shigorin <mike@altlinux.org> 2.00-alt21
- CVE-2015-8370: those who have set up GRUB passwords MUST
  upgrade or find their use of this "protection" inefficient:
  http://hmarco.org/bugs/CVE-2015-8370-Grub2-authentication-bypass.html
  (closes: #31631)
- added fedora patch to piggyback --unrestricted through CLASS
  thus changing the default for password-protected menuentry items
  to request password only when an attempt to change boot parameters
  is made (but to let the system boot by default); see also
  http://altlinux.org/grub#password
- added upstream texinfo patch to fix FTBFS
- explicit BR: texinfo

* Tue Dec 17 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt20
- updated pesign macros use, reworked binaries installation
- prepare for production signing

* Wed Nov 27 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt19
- rebuilt with current gnu-efi
- pesign with ALT key

* Tue Nov 26 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt18
- adapted debian patch to accept os-prober output for EFI binaries
  (see also RH#972355, RH#873207, deb#698914)

* Sat Nov 16 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt17
- updated grub-2.00-os-alt.patch for 2.00 (closes: #29583)

* Thu Oct 31 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt16
- 39_memtest: warning goes to stderr now and not into grub.cfg

* Thu Oct 24 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt15
- 39_memtest: support separate /boot properly (closes: #29460)

* Wed Jul 24 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt14
- efi: try loading efivars.ko just in case, no harm and no use otherwise

* Thu May 23 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt13
- firsttime: dropped (closes: #28966)

* Mon Mar 04 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt12
- better UEFI boot label support (mind the sysconfig fixes)
- dropped patch8 (irrelevant)

* Mon Feb 18 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt11.2
- revert patch suggested in #28218 (results in black-on-black text menu)

* Thu Feb 07 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt11.1
- firsttime: i18n support

* Thu Jan 31 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt11
- make grub less bold with its noisy opinions (closes: #25778)
- cas@: updated 05_altlinux_theme (closes: #28218)
- skip memtest in EFI mode
- changed default font from dejavu sans mono to univga

* Thu Jan 31 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt10
- whoops, actually added grub-efi-autoupdate script (closes: #28485)
- tweaked both grub-autoupdate and posttrans filetrigger
  to be almost quiet in EFI case

* Wed Jan 23 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt9
- efi subpackage is signed by default on x86_64
- introduced efi-unsigned subpackage with a clean copy
- initial grub-2.00-install-uefi-signed.patch based on
  ubuntu_install_signed.patch from 2.00-11ubuntu1 package
- initial efi postinstall update script

* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 2.00-alt8
- introduced efi-signed subpackage (x86_64 only)
- use rpm-macros-uefi

* Thu Dec 06 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt7
- dropped patch4 (see also #28181)

* Tue Dec 04 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt6
- cas@ fixed wrong path in theme patch (closes: #28176)
- introduced /etc/default/grub "compat" symlink
- dropped /boot/efi/* due to complete lack of applicability

* Thu Nov 22 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt5
- maintenance release:
  + fixed filetrigger lapse (thanks crux@, see also #27916)
  + grub2-common is now aware of grub-0.9x symlink (closes: #27935)

* Tue Nov 13 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt4
- initial EFI support merge
- NB: grub2-pc package got split into -pc and -common,
  please double-check that things went well

* Mon Nov 05 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt3
- try harder to warn that the configuration is not complete
  for automated grub upgrades thus needs to be updated manually
  (closes: #27916)
- adapted update-grub(8) from debian

* Sun Nov 04 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt2
- applied upstream patch to revert broken fix resulting in wrong
  assessment of core.img size and a failure to install grub:
  http://bzr.savannah.gnu.org/lh/grub/trunk/grub/revision/4586
  (closes: #25666)

* Fri Oct 26 2012 Michael Shigorin <mike@altlinux.org> 2.00-alt1
- 2.00 (closes: #27803)
- updated patches
  + fixed 05_altlinux_theme (closes: #27642)
- built with devmapper support
  + alterator-grub needs one-line fix to work again on mdraid though
- updated an Url: (closes: #26901)
- added a redundant but compatible unicode.pf2 font file
  (might be split off to a separate subpackage soonish)

* Fri May 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt9
- fix build with automake >= 1.11.2

* Mon Aug 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt8
- rename to grub2-pc
- fix build

* Fri Jul 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt7
- force grub config update on grub update

* Tue Jun 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt6
- increase probability of race winning during install on evms device
  (ALT #25628) again

* Wed Jun 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt5
- shaba@ (ALT #25666):
  build with -Os optimization
  add LZMA support
- shaba@: add man pages

* Tue May 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt4
- remove 'with Linux' within linux-only entries

* Fri May 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt3
- fix adding failsafe options to non-failsave cmdline (ALT #25676)
- change 'splash=silent' to 'splash' in default sysconfig

* Thu May 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt2
- disable floppies handling (ALT #24974)

* Fri May 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt1
- 1.99
- fix absolute pathnames during install (ALT #25444)

* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt24.20100804
- fix grub-1.98-evms-crap-alt.patch for /dev/vd* devices (ALT #25497)

* Wed Feb 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt23.20100804
- remove buggy brain which sets gfxpayload=keep in 10_linux
- mention timeout features in sysconfig
- mention GRUB_PRELOAD_MODULES in sysconfig

* Mon Jan 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt22.20100804
- add options to /ets/sysconfig/grub2:
  GRUB_AUTOUPDATE_CFG,GRUB_AUTOUPDATE_CFGNAME to control automatic config
   update
  GRUB_VMLINUZ_SYMLINKS to control symlinks handling in /boot/vmlinuz*
  GRUB_VMLINUZ_FAILSAFE to control failsafe entries
- temporary remove ntldr-img from grub-extras

* Fri Oct 29 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt21.20100804
- place default font in /boot/grub (ALT #24446)
- fix initrd finding (ALT #24442)

* Thu Oct 28 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.98-alt20.20100804
- fix this unhappy firsttime script
- use UUIDs for flavoured entries

* Wed Oct 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.98-alt19.20100804
- firsttime script added

* Mon Oct 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt18.20100804
- add GRUB_AUTOUPDATE_DEVICE and GRUB_AUTOUPDATE_FORCE options for
  automatic grub update (ALT #24114)

* Mon Sep 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt17.20100804
- update grub-1.98-evms-crap-alt.patch (evms/lvm2)

* Wed Sep 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt16.20100804
- make grub menu look tuneable with /etc/sysconfig/grub2

* Wed Sep 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt15.20100804
- hackaround: update evms-crap-alt.patch (strip devmapper for el-smp kernel)

* Wed Aug 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt14.20100804
- 20100804 snapshot
- add gettext to Requires (ALT #23845)

* Fri Jun 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt13
- update grub menu in filetrigger (ALT #23332)
- fix memtest finding

* Wed Apr 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt12
- add space before (failsafe mode) (ALT #23361)
- fix default xen initrd name

* Mon Apr 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt11
- add memtest and xen detection
- set localedir

* Fri Apr 16 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt10
- do not provide grub
- fix for evms/lvm device probing

* Mon Apr 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt9
- add 904_disable_floppies.patch from debian
- mark %_sysconfdir/grub.d/40_custom as config(noreplace)
- add Provides/Obsoletes for grub

* Tue Mar 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt8
- add 950-quick-boot.patch from debian
- enable savedefault feature by default

* Mon Mar 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt7
- remove evms crap in one more place

* Fri Mar 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt6
- make evms-crap-alt patch more common

* Fri Mar 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt5
- rewrite stupid evms-crap-alt patch

* Thu Mar 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt4
- remove evms crap (for installer)

* Tue Mar 09 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt3
- fix bug in default menuentries

* Mon Mar 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt2
- boot default (/boot/vmlinuz) kernel first
- change default font to 8x13

* Sat Mar 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.98-alt1
- 1.98

* Sat Jan 30 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.97-alt3
- 1.97.2

* Thu Jan 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.97-alt2
- add patches from fedora (initramfs,os name)
- remove buggy grub2-helper-10_altlinux
- make /etc/sysconfig/grub2 useful

* Mon Jan 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.97-alt1
- 1.97

* Fri Jun 19 2009 Denis Kuznetsov <dek@altlinux.ru> 1.96-alt2
- Fixed #20475

* Thu Jun 11 2009 Denis Kuznetsov <dek@altlinux.ru> 1.96-alt1
- Initial build for Sisyphus

