Name: neovim
Version: 0.3.8
Release: alt2

Summary: heavily refactored vim fork

License: ASLv2 and Vim
Group: Editors
Url: https://neovim.io/

# git://git.altlinux.org/gears/n/neovim.git
Source: %name-%version-%release.tar
Source1: %name.watch

BuildRequires(pre): rpm-macros-cmake cmake

BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: libjemalloc-devel
BuildRequires: libmsgpack-devel
BuildRequires: libtermkey-devel
BuildRequires: libuv-devel
BuildRequires: libvterm-devel
BuildRequires: lua lua-devel lua-lpeg lua-mpack
BuildRequires: unibilium-devel

BuildRequires(pre): rpm-macros-luajit
BuildRequires: luajit libluajit-devel

Provides: nvim = %EVR
Requires: %name-runtime = %EVR

ExclusiveArch: %luajit_arches

%package runtime
BuildArch: noarch
Summary: heavily refactored vim fork - runtime files
Group: Editors

%define common_descr \
Neovim is a refactor, and sometimes redactor, in the tradition of Vim (which\
itself derives from Stevie). It is not a rewrite but a continuation and\
extension of Vim. Many clones and derivatives exist; some are very clever, but\
none are Vim. Neovim strives to be a superset of Vim except for some\
intentionally-removed misfeatures. It is built for users who want the good parts\
of Vim, and more.

%description
%common_descr

%description runtime
%common_descr

This package contains runtime files.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DNVIM_VERSION_RELEASE=%release \
	#
%cmake_build VERBOSE=1

%install
%cmakeinstall_std
%find_lang nvim

gzip -9 LICENSE

install -pm0644 runtime/nvim.desktop -Dt %buildroot%_desktopdir
install -pm0644 runtime/nvim.png -Dt %buildroot%_pixmapsdir

%files -f nvim.lang
%doc LICENSE.gz
%_bindir/nvim
%_man1dir/nvim*

%_desktopdir/nvim.desktop
%_pixmapsdir/nvim.png

%files runtime
%dir %_datadir/nvim
%dir %_datadir/nvim/runtime
%_datadir/nvim/runtime/*

%changelog
* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 0.3.8-alt2
- fix build on ppc64le

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 0.3.8-alt1
- New version (fixes: #36883, CVE-2019-12735)

* Mon Jun 10 2019 Michael Shigorin <mike@altlinux.org> 0.3.7-alt2
- Moved to rpm-macros-luajit

* Mon Jun 10 2019 Vladimir Didenko <cow@altlinux.org> 0.3.7-alt1
- New version

* Tue Apr 30 2019 Vladimir Didenko <cow@altlinux.org> 0.3.5-alt1
- New version

* Wed Jan 16 2019 Vladimir Didenko <cow@altlinux.org> 0.3.4-alt1
- New version

* Wed Jan 9 2019 Vladimir Didenko <cow@altlinux.org> 0.3.3-alt1
- New version

* Wed Jul 25 2018 Vladimir Didenko <cow@altlinux.org> 0.3.1-alt1
- New version

* Thu Jun 28 2018 Vladimir Didenko <cow@altlinux.org> 0.3.0-alt1
- New version

* Mon Jun 04 2018 Vladimir Didenko <cow@altlinux.org> 0.2.2-alt1
- New version

* Wed May 03 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
