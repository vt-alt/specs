%define _unpackaged_files_terminate_build 1

Name: mpg321
Version: 0.3.2
Release: alt2
Summary: A Free command-line mp3 player, compatible with mpg123
Summary(ru_RU.UTF-8): mp3 плейер c интерфейсом командной строки, совместимый с mpg123
Group: Sound
License: GPLv2+
Url: http://mpg321.sourceforge.net/

Source0: %{name}_%{version}.orig.tar

# Patches from Gentoo
Patch1: mpg321-0.3.2-format-security.patch
Patch2: mpg321-0.3.2-CVE-2019-14247.patch
Patch3: mpg321-0.3.2-gcc10.patch

# Patches from ALT
Patch100: mpg321-0.3.2-alt-build.patch

# whether to replace mpg123 or not?
# on PII 350Mhz mpg321 uses 25 percents CPU time against 4.5 percents for mpg123.
%define REPLACE_123 0

%if %REPLACE_123
Provides: mpg123 = 0.59q
%endif

%define mad_ver 0.14.2b

# Automatically added by buildreq on Mon Nov 26 2012
# optimized out: zlib-devel
BuildRequires: libao-devel libid3tag-devel libmad-devel

%description
A Free command-line mp3 player, compatible with mpg123. mpg321 is a clone
of the popular mpg123 command-line mp3 player. It should function as a
drop-in replacement for mpg123 in many cases. While some of the
functionality of mpg123 is not yet implemented, mpg321 should function
properly in most cases for most people, such as for frontends such as
gqmpeg.

mpg321 is based on the mad MPEG audio decoding library. It therefore is
highly accurate, and also uses only fixed-point calculation, making it
more efficient on machines without a floating-point unit.

While mpg321 is not as fast as the non-free mpg123 on systems which have
a floating point unit, it comes under a fully Free license, which allows
greater freedom to its users. For most people who want mpg123, mpg321 is
a better alternative.

%description -l ru_RU.UTF-8
mpg321 - проигрыватель mp3 файлов с интерфейсом командной строки, может
заменить известный проигрыватель mpg123, в отличии от которого имеет
абсолютно свободную лицензию и некоторую дополнительную
функциональность, однако, уступает в производительности.

%prep
%setup -q -n %name-%version-orig
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch100 -p2

%build
%add_optflags -Werror=implicit-function-declaration

%if %REPLACE_123
%configure \
    --enable-alsa=no \
    --enable-ipv6
%else
%configure \
    --enable-mpg123-symlink=no \
    --enable-alsa=no \
    --enable-ipv6
%endif

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS BUGS HACKING NEWS README README.remote THANKS
%_bindir/*
%_man1dir/*

%changelog
* Tue Oct 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt2
- Applied patches from Gentoo (Fixes: CVE-2019-14247).

* Mon Nov 26 2012 Igor Zubkov <icesik@altlinux.org> 0.3.2-alt1
- 0.2.11 -> 0.3.2
- Enable IPv6
- Add -debuginfo subpackage

* Wed Dec 23 2009 Igor Zubkov <icesik@altlinux.org> 0.2.11-alt1
- 0.2.10.2 -> 0.2.11

* Tue Mar 20 2007 Igor Zubkov <icesik@altlinux.org> 0.2.10.2-alt1.1
- NMU
- rebuild with new gcc flags (-Wl,--as-needed)

* Tue Jul 26 2005 Michael Shigorin <mike@altlinux.org> 0.2.10.2-alt1
- security fix for #7465 (CVE-2003-0969: format string vulnerability)
- tarball updated from security.debian.org

* Mon Oct 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.10-alt3
- fixed %%build

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.10-alt2
- rebuild with gcc-3.2

* Sun Mar 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.10-alt1
- 0.2.10 

* Tue Mar 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.9-alt1
- 0.2.9 

* Tue Jan 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.3-alt1
- First build for Sisyphus
