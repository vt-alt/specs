# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname taskjuggler

Name:          %pkgname
Version:       3.6.0
Release:       alt2
Summary:       TaskJuggler - Project Management beyond Gantt chart drawing
Group:         Office
License:       GPLv2
URL:           http://www.taskjuggler.org
%vcs           https://github.com/taskjuggler/TaskJuggler.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(term-ansicolor)
BuildRequires: gem(mail)

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
TaskJuggler is a modern and powerful project management tool. Its new
approach to project planning and tracking is far superior to the
commonly used Gantt chart editing tools. It has already been
successfully used in many projects and scales easily to projects with
hundreds of resources and thousands of tasks. It covers the complete
spectrum of project management tasks from the first idea to the
completion of the project. It assists you during project scoping,
resource assignment, cost and revenue planning, and risk and
communication management.


%package       -n gem-%pkgname
Summary:       Library for %gemname gem
Summary(ru_RU.UTF-8): Библиотечные файлы для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%pkgname
Library for %gemname gem.

%description   -n gem-%pkgname -l ru_RU.UTF8
Библиотечные файлы для %gemname самоцвета.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      %pkgname-doc
Obsoletes:     %pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
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
#%_bindir/tj3*
#%_mandir/*

%files         -n gem-%pkgname
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version

* Wed Feb 06 2013 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version 3.4.0

* Wed Feb 06 2013 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt2
- Fix build in Sisyphus
- Apply Fedora patches

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.1
- Fixed build

* Sat Mar 05 2011 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt1
- Return to Sisyphus

