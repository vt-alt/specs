Name:  bacula-mls-backup
Version:  0.8.1
Release:  alt1

Summary:  Set of scripts and documentation to generate backup configs
License:  MIT
Group:    System/Configuration/Other

Source:   %name-%version.tar



BuildArch: noarch

%description
Documentation and scripts to generate
bacula backup scripts that will work with files of
a particular MLS level, producing volumes marked with that level.


%prep
%setup


%install
mkdir -p  %buildroot/%_docdir/bacula_mls_backup/

cp -ar doc %buildroot/%_docdir/bacula_mls_backup/

%files
%_docdir/bacula_mls_backup/*

%changelog
* Fri Sep 04 2020 Denis Medvedev <nbr@altlinux.org> 0.8.1-alt1
- fix installer workdir to avoid intersection with main bacula

* Tue Jan 24 2017 Denis Medvedev <nbr@altlinux.org> 0.8.0-alt0.M80P.1
- to p8

* Mon Jan 23 2017 Denis Medvedev <nbr@altlinux.org> 0.8.0-alt1
- Initial version

