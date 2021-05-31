%define  modulename bitarray

Name:    python3-module-%modulename
Version: 1.9.2
Release: alt1

Summary: Efficient arrays of booleans for Python
License: Python
Group:   Development/Python3
Url:     https://github.com/ilanschnell/bitarray
Vcs:     https://github.com/ilanschnell/bitarray.git

Packager: Andrew A. Vasilyev <andy@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

Source:  %modulename-%version.tar

%description
This module provides an object type which efficiently represents an array
of booleans.  Bitarrays are sequence types and behave very much like usual
lists.  Eight bits are represented by one byte in a contiguous block of
memory.  The user can select between two representations; little-endian
and big-endian.  All of the functionality is implemented in C.
Methods for accessing the machine representation are provided.
This can be useful when bit level access to binary files is required,
such as portable bitmap image files (.pbm).  Also, when dealing with
compressed data which uses variable bit length encoding, you may find
this module useful.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%check
make test PYTHON=%__python3

%files
%python3_sitelibdir/*
%doc LICENSE *.rst

%changelog
* Sat Apr 10 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.9.2-alt1
- 1.9.2

* Fri Apr 09 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.9.1-alt1
- 1.9.1

* Sun Apr 04 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.9.0-alt1
- 1.9.0

* Fri Mar 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Mar 22 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sat Feb 06 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.6.3-alt1
- 1.6.3

* Tue Nov 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Sep 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.5.3-alt1
- 1.5.3

* Fri Aug 09 2019 Andrew A. Vasilyev <andy@altlinux.org> 1.0.1-alt1
- 1.0.1-alt1

* Fri Jun 28 2019 Andrew A. Vasilyev <andy@altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus
