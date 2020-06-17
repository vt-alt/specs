%define        pkgname concurrent-ruby
%define        core_version   1.1.6
%define        edge_version   0.6.0

Name:          gem-%pkgname
Version:       %core_version
Release:       alt1.1
Summary:       Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more.
License:       MIT
Group:         Development/Ruby
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           http://www.concurrent-ruby.com
Vcs:           https://github.com/ruby-concurrency/concurrent-ruby.git

Source:        %name-%version.tar
Source1:       concurrent_ruby.jar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rake-compiler-dock)
#BuildRequires: gem(pry)
BuildRequires: gem(rspec)
BuildRequires: gem(yard)
BuildRequires: gem(redcarpet)
#BuildRequires: gem(md-ruby-eval)
BuildRequires: gem(timecop)
#BuildRequires: gem(sigdump)
BuildRequires: gem(simplecov)
BuildRequires: gem(coveralls)
BuildRequires: gem(benchmark-ips)
#BuildRequires: gem(bench9000)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
Modern concurrency tools for Ruby. Inspired by Erlang, Clojure, Scala, Haskell,
F#, C#, Java, and classic concurrency patterns.

The design goals of this gem are:

* Be an 'unopinionated' toolbox that provides useful utilities without debating
  which is better or why
* Remain free of external gem dependencies
* Stay true to the spirit of the languages providing inspiration
* But implement in a way that makes sense for Ruby
* Keep the semantics as idiomatic Ruby as possible
* Support features that make sense in Ruby
* Exclude features that don't make sense in Ruby
* Be small, lean, and loosely coupled
* Thread-safety
* Backward compatibility


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.


%package       edge
Version:       %edge_version
Summary:       Edge features and additions to the concurrent-ruby gem
Group:         Development/Ruby
BuildArch:     noarch

%description   edge
These features are under active development and may change frequently. They are
expected not to keep backward compatibility (there may also lack tests and
documentation). Semantic versions will be obeyed though. Features developed in
`concurrent-ruby-edge` are expected to move to `concurrent-ruby` when final.
Please see http://concurrent-ruby.com for more information.


%package       edge-doc
Version:       %edge_version
Summary:       Documentation files for %pkgname-edge gem
Group:         Development/Documentation
BuildArch:     noarch

%description   edge-doc
Documentation files for %{pkgname}-edge gem.


%package       ext
Version:       %core_version
Summary:       C extensions to optimize concurrent-ruby under MRI
Group:         Development/Ruby

%description   ext
C extensions to optimize the concurrent-ruby gem when running under MRI.
Please see http://concurrent-ruby.com for more information.


%package       ext-devel
Summary:       Development files for %pkgname-ext gem
Group:         Development/Ruby
BuildArch:     noarch

%description   ext-devel
Development files for %pkgname-ext gem.


%prep
%setup

%build
%ruby_build # --pre=repackage:all

%install
%ruby_install
# TODO: de-build-in
install -D -m644 %SOURCE1 %buildroot%ruby_gemlibdir/lib/concurrent-ruby/concurrent/concurrent_ruby.jar


%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         edge
%ruby_gemspecdir/concurrent-ruby-edge-%edge_version.gemspec
%ruby_gemslibdir/concurrent-ruby-edge-%edge_version

%files         edge-doc
%ruby_gemsdocdir/concurrent-ruby-edge-%edge_version

%files         ext
%ruby_gemspecdir/concurrent-ruby-ext-%version.gemspec
%ruby_gemslibdir/concurrent-ruby-ext-%version
%ruby_gemsextdir/concurrent-ruby-ext-%version

%files         ext-devel
%ruby_includedir/concurrent-ruby-ext

%changelog
* Tue May 12 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.6-alt1.1
- + java part

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.6-alt1
- ^ concurrent-ruby 1.1.5 -> 1.1.6
- ^ concurrent-ruby-ext 1.1.5 -> 1.1.6
- ^ concurrent-ruby-edge 0.5.0 -> 0.6.0
- ! spec syntax

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.5-alt1
- Bump to 1.1.5

* Mon Jan 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt1
- Bump to 1.1.4;
- Use Ruby Policy 2.0.

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt2
- Gemify build for Sisyphus

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus
