%define  modulename more-itertools

Name:    python-module-%modulename
Version: 5.0.0
Release: alt2
Epoch: 1

Summary: More routines for operating on iterables, beyond itertools
License: MIT
Group:   Development/Python
URL:     https://github.com/erikrose/more-itertools
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-setuptools

# git://git.altlinux.org/gears/p/python3-module-more-itertools.git
Source:  %modulename-%version.tar

%description
Python's itertools library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/more_itertools*

%changelog
* Wed Apr 03 2019 Dmitry V. Levin <ldv@altlinux.org> 1:5.0.0-alt2
- Removed python3-module-more-itertools subpackage.
- Starting with version 6.0.0 python 2.7 is no longer supported, so
  reverted to 5.0.0 which is the last version targeting Python 2.7.

* Tue Apr 02 2019 Andrey Cherepanov <cas@altlinux.org> 7.0.0-alt2
- Completely fix run from Python 2.

* Sat Mar 30 2019 Andrey Cherepanov <cas@altlinux.org> 7.0.0-alt1
- New version.

* Fri Feb 15 2019 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version.

* Fri Dec 28 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Mon Aug 13 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version.

* Tue Jul 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus
