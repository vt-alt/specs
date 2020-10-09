%define _unpackaged_files_terminate_build 1

Name: rzip
Version: 2.1
Release: alt3
License: GPL
Summary: A large-file compression program 
Summary(ru_RU.UTF-8): Программа для сжатия очень больших файлов
Group: Archiving/Compression
URL: https://rzip.samba.org

# http://rzip.samba.org/ftp/rzip/%name-%version.tar.gz
Source: %name-%version.tar

Patch1: rzip-2.1-CVE-2017-8364.patch

BuildRequires: bzlib-devel

%description
rzip  is a file compression program designed to do particularly well on
very large files containing long distance redundency.

%description -l ru_RU.UTF-8
rzip - это программа для сжатия, специально предназначенная для работы с
очень большими файлами, в следствие чего работает только с ними, не
поддерживая "трубы" (pipes) и прочее.

%prep
%setup
%patch1 -p1

%build
%configure

%make_build

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir

install -m 755 %name %buildroot%_bindir/
install -m 644 %name.1 %buildroot%_man1dir/

%files
%doc COPYING
%_bindir/rzip
%_man1dir/rzip.1*

%changelog
* Thu Aug 22 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1-alt3
- Applied security fix from Gentoo (Fixes: CVE-2017-8364)

* Wed Sep 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1-alt2
- Updated spec to allow any man page compression.
- Converted summary and description to UTF-8.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Oct 10 2006 Andrew Kornilov <hiddenman@altlinux.ru> 2.1-alt1
- New version
* Sun Jul 10 2005 Andrew Kornilov <hiddenman@altlinux.ru> 2.0-alt4
- Fixed permissions (#6015)

* Wed Aug 04 2004 Andrew Kornilov <hiddenman@altlinux.ru> 2.0-alt3
- Addes bzlib-devel to buildrequires

* Mon Mar 22 2004 Andrew Kornilov <hiddenman@altlinux.ru> 2.0-alt2
- Fixed few typos in spec, added spec translation to Russian

* Mon Mar 15 2004 Andrew Kornilov <andy@eva.dp.ua> 2.0-alt1
- First build for Sisyphus
