%define        pkgname ffi-yajl

Name:          gem-%pkgname
Version:       2.3.3
Release:       alt1
Summary:       ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chef/ffi-yajl
Vcs:           https://github.com/chef/ffi-yajl.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         use-system-yajl-without-wrapper.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rack)
BuildRequires: gem(rspec)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rake)
BuildRequires: gem-ffi
BuildRequires: gem(libyajl2)
BuildRequires: libyajl-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
ffi-yajl is a Ruby adapter for the yajl JSON parser/generator library.
ffi-yajl supports multiple Ruby C extension mechanisms, including both
MRI native extensions and FFI in order to be compatible with as many
Ruby implementations as possible while providing good performance where
possible.


%package       -n %{pkgname}-bench
Summary:       HTML, XML, SAX, and Reader parser
Group:         Development/Other
BuildArch:     noarch

%description   -n %{pkgname}-bench
Nokogiri parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support.
This package contanis Ruby libraries for Nokogiri.

Executable file for %gemname gem.

%description   -n %{pkgname}-bench -l ru_RU.UTF8
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


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libyajl-devel

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


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
%ruby_gemextdir

%files         -n %{pkgname}-bench
%doc README*
%_bindir/%{pkgname}-bench

%files          doc
%ruby_gemdocdir

%changelog
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.3-alt1
- ^ 2.3.1 -> 2.3.3
- ! spec stags and syntax

* Tue Mar 12 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt4
- ! built extensions by the patch

* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt3
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt2.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt2
- Fix yajl-ruby library name.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Jun 22 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt2
- Rebuild with new %%ruby_sitearchdir location
- Optionally build benchmark tool, disabled by default

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Tue Sep 22 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- New version

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux
