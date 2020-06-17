%define        pkgname turbolinks

Name:          ruby-%pkgname
Epoch:         1
Version:       5.2.1
Release:       alt1
Summary:       Turbolinks makes navigating your web application faster
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/turbolinks/turbolinks
%vcs           https://github.com/turbolinks/turbolinks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Turbolinks(r) makes navigating your web application faster. Get the
performance benefits of a single-page application without the added
complexity of a client-side JavaScript framework. Use HTML to render
your views on the server side and link to pages as usual. When you
follow a link, Turbolinks automatically fetches the page, swaps in its
<body>, and merges its <head>, all without incurring the cost of a full
page load.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
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
* Thu Sep 19 2019 Pavel Skrylev <majioa@altlinux.org> 1:5.2.1-alt1
- ^ v5.2.1
- ^ Ruby Policy 2.0

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 1:2.5.4-alt2
- Added new epoch.

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.4-alt1
- Downgrade to 2.5.4 for foreman.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Fri Jul 27 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1.1
- Use appropriate source from https://github.com/turbolinks/turbolinks-rails.
- Rebuild with new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- Initial build for Sisyphus
