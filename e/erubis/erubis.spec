%define        pkgname erubis

Name: 	       %pkgname
Version:       2.7.0
Release:       alt4
Summary:       A fast and extensible eRuby implementation
License:       MIT
Group:         Development/Ruby
Url:           http://www.kuwata-lab.com/erubis/
%vcs           https://github.com/kwatch/erubis.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Erubis is a fast, secure, and very extensible implementation of eRuby.
It has the following features:
* Very fast, almost three times faster than ERB and about ten percent
  faster than eruby (implemented in C).
* File caching of converted Ruby script support.
* Auto escaping (sanitizing) support, it means that '<%%= %%>' can be
  escaped in default. It is desirable for web application.
* Spaces around '<%% %%>' are trimmed automatically only when '<%%' is at the
  beginning of line and '%%>' is at the end of line.
* Embedded pattern changeable (default '<%% %%>'), for example '[%% %%]' or
  '<? ?>' are available.
* Enable to handle Processing Instructions (PI) as embedded pattern (ex.
  '<?rb ... ?>'). This is desirable for XML/HTML than '<%% .. %%>' because
  the latter breaks HTML design but the former doesn't.
* Multi-language support (Ruby/PHP/C/Java/Scheme/Perl/Javascript).
* Context object available and easy to combine eRuby template with YAML
  datafile (see the below example).
* Print statement available.
* Easy to expand and customize in subclass
* Ruby on Rails support.
* Mod_ruby support.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname самоцвета.


%package       -n gem-%pkgname
Summary:       Library file for %gemname gem
Summary(ru_RU.UTF-8): Библиотеки для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%pkgname
Library file for %gemname gem.

%description   -n gem-%pkgname -l ru_RU.UTF8
Библиотеки для %gemname самоцвета.


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
%_bindir/%name

%files         -n gem-%pkgname
%ruby_sitelibdir/*
%rubygem_specdir/*

%files         doc
%ruby_ri_sitedir/*

%changelog
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.0-alt4
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt3.1
- Rebuild with new Ruby autorequirements.

* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt3
- Fix ruby(compiler) unmet and remove Rails helper

* Tue Oct 04 2016 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt2
- Rebuild without ruby-actionpack

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- Initial build for ALT Linux (without tests)
