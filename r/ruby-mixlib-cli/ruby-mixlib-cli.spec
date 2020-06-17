%define        pkgname mixlib-cli

Name: 	       ruby-%pkgname
Version:       2.1.3
Release:       alt1
Summary:       A mixin for creating command line applications
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-cli
%vcs           https://github.com/chef/mixlib-cli.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Mixlib::CLI provides a class-based command line option parsing object,
like the one used in Chef, Ohai and Relish.


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
* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.3-alt1
^ v2.1.3
^ Ruby Policy 2.0

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.6-alt1
- New version.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux
