%define pkgname builder

Name:          ruby-%pkgname
Version:       3.2.3
Release:       alt2
Summary:       Provide a simple way to create XML markup and data structures
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tenderlove/builder
%vcs           https://github.com/tenderlove/builder.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Provide a simple way to create XML markup and data structures.
Builder::XmlMarkup:: Generate XML markup notiation
Builder::XmlEvents:: Generate XML events (i.e. SAX-like)

%description -l ru_RU.UTF8
Позволяет простым способом создавать XML разметку и структуры данных.
Builder::XmlMarkup:: Создание записи с XML разметкою.
Builder::XmlEvents:: Создание событий XML (т.е. подобные SAX)


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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.2.3-alt2
- Use Ruby Policy 2.0

* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 3.2.3-alt1
- new version 3.2.3

* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1.1
- Built version 3.2.0

* Wed Dec 05 2012 Led <led@altlinux.ru> 3.0.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 3.0.0-alt1
- [3.0.0]

* Tue Nov 30 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.2-alt4
- Fix build with Ruby 1.9.2

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 2.1.2-alt3
- Rebuilt with Ruby 1.9

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 2.1.2-alt2
- Rebuilt with rpm-build-ruby

* Mon Jan 07 2008 Sir Raorn <raorn@altlinux.ru> 2.1.2-alt1
- Initial build for ALT Linux

