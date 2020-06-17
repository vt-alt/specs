%define        pkgname jsminc

Name:          gem-%pkgname
Version:       2.0.0
Release:       alt3
Summary:       A fast JavaScript minifier written in C (by Douglas Crockford)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rf-/jsminc
Vcs:           https://github.com/rf-/jsminc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
%summary. JSMinC is the original C version of JSMin, embedded in Ruby.


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
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%changelog
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt3
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt2
- > Ruby Policy 2.0

* Sun Jun 10 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.1
- Rebuild for aarch64.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
