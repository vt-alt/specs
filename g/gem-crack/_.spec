%define        pkgname crack

Name:          gem-%pkgname
Version:       0.4.3
Release:       alt1
Summary:       Really simple JSON and XML parsing, ripped from Merb and Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jnunemaker/crack
%vcs           https://github.com/jnunemaker/crack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Really simple JSON and XML parsing, ripped from Merb and Rails. The XML parser
is ripped from Merb and the JSON parser is ripped from Rails. I take no credit,
just packaged them for all to enjoy and easily use.


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
* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
