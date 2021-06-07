%define oname pycdlib

Name:        pycdlib
Version:     1.11.0
Release:     alt1

Summary:     Tools and libraries for working with ISO images
License:     %lgpl21only
Group:       Other
Url:         https://github.com/clalancette/pycdlib
BuildArch:   noarch

Source:      %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-build-licenses
BuildPreReq:        python3-module-setuptools python3-devel

Requires:    %oname-tools = %EVR


%description
PyCdlib is a pure python library to parse, write (master), create, and 
manipulate ISO9660 files. These files are suitable for writing to a CD or USB.

The original ISO9660 (including ISO9660-1999) specification is supported, 
as well the El Torito, Joliet, Rock Ridge, and UDF extensions.

# python3-module-pycdlib
%package -n python3-module-%oname

Summary:        Python library to read and write ISOs
Group:          Development/Python3

%description -n python3-module-%oname
Python library to parse, write (master), 
and create ISO9660 files, suitable for writing to a CD or USB.

# pycdlib-tools
%package -n %oname-tools
Summary:        Tools for working with ISOs
Group:          File tools
Requires:       python3-module-%oname = %EVR

%description -n %oname-tools
Tools to compare, explore, generate and extract files from ISO iamges.

# pycdlib-docs
%package -n %oname-docs
Summary:        Docs for PyCdlib
Group:          Documentation

%description -n %oname-docs
Documentations for PyCdlib.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc COPYING README.md

%files -n %oname-tools
%_bindir/pycdlib-explorer
%_bindir/pycdlib-extract-files
%_bindir/pycdlib-genisoimage
%_mandir/man1/*

%files -n python3-module-%oname
%doc examples/
%python3_sitelibdir/*

%files -n %oname-docs
%doc docs/*.{md,html}


%changelog
* Tue Jun 01 2021 Ivan Razzhivin <underwit@altlinux.org> 1.11.0-alt1
- Update to upstream version 1.11.0 (closes: #40133)

* Mon Jun 24 2019 Ivan Razzhivin <underwit@altlinux.org> 1.7.0-alt1
- Initial build for ALT Linux Sisyphus
