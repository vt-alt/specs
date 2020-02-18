Name: neovim-qt
Version: 0.2.15
Release: alt1

Summary: Neovim client library and GUI, in Qt5.

License: ISC
Group: Editors
Url: https://github.com/equalsraf/neovim-qt

Source: %name-%version-%release.tar

BuildRequires(pre): rpm-macros-cmake cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: libmsgpack-devel
BuildRequires: nvim

ExcludeArch: aarch64

%description
Neovim client library and GUI, in Qt5.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DNVIM_VERSION_RELEASE=%release \
	-DUSE_SYSTEM_MSGPACK=ON \
	#
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%files
%doc %_datadir/nvim-qt/runtime/README.md
%doc %_datadir/nvim-qt/runtime/doc/*
%_bindir/nvim-qt
%_desktopdir/nvim-qt.desktop
%_datadir/nvim-qt/runtime/plugin/nvim_gui_shim.vim
%_iconsdir/hicolor/*/*/*.png

%changelog
* Fri Nov 8 2019 Vladimir Didenko <cow@altlinux.org> 0.2.15-alt1
- New version.

* Fri Sep 20 2019 Vladimir Didenko <cow@altlinux.org> 0.2.14-alt2
- Don't build on aarch64 platform(because we don't build neovim on it

* Thu Sep 19 2019 Vladimir Didenko <cow@altlinux.org> 0.2.14-alt1
- New version.

* Tue Aug 6 2019 Vladimir Didenko <cow@altlinux.org> 0.2.12-alt3.gitbef46156
- New version.
- Add patch for unicode issues.

* Fri Aug 2 2019 Vladimir Didenko <cow@altlinux.org> 0.2.12-alt2.git78224e71
- New version.

* Wed Jan 16 2019 Vladimir Didenko <cow@altlinux.org> 0.2.12-alt1
- New version.

* Wed Jan 9 2019 Vladimir Didenko <cow@altlinux.org> 0.2.11-alt1
- New version.

* Thu Jul 5 2018 Vladimir Didenko <cow@altlinux.org> 0.2.8-alt2
- New version (v0.2.8-43-gfaef696).

* Thu Jul 5 2018 Vladimir Didenko <cow@altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus (v0.2.8-37-gfcb99d6).
