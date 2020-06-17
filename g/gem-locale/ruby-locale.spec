%define        pkgname locale

Name:          gem-%pkgname
Version:       2.1.3
Release:       alt1
Summary:       Pure ruby library which provides basic APIs for localization
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/ruby-gettext/locale
Vcs:           https://github.com/ruby-gettext/locale.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(test-unit) >= 0
# BuildRequires: gem(test-unit-notify) >= 0
# BuildRequires: gem(test-unit-rr) >= 0
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Ruby-Locale is the pure ruby library which provides basic and general
purpose APIs for localization.

It aims to support all environments which ruby works and all kind of
programs (GUI, WWW, library, etc), and becomes the hub of other
i18n/l10n libs/apps to handle major locale ID standards.


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
* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.3-alt1
- ^ 2.1.3pre -> 2.1.2
- ! spec tags

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.3-alt0.1
- > Ruby Policy 2.0
- ^ 2.1.2 -> 2.1.3 pre

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt4.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt4
- Use system way  of gemspec installation.
- Disable tests.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt3
- Return jruby driver.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt2
- Rebuild with Ruby 2.4.2

* Sun May 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- New version
- Package with gemspec

* Wed Dec 05 2012 Led <led@altlinux.ru> 2.0.6-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 2.0.6-alt1
- [2.0.6]

* Sun Apr 18 2010 Alexey I. Froloff <raorn@altlinux.org> 2.0.5-alt1
- [2.0.5]

* Thu Nov 19 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt4
- Ignore invalid LANGUAGE variable

* Tue Oct 27 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt3
- Fixed String vs. Array clash

* Thu Oct 15 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt2
- Fixed charset detection when LC_* variables unset

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt1
- [2.0.4]

* Wed May 06 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.1-alt1
- Built for Sisyphus

