%define _unpackaged_files_terminate_build 1

Name: barrier
Version: 2.3.3
Release: alt2

Summary: Keyboard and mouse sharing solution
License: GPLv2
Group: Networking/Remote access

URL: https://github.com/debauchee/barrier
#Source: https://github.com/debauchee/barrier/archive/v%version.tar.gz
Source: %name-%version.tar

Patch0: %name-%version-%release.patch

BuildRequires: libgtest-devel
BuildRequires: libgmock-devel
BuildRequires: cmake
BuildRequires: libavahi-devel
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: qt5-base-devel
BuildRequires: libcurl-devel
BuildRequires: desktop-file-utils
BuildRequires: openssl-devel
BuildRequires: xvfb-run

%description
 Barrier allows you to share one mouse and keyboard between multiple computers.
 Work seamlessly across Windows, macOS and Linux.

%prep
%setup
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
%find_lang %name

install -D -p -m 0644 doc/barrierc.1 %buildroot%_man1dir/barrierc.1
install -D -p -m 0644 doc/barriers.1 %buildroot%_man1dir/barriers.1

mkdir -p %buildroot%_datadir/metainfo
## Write AppStream
cat <<END> %buildroot%_datadir/metainfo/%name.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2018 Ding-Yi Chen <dchen@redhat.com> -->
<component type="desktop-application">
  <id>%name</id>
  <metadata_license>FSFAP</metadata_license>
  <project_license>GPLv2</project_license>
  <name>barrier</name>
  <summary>Share mouse and keyboard between multiple computers over the network</summary>

  <description>
    <p>
      Barrier allows you to share one mouse and keyboard between multiple computers.
      Work seamlessly across Windows, macOS and Linux.
    </p>
  </description>

  <launchable type="desktop-id">%name.desktop</launchable>

  <url type="homepage">https://github.com/debauchee/barrier</url>

  <provides>
    <binary>barrier</binary>
    <binary>barrierc</binary>
    <binary>barriers</binary>
  </provides>

  <releases>
    <release version="%version" date="2019-03-21" />
  </releases>
</component>
END

%check
./BUILD/bin/unittests
xvfb-run --server-args='-extension GLX -screen 0 1280x1024x24 -noreset' ./BUILD/bin/integtests

%files -f %name.lang
%doc LICENSE ChangeLog res/Readme.txt doc/barrier.conf.example*
%_bindir/barrier*
%_desktopdir/barrier.desktop
%_iconsdir/hicolor/*/apps/barrier.svg
%_datadir/metainfo/%name.appdata.xml
%_man1dir/barrierc.1*
%_man1dir/barriers.1*

%changelog
* Thu Dec 03 2020 Danil Shein <dshein@altlinux.org> 2.3.3-alt2
- fixed integration tests failing in highly loaded build environment

* Wed Nov 11 2020 Danil Shein <dshein@altlinux.org> 2.3.3-alt1
- initial build for ALT


