%def_enable snapshot

%define modname ethtool
%def_with man
#test_show_ring_eth (tests.test_scripts.ScriptsTests) ... FAIL
%def_disable check

Name: python3-module-%modname
Version: 0.14
Release: alt2

Summary: Ethernet settings python bindings
Group: Development/Python3
License: GPL-2.0-only
Url: https://pypi.python.org/pypi/%modname/

%if_disabled snapshot
Source: https://pypi.io/packages/source/e/%modname/%modname-%version.tar.gz
%else
Vcs: https://github.com/fedora-python/python-ethtool
Source: python-%modname-%version.tar
%endif

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools libnl-devel
%{?_with_man:BuildRequires: asciidoc-a2x >= 8.6.8}
%{?_enable_check:BuildRequires: python3-module-tox}

%description
Python 3 bindings for the ethtool kernel interface, that allows querying
and changing of Ethernet card settings, such as speed, port,
auto-negotiation, and PCI locations.

%prep
%setup -n %{?_enable_snapshot:python-}%modname-%version

%build
%python3_build
%if_with man
a2x -d manpage -f manpage man/pethtool.8.asciidoc
a2x -d manpage -f manpage man/pifconfig.8.asciidoc
%endif

%install
%python3_install --install-scripts=%_sbindir
%if_with man
mkdir -p %buildroot%_man8dir
install -m644 man/pethtool.8 %buildroot%_man8dir/pethtool.8
install -m644 man/pifconfig.8 %buildroot%_man8dir/pifconfig.8
%endif

%check
tox.py3 -e py%(echo %__python3_version | tr -d .) --sitepackages -o -v

%files
%_sbindir/pethtool
%_sbindir/pifconfig
%python3_sitelibdir/ethtool*.so
%python3_sitelibdir/*.egg-info
%{?_with_man:%_man8dir/*}
%doc README.rst CHANGES.rst

%changelog
* Sat Oct 03 2020 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt2
- updated to v0.14-8-gb8b09b6 

* Tue Sep 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt1
- 0.14

* Wed Jun 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13 (new url)

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12

* Tue Feb 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1.1
- fixed build

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- 0.11

* Sat Jan 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Wed Oct 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- first build for Sisyphus
- wait for asciidoc >= 8.6.8 to build mans

