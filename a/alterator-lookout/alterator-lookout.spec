Name: alterator-lookout
Version: 2.7
Release: alt1

Source:%name-%version.tar

Summary: dialog based interface for alterator
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 5.1-alt7
Requires: alterator-l10n >= 1.5-alt1
Conflicts: alterator-browser-qt < 2.17.0-alt1
Conflicts: alterator-wizardface < 1.1-alt3

Patch: alterator-lookout-2.6-shift-reset.patch
Patch1: alterator-lookout-2.6-register-fluids.patch

BuildPreReq: alterator >= 5.1-alt7
%ifarch e2k
BuildRequires: guile20-devel libguile20-devel
%else
BuildPreReq: guile22-devel
%endif

%description
dialog based interface for alterator

%brp_strip_none %_alterator_libdir/*
%add_verify_elf_skiplist %_alterator_libdir/*
%add_findreq_skiplist %_alterator_libdir/*

%prep
%setup
%ifarch e2k
%patch -p2
%patch1 -p2
%endif

%build
%make_build libdir=%_libdir

%install
export GUILE_AUTO_COMPILE=0
export GUILE_LOAD_PATH="lookout"
%makeinstall

%files
%_bindir/*
%_alterator_libdir/interfaces/guile/*
%_alterator_libdir/lookout
%_alterator_libdir/ui/*
%_alterator_datadir/interfaces/guile/*
%_alterator_datadir/lookout
%_alterator_datadir/ui/*

%changelog
* Wed Aug 26 2020 Paul Wolneykien <manowar@altlinux.org> 2.7-alt1
- Allow to set mode change handler with (frame-bind
  "document:expert_mode" "change" ...)
- Try to reset the mode chane handler on frame replace.

* Thu Aug 20 2020 Paul Wolneykien <manowar@altlinux.org> 2.6.1-alt1
- Define 'form-update-cookie' and 'form-cookie' wrappers around
  globals.

* Wed Dec 20 2017 Paul Wolneykien <manowar@altlinux.org> 2.6-alt4
- Use registered fluids with shift/reset-based call/cc (patch).

* Fri Dec 15 2017 Paul Wolneykien <manowar@altlinux.org> 2.6-alt3
- Delimit shift-based continuation with reset (e2k, patch).

* Thu Dec 07 2017 Paul Wolneykien <manowar@altlinux.org> 2.6-alt2
- Build with guile 2.0 for E2K arch.

* Thu Aug 03 2017 Paul Wolneykien <manowar@altlinux.org> 2.6-alt1
- Added "groupbox" to the set of supported interactive widgets.
- Put the document URI query part in the \'document:query global.

* Wed Apr 05 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5-alt1
- rebuilt with alterator 5.0

* Wed Jul 13 2011 Mikhail Efremov <sem@altlinux.org> 2.4-alt1
- Added widget 'slideshow'.

* Tue Jul 13 2010 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- new widget 'checktree' (http://altlinux.org/Alterator/CheckTree)

* Mon Nov 23 2009 Stanislav Ievlev <inger@altlinux.org> 2.2-alt2
- form-update-value-list(): fix work with empty values

* Tue Nov 17 2009 Stanislav Ievlev <inger@altlinux.org> 2.2-alt1
- synchronize form-update-value-list with HTML version
- enum-rows is a hidded attribute now

* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt4
- replace frame:on-next, frame:on-back with modern (alterator wizard) library

* Wed Aug 26 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt3
- new (alterator wizard) library

* Wed Aug 12 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt2
- form library: fix radio support

* Tue May 19 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt1
- use generic effects library from alterator
- drop old form API
- form API: add simple i18n support, add form-confirm

* Fri May 15 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt4
- fix form-error call in catch/message

* Thu May 14 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt3
- move load-path hacking to single place
- fix typo in form-update-visibility function

* Fri May 08 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- resurrect old behaviour of clean-widget (alterator-vm uses it)
- call frame:on-next and frame:on-back with right global context (new form API now use it)

* Thu May 07 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- add ability to load and use callbacks from 'ajax.scm' files

* Thu Apr 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.7-alt1
- add support for 'nameref' attribute

* Fri Apr 10 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt8
- fix typo

* Tue Mar 24 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt7
- remove debug messages

* Fri Feb 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.6-alt6
- fix value metaattribute for checklistbox

* Mon Feb 09 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt5
- form library: add form-update-activity, form-update-visibility

* Thu Feb 05 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt4
- form library: add support for radio buttons, minor bugfixes

* Mon Feb 02 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt3
- improve form API (form-bind)

* Fri Jan 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt2
- form library: fix work with static labels

* Thu Jan 29 2009 Stanislav Ievlev <inger@altlinux.org> 1.6-alt1
- new improved form library
- use translations directly from alterator-l10n

* Tue Jan 20 2009 Mikhail Efremov <sem@altlinux.org> 1.5-alt2
- use resolve-path function
- atlas.scm is removed

* Wed Dec 10 2008 Stanislav Ievlev <inger@altlinux.org> 1.5-alt1
- replace radiolist with radiolistbox

* Wed Nov 12 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt3
- move effects into library, remove duplicates in code

* Wed Nov 05 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt2
- fix i-element?

* Wed Nov 05 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt1
- improve form library
- use module.mak

* Fri Oct 24 2008 Stanislav Ievlev <inger@altlinux.org> 1.3-alt13
- remove constraints usage
- fix "count" and "remove" attributes exporting
- fix modules deps

* Mon Oct 20 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt12
- revert re-export -> export in attributes.scm
- add macro (define-meta-attribute)

* Thu Oct 16 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt11
- export (remove count) -> re-export (remove count) in attributes.scm

* Fri Oct 10 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt10
- bugfix: reset page namelist in frame:replace
- move all widget definitions to (alterator lookout widgets)
- move add attribute definitions to (alterator lookout attributes)

* Wed Oct 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt9
- rewrite form module

* Tue Oct 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt8
- do not set values for widgets with wrong names:
- tune args-get-names/args-get-args
- rename form-document -> *form-document*, form-setdocument/getdocument -> form-document-set/get
- rename internal function form_element? -> form-element?

* Mon Oct 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt7
- change argument handling in form-read/-write

* Mon Oct 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt6
- in form module:
-   rename form:* to form-*
-   rename form-set -> form-set!
-   use form-error for error messages
-   form-set!: throw form-error when name is not found
-   firm-read: return nothing (map -> for-each)
-   form-write: use fold

* Fri Oct 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt5
- add form:apply
- fix form:write
- add support for textbox in form:read/write (textbox now has no attribute "value")
- use form:get and form:set in form:read and form:write functions

* Thu Oct 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt4
- add (alterator lookout form) module for "form-style" work with widgets

* Mon Sep 15 2008 Stanislav Ievlev <inger@altlinux.org> 1.3-alt3
- new catch/message with type-error support

* Fri Sep 12 2008 Stanislav Ievlev <inger@altlinux.org> 1.3-alt2
- update to latest alterator

* Mon Sep 01 2008 Stanislav Ievlev <inger@altlinux.org> 1.3-alt1
- add support for multicolumn enumref

* Mon Aug 04 2008 Stanislav Ievlev <inger@altlinux.org> 1.2-alt4
- move string-list-index to (alterator algo)

* Mon Jul 28 2008 Stanislav Ievlev <inger@altlinux.org> 1.2-alt3
- don't use (alterator r6rs)

* Wed Jul 02 2008 Stanislav Ievlev <inger@altlinux.org> 1.2-alt2
- document:url is always string

* Tue Jul 01 2008 Stanislav Ievlev <inger@altlinux.org> 1.2-alt1
- update i18n: builtin po-domain and _ functions
- add effect-enable, effect-hide

* Mon Jun 30 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt11
- remove update-constraints function

* Wed Jun 25 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt10
- move strong and bold to default library

* Mon Jun 23 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt9
- rename: effect-init -> init-effect, effect-update -> update-effect

* Fri Jun 20 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt8
- add effect-show

* Fri Jun 20 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt7
- create common effects library
- add effect-update

* Thu Jun 19 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt6
- add support for effect-disable

* Thu Jun 19 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt5
- add simple DOM (getElementsByName)
- remove header meta-attribute

* Thu Jun 19 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt4
- add hidden attributes
- remove keywords
- remove with-init-attributes function

* Tue Jun 17 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt3
- fix translation

* Tue Jun 17 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt2
- fix build

* Sat Jun 07 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt1
- document:subdocument can work without argument now
- new simplified frame:page function
- remove sub-type attribute

* Fri Jun 06 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt4
- remove unused code (timers)
- silent-set: allow to work with '() values
- fix checklist-rows meta-attribute initialization

* Tue Jun 03 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt3
- resurrect checklist for alterator-vm

* Fri May 30 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt2
- remove checklist support
- fix clear-cell function
- join to common translation database

* Wed May 28 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- add checklistbox support

* Mon May 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt5
- remove apply-actions helper
- "value" and "enumref" attribures now works in more flexible way.

* Fri May 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt3
- fix action-add

* Tue May 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt2
- enumref: add support for additional attributes

* Mon May 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- add support for enumref meta-attribute (smart select)
- fix define-init-attribute macro

* Sun May 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.8-alt1
- move widgets and attributes to common evaluation place

* Thu Apr 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt3
- remove (alterator glob) usage

* Wed Apr 16 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- add attributes: step-text step-pixmap action-text action-pixmap

* Tue Apr 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- finally remove atlas

* Mon Apr 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- remove atlas
- add init-cell functions

* Mon Apr 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- add common /std/frame

* Fri Apr 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- remove old profile.d support
- remove /std/auth
- add make-widget for simple widgets
- remove map file

* Wed Apr 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt4
- add active attribute (for radiolist)

* Fri Apr 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt3
- remove map/samples.map
- remove unused attributes mask position active layout-policy children-align background-color full-screen

* Wed Mar 12 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt2
- remove backend2/atlas
- getting paths from ALTERATOR_DATADIR env.var. in interfaces/guile/atlas.scm

* Thu Mar 06 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- add attributes: colspan, rowspan, url

* Thu Jun 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt10
- move woo-list/name+label to main alterator library

* Wed Jun 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt9
- new usefull functions: name+label , woo-list/name+label

* Mon Jun 04 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt8
- add splitbox

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- add Ukrainian translation

* Wed Apr 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- add tab-index attribute

* Tue Mar 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- add dateedit,timeedit widgets
- add expanded attribute
- remove expanded helper function

* Tue Feb 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- remove unused document:window
- add current-text attribute declaration
- add spinbox widget declaration
- remove widget visibility forcing during replace operation (it's a problem of browser now)

* Mon Feb 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- add gridbox and text-wrap
- hbox and vbox became wrappers over more general box widget

* Mon Jan 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- add separator and orientation

* Thu Jan 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add atlas backend

* Wed Jan 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- change socket path

* Tue Jan 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- add support for cursor attribute

* Fri Dec 29 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- remove dbus support

* Fri Dec 22 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- move atlas,context and alterator-pp here

* Thu Dec 21 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add support for mailboxes (simplest message passing engine, replacement of dbus)
- remove deprecated widgets

* Fri Dec 08 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- initial release
