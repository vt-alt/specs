%define        pkgname erubi

Name:          ruby-%pkgname
Version:       1.8.0
Release:       alt1
Summary:       Small ERB Implementation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jeremyevans/erubi
%vcs           https://github.com/jeremyevans/erubi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Erubi is a ERB template engine for ruby. It is a simplified fork of Erubis,
using the same basic algorithm, with the following differences:

* Handles postfix conditionals when using escaping
* Supports frozen_string_literal: true in templates via :freeze option
* Works with ruby's -enable-frozen-string-literal option
* Automatically freezes strings for template text when ruby optimizes it (on
  ruby 2.1+)
* Escapes ' (apostrophe) when escaping for better XSS protection
* Has 6x faster escaping on ruby 2.3+ by using cgi/escape
* Has 86% smaller memory footprint
* Does no monkey patching (Erubis adds a method to Kernel)
* Uses an immutable design (all options passed to the constructor, which returns
  a frozen object)
* Has simpler internals (1 file, <150 lines of code)
* Is not dead (Erubis hasn't been updated since 2011)
* It is not designed with Erubis API compatibility in mind, though most Erubis
  ERB syntax works, with the following exceptions:
* No support for debug output


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname самоцвета.


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
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- Bump to 1.8.0
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- Initial build for Sisyphus
