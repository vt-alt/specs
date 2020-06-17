%define        pkgname rails-dom-testing

Name:          gem-%pkgname
Version:       2.0.3
Release:       alt2
Summary:       Extracting DomAssertions and SelectorAssertions from ActionView
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/rails-dom-testing
Vcs:           https://github.com/rails/rails-dom-testing.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.

This gem is responsible for comparing HTML doms and asserting that DOM elements
are present in Rails applications. Doms are compared via assert_dom_equal and
assert_dom_not_equal. Elements are asserted via assert_select,
assert_select_encoded, assert_select_email and a subset of the dom can be
selected with css_select. The gem is developed for Rails 4.2 and above, and
will not work on previous versions.

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
* Thu May 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.3-alt2
- > Ruby Policy 2.0
- ! spec tags

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus
