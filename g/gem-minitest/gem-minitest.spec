%define  pkgname minitest

Name:          gem-%pkgname
Version:       5.14.0
Release:       alt1.1
Summary:       Minitest provides a complete suite of testing facilities supporting TDD, BDD, mocking, and benchmarking
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest
Vcs:           https://github.com/seattlerb/minitest.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-hoe
BuildRequires: ruby-rdoc

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Minitest provides a complete suite of testing facilities supporting TDD, BDD,
mocking, and benchmarking. "I had a class with Jim Weirich on testing last week
and we were allowed to choose our testing frameworks. Kirk Haines and I were
paired up and we cracked open the code for a few test frameworks... I MUST say
that minitest is *very* readable / understandable compared to the 'other two'
options we looked at. Nicely done and thank you for helping us keep our mental
sanity." -- Wayne E. Seguin minitest/test is a small and incredibly fast unit
testing framework. It provides a rich set of assertions to make your tests clean
and readable. minitest/spec is a functionally complete spec engine. It hooks
onto minitest/test and seamlessly bridges test assertions over to spec
expectations. minitest/benchmark is an awesome way to assert the performance of
your algorithms in a repeatable manner. Now you can assert that your newb
co-worker doesn't replace your linear algorithm with an exponential one!
minitest/mock by Steven Baker, is a beautifully tiny mock (and stub) object
framework. minitest/pride shows pride in testing and adds coloring to your test
output. I guess it is an example of how to write IO pipes too. :P minitest/test
is meant to have a clean implementation for language implementors that need
a minimal set of methods to bootstrap a working test suite. For example, there
is no magic involved for test-case discovery. "Again, I can't praise enough
the idea of a testing/specing framework that I can actually read in full in one
sitting!" -- Piotr Szotkowski Comparing to rspec: rspec is a testing DSL.
minitest is ruby. -- Adam Hawkins, "Bow Before MiniTest" minitest doesn't
reinvent anything that ruby already provides, like: classes, modules,
inheritance, methods. This means you only have to learn ruby to use minitest
and all of your regular OO practices like extract-method refactorings still
apply.


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
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*


%changelog
* Thu Apr 09 2020 Pavel Skrylev <majioa@altlinux.org> 5.14.0-alt1.1
- - obsolete/require pair

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 5.14.0-alt1
- > Ruby Policy 2.0
- ^ 5.11.3 -> 5.14.0
- ! spec tags

* Mon Jan 14 2019 Pavel Skrylev <majioa@altlinux.org> 5.11.3-alt1
- Initial build for Sisyphus, packaged as a gem
