%global import_path code.gitea.io/gitea

%def_without crutch

Name:    gitea
Version: 1.9.0
Release: alt1

Summary: Git with a cup of tea, painless self-hosted git service

License: MIT
Group:   Development/Other
Url:     https://gitea.io

# https://github.com/go-gitea/gitea
Source:  %name-%version.tar

Source1: gitea.service
Source2: gitea.service.d.conf
Source3: app-%version.ini
Source4: README.ALT

Patch1: make-version.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-bindata
BuildRequires: libpam0-devel

Requires: git-core

%description
The goal of this project is to make the easiest, fastest, and most painless way
of setting up a self-hosted Git service. It is similar to GitHub, Bitbucket,
and Gitlab. Gitea is a fork of Gogs.

%prep
%setup
%patch1 -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%if_with crutch
%golang_prepare
%endif

cd "$BUILDDIR"/src/%import_path
TAGS="bindata sqlite pam" make VERSION=%version generate all

%install
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name
install -Dm 0755 ".gopath/src/%import_path/%name" %buildroot%_bindir/%name
install -Dm 0640 %SOURCE1 %buildroot%systemd_unitdir/%name.service
mkdir -p %buildroot%_sysconfdir/systemd/system/gitea.service.d
install -Dm 0640 %SOURCE2 %buildroot%_sysconfdir/systemd/system/gitea.service.d/port.conf
install -Dm 0660 %SOURCE3 %buildroot%_sysconfdir/%name/app.ini

# install docs
mkdir -p %buildroot%_docdir/%name
install -Dm 0644 ".gopath/src/%import_path/custom/conf/app.ini.sample" \
%buildroot%_docdir/%name/default-app.ini
install -Dm 0644 %SOURCE4 %buildroot%_docdir/%name/

%pre
groupadd -rf %name
useradd -r -g %name -d %_localstatedir/%name %name -s /bin/sh ||:

%files
%_bindir/%name
%dir %attr(0700,%name,%name) %_localstatedir/%name
%dir %attr(0700,%name,%name) %_logdir/%name
%dir %_docdir/%name
%dir %_sysconfdir/%name
%config(noreplace) %attr(0660,root,%name) %_sysconfdir/%name/app.ini
%config(noreplace) %attr(0660,root,%name) %_sysconfdir/systemd/system/gitea.service.d/port.conf
%systemd_unitdir/%name.service
%_docdir/%name/default-app.ini
%_docdir/%name/README.ALT
%doc *.md

%changelog
* Wed Jul 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- new version 1.9.0
- Changed config file.
- Changed building scheme (thx to obirvalger@).

* Tue Jun 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.3-alt1
- new version 1.8.3

* Thu May 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.2-alt1
- new version 1.8.2

* Mon May 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.1-alt1
- Build new version.
- Changed config file.

* Tue Apr 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.0-alt1
- Build new version.
- Changed config file.

* Mon Apr 15 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.6-alt1
- Build new version.

* Thu Mar 28 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.5-alt1
- Build new version.

* Tue Mar 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.4-alt1
- Build new version.

* Mon Mar 04 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.3-alt1
- Build new version.

* Fri Feb 15 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.2-alt1
- Build new version.

* Fri Feb 08 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.1-alt3
- Fix ownership of catalogs
- Fix showing version

* Mon Feb 04 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt2
- Change user _gitea to gitea.

* Fri Feb 01 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt1
- Build new version.

* Wed Jan 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Build new version.

* Mon Jan 28 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.4-alt1
- Initial build for Sisyphus
