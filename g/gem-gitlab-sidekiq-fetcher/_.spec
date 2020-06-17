# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname gitlab-sidekiq-fetcher

Name:          gem-%pkgname
Version:       0.5.2
Release:       alt1
Summary:       Redis reliable queue pattern implemented in Sidekiq
License:       LGPLv3
Group:         Development/Ruby
Url:           https://gitlab.com/gitlab-org/sidekiq-reliable-fetch/
Vcs:           https://gitlab.com/gitlab-org/sidekiq-reliable-fetch.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.

gitlab-sidekiq-fetcher is an extension to Sidekiq that adds support for reliable
fetches from Redis.

It's based on https://github.com/TEA-ebook/sidekiq-reliable-fetch.

There are two strategies implemented: Reliable fetch using rpoplpush command and
semi-reliable fetch that uses regular brpop and lpush to pick the job and put it
to working queue. The main benefit of "Reliable" strategy is that rpoplpush is
atomic, eliminating a race condition in which jobs can be lost. However, it
comes at a cost because rpoplpush can't watch multiple lists at the same time
so we need to iterate over the entire queue list which significantly increases
pressure on Redis when there are more than a few queues. The "semi-reliable"
strategy is much more reliable than the default Sidekiq fetcher, though.
Compared to the reliable fetch strategy, it does not increase pressure on Redis
significantly.


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
* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
