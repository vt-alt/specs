%define        pkgname sinatra

Name: 	       ruby-%pkgname
Version:       2.0.5
Release:       alt1
Epoch:         1
Summary:       Classy web-development dressed in a DSL
License:       MIT
Group:         Development/Ruby
Url:           http://www.sinatrarb.com/
%vcs           https://github.com/sinatra/sinatra.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rack-test)
BuildRequires: gem(rspec) >= 3.6
BuildRequires: gem(haml)
BuildRequires: gem(erubi)
BuildRequires: gem(erubis)
BuildRequires: gem(slim)
BuildRequires: gem(less)
BuildRequires: gem(sass)
BuildRequires: gem(builder)
BuildRequires: gem(liquid)
BuildRequires: gem(redcarpet)
BuildRequires: gem(RedCloth) >= 4.2.9
BuildRequires: gem(asciidoctor)
BuildRequires: gem(radius)
BuildRequires: gem(coffee-script)
BuildRequires: gem(nokogiri)
BuildRequires: gem(creole)
BuildRequires: gem(wikicloth)
BuildRequires: gem(markaby)
BuildRequires: gem(rake) >= 11
%filter_from_requires \,^ruby(rack/show_exceptions)$,d
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n ruby-rack-protection
Summary:       This gem protects against typical web attacks
Group:         Development/Ruby

%description   -n ruby-rack-protection
This gem protects against typical web attacks. Should work for all Rack
apps, including Rails.


%package       -n ruby-rack-protection-doc
Summary:       Documentation files for ruby-rack-protection gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-rack-protection
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-rack-protection-doc
Documentation files for ruby-rack-protection gem.

%description   -n ruby-rack-protection-doc -l ru_RU.UTF8
Файлы сведений для самоцвета ruby-rack-protection.


%package       contrib
Summary:       Collection of common Sinatra extensions, semi-officially supported
Group:         Development/Ruby

%description   contrib
Collection of common Sinatra extensions, semi-officially supported:
- sinatra/capture: Let's you capture the content of blocks in templates.
- sinatra/config_file: Allows loading configuration from yaml files.
- sinatra/content_for: Adds Rails-style content_for helpers to Haml,
  Erb, Erubis and Slim.
- sinatra/cookies: A cookies helper for reading and writing cookies.
- sinatra/engine_tracking: Adds methods like haml? that allow helper
  methods to check whether they are called from within a template.
- sinatra/json: Adds a #json helper method to return JSON documents.
- sinatra/link_header: Helpers for generating link HTML tags and
  corresponding Link HTTP headers. Adds link, stylesheet and prefetch
  helper methods.
- sinatra/multi_route: Adds ability to define one route block for
  multiple routes and multiple or custom HTTP verbs.
- sinatra/namespace: Adds namespace support to Sinatra.
- sinatra/respond_with: Choose action and/or template automatically
  depending on the incoming request. Adds helpers respond_to and
  respond_with.
- sinatra/custom_logger: This extension allows you to define your own
  logger instance using +logger+ setting. That logger then will be
  available as #logger helper method in your routes and views.
- sinatra/required_params: Ensure if required query parameters exist


%package       contrib-doc
Summary:       Documentation files for %gemname-contrib gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname-contrib
Group:         Development/Documentation
BuildArch:     noarch

%description   contrib-doc
Documentation files for %gemname-contrib gem.

%description   contrib-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname-contrib.


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

%files         -n ruby-rack-protection
%doc rack-protection/README*
%ruby_gemspecdir/rack-protection-%version.gemspec
%ruby_gemslibdir/rack-protection-%version

%files         -n ruby-rack-protection-doc
%ruby_gemsdocdir/rack-protection-%version

%files         contrib
%doc sinatra-contrib/README*
%ruby_gemspecdir/%pkgname-contrib-%version.gemspec
%ruby_gemslibdir/%pkgname-contrib-%version

%files         contrib-doc
%ruby_gemsdocdir/%pkgname-contrib-%version


%changelog
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.0.5-alt1
- Bump to 2.0.5
- Use Ruby Policy 2.0

* Mon Nov 12 2018 Alexey Shabalin <shaba@altlinux.org> 1:2.0.4-alt1
- 2.0.4

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.4.8-alt1.2
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.4.8-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Jun 20 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.4.8-alt1
- Downgrade version to work with old ruby-rack

* Mon Jun 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt2
- Build with ruby-rack 1.x

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
