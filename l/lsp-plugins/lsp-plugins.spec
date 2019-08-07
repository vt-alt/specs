Name: lsp-plugins
Version: 1.1.10
Release: alt1

Summary: Linux Studio Plugins
Group: Sound
License: GPLv3
Url: https://lsp-plug.in/

#Source: https://sourceforge.net/projects/%name/files/%name/%version/%name-src-%version.tar.gz
#VCS: https://github.com/sadko4u/lsp-plugins
Source: https://github.com/sadko4u/%name/archive/%name-%version.tar.gz
Patch: %name-1.1.10-alt-rpath.patch

ExclusiveArch: %ix86 x86_64

BuildRequires: gcc-c++
BuildRequires: lv2-devel libjack-devel ladspa_sdk
BuildRequires: libsndfile-devel libcairo-devel
BuildRequires: libGL-devel libexpat-devel
BuildRequires: %_bindir/php

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

%package -n jack-%name
Summary: LSP (Linux Studio Plugins) JACK plugins
Group: Sound

%description -n jack-%name
LSP (Linux Studio Plugins) JACK plugins.

%package -n ladspa-%name
Summary: LSP (Linux Studio Plugins) LADSPA plugins
Group: Sound

%description -n ladspa-%name
LSP (Linux Studio Plugins) LADSPA plugins.

%package -n lv2-%name
Summary: LSP (Linux Studio Plugins) LV2 plugins
Group: Sound

%description -n lv2-%name
LSP (Linux Studio Plugins) LV2 plugins.

%package -n vst-%name
Summary: LSP (Linux Studio Plugins) LinuxVST plugins
Group: Sound

%description -n vst-%name
LSP (Linux Studio Plugins) LinuxVST plugins.

%package doc
Summary: Documentation for LSP (Linux Studio Plugins) plugins
Group: Sound
BuildArch: noarch

%description doc
Documentation for LSP (Linux Studio Plugins) plugins.

%prep
%setup -n %name-%name-%version
# remove rpath
%patch -b .rpath

%build
%add_optflags %optflags_warnings
export PLATFORM=Linux SYSTEM=Linux
%make PREFIX=%_prefix \
    BUILD_PROFILE=%_arch \
    CC_FLAGS=-DLSP_NO_EXPERIMENTAL \
    BIN_PATH=%_bindir LIB_PATH=%_libdir \
    LD_PATH=%_libdir
    DOC_PATH=%_docdir VERBOSE=1

%install
%makeinstall_std PREFIX=%_prefix LIB_PATH=%_libdir

%files -n jack-%name
%_bindir/*
%dir %_libdir/%name
%_libdir/%name/%name-jack-core-%version.so
%_libdir/%name/%name-r3d-glx.so

%doc CHANGELOG.txt README.txt

%files -n ladspa-%name
%_libdir/ladspa/*
%doc CHANGELOG.txt README.txt

%files -n lv2-%name
%_libdir/lv2/*
%doc CHANGELOG.txt README.txt

%files -n vst-%name
%_libdir/vst/*
%doc CHANGELOG.txt README.txt

%files doc
%_defaultdocdir/%name/


%changelog
* Wed Jul 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.10-alt1
- 1.1.10

* Thu Apr 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.9-alt1
- 1.1.9

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.7-alt1
- 1.1.7

* Tue Feb 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- first build for Sisyphus

