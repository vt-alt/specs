Name:		system-backup
Version:	0.1.0
Release:	alt1

Summary:	Script for local system backup
License:	GPL-3
Group:		Archiving/Backup

Url:		http://www.altlinux.org/Rescue/Recovery
Source:		%name-%version.tar
BuildArch:	noarch

Packager:	Leonid Krivoshein <klark@altlinux.org>

%description
Script for creation full backup of the installed ALT Linux.
This backup solution restricted by local mounted storages.

%prep
%setup

%install
mkdir -pm755 %buildroot%_bindir
install -pm755 %name %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Wed Jun 12 2019 Leonid Krivoshein <klark@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.

