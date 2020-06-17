%define        pkgname deep-cloneable
%define        gemname deep_cloneable

Name:          ruby-%pkgname
Version:       3.0.0
Release:       alt1
Summary:       This gem gives every ActiveRecord::Base object the possibility to do a deep clone that includes user specified associations.
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/moiristo/deep_cloneable
%vcs           http://github.com/moiristo/deep_cloneable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
This gem gives every ActiveRecord::Base object the possibility to do a deep
clone that includes user specified associations. It is a rails 3+ upgrade of
the deep_cloning plugin.


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
%doc readme*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ v3.0.0
- ^ Ruby Policy 2.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1
- Initial build for Sisyphus
