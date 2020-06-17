%define        pkgname roadie

Name:          ruby-%pkgname
Version:       3.5.0
Release:       alt1
Summary:       Making HTML emails comfortable for the Ruby rockstars
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Mange/roadie
%vcs           https://github.com/Mange/roadie.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Roadie tries to make sending HTML emails a little less painful by inlining
stylesheets and rewriting relative URLs for you inside your emails.


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
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- ^ v3.5.0
- ^ Ruby Policy 2.0

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt1
- + initial gemified build for Sisyphus
