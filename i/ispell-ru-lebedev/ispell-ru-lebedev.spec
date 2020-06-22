%define ispelldir	%_libdir/ispell
%define aspelldir	%_libdir/aspell
%define myspelldir	%_datadir/myspell
%define ispell_version	3.2.06
%define aspell_version	0.60.0

Name: ispell-ru-lebedev
Version: 0.99g5
Release: alt14

Packager: Sergey Kurakin <kurakin@altlinux.org>

Summary: Russian ispell dictionary, KOI8-R, "io" and "ie" spelling allowed
Summary(ru_RU.UTF-8): Словарь русского языка для ispell, KOI8-R, разрешена замена "ё" на "е"
Summary(be_BY.UTF-8): Слоўнік рускае мовы для ispell, KOI8-R, дазволена зьмена "ё" на "е"
# aspell is also GPL-2.0-only, see LICENSE.phonet
License: BSD-3-Clause
Group: Text tools
URL: http://scon155.phys.msu.su/~swan/orthography.html

# Note: ispell and aspell hash files are architecture-dependent.
# Do not put BuildArch: noarch here.

# ftp://scon155.phys.msu.su/pub/russian/ispell/rus-ispell-%version.tar.gz
Source: rus-ispell-%version.tar
# http://www.inp.nsk.su/~grozin/aspell/
Source2: rus-ispell-aspellfiles-0.3.tar
Source10: addition.words

Patch1:	rus-ispell-0.99g1-alt-no-substandard-language.patch
Patch3:	ispell-ru-lebedev-affix_flags.patch

Requires: %name-common
Requires: ispell >= %ispell_version
Provides: ispell-dictionary, ispell-ru = %version
Obsoletes: irussian, ispell-rus, ispell-russian, rispell, ispell-ru

# Automatically added by buildreq on Sun Nov 28 2010
BuildRequires: i2myspell vim-console

BuildPreReq: ispell >= %ispell_version
BuildPreReq: aspell >= %aspell_version
BuildPreReq: vim-devel >= 4:7.0

# The real ispell is required - not the aspell-provided emulation.
BuildConflicts:	aspell-ispell

%package common
Summary: Russian ispell/aspell/hunspell/vim dictionaries common files
Group: Text tools
BuildArch: noarch
Conflicts: %name < %EVR
Conflicts: %name-cp1251 < %EVR
Conflicts: %name-ie < %EVR
Conflicts: %name-ie-cp1251 < %EVR
Conflicts: %name-io < %EVR
Conflicts: %name-io-cp1251 < %EVR
Conflicts: aspell-ru-lebedev < %EVR
Conflicts: hunspell-ru-lebedev < %EVR
Conflicts: hunspell-ru-lebedev-ie < %EVR
Conflicts: hunspell-ru-lebedev-io < %EVR
Conflicts: vim-spell-ru-lebedev < %EVR
Conflicts: vim-spell-ru-lebedev-ie < %EVR
Conflicts: vim-spell-ru-lebedev-io < %EVR

%package cp1251
Summary: Russian ispell dictionary, CP1251, "io" and "ie" spelling allowed
Summary(ru_RU.UTF-8): Словарь русского языка для ispell, CP1251, разрешена замена "ё" на "е"
Summary(be_BY.UTF-8): Слоўнік рускае мовы для ispell, CP1251, дазволена зьмена "ё" на "е"
Group: Text tools
Requires: %name-common
Requires: ispell >= %ispell_version
Provides: ispell-dictionary, ispell-ru-cp1251 = %version
Obsoletes: irussian, ispell-rus, ispell-russian, rispell, ispell-ru-cp1251

%package -n aspell-ru-lebedev
Summary: Russian dictionary for GNU Aspell
Summary(ru_RU.UTF-8): Словарь русского языка для GNU Aspell
Summary(be_BY.UTF-8): Слоўнік рускае мовы для GNU Aspell
License: BSD-3-Clause and GPL-2.0-only
Group: Text tools
Requires: %name-common
Requires: aspell >= %aspell_version
Provides: aspell-dictionary, aspell-ru = %version
Provides: aspell-ru-lebedev-common = %version-%release
Obsoletes: aspell-ru, aspell-ru-lebedev-ie, aspell-ru-lebedev-io
Obsoletes: aspell-ru-lebedev-common
Obsoletes: aspell-ru-lebedev-common-ie, aspell-ru-lebedev-common-io

%package -n hunspell-ru-lebedev
Summary: Russian dictionary for myspell/hunspell, "io" and "ie" spelling allowed
Summary(ru_RU.UTF-8): Словарь русского языка для myspell/hunspell, разрешена замена "ё" на "е"
Group: Text tools
BuildArch: noarch
Requires: %name-common
Provides: hunspell-ru
Obsoletes: hunspell-ru

%package -n hunspell-ru-lebedev-ie
Summary: Russian dictionary for myspell/hunspell, only "ie" spelling allowed
Summary(ru_RU.UTF-8): Словарь русского языка для myspell/hunspell без поддержки буквы "ё"
Group: Text tools
BuildArch: noarch
Requires: %name-common
Provides: hunspell-ru

%package -n hunspell-ru-lebedev-io
Summary: Russian dictionary for myspell/hunspell, "io" required
Summary(ru_RU.UTF-8): Словарь русского языка для myspell/hunspell с обязательным употреблением буквы "ё"
Group: Text tools
BuildArch: noarch
Requires: %name-common
Provides: hunspell-ru

%package -n vim-spell-ru-lebedev
Summary: Russian dictionary for vim, "io" and "ie" spelling allowed
Summary(ru_RU.UTF-8): Словарь русского языка для vim, разрешена замена "ё" на "е"
Group: Text tools
BuildArch: noarch
Requires: %name-common
Provides: vim-spell-ru
Obsoletes: vim-spell-ru

%package -n vim-spell-ru-lebedev-ie
Summary: Russian dictionary for vim, only 'ie' spelling allowed
Summary(ru_RU.UTF-8): Словарь русского языка для vim без поддержки буквы "ё"
Group: Text tools
BuildArch: noarch
Requires: %name-common

%package -n vim-spell-ru-lebedev-io
Summary: Russian dictionary for vim, "io" required
Summary(ru_RU.UTF-8): Словарь русского языка для vim с обязательным употреблением буквы "ё"
Group: Text tools
BuildArch: noarch
Requires: %name-common

%package ie
Summary: Russian ispell dictionary, KOI8-R, only "ie" spelling allowed
Summary(ru_RU.UTF-8): Словарь русского языка для ispell, KOI8-R, без поддержки буквы "ё"
Summary(be_BY.UTF-8): Слоўнік рускае мовы для ispell, KOI8-R, бяз літары "ё"
Group: Text tools
Requires: %name-common
Requires: ispell >= %ispell_version
Provides: ispell-dictionary, ispell-ru = %version
Obsoletes: irussian, ispell-rus, ispell-russian, rispell, ispell-ru

%package ie-cp1251
Summary: Russian ispell dictionary, CP1251, only "ie" spelling allowed
Summary(ru_RU.UTF-8): Словарь русского языка для ispell, CP1251, без поддержки буквы "ё"
Summary(be_BY.UTF-8): Слоўнік рускае мовы для ispell, CP1251, бяз літары "ё"
Group: Text tools
Requires: %name-common
Requires: ispell >= %ispell_version
Provides: ispell-dictionary, ispell-ru-cp1251 = %version
Obsoletes: irussian, ispell-rus, ispell-russian, rispell, ispell-ru-cp1251

%package io
Summary: Russian ispell dictionary, KOI8-R, "io" required
Summary(ru_RU.UTF-8): Словарь русского языка для ispell, KOI8-R, обязательное употребление буквы 'ё'
Summary(be_BY.UTF-8): Слоўнік рускае мовы для ispell, KOI8-R, абавязковае выкарыстаньне літары 'ё'
Group: Text tools
Requires: %name-common
Requires: ispell >= %ispell_version
Provides: ispell-dictionary, ispell-ru = %version
Obsoletes: irussian, ispell-rus, ispell-russian, rispell, ispell-ru

%package io-cp1251
Summary: Russian ispell dictionary, CP1251, 'io' required
Summary(ru_RU.UTF-8): Словарь русского языка для ispell, CP1251, обязательное употребление 'ё'
Summary(be_BY.UTF-8): Слоўнік рускае мовы для ispell, CP1251, абавязковае выкарыстаньне літары 'ё'
Group: Text tools
Requires: %name-common
Requires: ispell >= %ispell_version
Provides: ispell-dictionary
Provides: ispell-ru-cp1251 = %version
Obsoletes: irussian, ispell-rus, ispell-russian, rispell, ispell-ru-cp1251


%description
Russian dictionary for ispell in KOI8-R encoding, based on original
Dr. Alexander Lebedev dictionary with a little additions.

This variant allows spellings with and without the "io" letter.

Dictionary is installed under the name "russian-lebedev",
default one with the name "russian" is selected
using alternatives subsystem.

%description -l ru_RU.UTF-8
Словарь русского языка для ispell в кодировке KOI8-R. Основан
на оригинальной версии проф. Александра Лебедева с небольшими
добавлениями.

Допускает замену буквы "ё" на "е" (выборочное употребление
буквы "ё").

Устанавливается под именем "russian-lebedev". Словарь по умолчанию
с именем "russian" выбирается при помощи подсистемы альтернатив.

%description common
This package contains files common among all Russian
ispell/aspell/hunspell/vim dictionaries.

%description cp1251
Russian dictionary for ispell in CP1251 encoding, based on original
Dr. Alexander Lebedev dictionary with a little additions.

This variant allows spellings with and without the "io" letter.

Dictionary is installed under the name "russianw-lebedev",
default one with the name "russianw" is selected
using alternatives subsystem.

%description cp1251 -l ru_RU.UTF-8
Словарь русского языка для ispell в кодировке CP1251. Основан
на оригинальной версии проф. Александра Лебедева с небольшими
добавлениями.

Допускает замену буквы "ё" на "е" (выборочное употребление
буквы "ё").

Устанавливается под именем "russianw-lebedev". Словарь по умолчанию
с именем "russianw" выбирается при помощи подсистемы альтернатив.


%description -n aspell-ru-lebedev
Russian dictionary for use with GNU Aspell, based on original Ispell
dictionary by Dr. Alexander Lebedev with a little additions.

There are three spelling variants available:

 - "ru-lebedev" - allows spellings with and without the "io" letter;
 - "ru-lebedev-io" - requires strict use of the "io" letter;
 - "ru-lebedev-ie" - does not support the "io" letter.

You can select the default Russian dictionary for GNU Aspell
(with the name "ru") using the alternatives subsystem.

%description -n aspell-ru-lebedev -l ru_RU.UTF-8
Словарь русского языка для GNU Aspell. Основан на оригинальной версии
словаря для Ispell проф. Александра Лебедева с небольшими добавлениями.

Доступны три варианта словаря:

 - "ru-lebedev" - допускает замену буквы "ё" на "е" (выборочное
   употребление буквы "ё");
 - "ru-lebedev-io" - требует обязательного использования буквы "ё";
 - "ru-lebedev-ie" - не поддерживает букву "ё".

Выбор словаря русского языка по умолчанию (с именем "ru")
осуществляется с помощью механизма альтернатив.


%description  -n hunspell-ru-lebedev
Russian dictionary for myspell/hunspell, based on original Ispell
dictionary by Dr. Alexander Lebedev with a little additions.

Used in OpenOffice, LibreOffice, Mozilla Firefox, Thunderbird
and others.

This variant allows spellings with and without the "io" letter.

This dictionary is installed under the name "ru_RU-lebedev".
Default Russian hunspell dictionary ("ru_RU") is selected
using alternatives.

%description  -n hunspell-ru-lebedev -l ru_RU.UTF-8
Словарь русского языка для myspell/hunspell. Основан на оригинальной
версии словаря для Ispell проф. Александра Лебедева с небольшими
добавлениями.

Используется в OpenOffice, LibreOffice, Mozilla Firefox,
Thunderbird и др.

Допускает замену буквы "ё" на "е" (выборочное употребление
буквы "ё").

Устанавливается под именем "ru_RU-lebedev". Словарь hunspell
по умолчанию ("ru_RU") выбирается с помощью механизма альтернатив.


%description  -n hunspell-ru-lebedev-io
Russian dictionary for myspell/hunspell, based on original Ispell
dictionary by Dr. Alexander Lebedev with a little additions.

Used in OpenOffice, LibreOffice, Mozilla Firefox, Thunderbird
and others.

This variant requires strict use of the "io" letter.

This dictionary is installed under the name "ru_RU-lebedev-io".
Default Russian hunspell dictionary ("ru_RU") is selected
using alternatives.

%description  -n hunspell-ru-lebedev-io -l ru_RU.UTF-8
Словарь русского языка для myspell/hunspell. Основан на оригинальной
версии словаря для Ispell проф. Александра Лебедева с небольшими
добавлениями.

Используется в OpenOffice, LibreOffice, Mozilla Firefox,
Thunderbird и др.

Требует обязательного использования буквы "ё".

Устанавливается под именем "ru_RU-lebedev-io". Словарь hunspell
по умолчанию ("ru_RU") выбирается с помощью механизма альтернатив.


%description  -n hunspell-ru-lebedev-ie
Russian dictionary for myspell/hunspell, based on original Ispell
dictionary by Dr. Alexander Lebedev with a little additions.

Used in OpenOffice, LibreOffice, Mozilla Firefox, Thunderbird
and others.

This variant does not support the "io" letter.

This dictionary is installed under the name "ru_RU-lebedev-ie".
Default Russian hunspell dictionary ("ru_RU") is selected
using alternatives.

%description  -n hunspell-ru-lebedev-ie -l ru_RU.UTF-8
Словарь русского языка для myspell/hunspell. Основан на оригинальной
версии словаря для Ispell проф. Александра Лебедева с небольшими
добавлениями.

Используется в OpenOffice, LibreOffice, Mozilla Firefox,
Thunderbird и др.

Этот вариант словаря не поддерживает букву "ё".

Устанавливается под именем "ru_RU-lebedev-ie". Словарь hunspell
по умолчанию ("ru_RU") выбирается с помощью механизма альтернатив.


%description  -n vim-spell-ru-lebedev
Russian dictionary for vim spellchecking feature, based on original
Ispell dictionary by Dr. Alexander Lebedev with a little additions.

This variant allows spellings with and without the "io" letter.

Accessible in vim under the name "ru-lebedev", so you can call it
with the following vim command:

:setlocal spell spelllang=ru-lebedev

%description  -n vim-spell-ru-lebedev-io
Russian dictionary for vim spellchecking feature, based on original
Ispell dictionary by Dr. Alexander Lebedev with a little additions.

This variant requires strict use of the "io" letter.

Accessible in vim under the name "ru-lebedev-io", so you can call it
with the following vim command:

:setlocal spell spelllang=ru-lebedev-io

%description  -n vim-spell-ru-lebedev-ie
Russian dictionary for vim spellchecking feature, based on original
Ispell dictionary by Dr. Alexander Lebedev with a little additions.

This variant does not support the "io" letter.

Accessible in vim under the name "ru-lebedev-ie", so you can call it
with the following vim command:

:setlocal spell spelllang=ru-lebedev-ie


%description ie
Russian dictionary for ispell in KOI8-R encoding, based on original
Dr. Alexander Lebedev dictionary with a little additions.

This variant does not support the "io" letter.

Dictionary is installed under the name "russian-lebedev-ie",
default one with the name "russian" is selected
using alternatives subsystem.

%description ie -l ru_RU.UTF-8
Словарь русского языка для ispell в кодировке KOI8-R. Основан
на оригинальной версии проф. Александра Лебедева с небольшими
добавлениями.

Этот вариант словаря не поддерживает букву "ё".

Устанавливается под именем "russian-lebedev-ie". Словарь по умолчанию
с именем "russian" выбирается при помощи подсистемы альтернатив.


%description ie-cp1251
Russian dictionary for ispell in CP1251 encoding, based on original
Dr. Alexander Lebedev dictionary with a little additions.

This variant does not support the "io" letter.

Dictionary is installed under the name "russianw-lebedev-ie",
default one with the name "russianw" is selected
using alternatives subsystem.

%description ie-cp1251 -l ru_RU.UTF-8
Словарь русского языка для ispell в кодировке CP1251. Основан
на оригинальной версии проф. Александра Лебедева с небольшими
добавлениями.

Этот вариант словаря не поддерживает букву "ё".

Устанавливается под именем "russianw-lebedev-ie". Словарь по умолчанию
с именем "russianw" выбирается при помощи подсистемы альтернатив.


%description io
Russian dictionary for ispell in KOI8-R encoding, based on original
Dr. Alexander Lebedev dictionary with a little additions.

This variant requires strict use of the "io" letter.

Dictionary is installed under the name "russian-lebedev-io",
default one with the name "russian" is selected
using alternatives subsystem.

%description io -l ru_RU.UTF-8
Словарь русского языка для ispell в кодировке KOI8-R. Основан
на оригинальной версии проф. Александра Лебедева с небольшими
добавлениями.

Этот вариант словаря требует обязательного использования буквы "ё".

Устанавливается под именем "russian-lebedev-io". Словарь по умолчанию
с именем "russian" выбирается при помощи подсистемы альтернатив.


%description io-cp1251
Russian dictionary for ispell in CP1251 encoding, based on original
Dr. Alexander Lebedev dictionary with a little additions.

This variant requires strict use of the "io" letter.

Dictionary is installed under the name "russianw-lebedev-io",
default one with the name "russianw" is selected
using alternatives subsystem.

%description io-cp1251 -l ru_RU.UTF-8
Словарь русского языка для ispell в кодировке CP1251. Основан
на оригинальной версии проф. Александра Лебедева с небольшими
добавлениями.

Этот вариант словаря требует обязательного использования буквы "ё".

Устанавливается под именем "russianw-lebedev-io". Словарь по умолчанию
с именем "russianw" выбирается при помощи подсистемы альтернатив.


%prep
%setup -q -c -a 2
cat %SOURCE10 | iconv -f=utf-8 -t=koi8-r > addition.koi
%patch1 -p1
%patch3 -p1

iconv -fkoi8r -tutf8 <README.koi >README.ru

%build

# BuildIspellEncoding <spelling> <encoding> <encoding-suffix>
BuildIspellEncoding()
{
	DICT="base.koi abbrev.koi computer.koi for_name.koi geography.koi \
		science.koi addition.koi"
		# rare.koi

	FileSuffix "$1"

	case $1 in
	"ie" )
		cat $DICT | sed "/^\(#\|$\)/d" | tr '\243\263' '\305\345' | ./sortkoi8 | uniq |
			./trans koi $2 > russian$3-lebedev$suffix.dict
		cat russian.aff.koi | sed -e "s/^\#e//;s/^\#$2/wordchars/" | \
			./trans koi $2 > russian$3-lebedev$suffix.aff
	;;
	"io" )
		cat $DICT | sed "/^\(#\|$\)/d" | ./sortkoi8 | uniq |
			./trans koi $2 > russian$3-lebedev$suffix.dict
		cat russian.aff.koi | sed -e "s/^\#y//;s/^\#$2/wordchars/" | \
			./trans koi $2 > russian$3-lebedev$suffix.aff
	;;
	* )
		cat russian-lebedev-ie.dict russian-lebedev-io.dict | ./sortkoi8 | uniq |
			./trans koi $2 > russian$3-lebedev.dict
		cat russian.aff.koi | sed -e "s/^\#e//;s/^\#y//;s/^\#$2/wordchars/" | \
			./trans koi $2 > russian$3-lebedev.aff
	;;
	esac

	buildhash ./russian$3-lebedev$suffix.dict ./russian$3-lebedev$suffix.aff \
		russian$3-lebedev$suffix.hash

}

# BuildWordList <spelling>
BuildWordList()
{
	ispell -d ./russian-lebedev-$1.hash -e < russian-lebedev-$1.dict | \
		tr ' ' '\n' | grep -v '^$' | \
		sort -u > "$1.list"
}

# BuildAspellHash <part>
BuildAspellHash()
{
	aspell --lang=ru-lebedev create master ./ru-lebedev-"$1"-only.rws \
		< ru-lebedev-"$1"-only.list
}

# BuildSpelling <spelling>
BuildSpelling()
{
	BuildIspellEncoding "$1" "win" "w"
	BuildIspellEncoding "$1" "koi" ""
	if [ -n "$1" ] ; then
		BuildWordList "$1"
	fi
}

MakeHunspell()
{
	FileSuffix "$1"

	# ALPHABET contains 3rd, 4th and 5th parameters for i2myspell
	# 3rd: alphabet uppercase
	# 4th: alphabet lowercase
	# 5th: all letters in frequency order, taken from original Dr. Lebedev's
	# dictionary for myspell
	ALPHABET="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
	ALPHABET="$ALPHABET абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
	ALPHABET="$ALPHABET оаитенрсвйлпкьыяудмзшбчгщюжцёхфэъАВСМКГПТЕИЛФНДОЭРЗЮЯБХЖШЦУЧЬЫЪЩЙЁ"

	# In case of "ie-only" remove "io" from the alphabet
	[ "$1" == "ie" ] && ALPHABET=`echo $ALPHABET | sed -e 's/ё//g;s/Ё//g'`

	# Convert alphabet to koi8-r
	ALPHABET=`echo $ALPHABET | iconv -fUTF-8 -tkoi8-r`

	i2myspell ./russian-lebedev$suffix.hash UTF-8 $ALPHABET | \
		iconv -fkoi8-r -tUTF-8 > ru_RU-lebedev$suffix.aff
	
	# The myspell dictionary is the same as ispell one.
	# The only difference -- words count in the first line.
	cat russian-lebedev$suffix.dict | wc -l > ru_RU-lebedev$suffix.dic
	cat russian-lebedev$suffix.dict | iconv -fkoi8-r -tUTF-8 >> ru_RU-lebedev$suffix.dic
}

MakeVimspell()
{
	FileSuffix "$1"

	# To bild vimspell dictionaries, we need a slightly changed
	# MySpell's affix file, so make a copy
	for ext in dic aff; do
		cp ru_RU-lebedev$suffix.$ext ru_RU-lebedev$suffix.vim.$ext
	done

	# In order to build suggestions feature, vim mkspell requires
	# additional information in SOFOFROM and SOFOTO fields.
	# Next data was proposed and upstreamed by Alexey I. Froloff (raorn@)
	SOFOINFO="\
FOL абвгдеёжзийклмнопрстуфхцчшщьыъэюя\n\
LOW абвгдеёжзийклмнопрстуфхцчшщьыъэюя\n\
UPP АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ\n\
SOFOFROM абвгдеёжзийклмнопрстуфхцчшщьыъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ\n\
SOFOTO   ебвгдеежзейклннепрстефхцчшшье'еееЕБВГДЕЕЖЗЕЙКЛННЕПРСТЕФХЦЧШШЬЕ'ЕЕЕ\n\
"
	sed -i "0,/^$/s/^$/$SOFOINFO/" ru_RU-lebedev$suffix.vim.aff

	LANG="ru_RU.UTF-8" vim-console -E -X -N -n -i NONE -u NONE -U NONE \
		-c "mkspell! ru-lebedev$suffix ru_RU-lebedev$suffix.vim" -c q
}

FileSuffix()
{
	if [ -n "$1" ] ; then
		suffix="-$1"
	else
		suffix=""
	fi
}

BuildSpelling "ie"
BuildSpelling "io"
# Note: "combined" run must be last, it uses files from previous ones
BuildSpelling ""

# Now we have ie.list and io.list.
# We want to create a combined dictionary which will allow spellings
# either with 'io' or without it.

# For aspell we build three partial dictionaries and combine them
# with .multi files.
comm -12 ie.list io.list | ./sortkoi8 > ru-lebedev-common-only.list
comm -13 ie.list io.list | ./sortkoi8 > ru-lebedev-io-only.list
comm -23 ie.list io.list | ./sortkoi8 > ru-lebedev-ie-only.list
BuildAspellHash common
BuildAspellHash io
BuildAspellHash ie

MakeHunspell "ie"
MakeHunspell "io"
MakeHunspell ""

MakeVimspell "ie"
MakeVimspell "io"
MakeVimspell ""

%install
install -d %buildroot%ispelldir
install -d %buildroot%aspelldir
install -d %buildroot%_datadir/aspell
install -d %buildroot%myspelldir
install -d %buildroot%vim_spell_dir

# Install vimspell dictionary and suggestions files
for spelling in "" "-ie" "-io" ; do
	install -p -m 644 ru-lebedev$spelling.utf-8.{spl,sug} \
		%buildroot%vim_spell_dir
done
for s in spl sug; do
	ln -s ru-lebedev.utf-8.$s %buildroot%vim_spell_dir/ru.utf-8.$s
done

# Install myspell/hunspell dictionary and affix files
for spelling in "" "-ie" "-io" ; do
	install -p -m 644 ru_RU-lebedev$spelling.{aff,dic} \
		%buildroot%myspelldir
done

# Install ispell hash and affix files
for spelling in "" "-ie" "-io" ; do
	install -p -m 644 russian{,w}-lebedev$spelling.{aff,hash} \
		%buildroot%ispelldir
done

# install aspell

# aspell language data files
install -p -m 644 ru-lebedev.dat %buildroot%_datadir/aspell
install -p -m 644 ru-lebedev_phonet.dat %buildroot%_datadir/aspell

# aspell hash files
for i in common ie io ; do
	install -p -m 644 ru-lebedev-"$i"-only.rws \
		%buildroot%aspelldir
done

# aspell .multi and .alias files
for spelling in "" "-ie" "-io" ; do
	install -p -m 644 ru-lebedev$spelling.multi russian-lebedev$spelling.alias \
		%buildroot%aspelldir
done


# install alternatives
install -d %buildroot%_altdir

# ispell and  myspell/hunspell alternatives
for spelling in "" "-ie" "-io" ; do
	case "$spelling" in
		"-io"	) weight=40 ;;
		"-ie"	) weight=10 ;;
		*	) weight=50 ;;
	esac

	# ispell koi8-r
	cat > %buildroot%_altdir/%name$spelling << EOF
%ispelldir/russian.hash	%ispelldir/russian-lebedev$spelling.hash	$weight
%ispelldir/russian.aff	%ispelldir/russian-lebedev$spelling.aff	%ispelldir/russian-lebedev$spelling.hash
EOF

	# ispell cp1251
	cat > %buildroot%_altdir/%name$spelling-cp1251 << EOF
%ispelldir/russianw.hash	%ispelldir/russianw-lebedev$spelling.hash	$weight
%ispelldir/russianw.aff	%ispelldir/russianw-lebedev$spelling.aff	%ispelldir/russianw-lebedev$spelling.hash
EOF

	# myspell/hunspell
	cat > %buildroot%_altdir/hunspell-ru-lebedev$spelling << EOF
%myspelldir/ru_RU.dic	%myspelldir/ru_RU-lebedev$spelling.dic	$weight
%myspelldir/ru_RU.aff	%myspelldir/ru_RU-lebedev$spelling.aff	%myspelldir/ru_RU-lebedev$spelling.dic
%myspelldir/ru.dic	%myspelldir/ru_RU.dic	1000
%myspelldir/ru.aff	%myspelldir/ru_RU.aff	1000
EOF

done

# aspell alternatives
cat > %buildroot%_altdir/aspell-ru-lebedev << EOF
%aspelldir/ru.multi	%aspelldir/ru-lebedev.multi	50
%aspelldir/russian.alias	%aspelldir/russian-lebedev.alias	%aspelldir/ru-lebedev.multi
%aspelldir/ru.multi	%aspelldir/ru-lebedev-io.multi	40
%aspelldir/russian.alias	%aspelldir/russian-lebedev-io.alias	%aspelldir/ru-lebedev-io.multi
%aspelldir/ru.multi	%aspelldir/ru-lebedev-ie.multi	10
%aspelldir/russian.alias	%aspelldir/russian-lebedev-ie.alias	%aspelldir/ru-lebedev-ie.multi
EOF
cat > %buildroot%_altdir/aspell-ru-lebedev-dat << EOF
/usr/share/aspell/ru.dat	/usr/share/aspell/ru-lebedev.dat	50
/usr/share/aspell/ru_phonet.dat	/usr/share/aspell/ru-lebedev_phonet.dat	/usr/share/aspell/ru-lebedev.dat
EOF

mkdir -p %buildroot%_docdir/%name
install -pm644 LICENSE LICENSE.phonet README README.ru \
	%buildroot%_docdir/%name/
for d in aspell-ru-lebedev hunspell-ru-lebedev{,-i{e,o}} \
	vim-spell-ru-lebedev{,-i{e,o}}; do
	ln -s %name %buildroot%_docdir/$d
done


%files common
%dir %_docdir/%name
%_docdir/%name/LICENSE
%_docdir/%name/README
%_docdir/%name/README.ru

%files
%_altdir/%name
%ispelldir/russian-lebedev.*

%files cp1251
%_altdir/%name-cp1251
%ispelldir/russianw-lebedev.*

%files -n aspell-ru-lebedev
%dir %_docdir/%name
%_docdir/%name/LICENSE.phonet
%_docdir/aspell-ru-lebedev
%_altdir/aspell-ru-lebedev
%aspelldir/*
%_datadir/aspell/*
%_altdir/aspell-ru-lebedev-dat

%files -n hunspell-ru-lebedev
%_docdir/hunspell-ru-lebedev
%_altdir/hunspell-ru-lebedev
%myspelldir/ru_RU-lebedev.*

%files -n hunspell-ru-lebedev-ie
%_docdir/hunspell-ru-lebedev-ie
%_altdir/hunspell-ru-lebedev-ie
%myspelldir/ru_RU-lebedev-ie.*

%files -n hunspell-ru-lebedev-io
%_docdir/hunspell-ru-lebedev-io
%_altdir/hunspell-ru-lebedev-io
%myspelldir/ru_RU-lebedev-io.*

%files -n vim-spell-ru-lebedev
%_docdir/vim-spell-ru-lebedev
%vim_spell_dir/ru-lebedev.*
%vim_spell_dir/ru.*

%files -n vim-spell-ru-lebedev-ie
%_docdir/vim-spell-ru-lebedev-ie
%vim_spell_dir/ru-lebedev-ie.*

%files -n vim-spell-ru-lebedev-io
%_docdir/vim-spell-ru-lebedev-io
%vim_spell_dir/ru-lebedev-io.*

%files ie
%_altdir/%name-ie
%ispelldir/russian-lebedev-ie.*

%files ie-cp1251
%_altdir/%name-ie-cp1251
%ispelldir/russianw-lebedev-ie.*

%files io
%_altdir/%name-io
%ispelldir/russian-lebedev-io.*

%files io-cp1251
%_altdir/%name-io-cp1251
%ispelldir/russianw-lebedev-io.*


%changelog
* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.99g5-alt14
- added alternatives for %_datadir/aspell/ru.dat(+_phonetic)
- (closes: #36827)

* Wed Jan 16 2019 Dmitry V. Levin <ldv@altlinux.org> 0.99g5-alt13
- Added an auxiliary subpackage for better intersubpackage dependencies.
- vim-spell-ru-lebedev: turned into a full replacement of vim-spell-ru.
- Removed redundant PreReqs on alternatives.
- Fixed license tags.

* Sat Jul 20 2013 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt12.1
- fix alternatives issue (ALT #28364)

* Thu Jul 18 2013 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt12
- a few more words
- hunspell-ru-lebedev obsoletes hunspell-ru
- hunspell: ru-alternative in addition to ru_RU-alternative (closes: #28364)

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.99g5-alt11.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-rpm-group-should-be-text-tools for aspell-ru-lebedev
  * altlinux-policy-rpm-group-should-be-text-tools for hunspell-ru-lebedev-ie
  * altlinux-policy-rpm-group-should-be-text-tools for hunspell-ru-lebedev-io
  * altlinux-policy-rpm-group-should-be-text-tools for hunspell-ru-lebedev
  * altlinux-policy-rpm-group-should-be-text-tools for ispell-ru-lebedev
  * altlinux-policy-rpm-group-should-be-text-tools for ispell-ru-lebedev-io-cp1251
  * altlinux-policy-rpm-group-should-be-text-tools for ispell-ru-lebedev-ie
  * altlinux-policy-rpm-group-should-be-text-tools for ispell-ru-lebedev-cp1251
  * altlinux-policy-rpm-group-should-be-text-tools for ispell-ru-lebedev-io
  * altlinux-policy-rpm-group-should-be-text-tools for ispell-ru-lebedev-ie-cp1251

* Sun Feb 26 2012 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt11
- a few more words

* Fri Jan  7 2011 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt10
- build vimspell dictionaries from the same source. New subpackages:
  + vim-spell-ru-lebedev
  + vim-spell-ru-lebedev-io
  + vim-spell-ru-lebedev-ie
- descriptions corrected to satisfy the license term: "Modified versions
  must be clearly marked as such". Byelorussian descriptions removed
  from specfile, sorry...
- a few more words

* Tue Jun  1 2010 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt9
- a few more words

* Fri Feb 26 2010 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt8
- myspell/hunspell: fixed affix rules with cutted suffixes
  (rebuild with fixed i2myspell convertor)
- myspelldir and aspelldir macros in spec
- a few more words

* Wed Feb 24 2010 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt7
- myspell alternatives grouped back, slave-master conflict was settled
- a few more words

* Wed Feb 24 2010 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt6
- myspell alternatives ungouped to avoid slave-master conflict
  with other myspell dictionaries in repository
- a few more words

* Tue Feb 23 2010 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt5
- build dictionaries in myspell/hunspell format too
- a few more words
- alternatives weights slightly changed
- spec cleanup

* Fri Feb 19 2010 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt4
- corrected the build of combined hashes for ispell
- a few more words

* Tue Jan 12 2010 Sergey Kurakin <kurakin@altlinux.org> 0.99g5-alt3
- added extra dictionary addition.koi

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.99g5-alt2
- support for alternatives 0.4

* Tue Sep 09 2008 Igor Vlasenko <viy@altlinux.ru> 0.99g5-alt1
- new version 0.99g5.

* Wed Mar 28 2007 Sergey Vlasov <vsu@altlinux.ru> 0.99g4-alt1
- Version 0.99g4.

* Wed Oct 11 2006 Sergey Vlasov <vsu@altlinux.ru> 0.99g3-alt2
- Fix %%_libdir paths in alternative definitions on x86_64 (#10110).
- Switch to uncompressed original tarballs in src.rpm.

* Tue Jun 27 2006 Sergey Vlasov <vsu@altlinux.ru> 0.99g3-alt1
- Version 0.99g3.
- Removed all %%__* macro abuse from spec.

* Sat Jan 28 2006 Sergey Vlasov <vsu@altlinux.ru> 0.99g1-alt1
- Version 0.99g1.
- Added alt-no-substandard-language patch: remove words which
  should not be present in a dictionary used for spellchecking (#8531).

* Sun Jun 12 2005 Sergey Vlasov <vsu@altlinux.ru> 0.99f9-alt1
- Version 0.99f9.
- Converted alternatives config files to new format (0.2.0).
- Updated BuildRequires.

* Thu Jul 29 2004 Sergey Vlasov <vsu@altlinux.ru> 0.99f7-alt1
- Version 0.99f7.
- Fixed aspell version dependencies.

* Thu Jul 29 2004 Vital Khilko <vk@altlinux.ru> 0.99f6-alt2
- NMU to fix #4441 and rebuild for new aspell-0.60
- fixed package descriptions
- added belarusian translation of descriptions

* Sun Nov 23 2003 Sergey Vlasov <vsu@altlinux.ru> 0.99f6-alt1
- Version 0.99f6.
- Updated for new aspell (no more pspell, different dictionary names).
- Updated BuildRequires.
- Spec file cleanup.
- Added Russian descriptions.
- Always build the aspell dictionary (no more --without aspell).

* Tue May 06 2003 Stanislav Ievlev <inger@altlinux.ru> 0.99f2-alt1.1
- move to new alternatives scheme

* Fri Oct 18 2002 Sergey Vlasov <vsu@altlinux.ru> 0.99f2-alt1
- Version 0.99f2.
- Updated URLs.

* Tue Apr 02 2002 Sergey Vlasov <vsu@altlinux.ru> 0.99e9-alt1
- Version 0.99e9.
- Added aspell phonetic rules file from Andrey Grozin.
- Combined all aspell dictionaries into one package.
- Fixed bugs in %%preun scripts (alternatives were lost
  after upgrading).
- Lots of %%triggerpostun to clean up after my %%preun bugs
  in the previous version :-(

* Sun Dec 02 2001 Sergey Vlasov <vsu@altlinux.ru> 0.99e5-alt1
- First spec
