%define        pkgname markaby

Name:          gem-%pkgname
Version:       0.9.0
Release:       alt1
Summary:       markup as ruby
License:       MIT
Group:         Development/Ruby
Url:           http://markaby.github.com/
%vcs           https://github.com/markaby/markaby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(builder)

%description
Markaby is a very short bit of code for writing HTML pages in pure Ruby. It is
an alternative to ERb which weaves the two languages together. Also
a replacement for templating languages which use primitive languages that blend
with HTML.


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
