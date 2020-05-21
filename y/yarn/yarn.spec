
Name: yarn
Version: 1.22.4
Release: alt0.1.p9
Summary: Fast, reliable, and secure dependency management
Group: Development/Tools
License: BSD
Url: https://yarnpkg.com
Source: https://github.com/yarnpkg/yarn/releases/download/v%version/yarn-v%version.tar.gz

BuildRequires(pre): rpm-macros-nodejs

BuildArch: noarch

Conflicts: hadoop-yarn
Conflicts: cmdtest

%description
Fast, reliable, and secure dependency management.
Yarn: Fast, reliable, and secure dependency management.

%prep
%setup -n %name-v%version

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%name %buildroot%_bindir
cp -a . %buildroot%nodejs_sitelib/%name/
ln -s %nodejs_sitelib/%name/bin/%name.js %buildroot%_bindir/%name
ln -s %nodejs_sitelib/%name/bin/%name.js %buildroot%_bindir/yarnpkg

%files
%_bindir/*
%nodejs_sitelib/%name

%changelog
* Wed May 20 2020 Andrey Cherepanov <cas@altlinux.org> 1.22.4-alt0.1.p9
- Backport new version to p9 branch.
- Set conflicts to hadoop-yarn and cmdtest.

* Sat Apr 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.22.4-alt1
- 1.22.4

* Sun Mar 01 2020 Alexey Shabalin <shaba@altlinux.org> 1.22.0-alt1
- 1.22.0

* Tue Aug 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.17.3-alt1
- 1.17.3

* Tue Feb 26 2019 Alexey Shabalin <shaba@altlinux.org> 1.14.0-alt1
- 1.14.0

* Fri Oct 19 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.10.1-alt1
- update to 1.10.1
- remove ubt macros due binary package identity changes

* Fri May 11 2018 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1.S1
- 1.6.0

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 0.27.5-alt1%ubt
- rebuild with Universal Branch Tag

* Wed Jul 26 2017 Alexey Shabalin <shaba@altlinux.ru> 0.27.5-alt1
- first build for ALT Linux.
