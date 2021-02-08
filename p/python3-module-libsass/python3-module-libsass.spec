%define  modulename libsass

Name:    python3-module-%modulename
Version: 0.20.1
Release: alt1

Summary: A straightforward binding of libsass for Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/sass/libsass-python

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: gcc-c++
BuildRequires: python3-module-setuptools
BuildRequires: libsass-devel >= 3.4.9

Source:  %modulename-python-%version.tar

%set_verify_elf_method strict
%add_python3_req_skip _sass

%description
This package provides a simple Python extension module sass which is
binding LibSass (written in C/C++ by Hampton Catlin and Aaron Leung).
It's very straightforward and there isn't any headache related Python
distribution/deployment. That means you can add just libsass into your
setup.py's install_requires list or requirements.txt file. Need no Ruby
nor Node.js.

%prep
%setup -n %modulename-python-%version
%__subst "s|-lstdc++|-lsass|" setup.py
pkg-config --modversion libsass > .libsass-upstream-version

%build
%python3_build

%install
%python3_install

%files
%doc CONTRIBUTING.rst README.rst
%_bindir/sassc
%_bindir/pysassc
%python3_sitelibdir/__pycache__/*.pyc
%python3_sitelibdir/*.so
%python3_sitelibdir/sass*
%python3_sitelibdir/pysassc.py
%python3_sitelibdir/*.egg-info

%changelog
* Sun Aug 30 2020 Andrey Cherepanov <cas@altlinux.org> 0.20.1-alt1
- New version.

* Fri May 01 2020 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version.

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.19.4-alt2
- fix libsass linking (ALT bug 37998)

* Mon Nov 04 2019 Andrey Cherepanov <cas@altlinux.org> 0.19.4-alt1
- New version.

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 0.19.3-alt1
- New version.

* Sun Jun 16 2019 Andrey Cherepanov <cas@altlinux.org> 0.19.2-alt1
- New version.

* Mon May 20 2019 Andrey Cherepanov <cas@altlinux.org> 0.19.1-alt1
- New version.

* Mon Mar 18 2019 Andrey Cherepanov <cas@altlinux.org> 0.18.0-alt1
- New version.

* Fri Jan 04 2019 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1
- New version.

* Mon Nov 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1
- New version.

* Fri Nov 16 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.0-alt1
- New version.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 0.15.1-alt1
- New version.

* Tue May 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.13.7-alt1
- Initial build for Sisyphus
