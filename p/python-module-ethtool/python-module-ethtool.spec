%def_enable snapshot

%define modname ethtool
%def_without man

Name: python-module-%modname
Version: 0.14
Release: alt2

Summary: Ethernet settings python bindings
Group: Development/Python
License: GPL-2.0-only
Url: https://pypi.python.org/pypi/%modname/

%if_disabled snapshot
Source: https://pypi.io/packages/source/e/%modname/%modname-%version.tar.gz
%else
Vcs: https://github.com/fedora-python/python-ethtool
Source: python-%modname-%version.tar
%endif

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools libnl-devel
%{?_with_man:BuildRequires: asciidoc-a2x >= 8.6.8}

%description
Python bindings for the ethtool kernel interface, that allows querying
and changing of Ethernet card settings, such as speed, port,
auto-negotiation, and PCI locations.

%prep
%setup -n %{?_enable_snapshot:python-}%modname-%version

%build
%python_build
%if_with man
a2x -d manpage -f manpage man/pethtool.8.asciidoc
a2x -d manpage -f manpage man/pifconfig.8.asciidoc
%endif

%install
%python_install --install-scripts=%_sbindir

# rename binaries
for f in %buildroot%_sbindir/{pethtool,pifconfig}; do
mv -f $f $f.py; done

%if_with man
mkdir -p %buildroot%_man8dir
install -m644 man/pethtool.8 %buildroot%_man8dir/pethtool.8
install -m644 man/pifconfig.8 %buildroot%_man8dir/pifconfig.8
%endif

%files
%_sbindir/pethtool.py
%_sbindir/pifconfig.py
%python_sitelibdir/ethtool.so
%python_sitelibdir/*.egg-info
%{?_with_man:%_man8dir/*}
%doc README.rst CHANGES.rst

%changelog
* Sat Oct 03 2020 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt2
- updated to v0.14-8-gb8b09b6
- disabled man pages build and renamed binaries
  to avoid conflict with python3 package

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

