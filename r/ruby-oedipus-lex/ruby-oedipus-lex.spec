%define        pkgname oedipus-lex
%define        gemname oedipus_lex

Name:          ruby-%pkgname
Version:       2.5.1
Release:       alt1
Summary:       This is not your father's lexer
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/oedipus_lex
%vcs           https://github.com/seattlerb/oedipus_lex.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe) >= 3.17
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7.0

Provides: ruby-%pkgname = %EVR

%description
Oedipus Lex is a lexer generator in the same family as Rexical and Rex.
Oedipus Lex is my independent lexer fork of Rexical. Rexical was in turn
a fork of Rex. We've been unable to contact the author of rex in order
to take it over, fix it up, extend it, and relicense it to MIT. So,
Oedipus was written clean-room in order to bypass licensing constraints
(and because bootstrapping is fun).


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
* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- Bump to 2.5.1
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus
