%def_without utils
%define module Gear-Remotes

Name: perl-%module
Version: 0.022
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for quering Gear remotes files
Group: Development/Perl
License: GPLv2+ or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
# TODO: upload to http://search.cpan.org/dist/%module
Url: https://www.altlinux.org/Gear/remotes

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Pod/Usage.pm) perl(Pod/Text.pm) perl(RPM/uscan.pm) perl(Gear/Rules.pm) perl(RPM/Source/Editor.pm)
Requires: gear perl(Pod/Text.pm)
Provides: gear-remotes = %version
%if_without utils
Provides: gear-remotes-utils = %version
Requires: gear-uupdate
%endif

%description
Perl library and tools to work with .gear/upstream/remotes files.
Gear is a tool for storing, building and maintaining rpm packages
in a git repository for ALT Linux team.

Gear, however, lack means to store essential parts of local configuration,
such as location of upstream VCS it was cloned from or updated.
.gear/upstream/remotes is an extension to Gear to cover this weakness.

See more on [www.altlinux.org/Gear/remotes].

%if_with utils
%package -n gear-remotes-utils
Summary: utilities for manipulating Gear upstream/remotes files
Group: Development/Other
Requires: perl-Gear-Remotes = %EVR
Requires: gear-uupdate
#Conflicts: perl-Gear-Remotes < %version

%description -n gear-remotes-utils
gear-remotes-utils are utils for managing .gear/upstream/remotes file.
.gear/upstream/remotes file is used to save, share and restore local
.git configuration to all maintainers.
%endif

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/G*
%if_with utils
%files -n gear-remotes-utils
%endif
%_bindir/*
%_man1dir/*

%changelog
* Sat Mar 07 2020 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- new version

* Tue Feb 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- new version

* Mon Dec 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- checks for transform-tag

* Tue Oct 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- better usability thanks to grenka@

* Mon Jul 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- added man pages

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- check for misspelled remotes/*-tag

* Fri Feb 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- submodules support

* Thu Oct 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- gear-remotes-* utils can now run deep in git tree

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- support for git repository comments in spec file

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- gear-remotes-save now git add .gear/upstream/remotes

* Wed Feb 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- bugfix release

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- new version

* Thu Jul 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- bugfix release

* Wed Jun 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- added gear-uupdate requires (closes: #32182)

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- proper argument handling in save

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- added documentation

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- added gear-remotes-save by cas@
- bugfixes

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- bugfix release

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- new version

* Fri Dec 04 2015 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- added gear-remotes-set-from-url utility

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- new version

* Wed Jul 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
