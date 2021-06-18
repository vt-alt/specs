Name:     github2spec
# NOTE update version in github2spec
Version:  1.4.12
Release:  alt2

Summary:  Script for generation RPM spec file from github using genspec
License:  MIT
Group:    System/Configuration/Packaging
URL:      http://altlinux.org/genspec
Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildArch: noarch

BuildPrereq: rpm-build-ruby

Requires: genspec >= 1.3.11

Source:   %name-%version.tar

%description
Script to get repository data from github and generate RPM spec file with
genspec. Program works in interactive mode, only one required value is URL.
Then you insert URL, the program will ask you to enter another values, but
before asking it would suggest default value. If you accept it then just press
Enter.

%prep
%setup

%install
install -Dm755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Fri Mar 19 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.12-alt2
- Switch back to ruby type (ALT #39821)

* Sat Sep 12 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.12-alt1
- Fix open-uri warning

* Thu Jul 09 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.11-alt1
- Proxy empty branch options to gnespec
- Add ocaml support

* Fri Feb 22 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.10-alt1
- Treat NOASSERTION license as none license

* Fri Jan 25 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.9-alt1
- Fix name translation

* Thu Jan 24 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.8-alt1
- Add support of multiple url types
- Change name translation behavior

* Fri Nov 16 2018 Grigory Ustinov <grenka@altlinux.org> 1.4.7-alt1
- Add option to generate only spec and rules.

* Mon Oct 22 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.6-alt1
- Rewrite forwarding options to genspec

* Mon Sep 17 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.5-alt1
- Add tag option to build from specified tag instead of last
- If not specified url option try to read it from first positional argument
- Forvard here and force options to gnespec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 05 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.4-alt1
- (ALT#34983) use version to change tag

* Fri Mar 02 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.3-alt1
- (ALT#34598) using empty strings instead of default values
- (ALT#34597) requires to inappropriate version of genspec
- (ALT#33934) show wrong version

* Mon Jan 08 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.2-alt1
- Use readline
- Add owner parameter

* Wed Sep 20 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.1-alt1
- (ALT#33907) multiple url requirement and bad changelog

* Sun Sep 17 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.0-alt1
- Rewrite github2spec without octokit

* Fri Sep 01 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.12-alt1
- Fix some issues

* Sun Aug 06 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.11-alt1
- Add command line option to pack stand alone programs

* Tue Jul 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.10-alt1
- Refactor code and add opportunity to pass arguments to genspec

* Wed Jun 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.8-alt1
- Change default python type to python3

* Tue Jun 20 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.3.6-alt1
- Pass git to genspec

* Mon Jun 19 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.3.4-alt1
- Pass tag to genspec

* Wed Jun 14 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.3.2-alt1
- Fix faults with missing description and tags

* Thu Jun 01 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.3.1-alt1
- Add command line options to control interactive level
- Fix issue with nil license
- Fix issue with quoting in data from github

* Tue May 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- Initial build as separate package (before it was part of genspec)
