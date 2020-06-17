%define        pkgname prometheus-client

Name:          gem-%pkgname
Version:       2.0.0
Release:       alt1
Summary:       A suite of instrumentation metric primitivesthat can be exposed through a web services interface
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/prometheus/client_ruby
%vcs           https://github.com/prometheus/client_ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
A suite of instrumentation metric primitives for Ruby that can be exposed
through a HTTP interface. Intended to be used together with a Prometheus server.


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
%ruby_build --ignore=rack

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
* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- updated (^) 0.9.0 -> 2.0.0

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt2
- added (+) findreq filter in spec
- fixed (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
