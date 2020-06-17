%define        pkgname jquery-turbolinks

Name:          gem-%pkgname
Version:       2.1.0
Release:       alt1.1
Summary:       jQuery plugin for drop-in fix binded events problem caused by Turbolinks
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/kossnocorp/jquery.turbolinks
Vcs:           https://github.com/kossnocorp/jquery.turbolinks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
This gem does not work with Turbolinks 5+, and is not compatible with many
jQuery plugins. We do not recommend using it. Instead, please consider writing
your JavaScript in a way that makes it compatible with Turbolinks. These
resources can help:

* RSJS - A reasonable structure for JS, a document outlining how to write
  JavaScript as "behaviors" that will be compatible with Turbolinks.

* onmount - 1kb library to run something when a DOM element appears and when it
  exits.

Rationale: making jQuery plugins compatible with Turbolinks requires more than
simply dropping in a library. It should be able to setup and teardown its
changes as needed, which is something you can't automate. jQuery Turbolinks's
approach worked well enough for many libraries back in 2013, but today this is
no longer the case. Given its utility is very limited, we've decided to no
longer maintain this library.


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
sed "s,'turbolinks','gitlab-turbolinks-classic'," -i %pkgname.gemspec

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Fri May 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1.1
- ! spec syntax, and tags
- ! replace require dep to gitlab-turbolinks-classic

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
