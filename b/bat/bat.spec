Name: bat
Version: 0.18.1
Release: alt1
Summary: A cat(1) clone with syntax highlighting and Git integration
License: MIT or Apache-2.0
Group: File tools
Url: https://github.com/sharkdp/bat
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildRequires: rust-cargo
BuildRequires: /proc
Conflicts: bacula9-bat

%description
A cat(1) clone which supports syntax highlighting for a large number of
programming and markup languages. It has git integration and automatic paging.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --offline --release

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
install -m 0755 target/release/%name %buildroot%_bindir
install -m 0644 target/release/build/%name-*/out/assets/manual/%name.1 %buildroot%_man1dir

%files
%_bindir/%name
%_man1dir/%name.1.xz
%doc README.md LICENSE-MIT LICENSE-APACHE

%changelog
* Sun Jun 06 2021 Alexander Makeenkov <amakeenk@altlinux.org> 0.18.1-alt1
- Updated to version 0.18.1

* Wed Apr 21 2021 Egor Ignatov <egori@altlinux.org> 0.18.0-alt1
- Update to version 0.18.0

* Sat Jan 09 2021 Alexander Makeenkov <amakeenk@altlinux.org> 0.17.1-alt1
- Updated to version 0.17.1

* Wed Jun 24 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.4-alt2
- Added conflict with bacula9-bat package

* Sat Jun 13 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.4-alt1
- Initial build for ALT

