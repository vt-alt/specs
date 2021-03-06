%define _unpackaged_files_terminate_build 1
%def_enable snapshot
%define modname gidocgen

# mypy too old?
%def_disable check

Name: gi-docgen
Version: 2021.6
Release: alt0.5

Summary: Documentation tool for GObject-based libraries
Group: Development/Other
License: Apache-2.0 or GPL-3.0-or-later
Url: https://pypi.org/project/gi-docgen/

%if_disabled snapshot
Source: https://pypi.io/packages/source/g/%name/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/GNOME/gi-docgen.git
Source: %name-%version.tar
%endif

BuildArch: noarch

Requires: python3 >= 3.6
Requires: %name-templates = %EVR

BuildRequires(pre): meson rpm-build-python3
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-markdown
BuildRequires: python3-module-markupsafe
BuildRequires: python3-module-Pygments
BuildRequires: python3-module-toml
BuildRequires: python3-module-typogrify
%{?_enable_check:BuildRequires: python3-module-flake8 python3-module-mypy}

%description
GI-DocGen is a document generator for GObject-based libraries. GObject is
the base type system of the GNOME project. GI-Docgen reuses the
introspection data generated by GObject-based libraries to generate the API
reference of these libraries, as well as other ancillary documentation.

%package templates
Summary: Templates for GI-DocGen
Group: Development/Other
License: Apache-2.0 or GPL-3.0-or-later and OFL-1.1

%description templates
This package provides basic template data for GI-DocGen.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

# move templates to %_datadir
mkdir -p %buildroot%_datadir/%modname
mv %buildroot%python3_sitelibdir_noarch/%modname/templates %buildroot%_datadir/%modname/
ln -sf ../../../../share/%modname/templates %buildroot%python3_sitelibdir_noarch/%modname/templates

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
%meson_test

%files
%_bindir/%name
%python3_sitelibdir_noarch/%modname/
%_datadir/pkgconfig/%name.pc
%doc README.md

%files templates
%dir %_datadir/%modname
%_datadir/%modname/templates/

%changelog
* Thu Apr 15 2021 Yuri N. Sedunov <aris@altlinux.org> 2021.6-alt0.5
- updated to 2021.5-3-g0b0c237

* Sun Apr 11 2021 Yuri N. Sedunov <aris@altlinux.org> 2021.3-alt0.5
- updated to 2021.2-90-g7fbbaf3

* Sat Mar 13 2021 Yuri N. Sedunov <aris@altlinux.org> 2021.2-alt1
- updated to 2021.2-12-g4ce8f10

* Fri Mar 12 2021 Yuri N. Sedunov <aris@altlinux.org> 2021.1-alt1
- first build for Sisyphus (29ed9ef)



