Name: deploy
Version: 0.2
Release: alt1

Summary: Script and set of ansible roles to deploy system services
License: GPL-3.0+
Group: System/Configuration/Other
Url: https://altlinux.org/Deploy

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

Requires: python3
Requires: ansible

%description
deploy is script using predefined ansible playbooks to deploy some
system services like PostgreSQL or Moodle.

%prep
%setup

%install
%makeinstall_std

%files
%_bindir/%name
%_datadir/%name

%changelog
* Fri May 29 2020 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Fix check return code of playbook run.
- Check for modules dir and superuser privileges.
- Pass variables from command-line paramenters.

* Thu May 21 2020 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1
- postgresql: check /var/lib/pgsql/data/global for initialized database.

* Wed May 20 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus.
