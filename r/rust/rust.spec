%define rust_ver 1.33.0
%define rust_rel alt1
%define cargo_ver 1.33.0
%define cargo_rel alt1

Name: rust
Epoch: 1
Version: %rust_ver
Release: %rust_rel
Summary: The Rust Programming Language

Group: Development/Other
License: Apache 2.0, MIT 
URL: http://www.rust-lang.org/

Source: https://static.rust-lang.org/dist/%{name}c-%version-src.tar.xz

BuildPreReq: /proc
BuildRequires: curl gcc-c++ python-devel cmake libffi-devel patchelf

%def_without  bootstrap
%def_with  bundled_llvm
%define abisuff %nil

%if_without bundled_llvm

BuildRequires: llvm7.0-devel

%endif

%if_without bootstrap

BuildRequires: rust rust-cargo
%define cargo %_bindir/cargo
%define rustc %_bindir/rustc

%else

%define r_ver 1.32.0
Source2: https://static.rust-lang.org/dist/rust-%r_ver-i686-unknown-linux-gnu.tar.gz
Source3: https://static.rust-lang.org/dist/rust-%r_ver-x86_64-unknown-linux-gnu.tar.gz
Source4: https://static.rust-lang.org/dist/rust-%r_ver-aarch64-unknown-linux-gnu.tar.gz
Source5: https://static.rust-lang.org/dist/rust-%r_ver-armv7-unknown-linux-gnueabihf.tar.gz
Source6: https://static.rust-lang.org/dist/rust-%r_ver-powerpc64le-unknown-linux-gnu.tar.gz

%ifarch %ix86
%define r_src %SOURCE2
%endif
%ifarch x86_64
%define r_src %SOURCE3
%endif
%ifarch aarch64
%define r_src %SOURCE4
%endif
%ifarch armh
%define r_src %SOURCE5
%define abisuff eabihf
%endif
%ifarch ppc64le
%define r_src %SOURCE6
%endif

%define rustdir %_tmppath/rust
%define cargo %rustdir/bin/cargo
%define rustc %rustdir/bin/rustc

%endif

%ifarch %ix86
%define r_arch i686
%endif
%ifarch x86_64
%define r_arch x86_64
%endif
%ifarch aarch64
%define r_arch aarch64
%endif
%ifarch armh
%define r_arch armv7
%endif
%ifarch ppc64le
%define r_arch powerpc64le
%endif

# Since 1.12.0: striping debuginfo damages *.so files
%add_debuginfo_skiplist %_libdir %_bindir

%description
Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety.

%package gdb
Group: Development/Other
Summary: run rust compiler under gdb
Requires: %name = %rust_ver-%rust_rel
Requires: gdb
AutoReq: nopython

%description gdb
%summary

%package doc
Summary: Documentation for Rust
Group: Development/Documentation

%description doc
This package includes HTML documentation for the Rust programming language and
its standard library.

%package cargo
Summary: The Rust package manager
Version: %cargo_ver
Release: %cargo_rel
Group: Development/Tools
Requires: rust
BuildRequires: libssh2-devel libgit2-devel openssl-devel zlib-devel

Obsoletes: rust-cargo < 1.29.0
Provides: rust-cargo = %cargo_ver

%description cargo
Cargo is a tool that allows Rust projects to declare their various dependencies
and ensure that you'll always get a repeatable build.

%package cargo-doc
Summary: Documentation for Cargo
Version: %cargo_ver
Group: Development/Documentation
Requires: rust-doc = %rust_ver-%rust_rel

%description cargo-doc
This package includes HTML documentation for Cargo.

%package -n rustfmt
Summary: Tool to find and fix Rust formatting issues
Version: 1.0.1
Release: alt1
Group: Development/Tools
Requires: rust-cargo = %cargo_ver-%cargo_rel

%description -n rustfmt
A tool for formatting Rust code according to style guidelines.

%package -n rls
Summary: Rust Language Server for IDE integration
Version: 1.33.0
Release: alt1
Group: Development/Tools
Requires: rust-analysis
Requires: %name = %rust_ver-%rust_rel

%description -n rls
The Rust Language Server provides a server that runs in the background,
providing IDEs, editors, and other tools with information about Rust programs.
It supports functionality such as 'goto definition', symbol search,
reformatting, and code completion, and enables renaming and refactorings.

%package -n clippy
Summary: Lints to catch common mistakes and improve your Rust code
Version: 0.0.212
Release: alt6
Group: Development/Tools
License: MPLv2.0
Requires: rust-cargo
Requires: %name = %rust_ver-%rust_rel

%description -n clippy
A collection of lints to catch common mistakes and improve your Rust code.

%package src
Version: %rust_ver
Summary: Sources for the Rust standard library
Group: Development/Other
AutoReq: no
AutoProv: no

%description src
This package includes source files for the Rust standard library.  It may be
useful as a reference for code completion tools in various editors.

%package analysis
Summary: Compiler analysis data for the Rust standard library
Group: Development/Tools
Requires: %name = %rust_ver-%rust_rel

%description analysis
This package contains analysis data files produced with rustc's -Zsave-analysis
feature for the Rust standard library. The RLS (Rust Language Server) uses this
data to provide information about the Rust standard library.

%prep
%setup -n %{name}c-%rust_ver-src

%if_with bootstrap
tar xf %r_src
mkdir -p %rustdir
pushd rust-%r_ver-%r_arch-unknown-linux-gnu%abisuff
./install.sh --prefix=%rustdir
popd

%ifarch aarch64
patchelf --set-interpreter /lib64/ld-linux-aarch64.so.1 %rustdir/bin/cargo
patchelf --set-interpreter /lib64/ld-linux-aarch64.so.1 %rustdir/bin/rustc
%endif

%else
# Fix libdir path for bootstrap
sed -i 's/Path::new("lib")/Path::new("%_lib")/' src/bootstrap/builder.rs
%endif

patch -p2 <<'EOF'
diff --git a/rustc-1.30.0-src/src/etc/rust-gdb b/rustc-1.30.0-src/src/etc/rust-gdb
index 743952a5bef..a495ddb12f0 100755
--- a/rustc-1.30.0-src/src/etc/rust-gdb
+++ b/rustc-1.30.0-src/src/etc/rust-gdb
@@ -13,8 +13,7 @@
 set -e
 
 # Find out where the pretty printer Python module is
-RUSTC_SYSROOT=`rustc --print=sysroot`
-GDB_PYTHON_MODULE_DIRECTORY="$RUSTC_SYSROOT/lib/rustlib/etc"
+GDB_PYTHON_MODULE_DIRECTORY=%_libdir/rustlib/etc
 
 # Run GDB with the additional arguments that load the pretty printers
 # Set the environment variable `RUST_GDB` to overwrite the call to a
diff --git a/rustc-1.30.0-src/src/etc/rust-gdbgui b/rustc-1.30.0-src/src/etc/rust-gdbgui
index 7e179ba927d..a7c224668d7 100755
--- a/rustc-1.30.0-src/src/etc/rust-gdbgui
+++ b/rustc-1.30.0-src/src/etc/rust-gdbgui
@@ -41,8 +41,7 @@ icon to start your program running.
 fi
 
 # Find out where the pretty printer Python module is
-RUSTC_SYSROOT=`rustc --print=sysroot`
-GDB_PYTHON_MODULE_DIRECTORY="$RUSTC_SYSROOT/lib/rustlib/etc"
+GDB_PYTHON_MODULE_DIRECTORY=%_libdir/rustlib/etc
 
 # Set the environment variable `RUST_GDB` to overwrite the call to a
 # different/specific command (defaults to `gdb`).
EOF

%build
cat > config.toml <<EOF
[build]
cargo = "%cargo"
rustc = "%rustc"
submodules = false
docs = true
verbose = 0
vendor = true
extended = true
[install]
prefix = "%prefix"
libdir = "%_lib"
[rust]
channel = "stable"
codegen-tests = false
rpath = false
debuginfo = false
debuginfo-lines = false
EOF

%if_without bundled_llvm
cat >> config.toml <<EOF
[target.%r_arch-unknown-linux-gnu%abisuff]
llvm-config = "./llvm-config-filtered"
EOF

cat > llvm-config-filtered <<EOF
#!/bin/sh
/usr/bin/llvm-config \$@ | sed -E 's/-Wcovered-switch-default|-Wstring-conversion|-fcolor-diagnostics|-Werror=unguarded-availability-new//g'
EOF

chmod +x llvm-config-filtered

export LLVM_LINK_SHARED=1
%endif

./x.py build
./x.py doc

%install
DESTDIR=%buildroot ./x.py install

%check
#./x.py test --no-fail-fast || :

%clean
%if_with bootstrap
rm -rf %rustdir
%endif

%files
%exclude %_datadir/doc/rust
%doc COPYRIGHT LICENSE-APACHE LICENSE-MIT README.md
%_bindir/rustc
%_bindir/rustdoc
%_libdir/lib*
%dir %_libdir/rustlib
%dir %_libdir/rustlib/etc
%dir %_libdir/rustlib/%r_arch-unknown-linux-gnu%abisuff
%_libdir/rustlib/%r_arch-unknown-linux-gnu%abisuff/*
%exclude %_bindir/*miri
%exclude %_libdir/rustlib/%r_arch-unknown-linux-gnu%abisuff/analysis
%exclude %_libdir/rustlib/etc/*
%exclude %_libdir/rustlib/install.log
%exclude %_libdir/rustlib/manifest-*
%exclude %_libdir/rustlib/rust-installer-version
%exclude %_libdir/rustlib/uninstall.sh
%exclude %_libdir/rustlib/components
%_man1dir/rustc.*
%_man1dir/rustdoc.*

%files gdb
%_bindir/rust-gdb
%exclude %_bindir/rust-lldb
%_libdir/rustlib/etc/*
%exclude %_libdir/rustlib/etc/lldb_*

%files doc
%_datadir/doc/%name
%exclude %_datadir/doc/%name/html/cargo

%files cargo
%doc src/tools/cargo/{LICENSE-APACHE,LICENSE-MIT,LICENSE-THIRD-PARTY,README.md}
%_bindir/cargo
%_man1dir/cargo*.1*
%_sysconfdir/bash_completion.d/cargo
%_datadir/zsh/site-functions/_cargo

%files cargo-doc
%_datadir/doc/rust/html/cargo

%files -n rustfmt
%_bindir/rustfmt
%_bindir/cargo-fmt
%doc src/tools/rustfmt/{README.md,CHANGELOG.md,Configurations.md,LICENSE-APACHE,LICENSE-MIT}

%files -n rls
%_bindir/rls
%doc src/tools/rls/{README.md,COPYRIGHT,debugging.md,LICENSE-APACHE,LICENSE-MIT}

%files -n clippy
%_bindir/cargo-clippy
%_bindir/clippy-driver
%doc src/tools/clippy/{README.md,CHANGELOG.md,LICENSE*}

%files src
%_libdir/rustlib/src

%files analysis
%_libdir/rustlib/%r_arch-unknown-linux-gnu%abisuff/analysis

%changelog
* Mon May 27 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.33.0-alt1
- 1.33.0

* Fri May 24 2019 Vladimir Lettiev <crux@altlinux.org> 1:1.32.0-alt1
- 1.32.0

* Wed May 15 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.31.1-alt4
- Added ppc64le support.

* Wed Jan 16 2019 Andrey Cherepanov <cas@altlinux.org> 1:1.31.1-alt3
- 1.31.1
- build with llvm7.0 (ALT #35874)
- disable test check

* Wed Dec 12 2018 Ivan Zakharyaschev <imz@altlinux.org> 1:1.30.0-alt2
- rust-gdb: fix %%_libdir path (to find the pretty-printers in Python).

* Mon Oct 29 2018 Vladimir Lettiev <crux@altlinux.org> 1:1.30.0-alt1
- 1.30.0

* Sun Oct 21 2018 Vladimir Lettiev <crux@altlinux.org> 1:1.29.2-alt1
- 1.29.2

* Thu Sep 27 2018 Vladimir Lettiev <crux@altlinux.org> 1:1.29.1-alt1
- 1.29.1
- security fix: https://blog.rust-lang.org/2018/09/21/Security-advisory-for-std.html
- added support for armv7 arch (thanks to sbolshakov@ for patch)
- require gdb for rust-gdb

* Fri Sep 14 2018 Vladimir Lettiev <crux@altlinux.org> 1:1.29.0-alt1
- 1.29.0
- packaged extended rust tool set and docs
- new arch: aarch64 (thanks to sbolshakov@ for help)

* Mon Apr 02 2018 Vladimir Lettiev <crux@altlinux.org> 1:1.24.1-alt2
- downgrade to 1.24.1 (1.25.0 unusable)

* Thu Mar 29 2018 Vladimir Lettiev <crux@altlinux.org> 1.25.0-alt1
- 1.25.0
- built with shared llvm

* Mon Mar 26 2018 Vladimir Lettiev <crux@altlinux.org> 1.24.1-alt1
- 1.24.1

* Sun Mar 25 2018 Vladimir Lettiev <crux@altlinux.org> 1.23.0-alt1
- 1.23.0

* Sat Mar 24 2018 Vladimir Lettiev <crux@altlinux.org> 1.22.1-alt1
- 1.22.1
- built with bundled llvm
- migrated from gear to srpm

* Thu Oct 19 2017 Vladimir Lettiev <crux@altlinux.org> 1.21.0-alt1
- 1.21.0

* Fri Sep 08 2017 Vladimir Lettiev <crux@altlinux.org> 1.20.0-alt1
- 1.20.0

* Fri Jul 21 2017 Vladimir Lettiev <crux@altlinux.org> 1.19.0-alt1
- 1.19.0

* Wed Jul 19 2017 Vladimir Lettiev <crux@altlinux.org> 1.18.0-alt1
- 1.18.0
- built with shared llvm4.0

* Fri Jun 16 2017 Vladimir Lettiev <crux@altlinux.org> 1.17.0-alt1
- 1.17.0
- switched to cargo-based build

* Fri Jun 16 2017 Vladimir Lettiev <crux@altlinux.org> 1.16.0-alt1
- 1.16.0

* Thu Jun 15 2017 Vladimir Lettiev <crux@altlinux.org> 1.15.1-alt1
- 1.15.1

* Fri Dec 23 2016 Vladimir Lettiev <crux@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Tue Nov 15 2016 Vladimir Lettiev <crux@altlinux.ru> 1.13.0-alt1
- 1.13.0
- disabled bootstrap

* Tue Nov 15 2016 Vladimir Lettiev <crux@altlinux.ru> 1.12.1-alt1
- 1.12.1
- rebootstrap

* Wed Oct 05 2016 Vladimir Lettiev <crux@altlinux.ru> 1.12.0-alt1
- 1.12.0
- disable debuginfo packaging

* Mon Oct 03 2016 Vladimir Lettiev <crux@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Mon Jul 11 2016 Vladimir Lettiev <crux@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Mon May 30 2016 Vladimir Lettiev <crux@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri Apr 22 2016 Vladimir Lettiev <crux@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Fri Mar 04 2016 Vladimir Lettiev <crux@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Fri Jan 22 2016 Vladimir Lettiev <crux@altlinux.ru> 1.6.0-alt1
- 1.6.0
- separated rust-gdb package

* Fri Jan 15 2016 Vladimir Lettiev <crux@altlinux.ru> 1.5.0-alt1
- initial build

