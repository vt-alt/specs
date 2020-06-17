%define        pkgname google-auth
%define        gemname googleauth

Name:          ruby-%pkgname
Epoch:         1
Version:       0.8.1
Release:       alt1
Summary:       Google Auth Library for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/googleapis/google-auth-library-ruby
%vcs           https://github.com/googleapis/google-auth-library-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

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
%ruby_build --use=%gemname --alias=%pkgname

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
* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.8.1-alt1
- Bump to 0.8.1
- Use Ruby Policy 2.0

* Wed Nov 14 2018 Pavel Skrylev <majioa@altlinux.org> 1:0.6.7-alt1
- rollback to 0.6.7.

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt1
- new version 0.7.1

* Wed Oct 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- bump to 0.7.0

* Tue Sep 04 2018 Pavel Skrylev <majioa@altlinux.org> 0.6.6-alt1
- bump to 0.6.6

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus
