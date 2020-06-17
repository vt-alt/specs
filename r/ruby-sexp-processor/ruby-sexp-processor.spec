%define        pkgname sexp-processor
%define        gemname sexp_processor

Name:          ruby-%pkgname
Version:       4.12.1
Release:       alt1
Summary:       sexp_processor branches from ParseTree bringing all the generic sexp processing tools with it
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/sexp_processor
%vcs           https://github.com/seattlerb/sexp_processor.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe)

%description
sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all for
your language processing pleasure.


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
* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 4.12.1-alt1
- Bump to 4.12.1
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.11.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 4.11.0-alt1
- Initial build for Sisyphus
