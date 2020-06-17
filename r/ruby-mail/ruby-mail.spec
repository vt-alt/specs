%define        pkgname mail

Name: 	       ruby-%pkgname
Version:       2.7.1
Release:       alt2
Summary:       A really Ruby Mail handler
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mikel/mail
%vcs           https://github.com/mikel/mail.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Mail is an internet library for Ruby that is designed to handle emails
generation, parsing and sending in a simple, rubyesque manner.


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
* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.1-alt2
^ Ruby Policy 2.0

* Sun Oct 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Nov 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version

* Sat Jun 10 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.6-alt1
- New version

* Thu Apr 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- New version
- Disable test because they require network connections

* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 2.5.4-alt1
- Initial build for ALT Linux
