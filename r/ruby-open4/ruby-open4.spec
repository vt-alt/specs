# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname open4

Name:          ruby-%pkgname
Version:       1.3.4
Release:       alt1
Summary:       Manage child processes and their IO handles easily
License:       Ruby
Group:         Development/Ruby
Url:           http://github.com/ahoward/open4
%vcs           https://github.com/ahoward/open4.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(test-unit)
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Open child process with handles on pid, stdin, stdout, and stderr: manage
child processes and their io handles easily.

This library can read and update netrc files, preserving formatting including
comments and whitespace.


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
* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.4-alt1
^ v1.3.4
^ Ruby Policy 2.0

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1.1
- Rebuild with Ruby 2.4.1

* Sun Sep 25 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.3-alt1
- Update to latest release

* Sat Dec 08 2012 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.0-alt1
- Initial build for Sisyphus

