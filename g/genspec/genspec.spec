Name:     genspec
Version:  1.3.11
Release:  alt1

Summary:  Script for generation RPM spec file from template
License:  GPLv3+
Group:    System/Configuration/Packaging
URL:      http://altlinux.org/genspec
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

BuildPrereq: rpm-build-python3

Requires: git-core gear perl-Gear-Remotes

Source:   %name-%version.tar

%description
Script for generation RPM spec file from template.

%prep
%setup

%install
install -Dm755 %name %buildroot%_bindir/%name
install -Dm644 %name.1 %buildroot%_man1dir/%name.1
mkdir -p %buildroot%_datadir/spectemplates
cp -av spectemplates/* %buildroot%_datadir/spectemplates/

%files
%_bindir/%name
%_datadir/spectemplates
%_man1dir/*

%changelog
* Thu Jul 09 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.11-alt1
- Add empty branch options
- Add ocaml support

* Fri Jul 26 2019 Andrey Cherepanov <cas@altlinux.org> 1.3.10-alt1
- Update ruby template according to Ruby Policy 2.0.

* Sun Feb 03 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.9-alt1
- Fix name translation again

* Fri Jan 25 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.8-alt1
- Fix name translation

* Fri Jan 25 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.7-alt1
- Add disable-name-translation option

* Thu Jan 24 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.6-alt1
- Ruby packages start with ruby, againg

* Mon Dec 24 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.5-alt1
- Fix default value for gitignore
- Use unified doc glob
- Use right build requires for python templates
- Add python2 templates (copy from python templates)


* Mon Dec 24 2018 Pavel Skrylev <majioa@altlinux.org> 1.3.4-alt1
- Rewritten rule, when creating a new ruby gem, to make it name begining with
  "gem-";
- Added .gitignore generation for a new package to true by default.

* Fri Nov 16 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt1
- Fix removing of duplication in package name if upstream name contains type.
- Add man page.
- Fix bogus date in changelog.

* Mon Oct 22 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.2-alt1
- Fix unwanted linebreak in changelog
- Add --verbose key and change call functions from global to instace variables
- Add --[no-]check option to control failures of external programs
- Remove duplication in package name if upstream name contains type

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Fix java-maven template.

* Mon Sep 17 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.0-alt1
- Allow working without rpm and gear tools
- Add here option to create spec in current directory
- Add force option to overwrite existing directories or spec
- Some refactoring

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.16-alt1
- Update Ruby templates: remove ruby-tool-setup, add %%rubygem_specdir/*.

* Fri Apr 06 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.15-alt2
- (ALT #34778) Add build requires to setuptools in python3* templates

* Mon Jan 08 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.15-alt1
- Add readline
- Create golang-bin spectemplate
- Add owner option

* Fri Oct 20 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.14-alt1
- Fix interactive mode broken with last update

* Thu Oct 19 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.13-alt1
- (ALT #34017) Use deafult value for optional arguments

* Mon Oct 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.12-alt1
- Replace tabs with whitespaces

* Thu Sep 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.11-alt1
- (ALT #33935) Print created directory

* Fri Sep 01 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.10-alt1
- Add newline to generating .gear/rules
- Fail if could not get packager

* Wed Aug 02 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.9-alt1
- Add new spectemplates for executables

* Thu Jul 06 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.8-alt1
- Add test option

* Wed Jul 05 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.7-alt1
- Fix using gear post operations without --git option

* Wed Jun 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.6-alt1
- Create python3 spectemplate

* Tue Jun 27 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.2.5-alt1
- (ALT #33596): wrong syntax for building from tag

* Tue Jun 20 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.2.4-alt1
- Add git command line option to clone from url, clear repo and configure
  gear remotes update (currently doesn't handle git error: no internet
  connection and not configured git)

* Mon Jun 19 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.2.2-alt1
- Add tag command line option (uses in .gear/rules)

* Tue May 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- Split in two packages: genspec and github2spec

* Tue May 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.2-alt1
- Fix several issues

* Thu May 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt2
- Add rpm-build-ruby rpm-build-python3 to BuildPrereq

* Thu May 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt1
- Fix invocation of ./genspec instead of genspec

* Thu May 11 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1
- Create script to get repository data from github and generate spec file

* Tue May 2 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt1
- Upgrade to python3

* Mon Apr 24 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.1-alt1
- Add interactive mode

* Fri Jan 30 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial publish
