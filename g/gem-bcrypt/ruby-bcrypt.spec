%define        pkgname bcrypt

Name:          gem-%pkgname
Version:       3.1.13
Release:       alt1.3
Summary:       bcrypt-ruby is a Ruby binding for the OpenBSD bcrypt() password hashing algorithm, allowing you to easily store a secure hash of your users' passwords
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/codahale/bcrypt-ruby
Vcs:           https://github.com/codahale/bcrypt-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project for hashing passwords. The bcrypt Ruby gem provides a
simple wrapper for safely handling passwords.


%package       devel
Summary:       Development files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


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
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/mri


%changelog
* Tue Apr 07 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.13-alt1.3
- ! spec obsoletes/provides pair

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.13-alt1.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.13-alt1.1
- fixed (!) spec according to changelog rules

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.13-alt1
- fixed (!) spec
- updated (^) 3.1.12 -> 3.1.13

* Thu Apr 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.12-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.12-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.12-alt1
- Initial build for Sisyphus
