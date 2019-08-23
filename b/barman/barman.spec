Name: barman
Version: 2.9
Release: alt1
Summary: Backup and Recovery Manager for PostgreSQL

License: GPLv3
Group: Databases
Url: http://www.pgbarman.org/

Source: https://files.pythonhosted.org/packages/source/b/%name/%name-%version.tar.gz
Source1: barman.cron
Source2: barman.logrotate

BuildArch: noarch
BuildRequires: python3-devel python3-module-setuptools
Requires(pre): shadow-utils
Requires: python3-module-argcomplete
Requires: rsync >= 3.0.4

%description
Barman (Backup and Recovery Manager) is an open-source
administration tool for disaster recovery of PostgreSQL
servers written in Python.
It allows your organization to perform remote backups of
multiple servers in business critical environments to
reduce risk and help DBAs during the recovery phase.

Barman is distributed under GNU GPL 3 and maintained
by 2ndQuadrant.

%package -n barman-cli
Summary: Client Utilities for Barman, Backup and Recovery Manager for PostgreSQL
Group: Databases

%description -n barman-cli
Client utilities for the integration of Barman in
PostgreSQL clusters.

Barman (Backup and Recovery Manager) is an open-source
administration tool for disaster recovery of PostgreSQL
servers written in Python.
It allows your organization to perform remote backups of
multiple servers in business critical environments to
reduce risk and help DBAs during the recovery phase.

Barman is distributed under GNU GPL 3 and maintained
by 2ndQuadrant.

%package -n python3-module-barman
Summary: The shared libraries required for Barman family components
Group: Databases
Requires: python3-module-setuptools, python3-module-psycopg2 >= 2.4.2, python3-module-argh >= 0.21.2, python3-module-argcomplete, python3-module-dateutil

%description -n python3-module-barman
Python libraries used by Barman.

Barman (Backup and Recovery Manager) is an open-source
administration tool for disaster recovery of PostgreSQL
servers written in Python.
It allows your organization to perform remote backups of
multiple servers in business critical environments to
reduce risk and help DBAs during the recovery phase.

Barman is distributed under GNU GPL 3 and maintained
by 2ndQuadrant.

%prep
%setup

# Change shebang in all relevant executable files in this directory and all subdirectories
find -type f -executable -exec sed -i '1s=^#!%_bindir/\(python\|env python\)[23]\?=#!%__python3=' {} +

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot%_sysconfdir/cron.d/
mkdir -p %buildroot%_logrotatedir/
mkdir -p %buildroot/var/lib/barman
mkdir -p %buildroot/var/log/barman
mkdir -p %buildroot%_sysconfdir/barman/conf.d
install -pm 644 doc/barman.conf %buildroot%_sysconfdir/barman/barman.conf
install -pm 644 doc/barman.d/* %buildroot%_sysconfdir/barman/conf.d
install -pm 644 %SOURCE1 %buildroot%_sysconfdir/cron.d/barman
install -pm 644 %SOURCE2 %buildroot%_logrotatedir/barman
install -Dpm 644 scripts/barman.bash_completion %buildroot%_datadir/bash-completion/completions/barman
touch %buildroot/var/log/barman/barman.log

%__subst 's|/etc/barman.d|/etc/barman/conf.d|g' %buildroot%_sysconfdir/barman/barman.conf

%files
%doc LICENSE
%doc NEWS README.rst
%_bindir/%name
%_man1dir/%name.1.xz
%_man5dir/%name.5.xz
%config(noreplace) %_sysconfdir/barman/%name.conf
%config(noreplace) %_sysconfdir/cron.d/%name
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/barman/conf.d/
%_datadir/bash-completion/completions/barman
%attr(700,barman,barman) %dir /var/lib/%name
%attr(755,barman,barman) %dir /var/log/%name
%attr(600,barman,barman) %ghost /var/log/%name/%name.log

%files -n barman-cli
%doc NEWS README.rst
%_bindir/barman-wal-archive
%_bindir/barman-wal-restore
%doc %_man1dir/barman-wal-archive.1.xz
%doc %_man1dir/barman-wal-restore.1.xz

%files -n python3-module-barman
%doc NEWS README.rst
%python3_sitelibdir/%name-%version%{?extra_version:%extra_version}-py*.egg-info
%python3_sitelibdir/%name/

%pre
getent group barman >/dev/null || groupadd -r barman
getent passwd barman >/dev/null || \
    useradd -r -g barman -d /var/lib/barman -s /bin/bash \
    -c "Backup and Recovery Manager for PostgreSQL" barman
exit 0

%changelog
* Thu Aug 22 2019 Leontiy Volodin <lvol@altlinux.org> 2.9-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
