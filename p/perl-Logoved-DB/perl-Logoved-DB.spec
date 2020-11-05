%def_with db
%define module Logoved-DB

Name: perl-%module
Version: 0.017
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: perl library for Logoved framework and DB
Group: Development/Perl
License: GPLv2+ or Artistic-2.0
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
#Url: http://search.cpan.org/dist/%module
#Url: http://git.altlinux.org/people/viy/packages/logoved.git
Url: http://wiki.altlinux.org/Logoved

BuildRequires: perl-devel perl(Logoved/Stream.pm) perl(autodie.pm) perl(Source/Shared/CLI.pm)
BuildRequires: perl-RPM-Source-Dependency-Analyzer >= 0.070

%description
perl library for Logoved framework and DB.

%package -n logoved
Summary: Logoved is a tool for build log analysis and processing.
Group: Development/Tools
Requires: perl-%module = %EVR
%if_with db
Requires: logoved-db = %EVR
%endif

%description -n logoved
Logoved is a tool for build log analysis and processing.

%package -n logoved-batchfix
Summary: fix packages in batch using logoved-report's FIXSCRIPT.
Group: Development/Tools
Requires: perl-RPM-Source-Transformation-Logoved-Batch = %EVR
BuildRequires: girar-nmu >= 2
Requires: girar-nmu >= 2
%if_with db
Requires: logoved-db = %EVR
%endif

%description -n logoved-batchfix
Logoved-batchfix is a tool to fix packages in batch
by applying to them logoved-report's 00FIXSCRIPT file

%package -n logoved-autorepo
Summary: helper scripts for using logoved in autorepo builder.
Group: Development/Tools
Requires: perl-%module = %EVR
Requires: logoved = %EVR
Requires: logoved-batchfix = %EVR

%description -n logoved-autorepo
Helper scripts for using logoved in autorepo builder.

%package -n perl-RPM-Source-Transformation-Logoved-Batch
Summary: libraary to fix packages in batch using FIXSCRIPT
Group: Development/Perl
BuildRequires: perl(RPM/Source/Transformation/Factory.pm) perl(Source/Repository/RPM/ALTLinuxSrcList.pm)

%description -n perl-RPM-Source-Transformation-Logoved-Batch
Perl library to fix packages in batch using FIXSCRIPT

%if_with db
%package -n logoved-db
Summary: Database for Logoved.
Group: Development/Perl

%description -n logoved-db
Logoved Database.
%endif

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build 

%install
%perl_vendor_install

%if_with db
mkdir -p %buildroot%_datadir/{logoved,srpmtools}/
cp -a db addon %buildroot%_datadir/logoved/
cp -a hooks %buildroot%_datadir/srpmtools/
%endif

%files
#doc Changes
#doc README
%perl_vendor_privlib/Logoved*

%files -n logoved
%_bindir/logoved-grep
%_bindir/logoved-report
%_man1dir/logoved-report*
# TODO: write man for logoved-grep!!!

%files -n logoved-batchfix
%_bindir/logoved-batchfix*
%_man1dir/logoved-batchfix*
%_bindir/girar-nmu-prepare-logoved-batchfix*
%_man1dir/girar-nmu-prepare-logoved-batchfix*

%files -n logoved-autorepo
%_bindir/logoved-autoimports
%_bindir/logoved-autorepo-helper-*

%files -n perl-RPM-Source-Transformation-Logoved-Batch
%perl_vendor_privlib/RPM/Source/Transformation

%if_with db
%files -n logoved-db
%_datadir/logoved
%_datadir/srpmtools/hooks
%endif

%changelog
* Wed Nov 04 2020 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- new version

* Wed Apr 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- new version

* Fri Apr 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- new version

* Sat Dec 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- new version

* Fri Apr 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- new version

* Mon Mar 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- new version

* Thu Feb 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- new version

* Thu Feb 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- new version

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- new version

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- logoved-batchfix first release

* Sun Feb 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- new version

* Fri Feb 08 2019 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- new version

* Wed Feb 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- new version

* Thu Jan 03 2019 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- new version
- note: DB is constantly updated, it is not packaged yet.
  use git repo for Logoved DB.

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- bugfix release

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- Sisyphus release (closes: #35459)
- note: DB is constantly updated, it is not packaged yet.
- use git repo for Logoved DB.

* Wed Oct 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial rpm build

