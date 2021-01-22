%define _unpackaged_files_terminate_build 1

%set_verify_elf_method strict,lint=relaxed

Name: gif2png
Version: 3.0.0
Release: alt2.git.a9592ae
Summary: A GIF to PNG converter
Group: Graphics
License: BSD-2-Clause
Url: http://catb.org/~esr/gif2png/

# https://gitlab.com/esr/gif2png
Source: %name-%version.tar
Patch1: gif2png-2.5.8-alt-web2png.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: python-modules xmlto

%description
The gif2png program converts files from the obsolescent Graphic
Interchange Format to Portable Network Graphics.  The conversion
preserves all graphic information, including transparency, perfectly.
The gif2png program can even recover data from corrupted GIFs.

There exists a 'web2png' program in a separate package which is able
to convert entire directory hierarchies.

%package -n web2png
Summary: A GIF to PNG converter for entire directory hierarchies
Group: Graphics
Requires: %name = %EVR
BuildArch: noarch

%description -n web2png
The gif2png program converts files from the obsolescent Graphic
Interchange Format to Portable Network Graphics.  The conversion
preserves all graphic information, including transparency, perfectly.
The gif2png program can even recover data from corrupted GIFs.

The distribution also includes a Python script, web2png, that will
convert entire web hierarchies (images and HTML or PHP pages).

%prep
%setup
%patch1 -p1

mkdir -p src/golang.org/x
cp -r %go_root/src/cmd/vendor/golang.org/x/sys src/golang.org/x/
cp -r %go_root/src/cmd/vendor/golang.org/x/crypto src/golang.org/x/

%build
export GOPATH="$(pwd):%go_path"
export CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS)"

%make_build

%install
%makeinstall_std

%check
%make_build -k -C test

%files
%doc NEWS README
%_bindir/gif2png
%_man1dir/gif2png.1*

%files -n web2png
%_bindir/web2png
%_man1dir/web2png.1*

%changelog
* Thu Jan 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt2.git.a9592ae
- Applied go macros for P9 compatibility.

* Wed Jan 20 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt1.git.a9592ae
- Updated to latest upstream snapshot (Fixes: CVE-2019-17371).

* Thu Mar 21 2019 Dmitry V. Levin <ldv@altlinux.org> 2.5.13-alt1
- 2.5.11 -> 2.5.13.

* Wed Jul 15 2015 Dmitry V. Levin <ldv@altlinux.org> 2.5.11-alt1
- 2.5.8 -> 2.5.11.

* Mon Sep 17 2012 Dmitry V. Levin <ldv@altlinux.org> 2.5.8-alt1
- Updated to 2.5.8.
- Moved web2png to separate subpackage.

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.1-alt1.2.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.5.1-alt1.1
- Rebuilt with python-2.5.

* Sun Nov 26 2006 Dmitry V. Levin <ldv@altlinux.org> 2.5.1-alt1
- Updated to 2.5.1.
- Imported patches from Debian gif2png_2.5.1-3 package.

* Mon Oct 21 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.6-alt1
- 2.4.6

* Thu Jun 20 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.4-alt1
- 2.4.4

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.2-alt1
- 2.4.2
- Rebuilt with libpng.so.3

* Wed Jun 27 2001 Stanislav Ievlev <inger@altlinux.ru> 2.4.1-ipl2
- Rebuilt with python-2.1

* Wed Feb 28 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.1-ipl1
- 2.4.1

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.0-ipl1
- Initial revision.
