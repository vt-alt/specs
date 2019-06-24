Name: fritzing
Version: 0.9.3b.0.31.git701e3a3
Release: alt4

Summary: Intuitive EDA platform featuring from prototype to product
License: GPLv3, CC-BY-SA-3.0
Group: Engineering

Url: http://fritzing.org
# https://github.com/fritzing/fritzing-app
Source0: %name-%version.tar
# https://github.com/fritzing/fritzing-parts
Source1: %name-parts.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires: boost-devel-headers desktop-file-utils gcc-c++ glibc-devel-static phonon-devel rpm-build-python3 rpmbuild-helper-desktop rpmbuild-helper-sugar-activity ruby ruby-stdlibs
BuildRequires: libgit2-devel qt5-base-devel qt5-svg-devel qt5-serialport-devel

# large chunk of arch-independent data is better not duplicated
Requires: %name-data = %version-%release

%description
Fritzing is an open-source initiative to support designers, artists,
researchers and hobbyists to take the step from physical prototyping
to actual product. It is in the spirit of Processing and Arduino which
allows users to document their Arduino and other electronic-based
prototypes, and to create a PCB layout for manufacturing.

%package data
Summary: Data files for %name
License: GPLv3
Group: Engineering
BuildArch: noarch

%description data
Fritzing is an open-source initiative to support designers, artists,
researchers and hobbyists to take the step from physical prototyping
to actual product. It is in the spirit of Processing and Arduino which
allows users to document their Arduino and other electronic-based
prototypes, and to create a PCB layout for manufacturing.

This package contains shared data files for Fritzing.

%prep
%setup -a1
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
qmake-qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot
cp -r %name-parts %buildroot/%_datadir/%name

%files
%doc LICENSE.*
%_bindir/Fritzing
%_iconsdir/%name.png
%_desktopdir/fritzing.desktop
%_man1dir/Fritzing.*
%_datadir/mime/packages/%name.xml

%files data
%_datadir/%name

%changelog
* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 0.9.3b.0.31.git701e3a3-alt4
- E2K: strip UTF-8 BOM for lcc < 1.24

* Tue Jul 17 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.3b.0.31.git701e3a3-alt3
- Fixed FTBFS (removed xdg macro).

* Thu Feb 01 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.3b.0.31.git701e3a3-alt2
- Add missing part definitions.

* Wed Jan 31 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.3b.0.31.git701e3a3-alt1
- Build new version (Closes: #30924).
- Transfer to Qt5.

* Thu Jun 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.7b-alt3
- Updated build for new toolchain

* Tue Apr 22 2014 Michael Shigorin <mike@altlinux.org> 0.8.7b-alt2
- rebuilt for Sisyphus
- minor spec cleanup

* Sat Apr 19 2014 Konstantin Kogan <kostyalamer at yandex.ru> 0.8.7b-alt1
- First build for ALT Linux t7

* Sat Jan 25 2014 bugs@vdm-design.de
- Update to version 0.8.7b
  * some schematic parts had reversed connectors
  Changes from 0.8.6b:
  * schematic view: all core parts now conform to a .1 inch grid (many thanks Fabian)
  * ratsnest wires now drawn with dashed lines
  * updated examples (many thanks Nushin)
  * updated French translation (thanks Roald)
  * gerber export: separate plated and unplated drill holes
  * more tips and tricks
  * bug fixes:
    offset silkscreen layer on rectangle pcbs
    part labels rotate along with part
    wire colors: orange was green
    set logo-text and netlabel from the text-entry widget at the top of the Inspector (this used to set part label)
    Mavericks ground fill crash
    Arduino part fixes
    equipotential highlight disappearing after wire color change
    wire self-connection prevention was broken
    disappearing wires in schematic or pcb view when parts were directly connected in breadboard view
    Changes from 0.8.5b:
  * another handful of styling changes
  * ICSP and ICSP-less Arduinos
  * bug fixes:
    infinite loop at startup for some languages
    Welcome View print crash
    Arduino swap crash
    Windows XP compatibility
    Note button incorrectly disabled
* Sun Dec 15 2013 bugs@vdm-design.de
- Update to version 0.8.4b
  * Fritzing gets a facelift! (special thanks to Christian and Fabian)
  * new Welcome view
  * new Fritzing Creator Kit examples (in both English and German)
  * Tips and Tricks updated
  * First Time Help now a separate dialog
  * updated Dutch translation (thanks Dave)
  * updated German translation
  * new parts:
    Breadboard BB 301 (contributed by Jeremy)
    RGB LED WS2812
  * bug fixes:
    Mac OSX Mavericks Parts Bin Hover crash
    Saving files with custom parts: sometimes the fzp did not list the latest svg files
    Boost 1.54 bug no longer crashes Fritzing
    Many part tweaks
* Sun Jul 28 2013 bugs@vdm-design.de
- Update to version 0.8.3b
  * fixes the breadboard bugs
* Sat Jul 27 2013 bugs@vdm-design.de
- Update to version 0.8.2b
  * 1000 new parts!
  * parts bin 'and' search implemented (use a space to separate terms)
  * stripboards now with both horizontal and vertical strips plus RS 276-150 layout
  * active layer button controls which side copper-fill fills
  * updated French translation (thanks Yvan)
  * updated German translation
  * new Bulgarian translation (thanks Nikolay)
  * a couple more new parts:
    TI Launchpad
    Raspberry Pi (rev 2)
  * bug fixes:
    Arduino Mega 2560 R3 repaired
    Teensy 3.0 repaired
    Raspberry Pi repaired
    Atmega 5mm tqfp replaced with an 8mm version
    netlabels were misbehaving when flipped or rotated
    Lilypad Mainboard no longer missing
    Generic IC DIP pcb-layer option repaired
    Autorouter crash eliminated
    Parts Editor was not saving pin assignments if loaded SVG files had no connector IDs
    export etchable was missing silk bottom layer
    removed mystery circles on silk bottom of some custom pcb shapes
    bug in the Half+ Breadboard part, and a few others
* Fri Jun 14 2013 bugs@vdm-design.de
- Update to version 0.8.0b
  * pcb view:
  view sketches from either 'above' or 'below'
    place THT parts "through" the top or bottom of the board
  silkscreen bottom layer support
    new Fritzing Fab price-quote feature
    drc now checks if connectors on the same part overlap
    board 'stickyness' is now disabled by default
    copper fill keepout setting on the ground fill submenu
  * schematic view improvements (sponsored by Analog Devices Inc.):
    rotation and flip are enabled for all parts
    when flipping or rotating parts, text elements remain upright and do not mirror
    new voltage label and voltage source parts--the older versions are now obsolete
  * inspector:
    'placement' properties grouped together
    new widgets to display and modify part coordinates and rotation
    editable comboboxes are now graphically distinct from drop-downs
  * new parts
  * other improvements
* Tue Feb 26 2013 bugs@vdm-design.de
- update to version 0.7.12b, now depends on boost-devel
  * autorouter: remove excess bendpoints
  * gerber export drill files now visible in MSN Gerber Viewer (set the m.n format to 2.4)
  * Updated Dutch translation (thanks Davy)
  * Updated Greek translation (thanks Alexander)
  * hide individual part silkscreen
  * imported parts now go to MyParts bin instead of Contrib
  * PNG export now taking much less disk space (thanks Jerome)
  * max pin count for generic IC bumped to 128
  * handful of fixes to DRC
  * find part in sketch (text search)
  * rgb led hole size enlarged
  * lots of little bug fixes
* Fri Jan  4 2013 bugs@vdm-design.de
- update to version 0.7.11b, depends now on Qt >= 4.7
  * new autorouter
    rarely breaks DRC
    handles diagonals
    misses fewer routing possibilities
    has variable keepout setting (in autorouter settings dialog)
  * curvy wires now enabled in pcb and schematic views
  * use shift-wheel to navigate SVGs in the parts editor; wheel events without shift will zoom (or pan) as usual
  * updated Simplified Chinese translation (thanks Yuelin and Ninjia)
  * new Bengali translation (thanks Faruk and friends)
  * improved DRC result highlighting
  * bug fixes:
    OCRA font broken under Windows 8
    free rotate broken when only top view was active (thanks to Gijs for spotting the connection)
    ground fill connections to small vias were being clipped
    annoying offset when dragging a via from the parts bin
* Wed Oct 17 2012 bugs@vdm-design.de
- update to 0.7.10b
  * new DRC
  * bug fixes:
    parts losing 'family' after editing part metadata (leading to "swapping is broken" message)
    SMD on bottom not reloading properly
    crash dropping pad part onto schematic view
    schematic logo text now appearing in printout
    unblocked schematic logo text editing
* Wed Oct 10 2012 bugs@vdm-design.de
- update to 0.7.9b
  * new parts editor--phase one (thanks to Shunichi and Tatsuya for beta-testing)
  * SMD parts can be added either to the top or bottom of a two-sided board
  * updated Greek translation (thanks Alexander)
  * resize schematic-frame part with text entry or combo box
  * 'delete plus' function--for those that miss the old 'delete' which included attached wires. For wires, this deletes up to the next bendpoint.
  * new parts:
    Schematic logo items
    Schematic net labels
  * bug fixes:
    "show unrouted" is also available under the routing menu
    schematic image export: bounding area fix
    default breadboard now aligned to grid
    miscellaneous Gerber export fixes
    culled most red dots (zero length traces) from pcb view
    text entry problems with notes
* Wed Aug 15 2012 bugs@vdm-design.de
- update to version 0.7.7b
  * connection changes in one view sometimes resulted in wandering or
    phantom traces in another view resizing a jumper item when there is
    no pcb caused a crash
* Sat Aug 11 2012 bugs@vdm-design.de
- update to version 0.7.6b
  * deleting a part no longer automatically deletes its connected wires
  * faster loading time (especially if you open two or more windows)
  * info view indicates whether a part is obsolete
  * export etchable now exports both mirrored and non-mirrored at once
  * paste-mask layer for SMDs added to export for production
  * new Slovak translation (thanks Ĺubomír)
  * convert via to bendpoint
  * default breadboard now matches the one in the starter kit
  * revert function
  * new parts:
    new pinheaders: long pad, molex, "alternating" footprint; new pin spacings
    new stereo jack (thanks Max)
    new rj45
  * bug fixes:
    temp parts could disappear when multiple sketches were open with the same temp part (thanks to Jerome and Joerg for help tracking this down)
    no longer possible to draw wires that connect back to themselves or that connect redundantly (thanks to Jerome for help tracking this down)
    breadboard view routing-status
    jpg export quality set to high
    progress bar for parts bin search
    copper blocker width- and height- text entry
    mirrored etchable export was broken
    default breadboard now matches the one shipped with the kits
    drc was incorrectly flagging hole parts
    nasty autorouter bug with split traces
    dragging from temp to another sketch would fail when reopening the other sketch
    rubber-banding bug when dragging a bendpoint with multiple wires
    individual ground fill crash bug
    one more attempt to fix the mac prefs-dialog crash
    missing contour in export etchable
* Mon Jul  2 2012 bugs@vdm-design.de
- update to version 0.7.5b
  * drag-and-drop from desktop onto Fritzing window will open fritzing files
  * align-to-grid and show-grid default to 'on'
  * new Greek translation (thanks Alexander)
  * updated Czech translation (thanks Josef)
  * updated German translation
  * PCB View:
    Fritzing now supports multiple pcbs in a single sketch
    streamlined custom pcb shape file import
    can modify pin size for pinheaders, screwterminals, generic sips and dips, and mystery parts
    pcb "stickiness" is now a setting (i.e. whether parts on a pcb stay in place or follow along when a pcb is dragged)
    'pad' part can now be placed on either copper0 or copper1
    right-click to convert a bendpoint to a via
  * new parts:
    arduino nano 3.0
    resizable ellipse pcb
    resizable copper fill "blocker"
    ardiuno mega shield pcb
    mini-breadboard
    3-axis accelerometer breakout (thanks azharul)
    PCF8574 (thanks c.sgamba)
    S1133 Si Photodiode (thanks Nick)
    double-row THT pin headers
    micro-SD socket
    4-pin audio jack
    new pin header spacings
  * bug fixes:
    'open' menu item now opens all Fritzing files; no more separate 'import' menu items
    all grid options can be found on the view menu
    added support for <use> elements in svgs
    more reliable panning when spacebar is down
    hole parts align to grid
    routing status fixes in pcb view
    simple pcb autoplacement fix
    locked copper fill parts are not deleted if the copper fill function is invoked again
    armel/linux compiler errors fixed
    OSX Preferences dialog crash finally fixed?
    export etchable no longer including board silkscreen on all layers
* Thu Apr 12 2012 bugs@vdm-design.de
- update to new upstream version 0.7.4b
  * fixed the resistor bugs introduced in 0.7.3
* Tue Apr 10 2012 bugs@vdm-design.de
- update to new upstream version 0.7.3b
* Tue Mar 13 2012 bugs@vdm-design.de
- update to new upstream version 0.7.1b
- remove tools and datasheet directorys because of licence issues
* Sat Feb  4 2012 bugs@vdm-design.de
- update to new upstream version 0.7.0b
* Tue Jan  3 2012 bugs@vdm-design.de
- update to new upstream version 0.6.5b
* Fri Dec 16 2011 bugs@vdm-design.de
- update to new upstream version 0.6.4b
- remove files that were included upstream
* Fri Aug 19 2011 bugs@vdm-design.de
- update to new upstream version 0.6.3b
* Mon Aug  1 2011 bugs@vdm-design.de
- add translations
- add runtime dependencies for libqsqlite.so and libqjpeg.so
- add packages for debian, mandriva, centos, sles and rhel
* Thu Jul 28 2011 bugs@vdm-design.de
- updated to 0.6.2b
- add packages for ubuntu and fedora
* Mon May 30 2011 prusnak@opensuse.org
- updated to 0.5.2b
* Sat Feb 12 2011 prusnak@opensuse.org
- updated to 0.5.0b
* Sat Feb 12 2011 prusnak@opensuse.org
- created package based on Fedora one by Ed Marshall
