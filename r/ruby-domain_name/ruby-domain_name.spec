# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname domain_name

Name: 	       ruby-%pkgname
Version:       0.5.20190701
Release:       alt1
Summary:       Domain Name manipulation library for Ruby
License:       BSD\MPLv2.0
Group:         Development/Ruby
Url:           https://github.com/knu/ruby-domain_name
%vcs           https://github.com/knu/ruby-domain_name.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
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


%changelog
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.20190701-alt1
- 0.5.20180417 -> 0.5.20190701
- update to Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.20180417-alt1.1
- Rebuild with new Ruby autorequirements.
- Package as gem.

* Thu Apr 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.20180417-alt1
- New version.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.5.20170404-alt1
- Initial build for Sisyphus.
