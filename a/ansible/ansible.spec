Name: ansible
Summary: SSH-based configuration management, deployment, and task execution system
Version: 2.8.12
Release: alt1

Group: System/Libraries
License: GPLv3
Source0: %name-%version.tar

Patch0:%name-%version-alt.patch

Url: http://www.ansible.com

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six
BuildRequires: python3-module-setuptools asciidoc-a2x python3-module-jinja2 python3-module-yaml python-modules-json python3-module-packaging python3-module-docutils

Requires: ca-certificates >= 2015.10.29
%py3_requires yaml
%py3_requires paramiko

# Skip findreq on all modules:
%add_findreq_skiplist %python3_sitelibdir/%name/modules/*
%add_findreq_skiplist %python3_sitelibdir/%name/plugins/*
%add_findreq_skiplist %python3_sitelibdir/%name/module_utils/ansible_tower.py

%add_python3_req_skip __main__

%py3_provides ansible.module_utils.six.moves
%py3_provides ansible.module_utils.six.moves.http_cookiejar
%py3_provides ansible.module_utils.six.moves.urllib.error
%py3_provides ansible.module_utils.six.moves.urllib.parse
%py3_provides ansible.module_utils.six.moves.urllib.request

%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot%_sysconfdir/%name/
cp examples/ansible.cfg %buildroot%_sysconfdir/%name/
touch %buildroot%_sysconfdir/%name/hosts
mkdir -p %buildroot/%_man1dir
make PYTHON=python3 docs
cp -v docs/man/man1/*.1 %buildroot/%_man1dir/

%files
%_bindir/%{name}*
%config(noreplace) %_sysconfdir/%name
%_man1dir/%{name}*
%python3_sitelibdir/%{name}*
%doc examples/playbooks examples/scripts examples/hosts
%doc README.rst changelogs/CHANGELOG-v*.rst CODING_GUIDELINES.md MODULE_GUIDELINES.md

%changelog
* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 2.8.12-alt1
- 2.8.12
- Fixes:
  + CVE-2020-1733
  + CVE-2020-1735
  + CVE-2020-1737
  + CVE-2020-1739
  + CVE-2020-1740
  + CVE-2020-1746

* Thu Mar 12 2020 Alexey Shabalin <shaba@altlinux.org> 2.8.10-alt1
- 2.8.10
- Fixes:
  + CVE-2019-14846
  + CVE-2019-14856
  + CVE-2019-14864
  + CVE-2019-14904
  + CVE-2019-14905

* Thu Sep 12 2019 Grigory Ustinov <grenka@altlinux.org> 2.8.4-alt2
- Transfer ansible on python3.

* Tue Sep  3 2019 Terechkov Evgenii <evg@altlinux.org> 2.8.4-alt1
- 2.8.4 (ALT#36899)

* Fri Jun 14 2019 Terechkov Evgenii <evg@altlinux.org> 2.7.11-alt1
- 2.7.11

* Tue Apr 30 2019 Terechkov Evgenii <evg@altlinux.org> 2.7.10-alt1
- 2.7.10
- Add python-module-docutils in BR: to build on e2k (patch by mike@)

* Thu Feb 21 2019 Terechkov Evgenii <evg@altlinux.org> 2.7.7-alt1
- 2.7.7

* Fri Jan 11 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.7.4-alt2
- Fix cheksum calculation to work with python3

* Wed Dec 12 2018 Terechkov Evgenii <evg@altlinux.org> 2.7.4-alt1
- 2.7.4

* Tue Oct 23 2018 Terechkov Evgenii <evg@altlinux.org> 2.7.0-alt1
- 2.7.0 (ALT#35540)

* Mon Oct 22 2018 Terechkov Evgenii <evg@altlinux.org> 2.6.6-alt1
- 2.6.6

* Fri Oct 12 2018 Terechkov Evgenii <evg@altlinux.org> 2.6.5-alt1
- 2.6.5

* Wed Aug 29 2018 Terechkov Evgenii <evg@altlinux.org> 2.6.3-alt1
- 2.6.3

* Thu Aug 16 2018 Terechkov Evgenii <evg@altlinux.org> 2.6.2-alt1
- 2.6.2 (ALT#35245)

* Wed May  2 2018 Terechkov Evgenii <evg@altlinux.org> 2.5.2-alt1
- 2.5.2

* Thu Apr 26 2018 Terechkov Evgenii <evg@altlinux.org> 2.5.1-alt1
- 2.5.1 (ALT#34791)

* Thu Feb  1 2018 Terechkov Evgenii <evg@altlinux.org> 2.4.0.0-alt2
- Fix build (lost json module)

* Sun Oct  8 2017 Terechkov Evgenii <evg@altlinux.org> 2.4.0.0-alt1
- 2.4.0.0-1 (ALT#33908)

* Wed Mar 29 2017 Terechkov Evgenii <evg@altlinux.org> 2.2.2.0-alt1
- 2.2.2.0-1 (ALT#32709)

* Tue May 31 2016 Terechkov Evgenii <evg@altlinux.org> 2.0.2.0-alt2
- Add requires to be out-of-box usable

* Wed May 11 2016 Terechkov Evgenii <evg@altlinux.org> 2.0.2.0-alt1
- 2.0.2.0-1

* Mon Feb 15 2016 Terechkov Evgenii <evg@altlinux.org> 2.0.0.1-alt2
- ca-certificates-2015.10.29 and up contains /etc/pki/tls/certs/ca-bundle.crt (symlink to /usr/share/ca-certificates/ca-bundle.crt)

* Sat Feb 13 2016 Terechkov Evgenii <evg@altlinux.org> 2.0.0.1-alt1
- 2.0.0.1

* Mon Nov 16 2015 Terechkov Evgenii <evg@altlinux.org> 1.9.4-alt2
- README.ALT added with distro-specific notes

* Tue Oct 20 2015 Terechkov Evgenii <evg@altlinux.org> 1.9.4-alt1
- 1.9.4

* Sat Jun 27 2015 Terechkov Evgenii <evg@altlinux.org> 1.9.2-alt1
- 1.9.2 (ALT#30995)

* Sat Feb 28 2015 Terechkov Evgenii <evg@altlinux.org> 1.8.4-alt1
- 1.8.4

* Fri Jan  2 2015 Terechkov Evgenii <evg@altlinux.org> 1.8.2-alt2
- Fix modules location (ALT#30619)
- Drop default hosts file (see examples/hosts, ALT#30620)

* Sun Dec  7 2014 Terechkov Evgenii <evg@altlinux.org> 1.8.2-alt1
- 1.8.2

* Sat Nov 29 2014 Terechkov Evgenii <evg@altlinux.org> 1.8.1-alt1
- 1.8.1

* Tue Oct 21 2014 Terechkov Evgenii <evg@altlinux.org> 1.7.2-alt1
- 1.7.2

* Thu Aug 21 2014 Terechkov Evgenii <evg@altlinux.org> 1.7.1-alt1
- 1.7.1

* Sat Aug  9 2014 Terechkov Evgenii <evg@altlinux.org> 1.7.0-alt2
- Oops, apt-rpm module renamed to apt_rpm (update your playbooks!)

* Fri Aug  8 2014 Terechkov Evgenii <evg@altlinux.org> 1.7.0-alt1
- 1.7.0

* Sat Jul 26 2014 Terechkov Evgenii <evg@altlinux.org> 1.6.8-alt1
- 1.6.8
- CVE-2014-4966 and CVE-2014-4967 fixed in v1.6.7


* Sun Jun  1 2014 Terechkov Evgenii <evg@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri May 23 2014 Terechkov Evgenii <evg@altlinux.org> 1.6.1-alt2
- Relax suds module requirement

* Wed May 21 2014 Terechkov Evgenii <evg@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Apr 22 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.5-alt1
- 1.5.5

* Tue Apr  8 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.4-alt2
- Fix for apt-rpm module (changed run_command behavior)

* Wed Apr  2 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.4-alt1
- 1.5.4

* Tue Apr  1 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.3-alt1
- 1.5.3

* Fri Mar 14 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.0-alt2
- Revert wrongly patched files to tag v1.5.0

* Wed Mar  5 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.0-alt1
- 1.5.0 (ALT #29865)

* Sun Jan 19 2014 Terechkov Evgenii <evg@altlinux.org> 1.4.4-alt2
- apt-rpm: Properly detect rpm packages installation/upgrade.

* Sun Jan 12 2014 Terechkov Evgenii <evg@altlinux.org> 1.4.4-alt1
- 1.4.4

* Mon Dec 30 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.3-alt3
- Fix in apt-rpm module (upgrade installed packages as documented)

* Sun Dec 29 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.3-alt2
- apt-rpm module added

* Sun Dec 29 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.3-alt1
- 1.4.3

* Sun Dec  1 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.1-alt1
- 1.4.1

* Tue Nov 26 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Nov 11 2013 Terechkov Evgenii <evg@altlinux.org> 1.3.4-alt1
- 1.3.4

* Tue Oct  8 2013 Terechkov Evgenii <evg@altlinux.org> 1.3.3-alt1
- 1.3.3

* Sun Sep 29 2013 Terechkov Evgenii <evg@altlinux.org> 1.3.2-alt1
- 1.3.2
