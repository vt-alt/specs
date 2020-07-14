%define _unpackaged_files_terminate_build 1
%define oname rabbitmq

%add_findreq_skiplist */ocf/resource.d/rabbitmq/*

# workaround for not find Provides in plugins/*.ez files
%add_erlang_req_modules_skiplist ranch delegate ec_semver file_handle_cache file_handle_cache_stats lg recon_alloc vm_memory_monitor worker_pool
%add_erlang_req_modules_skiplist app_utils credit_flow gen_server2 mirrored_supervisor pmon priority_queue rand_compat supervisor2 time_compat

Name: rabbitmq-server
Version: 3.8.3
Release: alt2
Summary: The RabbitMQ server
License: MPL-1.1
BuildArch: noarch
Group: System/Servers
Source: %name-%version.tar
Source1: rabbitmq-server.init
Source2: rabbitmq-script-wrapper
Source3: rabbitmq-server.logrotate
Source4: rabbitmq-env.conf
Source6: rabbitmq-server.service
Source7: rabbitmq-server.tmpfiles

Patch1: rabbitmq-server-0001-Remove-excessive-sd_notify-code.patch
Patch2: rabbitmq-server-0002-Add-systemd-notification-support.patch
Patch3: rabbitmq-server-0003-Allow-guest-login-from-non-loopback-connections.patch
Patch4: rabbitmq-server-0004-rabbit_prelaunch-must-use-RABBITMQ_SERVER_ERL_ARGS.patch
Patch101: rabbitmq-common-0001-Use-proto_dist-from-command-line.patch
Patch102: rabbitmq-common-0002-force-python3.patch
Patch201: rabbitmq-server-release-0001-Don-t-use-templates.patch
Patch202: rabbitmq-server-release-0002-Revert-Use-template-in-rabbitmq-script-wrapper-for-R.patch
Patch301: rabbitmq-amqp1.0-common-0001-force-python3.patch

URL: http://www.rabbitmq.com/

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-devel erlang-otp-devel elixir
BuildRequires: python3-module-simplejson
BuildRequires: xmlto zip unzip netcat rsync
Requires: erlang  >= 1:20.3.0

%filter_from_requires /^erlang_\(mod\|lib\|app\)(\(lager\|glc\|gr_\|gre\|prometheus\|ranch\|observer\|ra_\|ra)\|jose\|jsx\|cow\|aten\|recon\|stdout_formatter\|sysmon_handler\|credentials_obfuscation\|accept\|base64url\|gen_batch_server\|goldrush\|error_logger_lager_h\|syslog\)/d
%filter_from_provides /^erlang_\(mod\|lib\|app\)(\(lager\|glc\|gr_\|gre\|prometheus\|ranch\|observer\|ra_\|ra)\|jose\|jsx\|cow\|aten\|recon\|stdout_formatter\|sysmon_handler\|credentials_obfuscation\|accept\|base64url\|gen_batch_server\|goldrush\|error_logger_lager_h\|syslog\)/d

%description
RabbitMQ is an implementation of AMQP, the emerging standard for high
performance enterprise messaging. The RabbitMQ server is a robust and
scalable implementation of an AMQP broker.

%package -n %name-devel
Summary: %name header files
Group: Development/Erlang

%description -n %name-devel
Erlang header files for %name

%prep
%setup -q

pushd deps/rabbit
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
popd

pushd deps/rabbit_common
%patch101 -p1
%patch102 -p1
popd

%patch201 -p1
%patch202 -p1

pushd deps/amqp10_common
%patch301 -p1
popd

# We have to remove it until common_test subpackage lands RHOS
rm -f \
    deps/amqp_client/src/rabbit_ct_client_helpers.erl \
    deps/rabbit_common/src/rabbit_ct_broker_helpers.erl \
    deps/rabbit_common/src/rabbit_ct_helpers.erl

%build
sed -i 's|@libexecdir@|%_libexecdir|g' %SOURCE2
sed -i 's|@localstatedir@|%_localstatedir|g' %SOURCE2

export LANG=en_US.UTF-8
export VERSION=%version
%make_build

%install
export LANG=en_US.UTF-8
%makeinstall_std \
        VERSION="%version" \
        PREFIX=%_prefix \
        install-bin install-man


mkdir -p %buildroot%_localstatedir/%oname/mnesia
mkdir -p %buildroot%_logdir/%oname

#Copy all necessary lib files etc.

#Sysvinit support
install -p -D -m 0755 %SOURCE1 %buildroot%_initrddir/%oname

install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/rabbitmqctl
install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/%{oname}-server
install -p -D -m 0755 %SOURCE2 %buildroot%_sbindir/%{oname}-plugins
install -p -D -m 0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -p -D -m 0644 %SOURCE4 %buildroot%_sysconfdir/%oname/%{oname}-env.conf
install -p -D -m 0644 deps/rabbit/docs/rabbitmq.conf.example %buildroot%_sysconfdir/%oname/rabbitmq.conf
install -p -D -m 0644 %SOURCE6 %buildroot%_unitdir/%oname.service
install -p -D -m 0644 %SOURCE7 %buildroot%_tmpfilesdir/%oname.conf
install -d %buildroot%_runtimedir/%oname

# Make necessary symlinks
mkdir -p %buildroot%_libexecdir/%oname
for app in rabbitmq-defaults rabbitmq-env rabbitmq-plugins rabbitmq-server rabbitmqctl cuttlefish; do
    ln -r -s %buildroot%_erlanglibdir/rabbitmq_server-%version/sbin/${app} %buildroot%_libexecdir/%oname/${app}
done

install -p -D -m 0755 scripts/rabbitmq-server.ocf %buildroot%_libexecdir/ocf/resource.d/rabbitmq/rabbitmq-server
install -p -D -m 0755 scripts/rabbitmq-server-ha.ocf %buildroot%_libexecdir/ocf/resource.d/rabbitmq/rabbitmq-server-ha

mkdir -p %buildroot%_sysconfdir/%oname/conf.d
rm -f %buildroot%_erlanglibdir/rabbitmq_server-%version/{LICENSE,LICENSE-*,INSTALL}

# Install completions
mkdir -p %buildroot%_datadir/bash-completion/completions
mv %buildroot/usr/lib/erlang/autocomplete/bash_autocomplete.sh %buildroot%_datadir/bash-completion/completions/%name

mkdir -p %buildroot%_datadir/zsh/site-functions
mv %buildroot/usr/lib/erlang/autocomplete/zsh_autocomplete.sh %buildroot%_datadir/zsh/site-functions/_%name
rm -rf %buildroot/usr/lib/erlang/autocomplete

%pre
%_sbindir/groupadd -r -f rabbitmq &>/dev/null
%_sbindir/useradd -r -g rabbitmq  -d %_localstatedir/rabbitmq -s /dev/null \
   -c 'RabbitMQ messaging server' -M -n rabbitmq &>/dev/null ||:

%post
%post_service %oname

%preun
%preun_service %oname

%files
%doc LICENSE LICENSE-* deps/rabbit/docs/rabbitmq.conf.example
%_sbindir/*
%_libexecdir/%oname
%dir %_erlanglibdir/rabbitmq_server-%version
%_erlanglibdir/rabbitmq_server-%version/*
%_erldir/bin/*
%exclude %_erlanglibdir/rabbitmq_server-%version/include
%attr(0750, rabbitmq, rabbitmq) %dir %_localstatedir/%oname
%attr(0750, rabbitmq, rabbitmq) %dir %_localstatedir/%oname/mnesia
%attr(0750, rabbitmq, rabbitmq) %dir %_logdir/%oname
%attr(0750, rabbitmq, rabbitmq) %dir %_runtimedir/%oname
%config(noreplace) %attr(0644, rabbitmq, rabbitmq) %_sysconfdir/rabbitmq/rabbitmq.conf
%config(noreplace) %attr(0644, rabbitmq, rabbitmq) %_sysconfdir/rabbitmq/rabbitmq-env.conf
%config(noreplace) %_logrotatedir/*
%_man5dir/*
%_man8dir/*
%_unitdir/%oname.service
%_tmpfilesdir/%oname.conf
%_initrddir/%oname
%_libexecdir/ocf/resource.d/rabbitmq
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name

%files -n %name-devel
%_erlanglibdir/rabbitmq_server-%version/include
#%_datadir/%name

%changelog
* Wed Jun 10 2020 Andrey Cherepanov <cas@altlinux.org> 3.8.3-alt2
- Remove provides from bundled modules (ALT #36925).
- Fix License tag according to SPDX.

* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 3.8.3-alt1
- 3.8.3
- Rename /etc/rabbitmq/rabbitmq.config to /etc/rabbitmq/rabbitmq.conf.

* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 3.7.26-alt1
- 3.7.26

* Wed Apr 03 2019 Alexey Shabalin <shaba@altlinux.org> 3.7.14-alt1
- 3.7.14

* Sun Mar 24 2019 Alexey Shabalin <shaba@altlinux.org> 3.7.13-alt1
- 3.7.13

* Fri Jan 25 2019 Alexey Shabalin <shaba@altlinux.org> 3.7.10-alt1
- 3.7.10

* Fri Jun 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.16-alt1
- Updated to upstream version 3.6.16.

* Mon Nov 27 2017 Denis Medvedev <nbr@altlinux.org> 3.6.14-alt4
- added (Fixes: CVE-2016-9877).

* Sun Nov 26 2017 Denis Medvedev <nbr@altlinux.org> 3.6.14-alt3
- Added needed, but unusual dependencies

* Thu Nov 16 2017 Denis Medvedev <nbr@altlinux.org> 3.6.14-alt2
- recompilation with fixed rpm-build-utils

* Fri Nov 10 2017 Alexey Shabalin <shaba@altlinux.ru> 3.6.14-alt1
- 3.6.14

* Sun Apr 16 2017 Ivan Zakharyaschev <imz@altlinux.org> 3.6.8-alt4
- rabbitmq-script-wrapper: optimized and made the Bash-scipting safer
  (tolerant to spaces in values).

* Thu Apr 13 2017 Ivan Zakharyaschev <imz@altlinux.org> 3.6.8-alt3
- rabbitmq-script-wrapper: robust quoting of args when su is used
  (under root). The old approach (putting quotes around the args)
  could not be extended correctly to the case when there were both
  kinds of quotation marks (' and ") in one of the original args.

* Tue Mar 28 2017 Alexey Shabalin <shaba@altlinux.ru> 3.6.8-alt2
- fix logrotate config

* Fri Mar 17 2017 Alexey Shabalin <shaba@altlinux.ru> 3.6.8-alt1
- 3.6.8
- fixed CVE-2016-9877

* Wed Sep 28 2016 Alexey Shabalin <shaba@altlinux.ru> 3.6.5-alt1
- 3.6.5

* Fri Jun 10 2016 Denis Medvedev <nbr@altlinux.org> 3.5.4-alt2.2
- Recompile with OTP-18.3.3

* Sun Apr 10 2016 Denis Medvedev <nbr@altlinux.org> 3.5.4-alt2.1
- Recompile with OTP-18.3

* Thu Sep 17 2015 Alexey Shabalin <shaba@altlinux.ru> 3.5.4-alt2
- Fix version

* Wed Sep 16 2015 Alexey Shabalin <shaba@altlinux.ru> 3.5.4-alt1
- 3.5.4

* Sun Dec 29 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 3.2.2-alt1
- New version (ALT #27190)

* Wed Aug 21 2013 Pavel Shilovsky <piastry@altlinux.org> 2.8.7-alt4
- Fix spacing in the sysvinit script

* Fri Aug 16 2013 Pavel Shilovsky <piastry@altlinux.org> 2.8.7-alt3
- Fix sysvinit script

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 2.8.7-alt2
- Change configuration file name
- Return sysvinit support

* Thu Oct 04 2012 Pavel Shilovsky <piastry@altlinux.org> 2.8.7-alt1
- New version 2.8.7

* Sat Oct 31 2009 Maxim Ivanov <redbaron at altlinux.org> 1.7.0-alt1
- New version
- New plugin architecture introduced

* Sun Sep 20 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt3
- New conf.d dir for plugable addons configs
- fix condreload arg support in init script

* Mon Jul 20 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt2
- Header files packed separately now
- Fix added condstop to init script

* Sun Jul 19 2009 Maxim Ivanov <redbaron at altlinux.org> 1.6.0-alt1
- Initial build for ALTLinux

