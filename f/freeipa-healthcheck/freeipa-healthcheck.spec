%define _libexecdir %_usr/libexec
%define _unpackaged_files_terminate_build 1
%def_with check

Name: freeipa-healthcheck
Version: 0.9
Release: alt0.M90P.1

Summary: Check the health of a FreeIPA installation
License: GPLv3
Group: System/Base
Url: https://github.com/freeipa/freeipa-healthcheck

Source0: %name-%version.tar.gz
Patch: %name-%version-alt.patch

ExcludeArch: %ix86

Requires: python3-module-%name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-ipaserver

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(pytest)
BuildRequires: python3(pylint)
BuildRequires: /proc
%endif

%description
FreeIPA-healthcheck is a framework which is needed to assist with the
identification, diagnosis and potentially repair of problems.

%package -n python3-module-%name
Summary: FreeIPA-healthcheck python3 bindings and documentation
License: GPLv3
Group: Development/Python3
Requires: python3-module-lib389 >= 1.4.1.11

%description -n python3-module-%name
This FreeIPA-healthcheck Python3 module contains the library binding for
FreeIPA-healthcheck framework.

%prep
%setup

%patch -p1

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot%_sysconfdir/ipahealthcheck
echo "[default]" > %buildroot%_sysconfdir/ipahealthcheck/ipahealthcheck.conf

mkdir -p %buildroot%_unitdir

mkdir -p %buildroot%_libexecdir/ipa
install -p -m755 systemd/ipa-healthcheck.sh %buildroot%_libexecdir/ipa/

mkdir -p %buildroot%_logrotatedir/ipahealthcheck
install -p -m644 logrotate/ipahealthcheck %buildroot%_logrotatedir/ipahealthcheck/

mkdir -p %buildroot%_logdir/ipa/healthcheck
mkdir -p %buildroot%_man5dir
mkdir -p %buildroot%_man8dir
install -p -m644 man/man5/ipahealthcheck.conf.5 %buildroot%_man5dir/
install -p -m644 man/man8/ipa-healthcheck.8 %buildroot%_man8dir/
install -p -m644 systemd/ipa-healthcheck.service %buildroot%_unitdir/
install -p -m644 systemd/ipa-healthcheck.timer %buildroot%_unitdir/

# since we package python modules as arch dependent
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%post
%post_service ipa-healthcheck

%preun
%preun_service ipa-healthcheck

%check
export PIP_NO_INDEX=YES
export TOXENV=py3,lint
tox.py3 --sitepackages -vvr

%files
%doc README.md COPYING
%_bindir/ipa-healthcheck
%_bindir/ipa-clustercheck
%_sysconfdir/ipahealthcheck/
%_unitdir/ipa-healthcheck.service
%_unitdir/ipa-healthcheck.timer
%_libexecdir/ipa
%_logdir/ipa/healthcheck
%_logrotatedir/ipahealthcheck
%_man5dir/ipahealthcheck.conf.5.xz
%_man8dir/ipa-healthcheck.8.xz

%files -n python3-module-%name
%python3_sitelibdir/ipahealthcheck/
%python3_sitelibdir/ipahealthcheck-%version-py%__python3_version.egg-info/
%python3_sitelibdir/ipahealthcheck-%version-py%__python3_version-nspkg.pth
%python3_sitelibdir/ipaclustercheck/

%changelog
* Wed Jun 30 2021 Stanislav Levin <slev@altlinux.org> 0.9-alt0.M90P.1
- Backported to P9.

* Fri Jun 18 2021 Stanislav Levin <slev@altlinux.org> 0.9-alt1
- 0.8 -> 0.9.

* Tue Mar 30 2021 Stanislav Levin <slev@altlinux.org> 0.8-alt1
- 0.7 -> 0.8.

* Fri Nov 06 2020 Stanislav Levin <slev@altlinux.org> 0.7-alt1
- 0.6 -> 0.7.

* Thu Aug 06 2020 Stanislav Levin <slev@altlinux.org> 0.6-alt2
- Applied upstream fixes.

* Wed Jul 22 2020 Stanislav Levin <slev@altlinux.org> 0.6-alt1
- Initial build (by Ivan Alekseev <qwetwe@altlinux.org>).
