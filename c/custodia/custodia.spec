%define _unpackaged_files_terminate_build 1
%define provides_list %(echo `cat %SOURCE2`)

%def_with check

Name: custodia
Version: 0.6.0
Release: alt6

Summary: A tool for managing secrets
License: GPLv3+
Group: System/Configuration/Other

Url: https://github.com/latchset/custodia
BuildArch: noarch

Source: %name-%version.tar
Source2: provides.list
Source3: ns_root_modules.py
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-ipaclient
BuildRequires: python3-module-jwcrypto
BuildRequires: python3-module-requests-gssapi
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-tox
%endif

Requires: python3-module-%name = %EVR

%define overview                                                              \
Custodia is a Secrets Service Provider, it stores or proxies access to keys,  \
password, and secret material in general. Custodia is built to use the HTTP   \
protocol and a RESTful API as an IPC mechanism over a local Unix Socket. It   \
can also be exposed to a network via a Reverse Proxy service assuming proper  \
authentication and header validation is implemented in the Proxy.             \
                                                                              \
Custodia is modular, the configuration file controls how authentication,      \
authorization, storage and API plugins are combined and exposed.

%description
%overview

%package -n python3-module-%name
Summary: Subpackage with python3 custodia modules
Group: Development/Python
# to break circular dependency, since IPA directly requires python3-custodia
%filter_from_requires /^python3\(\.[[:digit:]]*\)\?(ipalib\(\..*\)\?)/d
%filter_from_requires /^python3\(\.[[:digit:]]*\)\?(ipaclient\(\..*\)\?)/d
# module 'requests' doesn't contain 'urllib3', but imports within
%add_python3_req_skip requests.packages.urllib3.connection
%add_python3_req_skip requests.packages.urllib3.connectionpool
%py3_requires urllib3.connection
%py3_requires urllib3.connectionpool
%py3_provides %name
%py3_provides %provides_list

# due to file conflicts https://bugzilla.altlinux.org/show_bug.cgi?id=36781
Conflicts: python-module-custodia

%description -n python3-module-%name
%overview

%prep
%setup
%patch -p1

%build
%python3_build

%install
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_man7dir
mkdir -p %buildroot%_defaultdocdir/custodia
mkdir -p %buildroot%_defaultdocdir/custodia/examples
mkdir -p %buildroot%_sysconfdir/custodia
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_tmpfilesdir
mkdir -p %buildroot%_sharedstatedir/custodia
mkdir -p %buildroot%_logdir/custodia
mkdir -p %buildroot%_runtimedir/custodia

%python3_install

mv -v %buildroot%_bindir/custodia %buildroot%_sbindir/custodia
install -m 644 -t "%buildroot%_man7dir" man/custodia.7
install -m 644 -t "%buildroot%_defaultdocdir/custodia" README API.md
install -m 644 -t "%buildroot%_defaultdocdir/custodia/examples" custodia.conf
install -m 600 %_builddir/%name-%version/contrib/config/custodia/custodia.conf %buildroot%_sysconfdir/custodia
install -m 644 %_builddir/%name-%version/contrib/config/systemd/system/custodia@.service  %buildroot%_unitdir
install -m 644 %_builddir/%name-%version/contrib/config/systemd/system/custodia@.socket  %buildroot%_unitdir
install -m 644 %_builddir/%name-%version/contrib/config/tmpfiles.d/custodia.conf  %buildroot%_tmpfilesdir/custodia.conf

set -o pipefail
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 %SOURCE3 | \
    sort > provides.actual.list
set +o pipefail
cat %SOURCE2 | sort > provides.expected.list
diff -y provides.actual.list provides.expected.list

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -vr

%pre
getent group custodia >/dev/null || groupadd -r custodia
getent passwd custodia >/dev/null || \
    useradd -r -g custodia -d / -s /sbin/nologin \
    -c "User for custodia" custodia

%post
if sd_booted && systemctl --version &>/dev/null; then
  systemctl daemon-reload
  if [ $1 -eq 1 ]; then
    systemctl -q preset custodia@*.{socket,service} --all
  else
    systemctl try-restart custodia@*.{socket,service} --all
  fi
fi

%preun
if sd_booted && systemctl --version &>/dev/null; then
  if [ $1 -eq 0 ]; then
    systemctl --no-reload -q disable --now custodia@*.{socket,service} --all
  fi
fi

%files
%doc %_defaultdocdir/custodia
%doc %_defaultdocdir/custodia/examples/custodia.conf
%_man7dir/custodia*
%dir %attr(0700,custodia,custodia) %_sysconfdir/custodia
%config(noreplace) %attr(600,custodia,custodia) %_sysconfdir/custodia/custodia.conf
%attr(644,root,root)  %_unitdir/custodia@.socket
%attr(644,root,root)  %_unitdir/custodia@.service
%dir %attr(0700,custodia,custodia) %_sharedstatedir/custodia
%dir %attr(0700,custodia,custodia) %_logdir/custodia
%dir %attr(0755,custodia,custodia) %_runtimedir/custodia
%_tmpfilesdir/custodia.conf

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version-py%_python3_version.egg-info
%python3_sitelibdir/%name-%version-py%_python3_version-nspkg.pth
%_sbindir/custodia
%_bindir/custodia-cli

%changelog
* Mon Mar 16 2020 Stanislav Levin <slev@altlinux.org> 0.6.0-alt6
- Added missing Provides.

* Mon Oct 07 2019 Stanislav Levin <slev@altlinux.org> 0.6.0-alt5
- Fixed build against urllib3 1.25+.
- Broke circular dependency on ipaclient.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 0.6.0-alt4
- Fixed testing against Pytest 5.

* Fri May 24 2019 Stanislav Levin <slev@altlinux.org> 0.6.0-alt3
- Fixed update (closes: #36781).

* Sat Mar 30 2019 Stanislav Levin <slev@altlinux.org> 0.6.0-alt2
- Fixed FTBFS (closes: #36426).
- Removed Python2 subpackage.

* Wed Sep 26 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.0 -> 0.6.0.
- Set Python3 as default within systemd service.

* Mon Jul 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt4
- Remove runtime requirements to setuptools (closes: #35114)

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt3
- NMU: rebuilt with python-3.6.

* Mon Jan 29 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt2
- Fix tests for Python3

* Wed Oct 25 2017 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- Put v0.5.0 sources from https://github.com/latchset/custodia

* Tue Sep 26 2017 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt4
- Really fix SimpleCreds authenticator.

* Fri Aug 04 2017 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt3
- Fix SimpleCreds authenticator.

* Thu Oct 06 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt2
- Mive binary to %%_sbindir.

* Wed May 11 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Allow tox to use locally installed packages (patch from upstream).
- Initial build.

