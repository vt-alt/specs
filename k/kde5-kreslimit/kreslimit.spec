%define rname kreslimit
Name: kde5-kreslimit
Version: 1.0.1
Release: alt1

%K5init altplace

Group: Graphical desktop/KDE
Summary: Application resource limit configurator
License: GPLv2+

Requires: plasma5-desktop
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: boost-devel extra-cmake-modules gcc-c++
BuildRequires: kf5-ki18n-devel kf5-kcmutils-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kservice-devel

Provides: kreslimit = %EVR
Obsoletes: kreslimit <= %EVR

%description
Resource limit for launched applications

%prep
%setup 

%build
%K5cmake \
    -DLIBEXEC_INSTALL_DIR=%_K5exec \
    -DCMAKE_BUILD_TYPE=Debug \

%K5make

%install
%K5install

%find_lang %rname --with-kde --all-name

%files -f %rname.lang
%_K5plug/*.so
%_K5srv/*.desktop
%_K5bin/*


%changelog
* Thu Apr 16 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0.1-alt1
- change package name
- change units
- set minimum limit size

* Fri Feb 28 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0.0-alt1
- init
