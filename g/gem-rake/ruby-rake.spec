%define        pkgname rake

Name:          gem-%pkgname
Version:       13.0.1
Release:       alt1
Summary:       Ruby based make-like utility
Summary(ru_RU.UTF-8): Make-подобная утилита для рубина
License:       MIT
Group:         Development/Ruby
Url:           https://ruby.github.io/rake/
Vcs:           https://github.com/ruby/rake.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(minitest)
BuildRequires: gem(rdoc)
BuildRequires: gem(coveralls)
BuildRequires: gem(rubocop)

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies
are specified in standard Ruby syntax.

%description -l ru_RU.UTF-8
Rake есть Make-подобная утилита и набор модулей, исполненные на рубине.
Задачи и зависимости описываются в рядовом правописании рубина.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета


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
%rake_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/%pkgname
%_mandir/*


%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 13.0.1-alt1
- ^ 12.3.3 -> 13.0.1
- ! spec tags

* Mon Sep 09 2019 Pavel Skrylev <majioa@altlinux.org> 12.3.3-alt1
- update (^) 12.3.2 -> 12.3.3
- fix (!) spec to allow building

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 12.3.2-alt3
- Use Ruby Policy 2.0

* Thu Jan 17 2019 Pavel Skrylev <majioa@altlinux.org> 12.3.2-alt2
- Fix the executable, which is being get from proper source;
- Place library files into gem folder.

* Fri Dec 28 2018 Pavel Skrylev <majioa@altlinux.org> 12.3.2-alt1
- Bump to 12.3.2.
- Russian descriptions.

* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 0.8.7-alt3
- Rebuild with new ruby.

* Tue Jan 04 2011 Alexey I. Froloff <raorn@altlinux.org> 0.8.7-alt2
- Updated to rake-0.8.7-134-g9dad179

* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 0.8.7-alt1
- [0.8.7]

* Wed May 06 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.4-alt1
- [0.8.4]

* Sun Mar 30 2008 Sir Raorn <raorn@altlinux.ru> 0.8.1-alt1
- [0.8.1]

* Thu Jan 24 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.7.3-alt2
- Add ruby-module-misc to requires

* Tue May 22 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Thu Jul 06 2006 Sir Raorn <raorn@altlinux.ru> 0.7.1-alt1
- [0.7.1]

* Tue Mar 07 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.7.0-alt2
- header in /usr/bin/rake fixed [#9195]

* Thu Feb 16 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Wed Aug 31 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.5.4-alt1
- Initial build for ALT Linux

