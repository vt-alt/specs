%define	       pkgname ronn

Name:          gem-%pkgname
Version:       0.7.3
Release:       alt4.1
Summary:       Ronn builds manuals from Markdown to roff format
License:       MIT
Group:         Development/Documentation
Url:           https://github.com/rtomayko/ronn/
Vcs:           https://github.com/rtomayko/ronn.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ronn)
BuildRequires: gem(hpricot)
BuildRequires: gem(rdiscount)
BuildRequires: gem(mustache)

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
Ronn builds manuals. It converts simple, human readable textfiles to
roff for terminal display, and also to HTML for the web. The source
format includes all of Markdown but has a more rigid structure and
syntax extensions for features commonly found in manpages (definition
lists, link notation, etc.). The ronn-format(7) manual page defines the
format in detail.


%package       -n %pkgname
Summary:       Ronn builds manuals from Markdown to roff format
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
%summary.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


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

%files         -n %pkgname
%doc README*
%_bindir/%pkgname
%_mandir/*.1*
%_mandir/*.7*

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt4.1
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt4
- fixed (!) spec according to changelog rules

* Thu Jul 25 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt3
- fixed (!) spec
- added (+) ronn gem build dependency

* Tue Apr 09 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus
