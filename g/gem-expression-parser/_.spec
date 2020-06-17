%define        pkgname expression-parser
%define        gemname expression_parser

Name:          gem-%pkgname
Version:       0.9.1
Release:       alt1
Summary:       Math parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nricciar/expression_parser
%vcs           https://github.com/nricciar/expression_parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(rake)
BuildRequires: gem(rspec)
#BuildRequires: gem()

%description
Math parser based on Lukasz Wrobel's blog post.


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
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
