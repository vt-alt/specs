# requires pandoc
%def_enable docs

Name: android-tools
Version: 8.1.0
Release: alt2.r23

Summary: Android Debug CLI tools
License: APL
Group: Development/Tools

Url: http://developer.android.com/guide/developing/tools/
# For sources use the following repositories:
#  https://android.googlesource.com/platform/system/core
#  https://android.googlesource.com/platform/system/extras
# fetching sources example:
# ANDROID_TAG="android-5.1.1_r38" debian/create-snapshot

Source: %name-%version-%release.tar

# Debian core patches
Patch0: move-log-file-to-proper-dir.patch
Patch1: Added-missing-headers.patch
Patch2: Direct-include-fs_config-header.patch
Patch3: libusb-header-path.patch
Patch4: stdatomic.patch
Patch5: Nonnull.patch
Patch6: ucontext.patch
Patch7: Vector-cast.patch
Patch8: use-Python-3-for-mkbootimg.patch
Patch9: major-minor-moved-to-sysmacros.patch
Patch10: drop-libext4_utils.patch
Patch11: throw-exception-on-unknown-os.patch
Patch12: ENODATA-BSD.patch

# Debian extras patches
Patch20: f2fs_dlutils_library_names.diff
Patch21: remove-duplicated-symbols.patch

# Debian libunwind patches
Patch30: user_pt_regs.patch
Patch31: legacy_built-in_sync_functions.patch
Patch32: 20150704-CVE-2015-3239_dwarf_i.h.patch

# patch from OpenMandriva
Patch100: libcrypto_utils-openssl-1.1.patch
Patch101: adb-system-openssl.patch

# ALT patches
Patch200: alt-libbacktrace-fix-GetErrorString-return.patch
Patch201: alt-make-ext4fs-fix-fs_config-include.patch
Patch202: alt-libunwind-fix-ppc64le-build.patch
#Patch20x: android-tools-5.1.1-boehm-use-stdatomic.patch

Requires: udev-android

BuildRequires: gcc-c++
BuildRequires: p7zip
BuildRequires: libssl-devel zlib-devel libselinux-devel
BuildRequires: libusb-devel libgtest-devel f2fs-tools-devel libsafe-iop-devel
%if_enabled docs
BuildRequires: pandoc
%endif

%description
This package contains following utilities:

Android Debug Bridge (adb) -- it is a versatile tool, which lets you manage the
state of an emulator instance or Android-powered device. Consider "udev-android"
package to used adb without superuser privileges.

Fastboot -- is a diagnostic protocol primarily used to update the flash
filesystem of Android devices over USB.

Mkbootimg -- creates Android boot images that includes kernel image and ramdisk,
in a special format which can be used with fastboot.

Command line tools to create sparse images for usage with Android devices.
Includes simgimg, img2simg, simg2simg, simg_dump and append2simg tools.
Look at /usr/lib/android/bin for binaries.

%prep
%setup
pushd system/core
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
popd
pushd system/extras
%patch20 -p1
%patch21 -p1
popd

pushd system/external/libunwind
%patch30 -p1
%patch31 -p1
%patch32 -p1
popd

pushd system/core
%patch100 -p3
%patch101 -p3

%patch200 -p1
popd

pushd system/extras
%patch201 -p3
popd

pushd system/external/libunwind
%patch202 -p4
popd

%build

%add_optflags %optflags_shared

%define makefilesdir %_builddir/%name-%version/debian/makefiles
%define outbindir %_builddir/%name-%version/out_bin
%define outlibdir %_builddir/%name-%version/out_lib
%define outmandir %_builddir/%name-%version/out_man

%define aprefix %_libdir/android

case %_arch in
    "aarch64")
        CPU="arm64"
        ;;
    "armh")
        CPU="arm"
        ;;
    "i586")
        CPU="x86"
        ;;
    "x86_64")
        CPU="x86_64"
        ;;
    "ppc64le")
        CPU="ppc64"
        ;;
    *)
        false
        ;;
esac

CFLAGS+="%optflags -DNDEBUG -UDEBUG "
CXXFLAGS+="%optflags -DNDEBUG -UDEBUG "
CPPFLAGS+=" -DNDEBUG -UDEBUG "
LDFLAGS+="-Wl,-R%aprefix/lib -L%outlibdir "
DEB_VERSION=%version \
export CFLAGS CPPFLAGS CXXFLAGS LDFLAGS DEB_VERSION CPU

mkdir -p %outbindir
mkdir -p %outlibdir
mkdir -p %outmandir

# building libunwind
pushd system/external/libunwind
CFLAGS=$CFLAGS" -I%_builddir/%name-%version/debian/include" \
      LDFLAGS=$LDFLAGS"%_libdir/p7zip/7z.so " \
      OUT_DIR=%outlibdir \
      make -f %makefilesdir/libunwind.mk
popd

# order is important
core_components_libs=" \
		    liblog \
		    libcutils \
		    libbase \
		    libcrypto_utils \
		    libadb \
 		    libbacktrace \
		    libutils \
		    libziparchive \
		    libsparse"
core_components_tools=" \
        adb \
        fastboot"
core_simg_tools=" \
		    simg2img \
		    simg2simg \
		    img2simg \
		    append2simg"

extras_components_libs=" \
		    libext4_utils \
        libf2fs_utils"
extras_components_tools=" \
        ext4fixup \
        make_ext4fs"

# building core libraries at first
pushd system/core
for i in $core_components_libs; do
    CFLAGS=$CFLAGS" -I../external/libunwind/include" \
          CPPFLAGS=$CPPFLAGS" -I../external/libunwind/include" \
          make -f %makefilesdir/$i.mk
    cp -a $i.so* %outlibdir
done
popd

# now building extra libraries
pushd system/extras
for i in $extras_components_libs; do
    CFLAGS=$CFLAGS" -I../core/include -I../core/libsparse/include" \
          CPPFLAGS=$CPPFLAGS" -I../core/include -I../core/libsparse/include" \
          OUT_DIR=%outlibdir \
          make -f %makefilesdir/$i.mk
done
popd

# building core tools
pushd system/core
for i in $core_components_tools; do
    CFLAGS=$CFLAGS" -I../extras/f2fs_utils" \
          CPPFLAGS=$CPPFLAGS" -I../extras/f2fs_utils" \
          make -f %makefilesdir/$i.mk
    cp -a $i/$i %outbindir
done
# simg stuff requires special handling as it is libsparse-based
for i in $core_simg_tools; do
    CFLAGS=$CFLAGS" -I../extras/f2fs_utils" \
          CPPFLAGS=$CPPFLAGS" -I../extras/f2fs_utils" \
          make -f %makefilesdir/$i.mk
    cp -a libsparse/$i %outbindir
done
popd

# building extra tools
pushd system/extras
for i in $extras_components_tools; do
    CFLAGS=$CFLAGS" -I../core -I../core/include" \
          CPPFLAGS=$CPPFLAGS" -I../core -I../core/include" \
          OUT_DIR=%outbindir \
          make -f %makefilesdir/$i.mk
done
popd

# do not forget about mkbootimg
cp system/core/mkbootimg/mkbootimg %outbindir

%if_enabled docs
# building man pages
pandoc -s -o %outmandir/adb.1 debian/adb.1.md
pandoc -s -o %outmandir/fastboot.1 debian/fastboot.1.md
%endif

%install
mkdir -p %buildroot%_bindir %buildroot%aprefix/bin %buildroot%aprefix/lib %buildroot%_man1dir

for i in adb fastboot mkbootimg; do
    install -pm0755 %outbindir/$i %buildroot%_bindir/$i
done
for i in append2simg ext4fixup img2simg make_ext4fs simg2img simg2simg; do
    install -pm0755 %outbindir/$i %buildroot%aprefix/bin
done

cp -a %outlibdir/* %buildroot%aprefix/lib

for i in adb fastboot; do
    install -pm0644 %outmandir/$i.1 %buildroot%_man1dir
done

mkdir -p %buildroot%_sysconfdir/bash_completion.d
for i in adb fastboot; do
    install -pm0644 debian/bash_completion.d/$i %buildroot%_sysconfdir/bash_completion.d
done

%files
%_bindir/adb
%_bindir/fastboot
%_bindir/mkbootimg
%_man1dir/adb.1*
%_man1dir/fastboot.1*
%_sysconfdir/bash_completion.d/*
%aprefix

%changelog
* Sun Oct 06 2019 Pavel Nakonechnyi <zorg@altlinux.org> 8.1.0-alt2.r23
- udev-android added as a requirement (closes #37284)

* Tue Aug 06 2019 Pavel Nakonechnyi <zorg@altlinux.org> 8.1.0-alt1.r23
- updated to 8.1.0_r23

* Sat Jul 06 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.1.1-alt4
- Fixed build on ppc64le (tnx to Hans Boehm for stdatomic patch).

* Tue Sep 04 2018 Pavel Nakonechnyi <zorg@altlinux.org> 5.1.1-alt3
- rebuilt with OpenSSL 1.1.x

* Tue Aug 21 2018 Pavel Nakonechnyi <zorg@altlinux.org> 5.1.1-alt2
- patches to support OpenSSL 1.1.x are enabled
- fixed bash completions installation

* Wed Mar 15 2017 Pavel Nakonechnyi <zorg@altlinux.org> 5.1.1-alt1
- updated to Debian 5.1.1_r38 release

* Tue Jun 04 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.2-alt1
- 4.2.2 released

* Mon Mar 04 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.1-alt1
- initial
