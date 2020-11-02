%define _unpackaged_files_terminate_build 1

Name: icmake
Version: 9.03.01
Release: alt1
Summary: Hybrid between a 'make' utility and a 'shell script' language
License: GPLv3
Group: Development/Tools
Url: https://gitlab.com/fbb-git/icmake

# https://gitlab.com/fbb-git/icmake.git
Source: %name-%version.tar

%description
Icmake is a hybrid between a 'make' utility and a 'shell script'
language.  Originally, it was concocted to provide a useful tool for
automatic program maintenance and system administrative tasks on MS-DOS
platforms.  As we learned to appreciate its flexibility, Icmake was
eventually ported to Unix platforms (SCO and Linux). By now Icmake also
runs on a HP-Unix platform.

%package doc
Summary: Documentation for Icmake
Group: Development/Documentation
BuildArch: noarch

%description doc
Icmake is a hybrid between a 'make' utility and a 'shell script'
language.  Originally, it was concocted to provide a useful tool for
automatic program maintenance and system administrative tasks on MS-DOS
platforms.  As we learned to appreciate its flexibility, Icmake was
eventually ported to Unix platforms (SCO and Linux). By now Icmake also
runs on a HP-Unix platform.

This package contains documentation for Icmake.

%prep
%setup

%build
pushd %name
./icm_prepare /
./icm_bootstrap /
popd

./manpages

%install
pushd %name
./icm_install all %buildroot
popd

%files
%doc %name/changelog %name/doc/*.doc
%_sysconfdir/*
%_bindir/*
%_libexecdir/%name
%_datadir/%name
%_man1dir/*
%_man7dir/*

%files doc
%_docdir/%name
%_docdir/icmake-doc

%changelog
* Wed Oct 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 9.03.01-alt1
- Updated to upstream version 9.03.01.

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.21.01-alt1.git20140120
- Version 7.21.01

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.21.00-alt1.git20130802
- Version 7.21.00

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.00-alt1.git20120722
- Version 7.19.00

* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.16.00-alt1
- Initial build for Sisyphus

