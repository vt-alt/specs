%define        pyagentx_version 0.4.pcs.2

Name: 	       pcs
Epoch:         1
Version:       0.10.5
Release:       alt2
Summary:       Pacemaker/Corosync configuration system
License:       GPLv2+ and MIT
Group:         Other
Url:           https://github.com/ClusterLabs/pcs
Vcs:           https://github.com/ClusterLabs/pcs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       pyagentx-v%pyagentx_version.tar.gz
Source2:       pcsd
Source3:       known-hosts
Patch:         compat.patch

%add_python3_req_skip pyagentx
Requires:      python3-module-pcs = %version
Requires:      python3-module-snmp = %version
Obsoletes:     pcs-pcsd < %EVR
Provides:      pcs-pcsd = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-ruby
BuildRequires: corosync fontconfig fonts-ttf-liberation
BuildRequires: python3-devel python3-module-setuptools

%description
Pacemaker/Corosync configuration system with remote access
Pacemaker/Corosync gui/cli configuration system and daemon


%package       -n python3-module-pcs
Summary:       Python module for pacemaker/corosync gui/cli configuration system and daemon
Group:         Other
BuildArch:     noarch
Requires:      %name = %version
Requires:      pacemaker >= 2.0.3-alt2

%description   -n python3-module-pcs
Python module for pacemaker/corosync gui/cli configuration system and daemon


%package       -n python3-module-snmp
Group:         Other
Summary:       Pacemaker cluster SNMP agent
License:       GPLv2 or BSD-2-Clause
Requires:      %name = %EVR
Requires:      pacemaker >= 2.0.3-alt2
Requires:      net-snmp
Obsoletes:     pcs-snmp < %EVR
Provides:      pcs-snmp = %EVR

%description   -n python3-module-snmp
SNMP agent that provides information about pacemaker cluster to the master
agent (snmpd).


%prep
%setup
%patch -p1
sed -e "s,/usr/lib/pcsd/vendor/bundle/ruby,/usr/lib/ruby," -i pcsd/pcsd-ruby.service
mkdir -p pcs/bundled/tmp
tar xf %SOURCE1 -C pcs/bundled/tmp

%build
make BUNDLE_PYAGENTX_SRC_DIR=pcs/bundled/tmp/pyagentx-%pyagentx_version \
     PYAGENTX_LIB_DIR=%buildroot%_libexecdir/pcs/bundled
%ruby_build --use=pcsd --alias=pcs --join=bin:lib

%install
mkdir -p %buildroot%_libexecdir/pcs
mkdir -p %buildroot%_localstatedir/pcsd
mkdir -p %buildroot%_logdir/pcsd
mkdir -p %buildroot%_sysconfdir/sysconfig/
%ruby_install
%makeinstall_std \
     BUNDLE_PYAGENTX_SRC_DIR=pcs/bundled/tmp/pyagentx-%pyagentx_version \
     PYAGENTX_LIB_DIR=%buildroot%_libexecdir/pcs/bundled \
     BUILD_GEMS=false \
     DEST_LIB=%buildroot%_libexecdir \
     SYSTEMCTL_OVERRIDE=true \
     DEST_SYSTEMD_SYSTEM=%buildroot%systemd_unitdir \

install -Dm 0644 pcsd/pcsd.logrotate %buildroot%_logrotatedir/pcsd.logrotate
install -Dm 0755 %SOURCE2 %buildroot%_initdir/pcsd
install -Dm 0644 %SOURCE3 %buildroot%_localstatedir/pcsd/known-hosts

%check
%ruby_test

%post
%post_service pcsd

%preun
%preun_service pcsd

%post          -n python3-module-snmp
%post_service pcs_snmp_agent

%preun         -n python3-module-snmp
%preun_service pcs_snmp_agent


%files
%doc CHANGELOG.md COPYING README.md

%files         -n python3-module-pcs
%doc README.md
%_sbindir/pcs
%python3_sitelibdir_noarch/*
%_man8dir/*.*
%exclude %_man8dir/pcs_snmp_agent.*
%_sysconfdir/bash_completion.d/pcs
%_libexecdir/pcs/pcs_internal
%_sbindir/pcsd
%_initdir/pcsd
%_libexecdir/pcsd
%_sysconfdir/logrotate.d/pcsd
%_sysconfdir/pam.d/pcsd
%_sysconfdir/sysconfig/pcsd
%dir %_logdir/pcsd
%dir %_localstatedir/pcsd
%_logrotatedir/pcsd.logrotate
%systemd_unitdir/pcsd.service
%systemd_unitdir/pcsd-ruby.service
%_localstatedir/pcsd/known-hosts

%files         -n python3-module-snmp
%config(noreplace) %_sysconfdir/sysconfig/pcs_snmp_agent
%_libexecdir/pcs/pcs_snmp_agent
%_libexecdir/pcs/bundled/packages/pyagentx*
%systemd_unitdir/pcs_snmp_agent.service
%_datadir/snmp/mibs/PCMK-PCS*-MIB.txt
%_man8dir/pcs_snmp_agent.*


%changelog
* Fri Apr 03 2020 Pavel Skrylev <majioa@altlinux.org> 1:0.10.5-alt2
- + proper patch to fix config
- + pcsd init script
- + joint pcs and ruby-pcsd

* Wed Mar 18 2020 Pavel Skrylev <majioa@altlinux.org> 1:0.10.5-alt1
- ^ 0.10.4 -> 0.10.5 (closes #36898)
- fixed ! pcsd start (closes #37837)
- fixed ! license according to SPDX and licenses in some files

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1:0.10.4-alt1
- updated (^) 0.10.3 -> 0.10.4
- fixed (!) spec
- fixed (!) lost provides, and requires

* Mon Sep 09 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.10.3-alt1.1
- fixed (!) spec according to changelog rules

* Sun Aug 25 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.10.3-alt1
- used (>) Ruby Policy 2.0
- updated (^) 0.10.2 -> 0.10.3
- fixed (!) names of subpackages according to the language they were written in

* Mon Aug 12 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.10.2-alt1
- New version.
- Remove obsolete initscript.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.166-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.165-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.165-alt1
- New version.

* Tue Apr 10 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.164-alt1
- New version.

* Wed Mar 14 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.163-alt1
- New version.

* Fri Nov 03 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.161-alt1
- New version

* Sun Oct 15 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.160-alt1
- New version

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt3
- Completely remove requirement rack as gem
- pcs-pcsd requires openssl

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt2
- Comment out rack as gem load to prevent daemon fail

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Jul 14 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.159-alt1
- New version

* Thu Jun 29 2017 Denis Medvedev <nbr@altlinux.org> 1:0.9.158-alt3
- Added systemd unit (ALT #33590).

* Fri Jun 23 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.158-alt2
- Fix pathes to pcsd and pacemaker data (ALT #33580)

* Tue Jun 20 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.158-alt1
- New version
- Build from upstream tag
- Use initscript and daemon executable from upstream (ALT #33562)
- pcs-pcsd requires ruby-rack-handler-webrick (ALT #33561)

* Fri Jun 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.99.156-alt5
- pcs-pcsd requires corosync and ruby-rack-handler-webrick
- fix initscript

* Wed Jun 14 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt4
- Packaged pcsd (ALT #33522) (thanks cas@)

* Wed Apr 05 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt3
- changed default placement of pacemaker files

* Tue Apr 04 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt2
- added dependency to pacemaker

* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 0.99.156-alt1
- Initial release
