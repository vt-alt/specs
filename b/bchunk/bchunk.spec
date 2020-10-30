%define _unpackaged_files_terminate_build 1

Name: bchunk
Version: 1.2.2
Release: alt1
Summary: A CD image format converter from .bin/.cue to .iso/.cdr/.wav
Summary (ru_RU.UTF-8): Преобразователь образов CD из формата .bin/.cue в .iso/.cdr/.wav
License: GPL-2.0+
Group: Archiving/Cd burning
Url: http://he.fi/bchunk/

# https://github.com/hessu/bchunk.git
Source: %name-%version.tar

Patch1: %name-alt.patch

%description
The bchunk package contains a UNIX/C rewrite of the BinChunker program.
BinChunker converts a CD image in a .bin/.cue format (sometimes .raw/.cue)
into a set of .iso and .cdr/.wav tracks.  The .bin/.cue format is used by some
non-UNIX CD-writing software, but is not supported on most other
CD-writing programs.

%description -l ru_RU.UTF-8
Пакет bchunk содержит UNIX версию программы BinChunker. BinChunker
преобразует образы компакт-дисков в формате .bin/.cue (иногда .raw/.cue)
в набор .iso и .cdr/.wav файлов-дорожек. Формат .bin/.cue используется
в нескольких программах записи компакт-дисков не для UNIX.

%prep
%setup
%patch1 -p1

%build
export CFLAGS="%optflags"
%make_build

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
install -m 755 bchunk %buildroot%_bindir
install -m 644 bchunk.1 %buildroot%_man1dir

%files
%doc COPYING
%doc README ChangeLog
%_bindir/bchunk
%_man1dir/bchunk.1*

%changelog
* Wed Oct 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.2-alt1
- Updated to upstream version 1.2.2 (Fixes: CVE-2017-15953, CVE-2017-15954, CVE-2017-15955).

* Thu Oct 28 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.2.0-alt1
- 1.2.0 thx to Aleksandr Blokhin!

* Thu Aug 28 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.1.1-alt1
- ALTLinux build
