%global _unpackaged_files_terminate_build 1

# Run tests in check section
# disable for bootstrapping
%def_without check

# out of memory on armv7hl
%ifarch %arm
%global _smp_mflags -j1
%endif

%global goipath  pkg.deepin.io/dde/api
%global forgeurl https://github.com/linuxdeepin/dde-api

Name: deepin-api
Version: 5.4.6
Release: alt1
Summary: Go-lang bingding for dde-daemon
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-api

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/dde-api-%version.tar.gz

BuildRequires(pre): rpm-build-golang
BuildRequires: libalsa-devel libcairo-devel libgio-devel libgtk+3-devel libgdk-pixbuf-devel libgudev-devel libcanberra-devel libpulseaudio-devel librsvg-devel libpoppler-glib-devel libpolkitqt5-qt5-devel libsystemd-devel libXfixes-devel libXcursor-devel libX11-devel libXi-devel deepin-gettext-tools deepin-gir-generator libgdk-pixbuf-xlib-devel
BuildRequires: golang-github-linuxdeepin-dbus-factory-devel golang-deepin-go-lib-devel golang-deepin-go-x11-client-devel golang-github-burntsushi-xgbutil-devel golang-github-burntsushi-xgbutil-devel golang-github-disintegration-imaging-devel golang-github-cryptix-wav-devel golang-github-fogleman-gg-devel golang-github-nfnt-resize-devel golang-gopkg-alecthomas-kingpin-2-devel golang-x-image-devel golang-golang-x-net-devel golang-github-rickb777-date-devel golang-github-rickb777-plural-devel golang-github-alecthomas-template-devel golang-github-alecthomas-units-devel golang-github-freetype-devel golang-github-mattn-sqlite3-devel go-xgettext-devel golang-github-fsnotify-devel golang-github-go-dbus-devel golang-golang-x-sys-devel
%if_with check
BuildRequires: golang-github-jinzhu-gorm-devel
BuildRequires: golang-github-jinzhu-inflection-devel
BuildRequires: golang-gopkg-check-1-devel
BuildRequires: golang-github-stretchr-testify-devel
BuildRequires: golang-github-kr-pretty-devel
BuildRequires: golang-github-kr-text-devel
BuildRequires: golang-github-davecgh-spew-devel
BuildRequires: golang-github-pmezard-difflib-devel
BuildRequires: golang-github-goconvey-devel
%endif
Requires: deepin-desktop-base rfkill
Requires(pre): shadow-utils dbus-tools

%description
%summary.

%package -n golang-%name-devel
Summary: %summary
Group: Graphical desktop/Other
BuildArch: noarch

%description -n golang-%name-devel
%summary.

This package contains library source intended for
building other packages which use import path with
%goipath prefix.

%prep
%setup -n dde-api-%version
# Remove debian build files.
rm -rf debian/
# Fix unmets.
sed -i 's|/usr/bin/true|/bin/true|' \
    misc/systemd/system/deepin-shutdown-sound.service
# Fixed build for i586.
sed -i 's|gobuild|.build|' Makefile
# Fixed paths.
sed -i 's|/etc/default/locale|%_datadir/locale|' \
    adjust-grub-theme/util.go \
    locale-helper/ifc.go
# sed -i 's|PREFIX}${libdir|LIBDIR|; s|libdir|LIBDIR|' \
#     Makefile adjust-grub-theme/main.go

%build
export BUILDDIR=$PWD/.build
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"
export GO111MODULE="auto"

%golang_prepare
#pushd .build/src/%%goipath
%golang_build
#popd

%make_build

%install
export BUILDDIR=$PWD/.build
export GOPATH="%go_path"

%golang_install

%makeinstall_std SYSTEMD_SERVICE_DIR="%_unitdir" -i
# HOME directory for user deepin-sound-player
mkdir -p %buildroot%_sharedstatedir/deepin-sound-player
# Make provides golang(pkg.deepin.io/dde/api/device) for i586
# cp -a device/ %buildroot%go_path/src/%goipath/
# Make provides golang(pkg.deepin.io/dde/api/graphic) for ppc64le
# cp -a graphic/ %buildroot%go_path/src/%goipath/

%if_with check
%check
export GOPATH="%go_path"
#go get github.com/smartystreets/goconvey/convey
make test ||:
make test-coverage
%endif

%files
%doc README.md LICENSE
%_bindir/*
%_libexecdir/deepin-api/*
%_iconsdir/hicolor/??x??/actions/*
%_iconsdir/hicolor/???x???/actions/*
%_iconsdir/hicolor/scalable/actions/*
%_datadir/dbus-1/*
%_datadir/polkit-1/*
%_unitdir/*.service
%_var/lib/polkit-1/*
%_datadir/dde-api/data/*

%files -n golang-%name-devel
%go_path/src/%goipath

%changelog
* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.6-alt1
- New version (5.4.6) with rpmgs script.

* Tue Apr 27 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version (5.4.5) with rpmgs script.

* Thu Mar 04 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.2-alt1
- New version (5.4.2) with rpmgs script.
- Fixed build with golang 1.16.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.2-alt1
- New version (5.3.2) with rpmgs script.

* Thu Dec 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.14-alt1
- New version (5.3.0.14) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.13-alt1
- New version (5.3.0.13) with rpmgs script.

* Thu Nov 19 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.12-alt2
- Fixed BuildRequires.

* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.12-alt1
- New version (5.3.0.12) with rpmgs script.

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
