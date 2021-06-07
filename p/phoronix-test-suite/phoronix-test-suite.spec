%define _unpackaged_files_terminate_build 1

Name: phoronix-test-suite
Version: 10.4.0
Release: alt1
Summary: An Automated, Open-Source Testing Framework
Summary(ru_RU.UTF8): Автоматизированная среда тестирования с открытым исходным кодом
License: GPLv3+
Group: Other

URL: https://%name.com/
Source0: %name-%version.tar.gz

BuildRequires: rpm-build-xdg
BuildRequires: desktop-file-utils
BuildRequires: systemd
BuildRequires: libappstream-glib

Requires: php7
Requires: php7-xml
Requires: php7-json
Requires: php7-openssl
Requires: php7-gd
Requires: php7-pdo_sqlite
Requires: php7-posix
Requires: php7-curl
Requires: php7-sockets
Requires: hicolor-icon-theme

%description
The Phoronix Test Suite is the most comprehensive testing and benchmarking
platform available for the Linux operating system. This software is designed to
effectively carry out both qualitative and quantitative benchmarks in a clean,
reproducible, and easy-to-use manner. The Phoronix Test Suite consists of a
lightweight processing core (pts-core) with each benchmark consisting of an
XML-based profile with related resource scripts. The process from the benchmark
installation, to the actual benchmarking, to the parsing of important hardware
and software components is heavily automated and completely repeatable, asking
users only for confirmation of actions.

%prep
%setup
sed -i 's/functions\.sh/functions/' deploy/phoromatic-initd/phoromatic-client
grep -rl '.sh'  pts-core/external-test-dependencies/scripts | grep -v install-pclinuxos-packages.sh | xargs rm
grep -rl '.xml'  pts-core/external-test-dependencies/xml/ | grep -v ubuntu-packages.xml | grep -v pclinuxos-packages.xml | grep -v angstrom-packages.xml | grep -v xsl | xargs rm
sed -i 's/python/python3/' ob-cache/test-profiles/pts/cython-bench-1.0.0/install.sh
find . -name "*windows*" -exec rm {} \;
find . -name "*macosx**" -exec rm {} \;
find . -name "*.sh" -exec chmod +x {} \;

%build

%install
DESTDIR=%buildroot ./install-sh %_prefix
desktop-file-validate %buildroot/%_desktopdir/%name.desktop
desktop-file-validate %buildroot/%_desktopdir/%name-launcher.desktop
appstream-util validate-relax --nonet %buildroot/%_datadir/appdata/*.appdata.xml
install -vdm755 %buildroot/%_unitdir
mv %buildroot/%_prefix/%_unitdir/* %buildroot/%_unitdir

%files
%doc %_defaultdocdir/%name
%_datadir/%name
%_liconsdir/phoronix-test-suite.png
%_iconsdir/hicolor/64x64/mimetypes/application-x-openbenchmarking.png
%_bindir/%name
%_man1dir/%name.1*
%config(noreplace) %_sysconfdir/bash_completion.d/phoronix-test-suite
%_desktopdir/*
%_xdgmimedir/packages/*
%_datadir/appdata/%name.appdata.xml
%_unitdir/phoromatic-server.service
%_unitdir/phoromatic-client.service
%_unitdir/phoronix-result-server.service

%changelog
* Wed May 26 2021 Evgeny Sinelnikov <sin@altlinux.org> 10.4.0-alt1
- Update to latest release

* Wed Jul 22 2020 Nikita Obukhov <nickf@altlinux.org> 9.8.0-alt1
- Initial build

