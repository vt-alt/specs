Name: scons
Version: 4.0.1
Release: alt1

Summary: an Open Source software construction tool
Summary(ru_RU.UTF-8): Open Source средство для сборки ПО

License: MIT
Group: Development/Python
Url: http://www.scons.org

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

Source: %name-src-%version.tar

Obsoletes: scons-doc < %version-%release
Provides: scons-doc = %version-%release

%description
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software.  SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax.  SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines.  SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched.  SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.

%description -l ru_RU.UTF-8
SCons -- открытое средство для сборки ПО -- представляет из себя улучшенную
замену классической утилите Make; это лучший способ собрать ПО. SCons
использует дизайн, победивший на соревновании средств для сборки ПО Software
Carpentry в августе 2000г.

Так как конфигурационные файлы SCons -- скрипты на языке Python, нет надобности
осваивать новый синтаксис для средства сборки ПО. SCons отслеживает общий список
зависимостей в дереве исходных текстов, он умеет сканировать исходные тексты
(или другие файлы) на предмет неявных зависимостей, таких как файлы, указанные
в строках #include. SCons использует подписи MD5 для того, чтобы
перекомпилировать только те файлы, чьё содержание действительно изменилось, а не
когда только изменилось время создания. SCons может быть легко расширен за счёт
определяемых пользователем объектов Builder и/или Scanner.

%prep
%setup -n %name-src-%version
sed -i 's|/usr/bin/env python|/usr/bin/python3|' scripts/*
sed -i 's|/usr/bin/env python|/usr/bin/python3|' bin/*

%build
%python3_build

%install
%python3_install \
    --install-scripts=%_bindir \
    --install-data=%_datadir

# Remove dead code generating garbage dependency
rm -fr %buildroot%python3_sitelibdir_noarch/SCons/Tool/docbook/docbook-xsl-1.76.1

# Add symlink for compability with Fedora and Mageia
ln -s scons %buildroot%_bindir/scons-3

%files
%doc LICENSE CHANGES.txt README.rst RELEASE.txt
%_bindir/*
%python3_sitelibdir_noarch/SCons
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Thu Aug 6 2020 Vladimir Didenko <cow@altlinux.org> 4.0.1-alt1
- 4.0.1

* Thu Dec 5 2019 Vladimir Didenko <cow@altlinux.org> 3.1.1-alt2
- add scons-3 symlink (closes: 37578)
- fix license name

* Thu Aug 29 2019 Vladimir Didenko <cow@altlinux.org> 3.1.1-alt1
- 3.1.1

* Fri Jul 5 2019 Vladimir Didenko <cow@altlinux.org> 3.0.5-alt1
- 3.0.5
- switch to Python 3

* Mon Jan 29 2018 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1
- Version 2.3.3

* Thu Apr 18 2013 Evgeny Sinelnikov <sin@altlinux.ru> 2.3.0-alt1
- Update to 2.3.0

* Sun Jan 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0.d20100117-alt1.1
- Rebuild with Python-2.7 (bootstrap without docs)

* Tue Mar 02 2010 Evgeny Sinelnikov <sin@altlinux.ru> 1.2.0.d20100117-alt1
- 1.2.0.d20100117 release.
- Build docs with epydoc-3.0.1-alt2 with Gentoo fixes (#287546, #288273)

* Mon Jan 11 2010 Evgeny Sinelnikov <sin@altlinux.ru> 1.2.0.d20091224-alt1
- 1.2.0.d20091224 release (Closes: 22540, 22689).

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.1
- Rebuilt with python 2.6
- TODO: need rebuild with texlive

* Mon Nov 03 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.0-alt1
- 1.1.0 release.

* Tue Aug 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.0.0-alt2
- Build and package compiled documentation

* Tue Aug 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.0.0-alt1
- 1.0.0 release.
- Changed summary and description encoding to UTF-8

* Tue Aug 28 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.97-alt2
- Applied patch fixing linkage problems due to as-needed (thx gvy@).

* Tue May 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.97-alt1
- 0.97 release.

* Tue May 01 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.96.96-alt1
- 0.96.96 release.
- Fixed building on x86_64.

* Sat Dec 09 2006 Yury Aliaev <mutabor@altlinux.ru> 0.96.93-alt1
- version 0.96.93

* Thu May 25 2006 Vitaly Lipatov <lav@altlinux.ru> 0.96.92-alt0.1
- NMU: new version 0.96.92 (with rpmrb script)
- fix Source URL

* Mon Jun 20  2005 Vitaly Lipatov <lav@altlinux.ru> 0.96.90-alt2
- NMU: new version
- cleanup spec

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.96.1-alt1.1
- Rebuilt with python-2.4.

* Sat Feb 26 2005 Yury Aliaev <mutabor@altlinux.ru> 0.96.1-alt1
- updated to 0.96.1
- spec adopted for new version features
- splitted into two packages, scons and scons-doc

* Wed Nov 19 2003 Yury Aliaev <mutabor@altlinux.ru> 0.94-alt1
- updated to new version
- spec cleanup

* Sat Nov 01 2003 Yury Aliaev <mutabor@altlinux.ru> 0.93-alt1
- alt 1
- initial release, spec cleanup
- based on original spec by Steven Knight <knight@scons.org>
