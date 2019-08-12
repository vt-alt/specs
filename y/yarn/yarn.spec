
Name: yarn
Version: 1.17.3
Release: alt1
Summary: Fast, reliable, and secure dependency management
Group: Development/Tools
License: BSD
Url: https://yarnpkg.com
Source: https://github.com/yarnpkg/yarn/releases/download/v%version/yarn-v%version.tar.gz

BuildRequires(pre): rpm-macros-nodejs

BuildArch: noarch

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
