%define        pkgname rspec-puppet

Name: 	       ruby-%pkgname
Version:       2.7.5
Release:       alt1
Summary:       RSpec tests for your Puppet manifests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rodjek/rspec-puppet/
%vcs           https://github.com/rodjek/rspec-puppet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*


%package       -n %pkgname-init
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname-init
Executable file for %gemname gem.

%description   -n %pkgname-init -l ru_RU.UTF8
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
%ruby_build --ignore=docs --use=%gemname --alias=%pkgname-init

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname-init
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%description
RSpec tests for your Puppet manifests & modules.

%changelog
* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.5-alt1
^ v2.7.5
^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Wed Dec 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1
- Initial build for ALT Linux
