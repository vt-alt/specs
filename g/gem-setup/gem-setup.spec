%define        pkgname setup

Name:          gem-%pkgname
Version:       5.999.3
Release:       alt15
Summary:       Ruby's Classic Site Installer
Group:         Development/Ruby
License:       BSD-2-Clause
Url:           https://github.com/rubyworks/setup
Vcs:           https://github.com/majioa/setup.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(olddoc)

Requires:      ruby-pry
Requires:      chrpath
Requires:      setup-rb

%description
Every well practiced Rubyist is aware of Minero Aoki's ever setup.rb script.
It's how most of us used to install our Ruby programs before RubyGems came
along. And it's still mighty useful in certain scenarios, not the least of
which is the job of the distro package maintainer.

Ruby Setup converts setup.rb into a stand-alone application. No longer
requiring the distribution of the setup.rb script with every Ruby package.
Just instruct one's users to install Ruby Setup (gem install setup) and go from
there. As long as a project is setup.rb compliant, as most are, then there is
little to nothing it's developer must do.


%package       -n setup-rb
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n setup-rb
Executable file for %gemname gem.

%description   -n setup-rb -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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
%patch -p1

%build
%__setup_rb build --use=setup --alias=setup-rb

%install
%ruby_install
%__setup_rb install --install_prefix=%buildroot

%check
%ruby_test
%__setup_rb test

%files
%doc README* HISTORY* MANIFEST
%ruby_gemspec
%ruby_gemlibdir

%files         -n setup-rb
%doc README*
%_bindir/setup.rb

%files         doc
%ruby_gemdocdir


%changelog
* Wed Apr 08 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt15
- - explicit use of prefixes key in build section

* Wed Apr 08 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt14
- + default prefixes to 'gem' value

* Wed Apr 08 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt13
- + separation prefixes and suffixes when detection the context (lib/bin/...)
- ! lost prefixes key into build macro (fixes #38337)

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt12
- - erroneous glob lib ext method

* Thu Mar 19 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt11
- * libdir replaced to libexecdir for ruby site target

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt10
- ! call to setup.rb with default pure %%__setup_rb

* Mon Sep 09 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt9
- ! spec according changlelog policy
- + making lost executables again workable (closes #37180)

* Mon Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt8
- - mistake in dependecies detection for Gemfile source
- ! default datadir to libdir for site ruby packages
- ! getting task list from MultiTask instead of Task
- + load rake task imports before executio pre tasks
- ! state dir for gem target from localstatedir to datadir
- + logdir option, and its processing
- ! installer's group methods
- ! options parser for sources to make both key and value changeable
- ! options pass via parser for rakefile source
- ! object class options store to specfic one by changing from @@ to @.
- + ronn man detection and compilation
- + prefixes command line parameter: gem,ruby...
- + source directory groups command line parameters: --src<param>dirs
- ! source module parameter parsing
- + String#pluralize
- + spec selection from Gem::PackageTask object for Rakefile
- - Require dirs detection mistake, not filters out only path with the beginning
  '/'
- - Hoe presence detection error
- + Rookbook gemspec parser (example: erubis gem)
- - Olddoc syntax typo
- - Hoe syntax typo
- + try load hoe gem in the beginning of the how gemspec module
- + support for group trees instead of file lists in sources
- - installation module to support trees
- - compilation modules supporting trees
- - dep module supporting trees
- - bin group name to exe in sources and targets
- - include group name to inc in sources and targets
- - etc group name to conf in sources and targets
- - lost methods in ruby target
- + some kernel methods
- - Prefix remove alias "rails-plugin" for packages
- - Gemfile installation for the Gemfile source is used for gem version
  replacements
- - ERROR msg profix replaced with WARN
- - fix DSL dependenciy replace list for #to_gemfile
- - added compatibility call to external program to do some things for the
  action with --compat=/path/to/program
- - fixed name of the gem file to Gemfile
- - fix loading and saving version replace list for the common and source parts
- - added gem replace verison list argument to gemfile source

* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt7
- Set default external CP to UTF8

* Tue Apr 23 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt6
- - added default value for __dir__ variable, when loading Rakefile info a module,
  this fixes unknown error when adding the var info "$:"
- - separated Hoe gemspec detector from the Rakefile one leading to
  correct evaluation of Rakefile in main space
- - Now old shebang args in the ruby executables will be passed to new
  shebang line
- - Fix sequence so Rakefile will be proceeded before Olddoc gemspecs.
- - Rakefile gemspec detector not will not fall when rakefile name is
  nil
- ! Redone gemspec procedure detection so sequence of gemspecs will be
  affected rather than filelist as before
- Parse olddoc gemspecs before rakefile ones
- Disable adaptive configuration on .so compilation, so extconf.rb will
  be run anytime
- + save aliases also for project and sources
- + add #has_name? to Source::Base to match alises also
- + hot on-source-load gem source version replacement
- + command line for source version replacement called as
  --version-replace
- + added call to chrpath binary to remove RPATH from .so during
  compile action
- - Merged detection of the gemfile in hoe or plain rakefile
- - Removed hoe/debug module
- + inferring gemfile from Rakefile, so when spec is defined in the
  Rakefile it will be detected
- - Fix class name for target ruby from erroneous Site to Ruby
- - Fix install folder for i586 arch, so .so files will be installed by
  using x86 arch

* Sat Apr 06 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt5
- fix req deps on executables when they are already installed only
- set autoalias on binaries only for its source not others, and when no
  other source names match the binary

* Tue Apr 02 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt4
- load Gemfile by temporary changing the root when creating the bundler's DSL

* Wed Mar 27 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt3
- fix requires deps detection over executable's shebang line

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt2
- Added novel approach to detect the dependencies of packages

* Sun Mar 17 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt1
- Bump to 5.999.3

* Thu Mar 14 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.2-alt1
- Bump to 5.999.2
- Use Ruby Policy 2.0

* Mon Mar 11 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.1-alt1
- Bump to 5.999.1

* Fri Jan 25 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.0-alt1
- Initial gemified build for Sisyphus with usage Ruby Policy 2.0.
