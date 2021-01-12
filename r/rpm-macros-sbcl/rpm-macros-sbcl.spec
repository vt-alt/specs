Name: rpm-macros-sbcl
Version: 0.2
Release: alt1
BuildArch: noarch

Summary: Arch macro to build sbcl clients
License: MIT
Group: Development/Other

Source0: macros

%description
sbcl supports only some architectures.

This package provides macro with a list of architectures supported
by sbcl.

%install
mkdir -p %buildroot%_rpmmacrosdir
cp %SOURCE0 %buildroot%_rpmmacrosdir/sbcl

%files
%_rpmmacrosdir/sbcl

%changelog
* Sun Dec 27 2020 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- Drop %%{arm}: its sbcl generates unresolved ELF symbols at the moment.

* Fri Jul 05 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Initial build.
