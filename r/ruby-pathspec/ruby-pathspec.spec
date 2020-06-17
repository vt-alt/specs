%define        pkgname pathspec

Name: 	       ruby-%pkgname
Version:       0.2.2
Release:       alt0.1
Summary:       Use to match path patterns such as gitignore
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/highb/pathspec-ruby
%vcs           https://github.com/highb/pathspec-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Match Path Specifications, such as .gitignore, in Ruby!


%package       -n %pkgname-rb
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname-rb
Executable file for %gemname gem.

%description   -n %pkgname-rb -l ru_RU.UTF8
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
%ruby_build --use=%gemname --alias=%pkgname-rb --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname-rb
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt0.1
^ v0.2.2pre
^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Dec 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.0.2-alt1
- Initial build for ALT Linux
