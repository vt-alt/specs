%define        pkgname psych

Name:          gem-%pkgname
Version:       3.1.1
Release:       alt0.0.1
Summary:       A libyaml wrapper for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/psych
Vcs:           https://github.com/ruby/psych.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rake-compiler-dock)

%description
Psych is a YAML parser and emitter. Psych leverages libyaml for its YAML parsing
and emitting capabilities. In addition to wrapping libyaml, Psych also knows how
to serialize and de-serialize most Ruby objects to and from the YAML format.


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %{name}.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.

%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         devel
%ruby_includedir/*

%files         doc
%ruby_gemdocdir

%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt0.0.1
- ^ 3.1.0 -> 3.1.1pre
- ! spec syntax and tags

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
