%define        pkgname mini_portile2

Name: 	       ruby-%pkgname
Version:       2.4.0
Release:       alt2
Summary:       Simple autoconf builder for developers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flavorjones/mini_portile
%vcs           https://github.com/flavorjones/mini_portile.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
It's intended primarily to make sure that you, as the developer of a
library, can reproduce a user's dependencies and environment by
specifying a specific version of an underlying dependency that you'd
like to use.


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
* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt2
^ Ruby Policy 2.0

* Wed Jan 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- Bump to 2.4.0;
- Place library into proper ruby gem folder.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt2.1
- Rebuild for new Ruby autorequirements.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt2
- Package as gem.
- Disable tests.

* Thu Sep 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version

* Mon Sep 26 2016 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux
