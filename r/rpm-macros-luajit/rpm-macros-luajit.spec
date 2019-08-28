Name: rpm-macros-luajit
Version: 0.2
Release: alt1
BuildArch: noarch

Summary: Arch macro to build luajit clients
License: MIT
Group: Development/Other

Source0: macros

%description
luajit supports only some architectures.

This package provides macro with a list of architectures supported
by luajit.

%install
mkdir -p %buildroot%_rpmmacrosdir
cp %SOURCE0 %buildroot%_rpmmacrosdir/luajit

%files
%_rpmmacrosdir/luajit

%changelog
* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 0.2-alt1
- add ppc64le to list of supported arches

* Fri Apr 12 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Initial build.
