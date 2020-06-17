%define        pkgname puppet-lint

Name: 	       ruby-%pkgname
Version:       3.0.1
Release:       alt0.1
Summary:       Check that your Puppet manifests conform to the style guide
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rodjek/puppet-lint/
%vcs           https://github.com/rodjek/puppet-lint.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
The goal of this project is to implement as many of the recommended
Puppet style guidelines from the Puppet Labs style guide as practical.
It is not meant to validate syntax. Please use "puppet parser validate"
for that.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt0.1
^ 3.0.1 pre (really 2.3.6)
^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 06 2017 Denis Medvedev <nbr@altlinux.org> 3.0.0-alt1
- bump to version 3.0.0

* Wed Dec 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux
