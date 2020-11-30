Name: altlinux-repolist-utils
Version: 0.008
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: map src/bin names and files in ALTLinux repos using src.list/bin.list
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Source: %name-%version.tar
Url: http://www.altlinux.org/Sisyphus/Tools/Repolist

BuildRequires: rpm-build-perl perl(Source/Shared/FindLocalMirror/ALTLinux.pm)

%description
%summary

%define module ALTLinux-RepoList

%package -n perl-%module
Summary: %module - Perl extension for quering ALTLinux repository list files
Group: Development/Perl

%description  -n perl-%module
%module - Perl extension for quering ALTLinux repository list files

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
cp -a altlinux-repolist-*-to-* %buildroot%_bindir/
mkdir -p %buildroot%perl_vendor_privlib/ALTLinux/RepoList/
install -m 644 ALTLinux/*.pm %buildroot%perl_vendor_privlib/ALTLinux/
install -m 644 ALTLinux/RepoList/*.pm %buildroot%perl_vendor_privlib/ALTLinux/RepoList/

%files
%doc README
%_bindir/*

%files -n perl-%module
%perl_vendor_privlib/ALTLinux/*

%changelog
* Thu Nov 19 2020 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- bugfix in altlinux-repolist-src-names-* thanks to grenka@

* Tue Sep 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- fixed false warning

* Thu Sep 10 2020 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- extended API
- support of zme'd list

* Thu Sep 10 2020 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2
- support of both compressed and uncompressed lists

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- support of compressed lists
- added perl module subpackage

* Fri Feb 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- use symlinks (closes: #36157)

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- new version

* Tue Apr 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- new version

* Sat Apr 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
