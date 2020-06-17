%define        pkgname truthy

Name:          gem-%pkgname
Version:       1.0.0
Release:       alt2
Summary:       Easily find out the truthiness of any Ruby object
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ymendel/truthy
Vcs:           https://github.com/ymendel/truthy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)
BuildRequires: gem(rspec)
BuildRequires: gem(hoe)

%description
This gem is to make it easier to discover the truth values of various Ruby
objects. Ask any object if it is truthy, and it will tell you.


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
%patch -p1

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
* Mon Mar 30 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- ! spec tags
- ! build with new hoe 3.22.1

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
