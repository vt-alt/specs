%define _altdata_dir %_datadir/alterator

Name: alterator-fbi
Version: 5.47
Release: alt1

Source: %name-%version.tar
Patch: alterator-fbi-5.42-call-cc-via-reset.patch

Summary: alterator on rails
License: GPL
Group: System/Configuration/Other

#backward compatibility
Provides: alterator-http = %version, ahttpd = %version, httpd-alterator = %version, alterator-ahttpd = %version
Obsoletes: alterator-http, ahttpd, httpd-alterator, alterator-ahttpd

Requires: alterator-sh-functions >= 0.13-alt2
Requires: avahi-sh-functions >= 0.1-alt2
Requires: design-alterator
Requires: alterator >= 5.0-alt1
Requires: alterator-l10n >= 2.7-alt4
Requires: alterator-sslkey
Requires: gettext
Requires: alterator-l10n >= 2.9.50
Requires: /etc/cron.d

Requires(pre): libguile-vhttpd >= 0.7.7-alt1
Requires(pre): shadow-utils

BuildPreReq: alterator >= 5.0-alt1, libguile-vhttpd, libexpat-devel

%ifarch %e2k
BuildRequires: guile20-devel libguile20-devel
BuildRequires: alterator >= 5.1-alt7
%else
BuildPreReq: guile22-devel
%endif

Provides: alterator-etcgit-bar

%description
this is an alterator based engine (form based interface) to create a simple form based html interface

%brp_strip_none %_alterator_libdir/*
%add_verify_elf_skiplist %_alterator_libdir/*
%add_findreq_skiplist %_alterator_libdir/*

%prep
%setup
%ifarch %e2k
%patch -p2
%endif

%build
%make_build
# broken for now, revisit later
#make check-api

%install
export GUILE_AUTO_COMPILE=0
export LD_LIBRARY_PATH=$(pwd)/src/libguile-xmltokenizer/
mkdir -p %buildroot/%_localstatedir/alterator/csrf-tokens
%makeinstall HTMLROOT=%buildroot%_var/www/ unitdir=%buildroot%_unitdir

#ahttpd
%__install -d %buildroot%_var/run/ahttpd
%__install -d %buildroot%_logdir/ahttpd
%__install -Dpm640 ahttpd.logrotate %buildroot/%_sysconfdir/logrotate.d/ahttpd
%__install -Dpm644 ahttpd.conf %buildroot%_sysconfdir/ahttpd/ahttpd.conf
%__install -Dpm644 acl.conf %buildroot%_sysconfdir/ahttpd/acl.conf
%__install -Dpm755 ahttpd.init %buildroot/%_initrddir/ahttpd
%__install -d %buildroot/%_cachedir/ahttpd
%__install -d %buildroot/

#ssl
touch %buildroot%_sysconfdir/ahttpd/ahttpd.cnf
mkdir -p %buildroot/%_localstatedir/ssl/certs/
touch %buildroot/%_localstatedir/ssl/certs/ahttpd.csr

#compatibility:begin
touch %buildroot/%_datadir/alterator/build/html-messages.mak
#compatibility:end

%pre
/usr/sbin/groupadd -r -f _ahttpd
/usr/sbin/groupadd -r -f _alteratord
/usr/sbin/useradd -r -g _ahttpd -G _alteratord -d /dev/null -s /dev/null -n _ahttpd >/dev/null 2>&1 ||:

%post
%post_service ahttpd

%preun
%preun_service ahttpd

%triggerin -- httpd-alterator
if /sbin/service httpd-alterator status >/dev/null 2>/dev/null; then
    /sbin/service httpd-alterator stop
    /sbin/service ahttpd start
fi ||:
/sbin/service configd stop
/sbin/chkconfig configd --del
/usr/sbin/usermod  -G _alteratord _ahttpd >/dev/null 2>&1 ||:

%triggerin -- ahttpd
/sbin/service configd stop
/sbin/chkconfig configd --del
/usr/sbin/usermod  -G _alteratord _ahttpd >/dev/null 2>&1 ||:

%triggerpostun -- ahttpd
/sbin/chkconfig ahttpd --add
/sbin/chkconfig ahttpd on
/sbin/service ahttpd start


%files
#common
%_bindir/*
%_libdir/guile/*.*/extensions/*.so
%_alterator_libdir/interfaces/guile/*
%_alterator_libdir/type/*
%_alterator_libdir/ui/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/build/*
%_datadir/alterator/design/images/*
%_datadir/alterator/design/scripts/*
%_datadir/alterator/design/styles/*
%_datadir/alterator/ui/*
%_datadir/alterator/type/*
%_datadir/alterator/interfaces/*/*
%_datadir/alterator/applications/*
%dir %_localstatedir/alterator/csrf-tokens

#server
%config(noreplace) %_sysconfdir/logrotate.d/*
%_initdir/*
%_sbindir/*
%_man5dir/*
%_man8dir/*
%_var/run/ahttpd
%attr(750,root,adm) %_logdir/ahttpd
%attr(700,_ahttpd,root) %dir %_sysconfdir/ahttpd
%attr(700,_ahttpd,root) %dir %_sysconfdir/ahttpd
%config(noreplace) %_sysconfdir/ahttpd/ahttpd.conf
%config(noreplace) %_sysconfdir/ahttpd/acl.conf
%attr(750,_ahttpd,root) %_cachedir/ahttpd
%_unitdir/ahttpd.service
%_unitdir/ahttpd.socket

#ssl
%ghost  %config(noreplace) %_sysconfdir/ahttpd/ahttpd.cnf
%ghost  %_localstatedir/ssl/certs/ahttpd.csr


%changelog
* Fri Dec 13 2019 Paul Wolneykien <manowar@altlinux.org> 5.47-alt1
- Fix/improve: Just touch /etc/cron.d in order to reload the schedule.

* Wed Dec 11 2019 Paul Wolneykien <manowar@altlinux.org> 5.46-alt1
- Fix: Use 'systemctl poweroff' to shutdown the system in the case
  of systemd.
- Use catch/message-and-ignore to always re-read the parameters.
- Added catch/message-and-ignore proc.
- Fix/improve: Require /etc/cron.d.
- Fix: Require alterator-l10n >= 2.9.50.
- Fix/improve: Additional checks for the crond service.
- Fix/improve: Reload crond service after schedule update.

* Tue Dec 03 2019 Paul Wolneykien <manowar@altlinux.org> 5.45-alt1
- Power module:
  -- Added support for reboot, suspend and hibernate
     scheduling and instant actions.
  -- Apply the changes to the schedule regardless of the
     instant action.
- Form.js: Added support to select elements by id.

* Tue Nov 26 2019 Paul Wolneykien <manowar@altlinux.org> 5.44-alt1
- Allow the email notification controls only if
  "state-change-notify-postfix" system service is available.
- Added controls for email notification to the "power" module.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 5.43-alt1
- Render table with dynamic fields from JSON (thanks majioa@).
  See alterator-domain-policy for details.

* Wed Apr 17 2019 Paul Wolneykien <manowar@altlinux.org> 5.42-alt1
- Update the call-cc-via-reset patch (for E2K).
- Fixed the accidentally overwritten URL query parsing regexp fix
  (see v5.39-alt3).

* Fri Apr 12 2019 Paul Wolneykien <manowar@altlinux.org> 5.41-alt1
- Add missing ";" to the JS AJAX response.
- Focus on the password input when the username is set and on the
  username otherwise.
- Added (form-focus name) and form_focus(name) AJAX binding to
  focus HTML input element at will.
- Suggest a username for each login. Use the different welcome
  message for the second (and so on) login.
- Also, misc-error's are formatted properly now.
- Added enchanced proc continue-with-new-session! which carries on
  some essintial ahttpd session values.
- Fixed the long-lived bug in how the wrong-type-arg and
  wrong-number-of-args errors are printed.
- Added ahttpd-session-user proc: the ahttpd session equivalent of
  (session-user id).
- Added continue-with-new-session proc to make a call with modified
  ahttpd session.
- Added ahttpd-config-ref proc to easily access the ahttpd
  configuration.
- Introduce the "loginchain" configuration parameter and check
  for the configured requirements before login.
- Store the ahttpd configuration in the current session under
  'ahttpd-config.

* Mon Jan 21 2019 Michael Shigorin <mike@altlinux.org> 5.40-alt2
- Replace e2k arch name with %%e2k macro (grenka@).

* Mon Dec 10 2018 Paul Wolneykien <manowar@altlinux.org> 5.40-alt1
- Use platform-based procedure to initialize the pseudo-random
  generator.

* Tue Dec 26 2017 Paul Wolneykien <manowar@altlinux.org> 5.39-alt3
- Require alterator >= 5.1-alt7 (e2k).
- Delimit a partial continuation with "with-ahttpd-session"
  (patch, e2k).
- Register the session fluid (patch, e2k).
- Fixed the double-anchored URL query parsing regexp.

* Wed Dec 20 2017 Paul Wolneykien <manowar@altlinux.org> 5.39-alt2
- Adapd build for the E2K platform.
- Support 'raw-href' attribute for 'alterator-href' links.

* Sat Nov 04 2017 Ivan Zakharyaschev <imz@altlinux.org> 5.39-alt1
- backend3/ahttpd-server (do_reload): fix for systemd.

* Thu Jun 22 2017 Ivan Zakharyaschev <imz@altlinux.org> 5.38-alt1
- form.js: fix arbitrary HTML+JS injection by constructing new HTML
  elements "structurally".
- workflow/none.scm: made SCRIPT external to fix the injection of
  arbitrary HTML+JS (from initial values).

* Thu Jun 08 2017 Denis Medvedev <nbr@altlinux.org> 5.37-alt1
- Fix help url for non-root users.

* Thu Jun 08 2017 Denis Medvedev <nbr@altlinux.org> 5.36-alt1
- Fix help url handling.

* Wed Jun 07 2017 Mikhail Efremov <sem@altlinux.org> 5.35-alt1
- Fix links translation (by nbr@).

* Fri Jun 02 2017 Ivan Zakharyaschev <imz@altlinux.org> 5.34-alt1
- Made /logout work with a (correct) CSRF token. And disallowed it to work
  without a (correct) CSRF token (which used to be a small vulnerability).

* Thu Apr 6 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.33-alt1
- rebuilt with alterator-5.0

* Mon Apr 3 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.32-alt11
- Fix work 'ahttpd -l' (with local modules)

* Thu Oct 20 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 5.32-alt10
- some debug prints removed

* Thu Oct 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.32-alt9
- non-user-visible source code maintenance: reindent .scm where
  spaces and tabs were mixed (no tabs left) for editability.

* Tue Jun 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.32-alt8
- Optimization: do not call the token backend that many times for
  generating a page (but only a few times).

* Mon Jun 27 2016 Denis Medvedev <nbr@altlinux.org> 5.32-alt7
- Fixed behavour of Help and Configure buttons

* Mon Jun 27 2016 Denis Medvedev <nbr@altlinux.org> 5.32-alt6
- Redirecting possible CSRFs to "/"

* Mon Jun 27 2016 Denis Medvedev <nbr@altlinux.org> 5.32-alt5
- Fix handling of prefix-href option in a tag

* Sun Jun 26 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.32-alt4
- Made the session-dependent code in translate.scm clean and simple.
  (This fixes the previously mentioned login problems, too.)

* Sun Jun 26 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 5.32-alt3.1
- backend don't raise exceptoins

* Fri Jun 24 2016 Denis Medvedev <nbr@altlinux.org> 5.32-alt3
- rewriting tag a with token.

* Thu Jun 23 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 5.32-alt2
- login without old cookie fixed

* Wed Jun 22 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 5.32-alt1.1
- build fixed

* Wed Jun 22 2016 Denis Medvedev <nbr@altlinux.org> 5.32-alt1
- Fixes CSRF.

* Fri Sep 18 2015 Mikhail Efremov <sem@altlinux.org> 5.31-alt1
- Use empty password to check in case of blocked IP.
- Allow empty passwords.
- Check password even if IP address is blocked.
- Write login attempts in the log.
- Don't allow to login after several failed attempts.

* Tue Sep 09 2014 Andrey Cherepanov <cas@altlinux.org> 5.30-alt1
- Replace %%H in any place of X-Alterator-URI for support different port
  in URI (ALT #30298)

* Wed May 08 2013 Paul Wolneykien <manowar@altlinux.org> 5.29-alt1
- Fix: do not use "submit" typed buttons as controls in the "acl"
  module (closes: 28551).

* Mon Dec 10 2012 Paul Wolneykien <manowar@altlinux.ru> 5.28-alt6
- Remove the 'PIDFile' option from the service unit file
  (closes: 27987).

* Mon Dec 10 2012 Paul Wolneykien <manowar@altlinux.ru> 5.28-alt5
- Add the 'PIDFile' option to the service unit.
- Remove the 'Also=ahttpd.socket' option.
- Fix the service unit file syntax and the SSL generator command
  (closes: 27987).

* Thu Dec 06 2012 Paul Wolneykien <manowar@altlinux.ru> 5.28-alt4
- Check/generate the SSL certificate before starting the service
  from systemd (closes: 27987).

* Wed Nov 28 2012 Paul Wolneykien <manowar@altlinux.ru> 5.28-alt3
- Use "a wretched-man's crutch" daemonization: start-stop-daemon
  for SysV-init (closes: 27865).

* Mon Nov 26 2012 Andrey Cherepanov <cas@altlinux.org> 5.28-alt2
- Add favicon support with design/images/product.png

* Thu Nov 22 2012 Paul Wolneykien <manowar@altlinux.ru> 5.28-alt1
- Do not daemonize in socket-activation mode (closes: 27865).
- Add the systemd unit files.
- Start the server on the given socket if any (closes: 27987).

* Thu Sep 20 2012 Paul Wolneykien <manowar@altlinux.ru> 5.27-alt2
- Reply with session info to a /ahttpd-cache/sessions/<session> URI.
- List only allowed modules in the menu.
- Add operation to list allowed URIs for a given user.

* Fri Aug 31 2012 Paul Wolneykien <manowar@altlinux.ru> 5.27-alt1
- Substitute %%H in X-Alterator-URI with the requested host address.
- Fix output of Unicode characters.
- Invoke message dialogs synchronously.
- Define procs for JS invocation.
- Allow clickable links.
- Provide alterator-etcgit-bar.
- JS function to update the profile name and modification status.
- Show profile name (link) in the presence of /etcgit backend.

* Tue May 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.26-alt5
- Fix LSB init header

* Fri Apr 23 2010 Dmitriy Kruglikov <dkr@altlinux.org> 5.26-alt4
- Changed editable checklistbox.

* Fri Apr 02 2010 Dmitriy Kruglikov <dkr@altlinux.org> 5.26-alt3
- Changed editable checklistbox. New widget.

* Tue Mar 16 2010 Dmitriy Kruglikov <dkr@altlinux.org> 5.26-alt2
- Input cursor auto focused into "Password" input

* Thu Dec 03 2009 Stanislav Ievlev <inger@altlinux.org> 5.26-alt1
- update to newest vhttpd
- drop workflow 'form' support
- table.alterator-listbox: fix global selector event handler

* Mon Nov 30 2009 Stanislav Ievlev <inger@altlinux.org> 5.25-alt9
- table.alterator-listbox: remove name attribute from template

* Tue Nov 24 2009 Stanislav Ievlev <inger@altlinux.org> 5.25-alt8
- use progressbar from jquery ui
- rename 'disabled' class into 'ui-state-disabled' to conform jquery ui standards

* Mon Nov 23 2009 Stanislav Ievlev <inger@altlinux.org> 5.25-alt7
- improve form_update_activity() and form_update_visibility().
- introduce alterator namespace in jquery sources.
- drop unused excanvas.js.
- form-update-value-list(): fix work with empty values.
- table.alterator-listbox: add support for single-select mode.

* Tue Nov 17 2009 Stanislav Ievlev <inger@altlinux.org> 5.25-alt6
- acc workflow: show title in AMC mode

* Tue Nov 17 2009 Stanislav Ievlev <inger@altlinux.org> 5.25-alt5
- form-update-value-list(): support both single command and multiple-command as a parameter

* Mon Nov 16 2009 Stanislav Ievlev <inger@altlinux.org> 5.25-alt4
- power management, login process: use alterator_export_var and alterator_export_proc
- hide help,configuration and logout buttons in AMC browser
- special support in acc workflow for AMC browser
- use single path for logout

* Thu Nov 05 2009 Stanislav Ievlev <inger@altlinux.org> 5.25-alt3
- add special support favicon in messsage-handler
  (was implicit second login page calling)

* Tue Nov 03 2009 Stanislav Ievlev <inger@altlinux.org> 5.25-alt2
- improve jquery.ajaxfileupload plugin (allow to send an additional data to server)
- destroy popup object after closing

* Wed Oct 28 2009 Stanislav Ievlev <inger@altlinux.org> 5.25-alt1
- use ui-corner-all companion class for some containers (box, top)
- replace jquery.alerts plugin with jquery.ui.dialog
- remove unused submit.js.
- form workflow: drop support of checklistbox.
- alterator-listbox tables: append template row to the end of the table to allow automatic sort order detection.
- alterator-accordion: add 'no-auto-height' mode (thx Anton Protopopov).

* Mon Oct 19 2009 Vladislav Zavjalov <slazav@altlinux.org> 5.24-alt1
- move card-index module to alterator package

* Wed Oct 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 5.23-alt1
- rewrite card-index.scm module

* Tue Oct 13 2009 Stanislav Ievlev <inger@altlinux.org> 5.22-alt2
- improve form-update-value-list:
  (form-update-value-list cmd) will call update for all available parameters in command..
- workflow form: drop process-radio.
- table.alterator-listbox:
   * automatically toggle 'selected' class in multi-select mode.
   * mass deselect

* Mon Oct 12 2009 Stanislav Ievlev <inger@altlinux.org> 5.22-alt1
- form.js:
    * add support for radiolistbox widget.
    * add support for color rows (alterator-class attribute for table.alterator-listbox)
- redesign callbacks arhitecture, remove possible memory leaks:
    * store callbacks in per session, not in global storage;
    * use single shot callbacks for form-set-timeout function;
    * clear all previous callbacks for url before "init" call..
- fix error message printing (use text/plain)
- fix help-popup animation ( button with absolute possition hides
  after slideUp effect).

* Wed Oct 07 2009 Stanislav Ievlev <inger@altlinux.org> 5.21-alt1
- replace help.js with better help-button jquery module, move ui/help into ui/ahttpd subdir
- main framework haven't deps on help feature now
- replace own hresizeable jquery plugin with a standard resizeable module from jquery.ui
- move jquery libraries into interfaces subdirectory

* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 5.20-alt3
- form-bind: allow to bind events to images

* Fri Sep 25 2009 Stanislav Ievlev <inger@altlinux.org> 5.20-alt2
- optimize menu generation

* Wed Sep 23 2009 Stanislav Ievlev <inger@altlinux.org> 5.20-alt1
- merge process-framework and process-module into process-module
- move login and logout uris out of framework.
- remove links to effects.js.
- (alterator ahttpd html): drop html:submit, html:hidden.
- form workflow: drop support of timeedit, dateedit and progress.
- drop 'message-async?' support.
- drop old "effects" library.

* Tue Sep 22 2009 Stanislav Ievlev <inger@altlinux.org> 5.19-alt4
- fix form-confirm: save and restore after resume 'ahttpd-full-args and 'ahttpd-woo-args.
- wf is equal to "none" by default

* Fri Sep 18 2009 Stanislav Ievlev <inger@altlinux.org> 5.19-alt3
- improve reboot/poweroff process (closes: #21403)
- form.js: no error on async callback
- improve clock design

* Tue Sep 15 2009 Stanislav Ievlev <inger@altlinux.org> 5.19-alt2
- enchance hidden quick fix

* Tue Sep 08 2009 Stanislav Ievlev <inger@altlinux.org> 5.19-alt1
- add jquery ui plugins (accordion and core)
- update jquery up to 1.3.2
- /login, /logout: improve basic html design

* Mon Sep 07 2009 Stanislav Ievlev <inger@altlinux.org> 5.18-alt6
- made root as a default login name
- fix tablesorter() usage in alterator-listbox with multi-select feature

* Tue Sep 01 2009 Stanislav Ievlev <inger@altlinux.org> 5.18-alt5
- always use asynchronous ajax calls
- form.js: add form_replace_if_ready() function (redirect only if target path is available)
- (alterator ajax): export ->json function

* Mon Aug 24 2009 Stanislav Ievlev <inger@altlinux.org> 5.18-alt4
- fix jquery.blockUI usage (opacity)

* Fri Aug 21 2009 Stanislav Ievlev <inger@altlinux.org> 5.18-alt3
- update top line design

* Fri Aug 21 2009 Stanislav Ievlev <inger@altlinux.org> 5.18-alt2
- (alterator login): replace hardcoded "/login" uri with real current uri
- ahttpd/server: use alterator-sslkey
- replace jquery.lock with jquery.blockUI

* Thu Aug 20 2009 Stanislav Ievlev <inger@altlinux.org> 5.18-alt1
- remove unused select.js script
- add documentation for login-uri and logout-uri parameters (closes: #21104)
- add login-uri and logout-uri parameters into default config file
- add (alterator login) library to organize login/logout pages

* Fri Aug 14 2009 Vladislav Zavjalov <slazav@altlinux.org> 5.17-alt7
- card-index.scm: fix working with empty lists (closes #20711)

* Fri Aug 14 2009 Stanislav Ievlev <inger@altlinux.org> 5.17-alt6
- pack javascript

* Fri Aug 07 2009 Stanislav Ievlev <inger@altlinux.org> 5.17-alt5
- fix string->json conversion (add support for #\cr symbol)

* Tue Aug 04 2009 Stanislav Ievlev <inger@altlinux.org> 5.17-alt4
- resurrect old ajax behaviour for workflow 'form' (turned off optimization)
- alterator-picture widget: add 'prefix-src' and 'suffix-src' properties

* Mon Aug 03 2009 Stanislav Ievlev <inger@altlinux.org> 5.17-alt3
- alterator-listbox/multi-select: add checkbox for 'select all' action
- dateedit and timeedit widgets are ready for ajax now
- drop unused 'alterator-text' widget
- page loading optimization: move first ajax call (init, on-load) to server side.

* Wed Jul 29 2009 Stanislav Ievlev <inger@altlinux.org> 5.17-alt2
- ajax-library:
    * (form-value) return actual value now (e.g. result of a previous (form-update-value) call)
    * add (form-session-ref), (form-session-set!) functions
    (these features allows to use a generic effects library now)
- ajax based 'alterator-listbox':
    * fix work if no rows available
    * add 'multi-select' mode

* Fri Jul 24 2009 Stanislav Ievlev <inger@altlinux.org> 5.17-alt1
- replace alert() and confirm() with javascript based dialogs
- form-update-enum: add support for 'alterator-listbox' tables

* Fri Jul 10 2009 Mikhail Efremov <sem@altlinux.org> 5.16-alt9
- acl: check that list of new users not empty (closes: #20746).

* Thu Jul 02 2009 Vladislav Zavjalov <slazav@altlinux.org> 5.16-alt8
- card-index.scm: add card-index-update function

* Thu Jun 25 2009 Stanislav Ievlev <inger@altlinux.org> 5.16-alt7
- update styles

* Mon Jun 15 2009 Stanislav Ievlev <inger@altlinux.org> 5.16-alt6
- improve behaviour tuning: add new parameters to ahttpd.conf - login-uri and logout-uri.
- login page: prevent standard form submit when 'enter' key pressed (closes: #20025)

* Thu Jun 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 5.16-alt5
- card-index.scm: send language to backend on read

* Wed Jun 03 2009 Vladislav Zavjalov <slazav@altlinux.org> 5.16-alt4
-  add new card-index module (experimental, see alterator-services for example)

* Thu May 28 2009 Stanislav Ievlev <inger@altlinux.org> 5.16-alt3
- form-blob, call-with-form-file: fix work when upload's content-type text/*

* Wed May 27 2009 Stanislav Ievlev <inger@altlinux.org> 5.16-alt2
- fix logout process
- improve error diagnostics for ui-file function

* Tue May 19 2009 Stanislav Ievlev <inger@altlinux.org> 5.16-alt1
- fix updateImageSource function
- work with undefined accept-language header field
- drop card-index workflow
- form API: add form-confirm, add simple i18n support
- explicitly define format in catch/message
- made dateedit and datepicker a real javascript widget

* Thu May 07 2009 Stanislav Ievlev <inger@altlinux.org> 5.15-alt1
- ajax file upload
- enchance ui-file function
- add colorpicker widget
- add button to restart ahttpd server at the end of acl changes (closes: #19904)
- support both "init" and "on-load" ajax constructors

* Thu Apr 30 2009 Stanislav Ievlev <inger@altlinux.org> 5.14-alt1
- add ui-replace (closes: #19761)
- ui-blob: add filename support (closes: #19757)
- little ui improvements for IE
- improve storage of session-data
- display error message for browsers without javascript support
- add support for nameref attribute

* Thu Apr 23 2009 Stanislav Ievlev <inger@altlinux.org> 5.13-alt1
- drop support of old table widget (tbody with optionlist)
- ui : add support for progressbar in form-update-value function,
       async ajax for form-set-timeout callbacks

* Tue Apr 21 2009 Stanislav Ievlev <inger@altlinux.org> 5.12-alt2
- add tablesorter

* Tue Apr 21 2009 Stanislav Ievlev <inger@altlinux.org> 5.12-alt1
- new experimental ui infrastructure

* Thu Apr 16 2009 Stanislav Ievlev <inger@altlinux.org> 5.11-alt2
- add form-set-timeout (manowar@)
- improve man-pages (mike@)
- prereq shadow-utils
- improve trigger for httpd-alterator to fix dist-upgrade from 4.0 to 5.0 (closes: #19574)

* Tue Apr 14 2009 Stanislav Ievlev <inger@altlinux.org> 5.11-alt1
- drop support for old templates
- show splash during ajax request
- move type definition to more convenient place

* Wed Apr 08 2009 Stanislav Ievlev <inger@altlinux.org> 5.10-alt1
- improve man-pages
- improve error messages on failure in ajax
- sync form-replace API with qt

* Tue Apr 07 2009 Stanislav Ievlev <inger@altlinux.org> 5.9-alt9
- fix typos

* Sat Apr 04 2009 Stanislav Ievlev <inger@altlinux.org> 5.9-alt8
- use html for async answers
- add man-pages
- automatically generate locale list on login page

* Wed Apr 01 2009 Stanislav Ievlev <inger@altlinux.org> 5.9-alt7
- add selection between base/expert views

* Tue Mar 31 2009 Stanislav Ievlev <inger@altlinux.org> 5.9-alt6
- add some Spanish locales

* Thu Mar 26 2009 Stanislav Ievlev <inger@altlinux.org> 5.9-alt5
- improve img tag processing
- add poweroff

* Thu Mar 19 2009 Stanislav Ievlev <inger@altlinux.org> 5.9-alt4
- redirect after login to previously visited page

* Thu Mar 12 2009 Stanislav Ievlev <inger@altlinux.org> 5.9-alt3
- more features to alterator-ref2
- add "enter" event
- process login on "enter" in password field

* Thu Feb 26 2009 Stanislav Ievlev <inger@altlinux.org> 5.9-alt2
- turn off authentication in local mode
- fix cookie setup

* Wed Feb 25 2009 Stanislav Ievlev <inger@altlinux.org> 5.9-alt1
- replace basic auth authentication with cookie based

* Tue Feb 24 2009 Stanislav Ievlev <inger@altlinux.org> 5.8-alt1
- redesign framework workflow
- add 'none' workflow
- fix card-index js support
- improve acc ui (show help/hide help buttons)
- move acc framework page from / to /acc
- more options in ahttpd.conf

* Tue Feb 17 2009 Stanislav Ievlev <inger@altlinux.org> 5.7-alt4
- configd-xgettext: add support for input of type button
- card-index, form: drop support for magic links

* Mon Feb 16 2009 Stanislav Ievlev <inger@altlinux.org> 5.7-alt3
- improve form API:
  * fix form-value-list function
  * form_update_value now works with static labels
  * add form-warning, form-error and catch/message functions

* Fri Feb 13 2009 Stanislav Ievlev <inger@altlinux.org> 5.7-alt2
- fix requires

* Thu Feb 12 2009 Stanislav Ievlev <inger@altlinux.org> 5.7-alt1
- ahttpd daemon: add support for avahi

* Mon Feb 09 2009 Stanislav Ievlev <inger@altlinux.org> 5.6-alt5
- add support for radio buttons
- form API:
    add form-update-activity, form-update-visibility
    form-update-enum (add support for checklistbox)
    fix value setup and form serialization

* Wed Feb 04 2009 Mikhail Efremov <sem@altlinux.org> 5.6-alt4
- remove chkpwd, use login backend instead
- add login backend

* Mon Feb 02 2009 Stanislav Ievlev <inger@altlinux.org> 5.6-alt3
- improve form API (form-bind)

* Fri Jan 30 2009 Stanislav Ievlev <inger@altlinux.org> 5.6-alt2
- form translation: add support for input type=button

* Thu Jan 29 2009 Stanislav Ievlev <inger@altlinux.org> 5.6-alt1
- new ajax form support
- use translations directly from alterator-l10n

* Fri Jan 23 2009 Stanislav Ievlev <inger@altlinux.org> 5.5-alt4
- fix parse-url-args
- add option to turn on debugging

* Mon Jan 19 2009 Mikhail Efremov <sem@altlinux.org> 5.5-alt3
- use resolve-path instead open-path
- rename templates/ -> ui/
- path.scm is removed

* Fri Jan 16 2009 Stanislav Ievlev <inger@altlinux.org> 5.5-alt2
- fix checkbox update

* Thu Jan 15 2009 Stanislav Ievlev <inger@altlinux.org> 5.5-alt1
- improve (ahttpd) library
- redesign workflow
- use help directly from alterator-l10n

* Mon Dec 29 2008 Stanislav Ievlev <inger@altlinux.org> 5.4-alt3
- first version of (ahttpd) library

* Thu Dec 11 2008 Stanislav Ievlev <inger@altlinux.org> 5.4-alt2
- port timeedit and part of select.js, card-index.js to jquery
- use encode-url-component from latest vhttpd
- minor updates for guile-1.8

* Tue Dec 09 2008 Stanislav Ievlev <inger@altlinux.org> 5.4-alt1
- switch to guile-1.8
- port ajaxSubmit function to jquery

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 5.3-alt5
- rebuild with new alterator-l10n (new help, pt_BR.po)

* Wed Dec 03 2008 Stanislav Ievlev <inger@altlinux.org> 5.3-alt4
- add embedded help
  (jquery.js, jquery.hresizeable.js, acc.js)

* Tue Dec 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 5.3-alt3
- rebuild with new help from alterator-l10n

* Mon Dec 01 2008 Stanislav Ievlev <inger@altlinux.org> 5.3-alt2
- port calendar library to jquery

* Wed Nov 26 2008 Stanislav Ievlev <inger@altlinux.org> 5.3-alt1
- fix link for csr file
- add jquery, port some JS code to new library (hostname, effects)

* Mon Nov 24 2008 Stanislav Ievlev <inger@altlinux.org> 5.2-alt3
- rebuild with new l10n (english help)

* Thu Nov 13 2008 Vladislav Zavjalov <slazav@altlinux.org> 5.2-alt2
- card-index.js: hide select button even if list is empty

* Fri Nov 07 2008 Stanislav Ievlev <inger@altlinux.org> 5.2-alt1
- improve help viewer
- move help to alterator-l10n

* Fri Oct 31 2008 Stanislav Ievlev <inger@altlinux.org> 5.1-alt7
- fix calendar generation

* Fri Oct 24 2008 Stanislav Ievlev <inger@altlinux.org> 5.1-alt6
- remove support for constraints

* Fri Sep 26 2008 Stanislav Ievlev <inger@altlinux.org> 5.1-alt5
- improve style form-table
- new style form-table-annotated
- improve ahttpd/server UI

* Wed Sep 24 2008 Stanislav Ievlev <inger@altlinux.org> 5.1-alt4
- rename type according common policy
- improve widget generation

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 5.1-alt3
- change dictionary name in card-index workflow

* Wed Sep 17 2008 Stanislav Ievlev <inger@altlinux.org> 5.1-alt2
- rebuild with latest alterator-xinetd

* Wed Sep 17 2008 Stanislav Ievlev <inger@altlinux.org> 5.1-alt1
- merge with alterator-ahttpd
- minor bugfixes

* Mon Sep 15 2008 Stanislav Ievlev <inger@altlinux.org> 5.0-alt4
- new catch/message with type-error support

* Fri Sep 12 2008 Stanislav Ievlev <inger@altlinux.org> 5.0-alt3
- update to latest alterator

* Wed Sep 10 2008 Stanislav Ievlev <inger@altlinux.org> 5.0-alt2
- replace configd-cmdline utility with d-query call
- redesign html:redirect algo
- replace html:exception function with single catch point

* Tue Sep 09 2008 Stanislav Ievlev <inger@altlinux.org> 5.0-alt1
- merge with ahttpd package

* Mon Sep 01 2008 Stanislav Ievlev <inger@altlinux.org> 2.11-alt1
- add new autogenerated table

* Fri Aug 29 2008 Stanislav Ievlev <inger@altlinux.org> 2.10-alt6
- don't redirect if redirect-url is empty

* Wed Aug 27 2008 Stanislav Ievlev <inger@altlinux.org> 2.10-alt5
- fix input adjusting (for checkbox search both by name and by value)

* Mon Aug 25 2008 Stanislav Ievlev <inger@altlinux.org> 2.10-alt4
- add support for acl in main page

* Fri Aug 22 2008 Stanislav Ievlev <inger@altlinux.org> 2.10-alt3
- improve current module recognition
- update main help

* Thu Aug 21 2008 Stanislav Ievlev <inger@altlinux.org> 2.10-alt2
- rebuild

* Mon Aug 18 2008 Stanislav Ievlev <inger@altlinux.org> 2.10-alt1
- use libguile-vhttpd

* Fri Aug 15 2008 Stanislav Ievlev <inger@altlinux.org> 2.9-alt6
- redesign workflows as a native guile dynamic loaded modules

* Fri Aug 15 2008 Stanislav Ievlev <inger@altlinux.org> 2.9-alt5
- improve dateedit widget: setup default value (current date)

* Thu Aug 14 2008 Stanislav Ievlev <inger@altlinux.org> 2.9-alt4
- fix clock widget wirk on IE
- add datepicker widget

* Fri Aug 08 2008 Stanislav Ievlev <inger@altlinux.org> 2.9-alt3
- move workflow engine to separate library
- replace backend2 with own workflow loading engine.

* Thu Aug 07 2008 Stanislav Ievlev <inger@altlinux.org> 2.9-alt2
- move both template processing algorithms into one place

* Wed Aug 06 2008 Stanislav Ievlev <inger@altlinux.org> 2.9-alt1
- more fast menu

* Mon Aug 04 2008 Stanislav Ievlev <inger@altlinux.org> 2.8-alt6
- (alterator http template): use own list-flat function

* Tue Jul 29 2008 Stanislav Ievlev <inger@altlinux.org> 2.8-alt5
- update for new build system

* Thu Jul 24 2008 Stanislav Ievlev <inger@altlinux.org> 2.8-alt4
- merge with alterator-http

* Wed Jul 23 2008 Stanislav Ievlev <inger@altlinux.org> 2.8-alt3
- update coolclock.js (bugfix for firefox 3.0)

* Fri Jul 04 2008 Stanislav Ievlev <inger@altlinux.org> 2.8-alt2
- fix span processing

* Tue Jul 01 2008 Stanislav Ievlev <inger@altlinux.org> 2.8-alt1
- update i18n support
- improve acc workflow: get title from menu

* Mon Jun 30 2008 Stanislav Ievlev <inger@altlinux.org> 2.7-alt3
- remove i18n support for javascript
- remove unused fbi/password.js
- effectEnable and effectShow little improvements
- single nodeFindByName function
- join to common translation database
- use module.mak

* Fri Jun 27 2008 Stanislav Ievlev <inger@altlinux.org> 2.7-alt2
- add common dateedit widget

* Fri Jun 27 2008 Stanislav Ievlev <inger@altlinux.org> 2.7-alt1
- add common timeedit widget

* Wed Jun 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 2.6-alt12
- add effectEnable and effectHide

* Tue Jun 24 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt11
- card-index workflow: always add submit.js + card-index.js
- card-index.js: rename effectUpdate -> updateEffect

* Mon Jun 23 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt10
- effectDisable: apply 'disabled' class to all elements

* Mon Jun 23 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt9
- remove case-attribute support
- rename: effectUpdate -> updateEffect, effectInit -> initEffect
- select.js: always call effectUpdate
- card-index.js: add call of effectUpdate

* Fri Jun 20 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt8
- add effectShow
- fix reset processing for select items

* Fri Jun 20 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt7
- create common effect library
- add effectUpdate

* Thu Jun 19 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt6
- improve effectDisable algo

* Wed Jun 18 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt5
- add support for 'effectDisable'
- don't remove span on translate
- js library: namespace cleanup

* Mon Jun 09 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt4
- fix build with latest alterator
- remove /var/lib/alterator/rss directory

* Thu Jun 05 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt3
- fix daemon restart on upgrade

* Tue Jun 03 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt2
- rebuild to fix localization

* Tue Jun 03 2008 Stanislav Ievlev <inger@altlinux.org> 2.6-alt1
- replace layout files with standalone scripts (configd, configd-cmdine)
- drop fbi-stdin and css-embed support (this features should move to alterator-ovz module)

* Wed May 28 2008 Stanislav Ievlev <inger@altlinux.org> 2.5-alt1
- select.js: fix alterator-ref2 update algo
- fix class attribute retreive in IE
- add support for checklistbox

* Wed May 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 2.4-alt6
- rename "target" attribute to "hrefarg"
  use: <a href="/net-wifi?iface=" class="alterator-ref2" hrefarg="ifname">

* Mon May 26 2008 Vladislav Zavjalov <slazav@altlinux.org> 2.4-alt5
- add "target" attribute to alterator-ref2 anchors, modify fAdjustAnchors:
  Now <a href="/net-wifi?iface=" class="alterator-ref2" target="ifname">
  will be changed to <a href="/net-wifi?iface=<ifname>">
  (This feature is used only in alterator-net-eth now)
- remove timeZone* and ci* names from select.js

* Mon May 26 2008 Vladislav Zavjalov <slazav@altlinux.org> 2.4-alt4
- remove pclass == selector-data test for anchors in card-index.js/ciAdjust

* Tue May 13 2008 Stanislav Ievlev <inger@altlinux.org> 2.4-alt3
- fix ajax submit code
- add javascript support for form based card-indexes

* Mon May 12 2008 Stanislav Ievlev <inger@altlinux.org> 2.4-alt2
- add div class "alterator-label" support

* Tue May 06 2008 Stanislav Ievlev <inger@altlinux.org> 2.4-alt1
- add enum-ref support

* Tue Apr 29 2008 Stanislav Ievlev <inger@altlinux.org> 2.2-alt5
- form workflow:
  * add alias "redirect-url" = "redirect"
  * case-attribute now works with "div", not "form"
  * add name-attribute (card-index replacement)

* Sat Apr 19 2008 Stanislav Ievlev <inger@altlinux.org> 2.2-alt4
- optimize card-index workflow in async mode (skip selector-chooser form processing)

* Fri Apr 18 2008 Stanislav Ievlev <inger@altlinux.org> 2.2-alt3
- submit.js: fix url construction

* Tue Apr 15 2008 Stanislav Ievlev <inger@altlinux.org> 2.2-alt2
- fix open-template function (close port on finish)
- add common.css: common styles according HIG

* Thu Apr 10 2008 Stanislav Ievlev <inger@altlinux.org> 2.2-alt1
- remove html-messages rule

* Tue Apr 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 2.1-alt4
- support for <span class="alterator-label">..</span> in card-index.js

* Wed Apr 02 2008 Stanislav Ievlev <inger@altlinux.org> 2.1-alt3
- acc workflow usage: fix current element and help selection
- fix main help

* Mon Mar 31 2008 Stanislav Ievlev <inger@altlinux.org> 2.1-alt2
- improve case-form feature:
    * multiple variants in single case instruction
    * meta with case
- fix requires for alterator

* Thu Mar 27 2008 Stanislav Ievlev <inger@altlinux.org> 2.1-alt1
- replace separate woo-bus module menu with acc workflow

* Tue Mar 25 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt9
- improve card-index workflow: hide all forms on delete operation

* Mon Mar 24 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt8
- fix module requires (unbound variable design-path)
- improve card-index.js ( hide card-index-select button )

* Thu Mar 20 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt7
- form workflow: move most code to functions
- use new /language url

* Wed Mar 19 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt6
- form workflow: add support for "case forms".

* Tue Mar 18 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt5
- resurrect old 'alterator-ref' behavior
- improve alterator-ref2 (replace basename with woo-get-option 'name)

* Mon Mar 17 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt4
- resurrect '-l'

* Mon Mar 17 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt3
- remove unused ensign configurator
- replace template-help with new workflow
- update internal help to new system
- remove cgi scripts
- move empty.gif to design package

* Fri Mar 14 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- workflow-form: ability to use backend with name different from url
- add dynamically created img for multiple state demonstration

* Thu Mar 13 2008 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- replace index.html + menu.html with single index.html
- remove obsolete index and template-index backends

* Wed Mar 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.16-alt5
- remove alterator-ref3
- alterator-ref, alterator-ref2 : encode url component
- card-index: pass args to woo-list

* Tue Mar 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.16-alt4
- move scripts to design directory
- ability to create dynamic content inside hyperlinks
- new dynamic symlink type - 'alterator-ref3'

* Wed Mar 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.16-alt3
- password.js, card-index.js: fix path for ahttpd

* Wed Mar 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.16-alt2
- card-index now supports a new schema too

* Tue Mar 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.16-alt1
- improve template loading schema (without template-* backends)

* Mon Mar 03 2008 Stanislav Ievlev <inger@altlinux.org> 0.15-alt6
- require ahttpd and alterator-ahttpd

* Fri Feb 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.15-alt5
- fix woo action hackaround

* Tue Feb 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.15-alt4
- remove old hack (requires for alterator-apt),
  all ve-* should require alterator-apt (or alterator pkg) now

* Thu Jan 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.15-alt3
- workflow-help: move string-sure-slash to common place (alterator str)
- menu.scm: fix menu highlighting algorithm (to correct highlighting of /a/b and /a/c like uris)

* Thu Jan 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.15-alt2
- add-support for X-Alterator-Help desktop-file parameter
- desktop-file: improve translation

* Wed Jan 09 2008 Stanislav Ievlev <inger@altlinux.org> 0.15-alt1
- use common help backend from alterator-menu package

* Wed Nov 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.14-alt4
- PreReq shadow-utils

* Wed Jul 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.14-alt3
- add meta-information to alterator.html help file

* Fri Jun 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.14-alt2
- fix requires

* Thu Jun 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.14-alt1
- new menu system
- move card-index.css to design package

* Fri Jun 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.13-alt9
- fix i18n support for javascript

* Wed Jun 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.13-alt8
- improve i18n support for javascript

* Tue Jun 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.13-alt7
- don't override template form values that missing in backend answer

* Mon Jun 04 2007 Stanislav Ievlev <inger@altlinux.org> 0.13-alt6
- improve i18n support in card-index workflow

* Wed May 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.13-alt5
- fix menu item name

* Fri May 25 2007 Stanislav Ievlev <inger@altlinux.org> 0.13-alt4
- add desktop file
- improve UI

* Thu May 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.13-alt3
- fix requires for service
- fix support for Konqueror and Safari.

* Fri May 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.13-alt2
- fix ajax submit work with checkbox inputs

* Wed May 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.13-alt1
- fix typo
- move design to separate package

* Thu May 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.12-alt1
- improve error message notification
- rename internal interfaces from fbi to configd
- remove unused functions

* Thu May 03 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt9
- improve constraints visualization
- improve language CGI: return to refferer, not to /

* Fri Apr 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt8
- improve ajax features
- improve local:a support

* Thu Apr 26 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt7
- add support for radio buttons

* Tue Apr 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt6
- add CSS rules for select and textarea

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt5
- add Ukrainian translation

* Thu Apr 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt4
- another CSS optimizations

* Wed Apr 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt3.1
- hotfix

* Wed Apr 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt3
- little CSS optimization
- rename function to initTitle

* Tue Apr 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.11-alt2
- assign classes to menu items

* Tue Apr 17 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt1
- updated design for server

* Mon Apr 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.10-alt1
- add rss feeds

* Thu Apr 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt18
- require alterator-apt

* Tue Apr 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt17
- rename fbi.layout and fbi-cmdline.layout to configd.layout and configd-cmdline.layout
- form workflow: add support for redirect after get
- submit.js: common library for asyncronyous submit requests
- add progress bar support in forms

* Mon Apr 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt16
- fix <head> generation (was <head> inside <head>)
- add <title> autogeneration if <title> was not defined in module.

* Fri Apr 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt15
- help improvements from kirill@
- improve language selection

* Thu Apr 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt14
- add documentation about alterator

* Tue Apr 03 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt13
- add 'configurator' script to start web browser with appropriate url

* Mon Apr 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt12
- minor fixes in CSS
- add 'alt' to img

* Fri Mar 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt11
- help improvements from kirill@

* Wed Mar 28 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt10
- add documentation for index

* Tue Mar 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt9
- add Ukrainian translation

* Mon Mar 26 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt8
- improve menu items sorting
- add help subsystem

* Fri Mar 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt7
- add logrotate script

* Thu Mar 22 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt6
- improve message extraction from html
- move css to separate package
- css embedding
- remove requires to webserver

* Wed Mar 21 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt5
- add 'alterator-ref2' special reference (remove old hacks for index)
- use PORT-redirect-GET pattern for 'form' workflow

* Tue Mar 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt4
- fix ajax password
- fix ajax selector
- fix js'ed auto-select
- add translations to js
- translate "redirect" message
- add fbi-stdin layout

* Mon Mar 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt3
- html:exception - optimizations
- restrict access to configd.log
- fix typo (redirect-url -> redirect-template)
- auto join same parameters into array (for multiple select lists)

* Fri Mar 16 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt2
- improve CGI and FBI error messages
- force guile16 usage
- add xml declaration for async requests

* Wed Mar 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- new smart, template based, two-level menu subsystem

* Tue Mar 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- move language convertion into cgi
- improve ensign interface
- frontends are backends now
- optimization: don't generate menu for async requests
- fix "exclude" constraints visualization

* Mon Mar 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt10
- improve main menu

* Fri Mar 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt9
- CSS improvements
- fix translation package name calculation
- optimize index backend (cache requests)
- add preliminary version of the main menu generation

* Wed Mar 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt8
- pass url args to all subrequests
- more support for -l: new ability to test with local templates
- significantly improve translation engine
- add translations
- remove unused functions
- apply CSS from SOHO Server

* Tue Mar 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt7
- improve 'form' and 'card-index' workflow

* Thu Mar 01 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt6.1
- turn off debug logfile

* Tue Feb 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt6
- add command line gate to configd service

* Mon Feb 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt5
- remove unused html:field function
- html:select-options - separate values and labels
- constraints visualization: don't mark hidden fields
- improve select_all library
- bugfix: mark only '#t' requires
- index backend: sort items

* Thu Feb 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt4
- init script: add lightweight reload
- automatic top-level menu
- add interface for ensign

* Mon Feb 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt3
- daemonize
- fix socket permissions

* Fri Feb 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- woo-args fix: don't return empty list of the commands

* Thu Feb 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- move ui data to appropriate packages
- install internall backends

* Tue Feb 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- new nut-devices interface
- new feature in form frontend: allow user to define action (new,delete, write by default)
- pass incoming arguments to template backend
- form frontend now can work as a wizard step

* Mon Feb 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt5
- rename log to logfile

* Mon Jan 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- replace bridge-book with log
- more translations: "alternatives", "control"
- minor bugfixes and improvements

* Mon Jan 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- more translations

* Fri Jan 12 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- add support for "label" constraints in card-index engine

* Thu Jan 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- translate language and country codes to locale names
- fill label value from constraints

* Wed Dec 20 2006 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- optimize asynchronous request
- control template improvements
- auto append meta-information
- resurrect doctype definitions in templates

* Tue Dec 19 2006 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- enable ajax-selector in users
- change layout

* Wed Dec 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- control configurator (demo of auto-list usage)
- add support for the page redirection after apply

* Wed Dec 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- auto-list filler
- second generation of card-index frontend

* Mon Dec 11 2006 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- common.js: add support for xmlhttprequest
- password.js: ajax password widget

* Fri Dec 08 2006 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- fbi is an alterator module now
- woo-args return plist now
- rewrite fbi template engine and rename it to frontend

* Wed Dec 06 2006 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- move common JS code to common.js
- remove name auto concatenation to url
- enable constraints in small-card-index template
- small-card-index: add support for new/write/delete operations

* Mon Dec 04 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt9
- remove unused template samples
- add error message html template
- add small-card-index template

* Fri Dec 01 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt8
- use compose from algo library

* Fri Nov 24 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt7
- checkboxes, form template: auto translation
- add "exclude" constraint visualization

* Fri Nov 24 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- fix plist requires

* Mon Nov 20 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- improve woo functions
- enable constraints
- automatic form interface template

* Thu Nov 16 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- improve content checks

* Tue Nov 07 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- add gettext support

* Fri Nov 03 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add: register-get/post-url feature

* Thu Oct 26 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release

