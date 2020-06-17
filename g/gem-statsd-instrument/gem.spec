# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname statsd-instrument

Name:          gem-%pkgname
Version:       2.4.0
Release:       alt1
Summary:       A StatsD client for Ruby apps. Provides metaprogramming methods to inject StatsD instrumentation into your code
License:       MIT
Group:         Development/Ruby
Url:           http://shopify.github.io/statsd-instrument/
%vcs           https://github.com/Shopify/statsd-instrument.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
This is a ruby client for statsd (http://github.com/etsy/statsd). It provides a
lightweight way to track and measure metrics in your application.

We call out to statsd by sending data over a UDP socket. UDP sockets are fast,
but unreliable, there is no guarantee that your data will ever arrive at its
location. In other words, fire and forget. This is perfect for this use case
because it means your code doesn't get bogged down trying to log statistics. We
send data to statsd several times per request and haven't noticed a performance
hit.

For more information about StatsD, see the README of the Etsy project.


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
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- updated to (^) v2.4.0
- fix (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.2-alt1
- added (+) initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
