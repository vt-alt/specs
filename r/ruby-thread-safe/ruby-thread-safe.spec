%define        pkgname thread-safe
%define        gemname thread_safe

Name:          ruby-%pkgname
Version:       0.3.6
Release:       alt2
Summary:       Thread-safe collections for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/ruby-concurrency/thread_safe
%vcs           https://github.com/ruby-concurrency/thread_safe.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary


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
* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.6-alt2
^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.6-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.6-alt1
- Initial build for Sisyphus
