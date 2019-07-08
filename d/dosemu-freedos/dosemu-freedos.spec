Name: dosemu-freedos
Version: 050405
Release: alt4

Summary: Minimum FreeDOS image for dosemu
License: GPL
Group: Emulators

Url: http://www.freedos.org
Packager: Grigory Batalov <bga@altlinux.ru>

Source0: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/attrib/attrib21.zip
Source1: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/choice/choice43a.zip
#Source2: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/cls/cls201.zip
#Source3: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/comp/comp_pv2.zip
Source3: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/comp/comp0103.zip
#Source4: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/copy/copy300.zip
Source5: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/debug/debug98.zip
Source6: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/diskcomp/diskcomp-06jun2003.zip
Source7: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/diskcopy/dskcp094.zip
Source8: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/exe2bin/exe2b10x.zip
Source9: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/edit/edit082.zip
Source10: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/fc/fc303x.zip
Source11: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/find/find-01nov2003.zip
#Source12: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/format/xmat090.zip
#Source13: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/format/format08.zip
Source12: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/format/format-0.91t.zip
Source13: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/shsucdx/shcd300.zip
Source14: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/help/fasthelp/fsuite04.zip
#Source14: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/help/hhs101.zip
Source15: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/join/swsubs32.zip
Source16: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/label/label14.zip
Source17: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/loadhi/loadh01x.zip
Source18: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/mem/mem16.zip
Source19: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/mode/mode-30nov2004.zip
Source20: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/more/more40b.zip
Source21: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/move/move32x.zip
Source22: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/nansi/nansi40a.zip
Source23: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/pause/pause31b.zip
Source24: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/replace/replace12.zip
Source25: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/sort/sort-09jul2004.zip
#Source26: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/sort/rpsrt102.zip
#Source27: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/tree/tree372s.zip
Source28: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/tree/tree372x.zip
Source29: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/verify/verif10x.zip
Source30: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/vol/vol.zip
Source31: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/xcopy/rxcopy/rxcopy11.zip
Source32: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/assign/asgn-14.zip
Source33: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/dos/deltree/deltree102e.zip
Source34: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/util/file/touc143x.zip
Source36: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/lang/basic/bwb220ax.zip
Source37: http://www.mindspring.com/~minyard/du.zip
#Source37: http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/util/disk/du10x.zip

# GNU utils binaries
Source38: gnu.tar.bz2

Source45: http://www.freedos.org/jhall/freedos/utils/files/runtime21c.zip
Source46: http://www.freedos.org/jhall/freedos/utils/files/tee10.zip
Source47: http://www.freedos.org/jhall/freedos/utils/files/trch31c.zip

# kernel and FreeCOM binaries
Source40: http://heanet.dl.sourceforge.net/sourceforge/freedos/com082pl3-bin.zip
#Source41: http://heanet.dl.sourceforge.net/sourceforge/freedos/ke2035a_16.zip
Source44: http://fdos.org/kernel/kwc38632.dev.zip

Source42: dosemu-freedos-031113-alt-autoexec.bat
Source43: dosemu-freedos-050709-alt-config.sys

BuildArch: noarch
#Requires: dosemu >= 1.3.4

# Automatically added by buildreq on Thu Nov 13 2003
BuildRequires: unzip

Summary(ru_RU.UTF-8): Минимальный образ FreeDOS для dosemu

%description
FreeDOS aims to be a complete, free, 100%% MS-DOS compatible operating system.
This is minimal image of FreeDOS making possible to boot under DOSEmu.

%description -l ru_RU.UTF-8
FreeDOS - свободный, 100%% совместимый аналог операционной системы MS-DOS.
Пакет содержит её минимальный вариант, достаточный для загрузки в DOSEmu.

%prep
%setup -c %name-%version -T
# extracting archives
for i in %SOURCE0 %SOURCE1 %SOURCE3 %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 \
         %SOURCE9 %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14 %SOURCE15 \
	 %SOURCE16 %SOURCE17 %SOURCE18 %SOURCE19 %SOURCE20 %SOURCE21 \
	 %SOURCE22 %SOURCE23 %SOURCE24 %SOURCE25 %SOURCE28 \
	 %SOURCE29 %SOURCE30 %SOURCE31 %SOURCE32 %SOURCE33 %SOURCE34 \
	 %SOURCE36 %SOURCE37 %SOURCE40 %SOURCE44 %SOURCE45 %SOURCE46 %SOURCE47
do
  echo $i
  unzip -L -o -q $i
done
#unzip -L -o -q %%SOURCE35 bin/tee.com help/tee

# freedos tree
mkdir -p tmp/dosemu/freedos/{bin,dosemu,gnu,help,nls,tmp}

FREEDOS=tmp/dosemu/freedos
# adjusting binaries
find -type f -iregex ".*\.com" -o -iregex ".*\.exe" | grep -v "$FREEDOS/bin" | xargs -r -i{} mv {} $FREEDOS/bin
tar -xjf %SOURCE38 -C $FREEDOS
(cd $FREEDOS/bin
 rm -f _*
 for upper in *; do
    chmod 644 $upper
    lower=`echo $upper | tr [:upper:] [:lower:]`
    if [ "x$upper" != "x$lower" ]; then
       mv $upper $lower
    fi
 done
 ln -s swsubst.exe join.exe
 ln -s swsubst.exe subst.exe
 ln -s fasthelp.exe help.exe
 mv command.com ..
 ln -s ../command.com command.com
)

mv source/nansi/nansi.sys $FREEDOS/bin
#mv bin/kernel.sys $FREEDOS
mv kwc38632.sys $FREEDOS/kernel.sys
mv country.sys $FREEDOS/bin
#install -m0644 %%SOURCE42 $FREEDOS/autoexec.bat
#install -m0644 %%SOURCE43 $FREEDOS/config.sys

# adjusting docs
mv doc/fc/fc.txt $FREEDOS/help/fc
mv doc/diskcopy/diskcopy help/{loadhi,tee,touch,verify} $FREEDOS/help/
mv help/attrib.txt $FREEDOS/help/attrib
mv choice/help/choice.en $FREEDOS/help/choice
mv comp.doc $FREEDOS/help/comp
mv debug.doc $FREEDOS/help/debug
mv edit.hlp $FREEDOS/bin
mv doc/format/help.txt $FREEDOS/help/format
mv doc/Fasthelp/README $FREEDOS/help/fasthelp
mv doc/Whatis/README $FREEDOS/help/whatis
mv doc/mem/readme $FREEDOS/help/mem
#mv mode.txt $FREEDOS/help/mode
mv more40/doc/help $FREEDOS/help/more
mv doc/nansi/nansi.doc $FREEDOS/help/nansi
mv doc/sort/sort.1 $FREEDOS/help/sort
mv doc/xcopy.txt $FREEDOS/help/xcopy
mv deltree.txt $FREEDOS/help/deltree
mv doc/bwbasic/bwbasic.doc $FREEDOS/help/bwbasic
#mv doc/sys.txt $FREEDOS/help/sys
mv shsucdx.txt $FREEDOS/help/shsucdx

# help wants 'name.en' pages
for i in $FREEDOS/help/*; do
  mv $i $i.en
done

# adjusting translations
mv nls/* $FREEDOS/nls
mv pause/nls/* more40/nls/* NLS/* choice/nls/* trch/nls/* runtime/nls/* source/diskcopy/nls/* $FREEDOS/nls

%build
%install
mkdir -p %buildroot%_datadir
cp -a tmp/dosemu %buildroot%_datadir/dosemu

%files
%_datadir/dosemu/freedos

%changelog
* Wed Jun 26 2019 Michael Shigorin <mike@altlinux.org> 050405-alt4
- Don't require dosemu, there are more use cases
- Spec cleanup (and UTF-8 conversion)

* Sat Apr 14 2007 Grigory Batalov <bga@altlinux.ru> 050405-alt3
- Pack FreeDOS in plain directory instead of archive.
- Quote percent sign in description.

* Sat Jul 09 2005 Grigory Batalov <bga@altlinux.ru> 050405-alt2
- FreeDOS kernel 1.1.35w (build 2035w-UNSTABLE) that understands
  country settings, so localized filenames could be used

* Tue Apr 05 2005 Grigory Batalov <bga@altlinux.ru> 050405-alt1
- FreeDOS kernel 1.1.35 (build 2035a)
- Tools were updated to 05.04.05:
  + choice 4.3a
  + diskcopy 0.94
  + edit 0.82
  + fc 3.03
  + find 2.9 (01nov2003)
  + format 0.91t
  + fasthelp 3.5
  + whatis 1.1
  + mem 1.6
  + mode 30nov2004
  + more 4.0
  + move 3.2
  + shcd 3.00
  + sort 1.4 (09jul2004)
  + tee 1.0
  + trch 1.31
- Runtime 2.1 was added

* Tue Feb 24 2004 Grigory Batalov <bga@altlinux.ru> 040224-alt1
- FreeDOS kernel 1.1.33 (build 2033)
- FreeCOM v0.82pl3
- Tools updated to 24.02.04

* Thu Nov 13 2003 Grigory Batalov <bga@altlinux.ru> 031113-alt1
- FreeDOS kernel 1.1.32a (build 2032a)
- FreeCOM v0.82pl1
- Tools updated to 13.11.03
- Added shsucdx (CD-ROM driver)

* Fri Dec 20 2002 Grigory Batalov <bga@altlinux.ru> 021220-alt1
- Initial build
