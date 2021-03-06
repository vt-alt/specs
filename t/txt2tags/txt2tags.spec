Name: txt2tags
Version: 2.7
Release: alt0.1.dev.gitd737c8e
Epoch: 1

Summary: Converts text files to HTML, XHTML, sgml, LaTeX, man...
License: GPL-2.0
Group: Text tools
URL: http://txt2tags.sourceforge.net/
# VCS: https://github.com/txt2tags/txt2tags
Source: %name-%version.tar
BuildArch: noarch

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python
%if_with docs
BuildRequires: %name
%endif

%description
Txt2tags is a generic text converter. From a simple text file with minimal
markup, it generates documents on the following formats: HTML, XHTML, sgml,
LaTeX, Lout, man, Magic Point (mgp), MoinMoin and Adobe PageMaker. Supports
heading, font beautifiers, verbatim, quote, link, lists, table and image.
There are GUI, Web and cmdline interfaces. It's a single Python script and
no external commands or libraries are needed.

%prep
%setup
# Set correct python2 executable in shebang
subst 's|#!.*python$|#!%__python|' $(grep -Rl '#!.*python$' *)

%build
%python_build
for file in $(ls -1 po/*.po); do
	msgfmt -o ${file//.po/.mo} $file
done

%install
%python_install
# locale files
for file in $(ls -1 po/*.mo); do
        basename=${file##po/}
        lang=${basename%%.mo}
        %__install -Dp -m0644 $file %buildroot%_datadir/locale/$lang/LC_MESSAGES/txt2tags.mo
done
%find_lang %name

%files -f %name.lang
%doc AUTHORS README samples/
%_bindir/*
%python_sitelibdir/*

%changelog
* Sat Apr 18 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.7-alt0.1.dev.gitd737c8e
- New version.
- Build without man pages.

* Fri Apr 17 2020 Andrey Cherepanov <cas@altlinux.org> 3.7-alt1
- New version.

* Wed Apr 15 2020 Andrey Cherepanov <cas@altlinux.org> 2.6-alt1.2
- Set correct python2 executable in shebang
- Fix License tag according to SPDX.
- Package localization files.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6-alt1.1
- Rebuild with Python-2.7

* Wed Jan 12 2011 Alex Negulescu <alecs@altlinux.org> 2.6-alt1
- version up

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.5-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * macos-resource-fork-file-in-package for txt2tags
  * postclean-05-filetriggers for spec file

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Alex Negulescu <alecs@altlinux.org> 2.5-alt1
- Initial package
