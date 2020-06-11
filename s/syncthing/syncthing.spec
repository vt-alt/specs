# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define goipath github.com/syncthing/syncthing
%define gopath %_libdir/golang

Name: syncthing
Summary: FOSS Continuous File Synchronisation
Summary(ru_RU.UTF-8): Свободная программа непрерывной синхронизации файлов
Version: 1.5.0
Release: alt1
License: MPL-2.0
Group: Networking/Other
Url:https://github.com/syncthing/syncthing

Packager: Anton Midyukov <antohami@altlinux.org>

#Source-url: https://github.com/syncthing/syncthing/releases/download/v%version/syncthing-source-v%version.tar.gz
Source: %name-%version.tar
BuildRequires(pre): rpm-macros-golang rpm-build-golang
BuildRequires: go >= 1.3
BuildRequires: udev-rules

Obsoletes: syncthing-inotify

%description
Syncthing replaces proprietary sync and cloud services with
something open, trustworthy and decentralised. Your data is your
data alone and you deserve to choose where it is stored, if it is
shared with some third party and how it's transmitted over the
Internet.

%description -l ru_RU.UTF-8
Syncthing призван заменить собой проприетарные программы синхронизации и
облачные сервисы на открытый, надёжный и децентрализованный сервис. Ваши данные
это ваши данные и вы должны иметь возможность выбрать, где им храниться,
совместно с какой-то третьей стороной или нет, и как им передаваться через
Интернет.

%package tools
Summary: Continuous File Synchronization (server tools)
Group: Networking/Other

%description tools
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the main syncthing server tools:

* strelaysrv / strelaypoolsrv, the syncthing relay server for indirect
  file transfers between client nodes, and
* stdiscosrv, the syncthing discovery server for discovering nodes
  to connect to indirectly over the internet.

%package cli
Summary: Continuous File Synchronization (CLI)
Group: Networking/Other

%description cli
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the CLI program.

%prep
%setup

%build
export GO111MODULE=off

# prepare build environment
mkdir -p ./_build/src/github.com/syncthing

TOP=$(pwd)
pushd _build/src/github.com/syncthing
ln -s $TOP syncthing
popd

export GOPATH=$(pwd)/_build:%gopath
export BUILDDIR=$(pwd)/_build/src/%goipath

# compile assets used by the build process
pushd _build/src/%goipath
go run build.go assets
rm build.go
popd

# set variables expected by syncthing binaries as additional LDFLAGS
export BUILD_HOST=alt-linux
export LDFLAGS="-X %goipath/lib/build.Version=v%version -X %goipath/lib/build.Stamp=$(date +%s) -X %goipath/lib/build.User=$USER -X %goipath/lib/build.Host=$BUILD_HOST"
export BUILDTAGS="noupgrade"

%gobuild -o _bin/syncthing %goipath/cmd/syncthing
%gobuild -o _bin/stdiscosrv %goipath/cmd/stdiscosrv
%gobuild -o _bin/strelaysrv %goipath/cmd/strelaysrv
%gobuild -o _bin/strelaypoolsrv %goipath/cmd/strelaypoolsrv
%gobuild -o _bin/stcli %goipath/cmd/stcli

%install
export GO111MODULE=off

# install binaries
mkdir -p %buildroot/%_bindir

cp -pav _bin/syncthing %buildroot/%_bindir/
cp -pav _bin/stdiscosrv %buildroot/%_bindir/
cp -pav _bin/strelaysrv %buildroot/%_bindir/
cp -pav _bin/strelaypoolsrv %buildroot/%_bindir/
cp -pav _bin/stcli %buildroot/%_bindir/

# install man pages
mkdir -p %buildroot/%_man1dir
mkdir -p %buildroot/%_man5dir
mkdir -p %buildroot/%_man7dir

cp -pav ./man/syncthing.1 %buildroot/%_man1dir/
cp -pav ./man/*.5 %buildroot/%_man5dir/
cp -pav ./man/*.7 %buildroot/%_man7dir/
cp -pav ./man/stdiscosrv.1 %buildroot/%_man1dir/
cp -pav ./man/strelaysrv.1 %buildroot/%_man1dir/

# install systemd units
mkdir -p %buildroot/%_unitdir
mkdir -p %buildroot/%_libexecdir/systemd/user

cp -pav etc/linux-systemd/system/syncthing@.service %buildroot/%_unitdir/
cp -pav etc/linux-systemd/system/syncthing-resume.service %buildroot/%_unitdir/
cp -pav etc/linux-systemd/user/syncthing.service %buildroot/%_libexecdir/systemd/user/

# install systemd preset disabling the service per default
mkdir -p %buildroot/%_libexecdir/systemd/user-preset
echo "disable syncthing*" > %buildroot/%_libexecdir/systemd/user-preset/90-syncthing.preset

# Unmark source files as executable
for i in $(find -name "*.go" -executable -print); do
    chmod a-x $i;
done

%check
export LANG=C.utf8
export GOPATH=$(pwd)/_build:%gopath
export GO111MODULE=off

%gotest %goipath/cmd/stdiscosrv || :
%gotest %goipath/cmd/strelaypoolsrv || :
%gotest %goipath/cmd/syncthing || :

%gotest %goipath/lib/api || :
%gotest %goipath/lib/auto || :
%gotest %goipath/lib/beacon || :
%gotest %goipath/lib/config || :
%gotest %goipath/lib/connections || :
%gotest %goipath/lib/db || :
%gotest %goipath/lib/dialer || :
%gotest %goipath/lib/discover || :
%gotest %goipath/lib/events || :
%gotest %goipath/lib/fs || :
%gotest %goipath/lib/ignore || :
%gotest %goipath/lib/logger || :

# This test sometimes fails dependent on load on some architectures:
# https://github.com/syncthing/syncthing/issues/4370
%gotest %goipath/lib/model || :

%gotest %goipath/lib/nat || :
%gotest %goipath/lib/osutil || :
%gotest %goipath/lib/pmp || :
%gotest %goipath/lib/protocol || :
%gotest %goipath/lib/rand || :
%gotest %goipath/lib/relay/client || :
%gotest %goipath/lib/relay/protocol || :
%gotest %goipath/lib/scanner || :
%gotest %goipath/lib/signature || :
%gotest %goipath/lib/stats || :
%gotest %goipath/lib/sync || :
%gotest %goipath/lib/tlsutil || :
%gotest %goipath/lib/upgrade || :
%gotest %goipath/lib/upnp || :
%gotest %goipath/lib/util || :

# This test sometimes fails dependent on load on some architectures:
# https://github.com/syncthing/syncthing/issues/4351
%gotest %goipath/lib/versioner || :

%gotest %goipath/lib/watchaggregator || :
%gotest %goipath/lib/weakhash || :

%files
%doc AUTHORS CONDUCT.md CONTRIBUTING.md LICENSE README.md
%_bindir/%name
%_unitdir/%name@.service
%_unitdir/%name-resume.service
%_libexecdir/systemd/user/*.service
%_libexecdir/systemd/user-preset/*.preset
%_mandir/man?/%{name}*

%files tools
%doc LICENSE
%doc README.md AUTHORS
%_bindir/stdiscosrv
%_bindir/strelaysrv
%_bindir/strelaypoolsrv
%_man1dir/stdiscosrv*
%_man1dir/strelaysrv*

%files cli
%doc LICENSE
%doc README.md AUTHORS
%_bindir/stcli

%changelog
* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Wed May 20 2020 Anton Midyukov <antohami@altlinux.org> 1.4.2-alt2
- build new version 1.4.2 realy

* Fri Apr 24 2020 Anton Midyukov <antohami@altlinux.org> 1.4.2-alt1
- new version 1.4.2 (Closes: 38377)

* Tue Nov 19 2019 Anton Midyukov <antohami@altlinux.org> 1.3.1-alt1
- new version 1.3.1

* Wed Sep 04 2019 Anton Midyukov <antohami@altlinux.org> 1.2.2-alt1
- new version 1.2.2

* Tue Aug 06 2019 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt1
- new version 1.2.1

* Wed Feb 06 2019 Cronbuild Service <cronbuild@altlinux.org> 1.0.1-alt1
- new version 1.0.1

* Fri Jan 04 2019 Cronbuild Service <cronbuild@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Sat Dec 08 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.54-alt1
- new version 0.14.54

* Wed Dec 05 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.53-alt1
- new version 0.14.53

* Thu Nov 08 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.52-alt1
- new version 0.14.52

* Wed Oct 03 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.51-alt1
- new version 0.14.51

* Wed Sep 12 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.50-alt1
- new version 0.14.50

* Thu Jul 26 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.49-alt1
- new version 0.14.49

* Fri Jun 08 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.48-alt1
- new version 0.14.48

* Thu May 03 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.47-alt1
- new version 0.14.47

* Fri Apr 06 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.46-alt1
- new version 0.14.46

* Wed Mar 07 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.45-alt1
- new version 0.14.45

* Tue Feb 13 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.44-alt1
- new version 0.14.44

* Thu Jan 11 2018 Cronbuild Service <cronbuild@altlinux.org> 0.14.43-alt1
- new version 0.14.43

* Wed Dec 27 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.42-alt1
- new version 0.14.42

* Wed Dec 06 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.41-alt1
- new version 0.14.41

* Thu Nov 09 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.40-alt1
- new version 0.14.40

* Wed Oct 11 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.39-alt1
- new version 0.14.39

* Tue Sep 19 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.38-alt1
- new version 0.14.38

* Thu Sep 07 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.37-alt1
- new version 0.14.37

* Fri Aug 11 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.36-alt1
- new version 0.14.36

* Tue Aug 08 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.35-alt1
- new version 0.14.35

* Wed Jul 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.32-alt1
- new version 0.14.32

* Fri Jun 30 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.31-alt1
- new version 0.14.31

* Thu Jun 15 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.30-alt1
- new version 0.14.30

* Wed May 31 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.29-alt1
- new version 0.14.29

* Fri May 19 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.28-alt1
- new version 0.14.28

* Tue Apr 25 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.27-alt1
- new version 0.14.27

* Fri Apr 07 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.26-alt1
- new version 0.14.26

* Thu Mar 23 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.25-alt1
- new version 0.14.25

* Wed Mar 08 2017 Cronbuild Service <cronbuild@altlinux.org> 0.14.24-alt1
- new version 0.14.24

* Fri Feb 17 2017 Anton Midyukov <antohami@altlinux.org> 0.14.23-alt1
- new version 0.14.23

* Fri Feb 03 2017 Anton Midyukov <antohami@altlinux.org> 0.14.21-alt1
- new version 0.14.21

* Thu Jan 05 2017 Anton Midyukov <antohami@altlinux.org> 0.14.18-alt1
- new version 0.14.18

* Mon Dec 05 2016 Denis Smirnov <mithraen@altlinux.ru> 0.14.13-alt1
- new version 0.14.13

* Wed Nov 23 2016 Anton Midyukov <antohami@altlinux.org> 0.14.12-alt1
- new version 0.14.12

* Thu Nov 10 2016 Anton Midyukov <antohami@altlinux.org> 0.14.10-alt1
- new version 0.14.10

* Sun Oct 09 2016 Anton Midyukov <antohami@altlinux.org> 0.14.8-alt1
- new version 0.14.8

* Sun Sep 04 2016 Anton Midyukov <antohami@altlinux.org> 0.14.5-alt1
- new version 0.14.5
- added cronbuild-update-source

* Sun Aug 21 2016 Denis Smirnov <mithraen@altlinux.ru> 0.14.4-alt1
- new version 0.14.4
- disable auto update

* Mon Jul 18 2016 Anton Midyukov <antohami@altlinux.org> 0.13.10-alt1
- new version 0.13.10

* Wed Jun 08 2016 Denis Medvedev <nbr@altlinux.org> 0.13.5-alt1
- new version 0.13.5

* Fri May 27 2016 Anton Midyukov <antohami@altlinux.org> 0.13.4-alt1
- New version (Closes: 32138).

* Tue Apr 26 2016 Anton Midyukov <antohami@altlinux.org> 0.12.22-alt1
- Initial build for ALT Linux Sisyphus.
