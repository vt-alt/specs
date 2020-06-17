# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname mechanize

Name:          gem-%pkgname
Version:       2.7.7
Release:       alt0.1
Summary:       WWW::Mechanize, a handy web browsing ruby object
License:       GPLv2
Group:         Development/Ruby
Url:           https://github.com/sparklemotion/mechanize
Vcs:           https://github.com/sparklemotion/mechanize.git
BuildArch:     noarch
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
The Mechanize library is used for automating interaction with websites.
Mechanize automatically stores and sends cookies, follows redirects,
can follow links, and submit forms.  Form fields can be populated and
submitted.  Mechanize also keeps track of the sites that you have visited as
a history.


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
%ruby_build --use=%gemname --version-replace=%version

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
* Thu Apr 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.7-alt0.1
- ^ 2.7.6 -> 2.7.7pre
- ! spec tags

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.6-alt1
- > Ruby Policy 2.0
- ^ 0.9.3 -> 2.7.6

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1.4
- Rebuild with new Ruby autorequirements.

* Sat Mar 15 2014 Led <led@altlinux.ru> 0.9.3-alt1.3
- fixed encoding without iconv

* Sat Mar 15 2014 Led <led@altlinux.ru> 0.9.3-alt1.2
- don't use iconv for ruby >= 1.9.2

* Fri Dec 07 2012 Led <led@altlinux.ru> 0.9.3-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Dec 11 2009 Igor Zubkov <icesik@altlinux.org> 0.9.3-alt1
- build for Sisyphus

