Name:     hyperfine
Version:  1.11.0
Release:  alt3

Summary:  A command-line benchmarking tool
License:  Apache-2.0
Group:    Development/Tools
Url:      https://github.com/sharkdp/hyperfine

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
%summary

%prep
%setup
%patch -p1

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/*
%doc *.md

%changelog
* Wed Jun 23 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.0-alt3
- Use rpm-build-rust macros

* Tue Jan 19 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.0-alt2
- Add generation of debuginfo

* Mon Nov 09 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.0-alt1
- Initial build for Sisyphus
