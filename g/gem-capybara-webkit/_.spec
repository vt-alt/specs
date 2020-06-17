# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname capybara-webkit

Name:          gem-%pkgname
Version:       1.15.1
Release:       alt1.1
Summary:       Headless Webkit driver for Capybara
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thoughtbot/capybara-webkit
Vcs:           https://github.com/thoughtbot/capybara-webkit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: qt5-base-devel
BuildRequires: qt5-webkit-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
A Capybara driver for headless WebKit to test JavaScript web apps.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

Requires:      qt5-base-devel
Requires:      qt5-webkit-devel

%description   devel
Development headers for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


%prep
%setup

%build
export PATH=/usr/share/qt5/bin:$PATH
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel


%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.15.1-alt1.1
- ! spec tag

* Thu Sep 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.15.1-alt1
- + packaged gem with usage Ruby Policy 2.0
