Name:     alt-checksums
Version:  1.0 
Release:  alt2

Summary:  ALT SP checksumming for sp distros.
License:  MIT
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/alt-checksums.git

BuildArch: noarch


Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar


%description
This set of scripts allow to check system binaries from one install
and compare it to a different install to ensure that all binaries
were installed correctly. First script starts on first boot
and creates a list of ELF binaries and are mentioned in RPM
base. Second script creates a file with checksums of that files
and after that stores the checksum of that file.

%prep
%setup

%install
mkdir -p %buildroot%_sbindir
install -Dm 0700  alt-gensum %buildroot%_sbindir/alt-gensum
install -Dm 0700  alt-gensum-chk %buildroot%_sbindir/alt-gensum-chk

mkdir -p %buildroot%_docdir
install -Dm 0600 README.md  %buildroot%_docdir
install -Dm 0600 COPYING.md  %buildroot%_docdir

mkdir -p %buildroot%_unitdir
install -Dm 0600 alt-checksum.service %buildroot%_unitdir 


%files
%_sbindir/*
%_unitdir/*
%doc *.md

%changelog
* Tue Dec 01 2020 Denis Medvedev <nbr@altlinux.org> 1.0-alt2
- fix of file presense test.

* Mon Nov 30 2020 Denis Medvedev <nbr@altlinux.org> 1.0-alt1
- List creation and checksumming are done separately.

* Fri Nov 27 2020 Denis Medvedev <nbr@altlinux.org> 0.9-alt1
- A list of files is now being generated after first boot by
asking rpm base of installed packages and checking for ELF files
in that list.

* Sat Nov 14 2020 Denis Medvedev <nbr@altlinux.org> 0.8-alt1
- removed generation phase, a list is predefined

* Fri Nov 13 2020 Denis Medvedev <nbr@altlinux.org> 0.7-alt1
- cleaned script and spec, moved default list  of files and workdir to
localstatedir

* Fri Nov 13 2020 Denis Medvedev <nbr@altlinux.org> 0.6-alt1
- added first set of files to check, fixed small glitches

* Fri Nov 13 2020 Denis Medvedev <nbr@altlinux.org> 0.5-alt3
- added option to optionaly generate a list, instead to work on a default one

* Fri Nov 13 2020 Denis Medvedev <nbr@altlinux.org> 0.5-alt2
- fixed group

* Wed Nov 11 2020 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
Initial version
