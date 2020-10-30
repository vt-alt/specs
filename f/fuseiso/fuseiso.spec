%define _unpackaged_files_terminate_build 1

Name: fuseiso
Version: 20070708
Release: alt3
Summary: Mount ISO filesystem images as a non-root user
Group: File tools
URL: http://sourceforge.net/projects/fuseiso/
License: GPL-2.0+

Source0: %name-%version.tar

Patch0: fuseiso-20070708-alt-build.patch
# Patches from Gentoo
Patch1: fuseiso-20070708-largeiso.patch
Patch2: fuseiso-20070708-fix-typo.patch
Patch3: fuseiso-20070708-CVE-2015-8837.patch
Patch4: fuseiso-20070708-integer-overflow.patch

# Automatically added by buildreq on Sun Nov 16 2008
BuildRequires: gcc-c++ glib2-devel libfuse-devel zlib-devel

%description
Mount ISO filesystem images as a non-root user. Currently supports
plain ISO9660 Level 1 and 2, Rock Ridge, Joliet, zisofs..
Supported image types: ISO, BIN (single track only), NRG, MDF, IMG (CCD).

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/%name

%changelog
* Thu Oct 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20070708-alt3
- Applied patches from Gentoo (Fixes: CVE-2015-8836, CVE-2015-8837).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 20070708-alt2.qa1
- NMU: rebuilt for debuginfo.

* Sun Nov 16 2008 Igor Zubkov <icesik@altlinux.org> 20070708-alt2
- update Url

* Sun Jun 29 2008 Igor Zubkov <icesik@altlinux.org> 20070708-alt1
- build for Sisyphus

