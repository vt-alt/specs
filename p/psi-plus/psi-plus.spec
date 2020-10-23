%define _unpackaged_files_terminate_build 1

%def_disable webkit

Name: psi-plus
Version: 1.4.1513
Release: alt1

Summary: Psi+ Jabber client
Summary(ru_RU.UTF-8): Jabber-клиент Psi+
License: GPLv2
Group: Networking/Instant messaging

Url: https://www.psi-plus.com/

# https://github.com/psi-plus/psi-plus-snapshots/archive/%version.tar.gz
Source: %name-snapshots-%version.tar

Patch1: %name-disable-sm-alt.patch
Patch2: %name-doubleclick-alt.patch
Patch3: %name-events-alt.patch
Patch4: %name-disable-omemo-alt.patch

Requires: qt5-translations
Requires: qca-qt5-ossl
Requires: qca-qt5-gnupg

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glibc-devel-static
BuildRequires: libXScrnSaver-devel
BuildRequires: libaspell-devel
BuildRequires: libidn-devel
BuildRequires: libhunspell-devel
BuildRequires: libqca-qt5-devel
BuildRequires: libtidy-devel >= 1.2.0
BuildRequires: libotr-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-phonon-devel
BuildRequires: qt5-svg-devel
%if_enabled webkit
BuildRequires: libqt5-webkit qt5-webkit-devel
%else
BuildRequires: qt5-webengine-devel
%endif
BuildRequires: qt5-x11extras-devel
BuildRequires: zlib-devel
BuildRequires: libminizip-devel

%description
Psi is a Jabber Instant Messaging client based on Qt.  Jabber supports
gateways (transports) to other IM systems, such as ICQ, MSN, Yahoo and
AIM.  Psi supports many Jabber features, such as simulatenous login to
several servers, conferences, cryptographic abilities (via SSL and
GnuPG), connection via HTTP(S) proxy, etc.

%description -l ru_RU.UTF-8
Psi - это удобный графический клиент сети быстрого обмена сообщениями
Jabber.  Jabber имеет шлюзы в другие сети, включая ICQ, MSN, Yahoo и
AIM.  Psi поддерживает такие возможности Jabber, как одновременная
работа с несколькими серверами, конференции, криптозащиту передаваемой
информации (через SSL и GnuPG), работу через HTTP(S) прокси-сервер и
т.д.

# Attention plugin
%package plugin-attention
Summary: Attention support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-attention
This plugin is designed to send and receive special messages such as Attentions.
To work correctly, the plugin requires that the client of the other party supports XEP-0224 (for example: Pidgin, Miranda IM with Nudge plugin).

%description plugin-attention -l ru_RU.UTF-8
Данный плагин предназначен для отправки и приёма сообщений типа Attention.
Для работы необходимо, чтобы клиент собеседника поддерживал XEP-0224 (например: Pidgin, Miranda IM с плагином Nudge).

# Autoreply plugin
%package plugin-autoreply
Summary: Autoreply support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-autoreply
This plugin acts as an auto-answering machine. It has a number of simple configuration options, which you can use to:

 - set a text message for auto-answer
 - exclude specified jids, including conferences, from the objects for auto-answer (if a jid conference is set, the exception will include all private messages)
 - disable the auto-responder for some of your accounts
 - set the number of sent auto messages
 - set the time interval after which the number of auto messages counter will be reset
 - disable the auto-responder for the active tab
 - disable the auto-responder for contacts that are not in your roster

The list of exceptions for jids has two operating modes:

 - auto-responder is _switched off_ for the list of exceptions, for the others is _switched on_ (Disable mode)
 - auto-responder is _switched on_ for the list of exceptions, for the others is _switched off_ (Enable mode)

%description plugin-autoreply -l ru_RU.UTF-8
Данный плагин выполняет роль автоответчика. Имеет ряд несложных настроек, с помощью которых можно:

 - задать текст сообщения для автоответа
 - исключить определённые jid'ы, включая конференции, из объектов для автоответа (если задан jid конференции, то в исключения попадают все приватные сообщения)
 - отключить автоответчик для некоторых ваших аккаунтов
 - задать количество посылок автоответа
 - задать интервал времени, по истечении которого счётчик количества автоответов будет обнулён
 - отключить автоответчик для активной вкладки/таба
 - отключить автоответчик для контактов не из вашего ростера

Список исключений для jid'ов имеет два режима работы:

 - автоответчик выключен для списка исключений, для остальных - включён (Disable mode)
 - автоответчик включён для списка исключений, для остальных - выключен (Enable mode)

# Birthday reminder plugin
%package plugin-birthdayreminder
Summary: Birthdayreminder support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-birthdayreminder
This plugin is designed to show reminders of upcoming birthdays.
The first time you install this plugin, you need to log on to all of your accounts, go to the plugin settings and click "Update Birthdays". The plugin will then collect the information about the birthdays of all the users in your roster, but when the 'Use vCards cache' option is selected, the users' vCards that are cached on your hard disk will be used.

%description plugin-birthdayreminder -l ru_RU.UTF-8
Данный плагин предназначен для напоминаний о приближающихся днях рождения.
Если плагин установлен впервые, то необходимо выйти всеми своими аккаунтами в «онлайн», затем зайти в настройки плагина и нажать кнопку Update Birthdays. В результате будет собрана доступная информация о днях рождения пользователей из всех аккаунтов ростера, а если выбрать соответствующую опцию, то и информация о пользователях, vCard'ы которых находятся в кэше на локальном диске.

# Chess plugin
%package plugin-chess
Summary: Chess forms support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-chess
This plugin allows you to play chess with your friends.
The plugin is compatible with a similar plugin for Tkabber.
For sending commands, normal messages are used, so this plugin will always work wherever you are able to log in.
To invite a friend for a game, you can use contact menu item or the button on the toolbar in a chat window.

%description plugin-chess -l ru_RU.UTF-8
Данный плагин позволяет играть в шахматы с пользователями из ростера.
Плагин совместим с аналогичным плагином в jabber-клиенте Tkabber.
Для передачи команд используются обычные сообщения, поэтому плагин будет работать везде, где у Вас есть возможность выйти в «онлайн».
Чтобы пригласить друга в игру, можно воспользоваться пунктом меню контакта или кнопкой на тулбаре в окне чата.

# Cleaner plugin
%package plugin-cleaner
Summary: Cleaner support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-cleaner
This plugin is designed to clear the avatar cache, saved local copies of vCards and history logs.
You can preview items before deleting them from your hard drive.

%description plugin-cleaner -l ru_RU.UTF-8
Данный плагин предназначен для очистки кэша аватар, сохранённых локальных копий vCard, а также логов истории переписки.
Имеется возможность предварительного просмотра элементов перед их удалением с локального диска.

# Client switcher plugin
%package plugin-clientswitcher
Summary: Client switcher support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-clientswitcher
This plugin is intended to spoof version of the Jabber client, the name and type of operating system. It is possible to manually specify the version of the client and the operating system or choose from a predefined list.
Note: It is recommended to use the plugin only when really necessary. Keep in mind that the substitution of the name and version of the client may have a negative impact on support in their respective conferences.

%description plugin-clientswitcher -l ru_RU.UTF-8
Данный плагин предназначен для подмены версии Jabber-клиента, его названия и типа операционной системы. Имеется возможность вручную указать версию клиента и операционной системы или выбрать их из заданного списка.
Примечание: Рекомендуется использовать плагин только в случае реальной необходимости. Следует помнить, что подмена имени и версии клиента может негативно сказаться на поддержке в соответствующих конференциях.

# Conference logger plugin
%package plugin-conferencelogger
Summary: Conference logger support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-conferencelogger
This plugin is designed to save conference logs in which the Psi+ user sits.
Conferences logs can be viewed from the plugin settings or by clicking on the appropriate button on the toolbar in the active window/tab with conference.
Note: To work correctly, the option options.ui.chat.central-toolbar must be set to true.

%description plugin-conferencelogger -l ru_RU.UTF-8
Данный плагин предназначен для записи (сохранения) логов конференций, в которых находится пользователь Psi+.
Логи конференций можно просмотреть из настроек плагина, либо нажав соответствующую кнопку на тулбаре в активном окне/табе конференции.
Примечание: Для корректной работы опция options.ui.chat.central-toolbar должна быть установлена в положение true.

# Content downloader plugin
%package plugin-contentdownloader
Summary: Content downloader support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-contentdownloader
This plugin is designed to make it easy to download and install iconsets and other resources for Psi+.
This plugin can currently be used to download and install roster iconsets and emoticons.

%description plugin-contentdownloader -l ru_RU.UTF-8
Данный плагин предназначен для скачивания из Интернет наборов иконок и прочих дополнительных ресурсов для Psi+.
Примечание: В настоящее время плагин умеет скачивать и устанавливать наборы иконок для ростера и смайлпаки.

# Enum messages plugin
%package plugin-enummessages
Summary: Enum messages support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-enummessages
The plugin is designed to enumerate messages, adding the messages numbers in chat logs and notification of missed messages. 
Supports per contact on / off message enumeration via the buttons on the chats toolbar.

%description plugin-enummessages -l ru_RU.UTF-8
Данный плагин предназначен для перечисления сообщений, добавление номера сообщения в журналах чата и уведомления о пропущенных сообщениях.
Поддерживается вкл / выкл перечисления сообщений для каждого контакта по отдельности с помощью кнопок на панели инструментов чата.

# Extended menu
%package plugin-extendedmenu
Summary: Extended menu support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-extendedmenu
This plugin adds roster submenu 'Extended Actions' to contact's context menu. At the moment we have the following items: 'Copy JID', 'Copy the nickname', 'Copy the status message' and 'Ping'.

%description plugin-extendedmenu -l ru_RU.UTF-8
Данный плагин добавляет в контекстное меню контакта ростера подменю «Extended Actions». На данный момент имеются следующие пункты: «Скопировать JID», «Скопировать ник», «Скопировать статусное сообщение» и «Ping».

# Extended options
%package plugin-extendedoptions
Summary: Extended options support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-extendedoptions
This plugin is designed to allow easy configuration of some advanced options in Psi+.
This plugin gives you access to advanced application options, which do not have a graphical user interface.
Importantly: A large part of the options are important system settings. These require extra attention and proper understanding of the results when changing the option.

%description plugin-extendedoptions -l ru_RU.UTF-8
Данный плагин предназначен для более удобной настройки дополнительных параметров Psi+.
Плагин предоставляет доступ к дополнительным настройкам приложения, которые не имеют своего графического интерфейса.
Важно: бОльшая часть настроек имеет системный характер и требует внимания и понимания смысла изменяемых функций.

# GnuPG plugin
%package plugin-gnupg
Summary: GnuPG support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-gnupg
GnuPG support for %name

# Gomoku game plugin
%package plugin-gomokugame
Summary: Gomoku game support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-gomokugame
Gomoku game support plugin for %name

%description plugin-gomokugame -l ru_RU.UTF-8
Данный плагин позволяет играть с контактами ростера и конференции в игру Гомоку. Реализована разновидность правил «Международное гомоку».
Для передачи команд используются обычные сообщения, поэтому плагин будет работать везде, где есть возможность выйти в онлайн.

# History keeper plugin
%package plugin-historykeeper
Summary: History keeper support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-historykeeper
This plugin is designed to remove the history of selected contacts when the Psi+ is closed.
You can select or deselect a contact for history removal from the context menu of a contact or via the plugin options.

%description plugin-historykeeper -l ru_RU.UTF-8
Данный плагин предназначен для удаления истории переписки с отмеченными контактами при выходе из Psi+.
Отметить контакт или удалить отметку можно из контекстного меню контакта, либо через окно с настройками плагина.

# Image plugin
%package plugin-image
Summary: Image support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-image
This plugin is designed to send images to roster contacts.
Your contact's client must be support XEP-0071: XHTML-IM and support the data:URI scheme.
Note: To work correctly, the option options.ui.chat.central-toolbar must be set to true.

%description plugin-image -l ru_RU.UTF-8
Данный плагин предназначен для отправки собеседнику графического изображения.
Клиент собеседника должен поддерживать XEP-0071: XHTML-IM и поддерживать схему data:URI.
Примечание: Для корректной работы плагина опция options.ui.chat.central-toolbar должна быть установлена в положение true.

# Image preview plugin
%package plugin-imagepreview
Summary: Image preview support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-imagepreview
This plugin shows the preview image for an image URL.

%description plugin-imagepreview -l ru_RU.UTF-8
Этот плагин показывает превью изображений по URL ссылкам.

# Jabber disk plugin
%package plugin-jabberdisk
Summary: Jabber disk support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-jabberdisk
Jabber disk support plugin for %name

%description plugin-jabberdisk -l ru_RU.UTF-8
Данный плагин предназначен для комфортной работы с файловыми хранилищами Jabber Disk.
Реализовано через соответствующую команду в контекстном меню контакта ростера.
Работа с файлами представлена в виде графического интерфейса.
Добавлять/удалять/редактировать глобальные настройки плагина можно на вкладке Plugins в настройках приложения.

# Juick plugin
%package plugin-juick
Summary: Juick support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-juick
This plugin is designed to work efficiently and comfortably with the Juick microblogging service.
Currently, the plugin is able to:

 - Coloring @nick, *tag and #message_id in messages from the juick@juick.com bot
 - Detect >quotes in messages
 - Enable clickable @nick, *tag, #message_id and other control elements to insert them into the typing area
 - Note: To work correctly, the option options.html.chat.render must be set to true.

%description plugin-juick -l ru_RU.UTF-8
Плагин предназначен для эффективной и комфортной работы с сервисом микроблогов Juick.
На данный момент плагин умеет:

 - Раскрашивать @ники, *тэги, #id_сообщений в сообщениях от бота juick@juick.com
 - Распознавать >цитаты в сообщениях
 - Кликабельные @ники, *тэги, #id_сообщений и другие управляющие элементы для подстановки их в строку ввода
 - Примечание: Для корректной работы плагина опция options.html.chat.render («Использовать формат текста отправителя») должна быть установлена в положение true.

# Message filter plugin
%package plugin-messagefilter
Summary: Message filter support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-messagefilter
Placeholder

%description plugin-messagefilter -l ru_RU.UTF-8
Placeholder

# PEP change notify plugin
%package plugin-pepchangenotify
Summary: PEP change notify support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-pepchangenotify
The plugin is designed to display popup notifications on change of moods, activities and tunes at the contacts of the roster. In the settings you can choose which ones to include notification of events, specify the time within which a notice will appear, as well as play a sound specify.

%description plugin-pepchangenotify -l ru_RU.UTF-8
Плагин предназначен для показа всплывающих уведомлений о смене настроений, занятий и мелодий у контактов из ростера. В настройках можно выбрать для каких именно событий включены уведомления, задать время, в течение которого уведомление будет показываться, а также указать проигрываемый звук.

# OTR plugin
%package plugin-otr
Summary: Off-the-Record Messaging plugin for Psi+
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-otr
Off-the-Record (OTR) Messaging allows you to have private conversations over instant messaging by providing:
Encryption
No one else can read your instant messages.
Authentication
You are assured the correspondent is who you think it is.
Deniability
The messages you send do not have digital signatures that are checkable by a third party. Anyone can forge messages after a conversation to make them look like they came from you. However, during a conversation, your correspondent is assured the messages he sees are authentic and unmodified.
Perfect forward secrecy
If you lose control of your private keys, no previous conversation is compromised.

# QIP X-Statuses plugin
%package plugin-qipxstatuses
Summary: QIP X-Statuses support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-qipxstatuses
This plugin is designed to display X-statuses of contacts using the QIP Infium jabber client.

%description plugin-qipxstatuses -l ru_RU.UTF-8
Данный плагин предназначен для отображения х-статусов контактов, использующих в качестве jabber-клиента QIP Infium.

# Redirector plugin
%package plugin-redirector
Summary: Redirect support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-redirector
Redirect support for %name

# Screenshot plugin
%package plugin-screenshot
Summary: Screenshot support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-screenshot
This plugin allows you to make a snapshot (screenshot) of the screen, edit the visible aria to make a screenshot and save the image to a local drive or upload to HTTP/FTP server.
The plugin has the following settings:

 - Shortcut - Hotkey to call the plugin (Ctrl + Alt + P by default)
 - Format - type of image file, which will save a snapshot of the screen (png by default)
 - File Name - format of the filename (default: pic-yyyyMMdd-hhmmss, where yyyyMMdd=YYYYMMDD, and hhmmss are current date in the format yearmonthday-hourminutesecond; for example, pic-20100711-135132.png)

The address of FTP server is specified as ftp://ftp.domain.tld/path1/path2.

%description plugin-screenshot -l ru_RU.UTF-8
Данный плагин позволяет делать снимок (скриншот) экрана, редактировать видимую область на сделанном скриншоте и сохранять снимок на локальный диск или загружать на HTTP/FTP-сервер.
Плагин имеет следующие настройки:

 - Shortcut - горячая клавиша для вызова плагина (по умолчанию, Ctrl+Alt+P)
 - Format - тип графического файла, в котором будет сохранён снимок экрана (по умолчанию, png)
 - File Name - формат имени графического файла (по умолчанию, pic-yyyyMMdd-hhmmss, где yyyyMMdd=ГГГГММДД, hhmmss=ччммсс - текущая дата в формате годмесяцдень-часминутасекунда; например, pic-20100711-135132.png)

Адрес FTP-сервера задаётся в виде ftp://ftp.domain.tld/path1/path2.
Примечание: Для работы со скриншотами также можно использовать отдельное (самостоятельное) приложение qScreenshot. Доступно на различных платформах (в т.ч. и под MS Windows).

# Stop spam plugin
%package plugin-stopspam
Summary: Stop spam support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-stopspam
This plugin is designed to block spam messages and other unwanted information from Psi+ users.
The functionality of the plugin is based on the principle of "question - answer".
With the plugin settings you can:

 - Define a security question and the answer
 - Define the set of rules that define whether to the trigger plugin for a contact
 - Define the text messages sent in the case of the correct answer
 - Enable notification through popups
 - Enable the saving of blocked messages in the history of the contact
 - Define the number of subject parcels
 - Set the time interval after which to reset the number of how many questions will be sent
 - Enable blocking of private messages in conferences
 - Choose for which ranks and roles of conference participants blocking messages will be disabled
 - Enable deadlocks in private messages to participants who do not fall into the exceptions list for the roles and ranks which include blocking.

The rules are checked from top to bottom. If the rule is Enabled - stopspam is triggered, otherwise - stopspam is not triggered. In the case where none of the rules triggered stopspam for roster messages, you can specify whether the plugin will activate or not. For private messages from the same conference, it will always work.
Question and answer as well as a list of rules is common for ordinary messages and for private messages in conferences.
When a user has passed, the test will send a re-authorization request. It should be noted in the messages that are sent back the security question was correctly answered.
The plugin keeps a log of blocked messages, which you can view through the plugin settings.
The Reset button deletes the log and resets the counter of blocked messages.
WARNING!!! Before registering a new transport, it is recommended to add its jid to transport exceptions. This is due to the fact that after the transport registration, authorization requests for all contacts will be sent and if the transport was not added to as an exception, the plugin will block all the requests.

%description plugin-stopspam -l ru_RU.UTF-8
Данный плагин предназначен для блокировки получения в ростер пользователя Psi+ рассылок спама и другой нежелательной информации.
Функционал плагина основан на принципе «вопрос - ответ».
С помощью настроек плагина можно:

 - Ввести контрольный вопрос и ответ на него
 - Задать набор правил, определяющих, будет ли срабатывать плагин для данного контакта
 - Задать текст сообщения, посылаемого в случае правильного ответа
 - Включить уведомления при помощи всплывающих окон
 - включить сохранение заблокированных сообщений в истории контакта
 - Задать количество посылок вопроса
 - Задать интервал времени, по истечении которого счетчик количества отправленных вопросов будет обнулён
 - Включить блокировку приватных сообщений в конференциях
 - Выбрать для каких рангов и ролей участников конференции блокировка сообщений будет отключена
 - Включить полную блокировку приватных сообщений для участников конференции, которые не попадают в список исключений и для ролей и рангов которых включена блокировка.

Правила проверяются сверху вниз. Если напротив правила стоит галочка Enabled, то стоп-спам сработает, в противном случае - не сработает.
В случае когда ни одно из правил не сработало, для сообщений из ростера можно задать, сработает ли плагин или нет. Для приватных сообщений из конференций - всегда сработает.
Контрольный вопрос и ответ, а также список правил является общим, как для обычных сообщений, так и для приватных сообщений в конференциях.
Также пользователю, успешно прошедшему тест, придётся заново запрашивать авторизацию. Это стОит отметить в сообщении, отсылаемом в случае правильного ответа на контрольный вопрос.
Плагин ведёт лог заблокированных сообщений, который можно просмотреть командой View log.
Команда Reset позволяет удалить этот лог и сбросить счётчик заблокированных сообщений.
ВНИМАНИЕ!!! Перед регистрацией на новом транспорте рекомендуется добавить JID транспорта в исключения. Это связано с тем, что после регистрации транспорт запрашивает авторизацию для всех контактов и если его не добавить в исключения, то плагин заблокирует все запросы.

# Storage notes plugin
%package plugin-storagenotes
Summary: Storage notes support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-storagenotes
This plugin is an implementation of XEP-0049: Private XML Storage.
The plugin is fully compatible with notes saved using Miranda IM.
The plugin is designed to keep notes on the jabber server with the ability to access them from anywhere using Psi+ or Miranda IM.

%description plugin-storagenotes -l ru_RU.UTF-8
Данный плагин представляет собой реализацию XEP-0049: Private XML Storage.
Плагин полностью совместим с заметками, сохранёнными из клиента Miranda IM.
Плагин предназначен для хранения заметок на jabber-сервере с возможностью доступа к ним из любого места через клиент Psi+ или Miranda IM.

# Translate plugin
%package plugin-translate
Summary: Translation support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-translate
This plugin allows you to convert selected text into another language.

%description plugin-translate -l ru_RU.UTF-8
Данный плагин позволяет конвертировать выделенный текст в другую языковую раскладку.

# Video status plugin
%package plugin-videostatus
Summary: Video status support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-videostatus
This plugin is designed to set the custom status when you see the video in selected video player.
Communication with players made by D-Bus.
Note: This plugin is designed to work in Linux family operating systems ONLY.

 - To work with Totem player you need to enable appropriate plugin in this player (Edit\Plugins\D-Bus)
 - To work with VLC player you need to enable the option "Control Interface D-Bus" in the Advanced Settings tab on "Interface\Control Interface" section of the player settings
 - To work with Kaffeine player you must have player version (>= 1.0), additional configuration is not needed
 - To work with GNOME MPlayer additional configuration is not needed

%description plugin-videostatus -l ru_RU.UTF-8
Плагин предназначен для установки заданного статуса во время просмотра видео в указанном видеопроигрывателе.
Связь с проигрывателями осуществляется посредством D-Bus.
Важно: Работа с видеопроигрывателями осуществляется ТОЛЬКО в операционных системах семейства Linux/BSD. В MS Windows реализовано ТОЛЬКО определение полноэкранного режима работы другого приложения на машине пользователя.

 - Для работы с Totem необходимо в самом проигрывателе включить соответствующий плагин (Правка\Модули\Служба D-Bus);
 - Для работы с VLC необходимо в расширенных настройках проигрывателя на вкладке «Интерфейс\Интерфейсы управления» включить опцию «Интерфейс управления D-Bus»;
 - Для работы с Kaffeine необходимо иметь плеер версии (>=1.0), дополнительных настроек не нужно;
 - Для работы с GNOME MPlayer дополнительных настроек не нужно.

# Watcher plugin
%package plugin-watcher
Summary: Watcher support for %name
Group: Networking/Instant messaging
Requires: %name = %EVR

%description plugin-watcher
This plugin is designed to monitor the status of specific roster contacts, as well as for substitution of standard sounds of incoming messages.
On the first tab set up a list of contacts for the status of which is monitored. When the status of such contacts changes a popup window will be shown and when the status changes to online a custom sound can be played.
On the second tab is configured list of items, the messages are being monitored.
Each element can contain a regular expression to check for matches with JID, from which the message arrives, a list of regular expressions to check for matches with the text of an incoming message, the path to sound file which will be played in case of coincidence, as well as the setting, whether the sound is played always, even if the global sounds off.

%description plugin-watcher -l ru_RU.UTF-8
Данный плагин предназначен для наблюдения за статусом определённых пользователей в ростере, а также для подмены стандартных звуковых событий входящих сообщений.
На первой вкладке настраивается список контактов, за статусом которых осуществляется наблюдение. При смене статуса таких контактов будет показываться всплывающее окно, а при смене статуса на «онлайн» - ещё и проигрываться указанный звук.
На второй вкладке настраивается список элементов, за сообщениями которых ведётся наблюдение.
Каждый элемент может содержать:

 - Регулярное выражение для проверки на совпадение с JID, от которого приходит сообщение;
 - Список регулярных выражений для проверки на совпадение с текстом входящего сообщения;
 - Путь к звуковому файлу, который будет проигран в случае совпадения;
 - Настройку для воспроизведения звукового файла всегда, даже если глобальные звуки выключены.

%prep
%setup -n %name-snapshots-%version
#%patch1 -p2
%patch2 -p1
%patch3 -p2
%patch4 -p2

rm -rf src/libpsi/tools/zip/minizip

%build
for plugin in \
	plugins/dev/redirectorplugin ; do

	pushd $plugin
	%qmake_qt5 $(basename $plugin).pro
	%make_build
	popd
done

%cmake \
    -DBUILD_PLUGINS="ALL" \
    -DENABLE_PLUGINS=ON \
    -DBUILD_DEV_PLUGINS=ON
%cmake_build

%install
%cmakeinstall_std

# Generic plugins
pushd plugins/dev
install -pDm644 redirectorplugin/libredirectplugin.so %buildroot%_libdir/%name/plugins
popd

rm %buildroot%_datadir/%name/{COPYING,README.html}
rm %buildroot%_libdir/%name/plugins/lib{battleshipgame,openpgp}plugin.so

%files
%doc COPYING INSTALL README.html TODO
%_bindir/%name
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_desktopdir/%name.desktop
%dir %_datadir/%name
%_datadir/%name/client_icons.txt
%_datadir/%name/certs
%_datadir/%name/iconsets
%_datadir/%name/sound
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/apps/*.png
%_datadir/metainfo/%name.appdata.xml

# Attention plugin
%files plugin-attention
%_libdir/%name/plugins/libattentionplugin.so

# Autoreply plugin
%files plugin-autoreply
%_libdir/%name/plugins/libautoreplyplugin.so

# Birthday reminder plugin
%files plugin-birthdayreminder
%_libdir/%name/plugins/libbirthdayreminderplugin.so

# Chess plugin
%files plugin-chess
%_libdir/%name/plugins/libchessplugin.so

# Cleaner plugin
%files plugin-cleaner
%_libdir/%name/plugins/libcleanerplugin.so

# Client switcher plugin
%files plugin-clientswitcher
%_libdir/%name/plugins/libclientswitcherplugin.so

# Conference logger plugin
%files plugin-conferencelogger
%_libdir/%name/plugins/libconferenceloggerplugin.so

# Content downloader plugin
%files plugin-contentdownloader
%_libdir/%name/plugins/libcontentdownloaderplugin.so

# Enum messages plugin
%files plugin-enummessages
%_libdir/%name/plugins/libenummessagesplugin.so

# Extended menu plugin
%files plugin-extendedmenu
%_libdir/%name/plugins/libextendedmenuplugin.so

# Extended options plugin
%files plugin-extendedoptions
%_libdir/%name/plugins/libextendedoptionsplugin.so

# Gomoku game plugin
%files plugin-gomokugame
%_libdir/%name/plugins/libgomokugameplugin.so

# History keeper plugin
%files plugin-historykeeper
%_libdir/%name/plugins/libhistorykeeperplugin.so

# Image plugin
%files plugin-image
%_libdir/%name/plugins/libimageplugin.so

# Image preview plugin
%files plugin-imagepreview
%_libdir/%name/plugins/libimagepreviewplugin.so

# Jabber disk plugin
%files plugin-jabberdisk
%_libdir/%name/plugins/libjabberdiskplugin.so

# Juick plugin
%files plugin-juick
%_libdir/%name/plugins/libjuickplugin.so

# Message filter plugin
%files plugin-messagefilter
%_libdir/%name/plugins/libmessagefilterplugin.so

# OTR plugin
%files plugin-otr
%_libdir/%name/plugins/libotrplugin.so

# PEP change notify plugin
%files plugin-pepchangenotify
%_libdir/%name/plugins/libpepchangenotifyplugin.so

# QIP X-Statuses plugin
%files plugin-qipxstatuses
%_libdir/%name/plugins/libqipxstatusesplugin.so

# Redirector plugin
%files plugin-redirector
%_libdir/%name/plugins/libredirectplugin.so

# Screenshot plugin
%files plugin-screenshot
%_libdir/%name/plugins/libscreenshotplugin.so

# Stopspam plugin
%files plugin-stopspam
%_libdir/%name/plugins/libstopspamplugin.so

# Storagenotes plugin
%files plugin-storagenotes
%_libdir/%name/plugins/libstoragenotesplugin.so

# Translate plugin
%files plugin-translate
%_libdir/%name/plugins/libtranslateplugin.so

# Video status plugin
%files plugin-videostatus
%_libdir/%name/plugins/libvideostatusplugin.so

# Watcher plugin
%files plugin-watcher
%_libdir/%name/plugins/libwatcherplugin.so

%changelog
* Fri Oct 02 2020 Oleg Solovyov <mcpain@altlinux.org> 1.4.1513-alt1
- Version 1.4.1513

* Wed Oct 16 2019 Oleg Solovyov <mcpain@altlinux.org> 1.4.912-alt1
- Version 1.4.912
- disabled QtWebKit (Closes: #37381)

* Tue Oct 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.109-alt2
- NMU: rebuilt for debuginfo.
- Fixed main window blanking issue which appears on closing main window in a specific way.
- Cleaned up spec.

* Tue Dec 05 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.109-alt1
- Version 1.2.109

* Fri Nov 17 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.105-alt4
- fix e2k build
- fix unowned files

* Mon Nov 13 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.105-alt3
- add OTR plugin (Closes: #32384)

* Thu Nov 09 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.105-alt2
- clean unpackaged files
- cleanup

* Mon Oct 30 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.105-alt1
- Version 1.2.105

* Tue Oct 17 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.100-alt1
- Version 1.2.100

* Mon Sep 25 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.80-alt1
- Version 1.2.80 

* Mon Sep 11 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.71-alt1
- Version 1.2.71

* Fri Sep 08 2017 Michael Shigorin <mike@altlinux.org> 1.2.40-alt2
- introduced webkit knob (on by default)
- minor spec cleanup

* Tue Aug 29 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.40-alt1
- Version 1.2.40

* Fri Aug 17 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.32-alt4
- fix doubleclick patch

* Wed Aug 16 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.32-alt3
- fix tray

* Tue Aug 15 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.32-alt2
- fix doubleclick

* Mon Aug 09 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.32-alt1
- Version 1.2.32

* Mon Aug 07 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.30-alt1
- Version 1.2.30

* Thu Aug 03 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.27-alt1
- Version 1.2.27

* Mon Jul 31 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.20-alt1
- Version 1.2.20

* Fri Jul 28 2017 Oleg Solovyov <mcpain@altlinux.org> 1.2.15-alt1
- Version 1.2.15

* Tue Jul 25 2017 Oleg Solovyov <mcpain@altlinux.org> 1.1.28-alt1
- Version 1.1.28

* Mon Jul 24 2017 Oleg Solovyov <mcpain@altlinux.org> 1.1.23-alt2
- Fix: no client icons

* Mon Jul 24 2017 Oleg Solovyov <mcpain@altlinux.org> 1.1.23-alt1
- Version 1.1.23

* Thu Jul 20 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.140-alt2
- Fix: no themes

* Tue Jul 18 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.140-alt1
- Version 1.0.140

* Tue Jul 18 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.134-alt3
- Build with Qt5

* Thu Jul 14 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.134-alt2
- New patch for disabling stream management

* Thu Jul 14 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.134-alt1
- Version 1.0.134

* Thu Jul 06 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.127-alt1
- Version 1.0.127

* Tue Jul 04 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.120-alt1
- Version 1.0.120

* Thu Jun 29 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.116-alt1
- Version 1.0.116

* Fri Dec 04 2015 Nazarov Denis <nenderus@altlinux.org> 0.16.475.1-alt0.M70T.1
- Build for branch t7

* Wed Dec 02 2015 Nazarov Denis <nenderus@altlinux.org> 0.16.475.1-alt1
- Version 0.16.475.1 (ALT #31565)

* Mon Oct 12 2015 Michael Shigorin <mike@altlinux.org> 0.16.309-alt0.M70T.1
- built for t7/branch

* Sun Mar 23 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.309-alt1
- Version 0.16.309

* Tue Mar 18 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.298-alt1
- Version 0.16.298

* Sun Mar 16 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.295-alt1
- Version 0.16.295

* Sat Mar 15 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.292-alt1
- Version 0.16.292

* Thu Mar 13 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.291-alt1
- Version 0.16.291

* Tue Mar 11 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.290-alt1
- Version 0.16.290

* Sat Mar 08 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.289.1-alt1
- Version 0.16.289.1

* Tue Mar 04 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.289-alt0.M70T.1
- Build for branch t7

* Mon Mar 03 2014 Nazarov Denis <nenderus@altlinux.org> 0.16.289-alt1
- Version 0.16.289

* Thu May 09 2013 Nazarov Denis <nenderus@altlinux.org> 0.16.116-alt0.M60T.1
- Build for branch t6

* Mon May 06 2013 Nazarov Denis <nenderus@altlinux.org> 0.16.116-alt1
- Version 0.16.116

* Mon Mar 18 2013 Nazarov Denis <nenderus@altlinux.org> 0.16.105-alt0.M60T.1
- Build for branch t6

* Sun Mar 17 2013 Nazarov Denis <nenderus@altlinux.org> 0.16.105-alt1
- Version 0.16.105

* Wed Nov 14 2012 Nazarov Denis <nenderus@altlinux.org> 0.16.25-alt2
- Fix version

* Wed Nov 14 2012 Nazarov Denis <nenderus@altlinux.org> 0.16.25-alt0.M60T.1
- Build for branch t6

* Wed Nov 14 2012 Nazarov Denis <nenderus@altlinux.org> 0.16.25-alt1
- Version 0.16.25

* Sat Jun 09 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5337-alt0.M60T.1
- Build for branch t6

* Fri Jun 08 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5337-alt1
- Version 0.15.5337

* Wed Apr 25 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5320-alt1
- Version 0.15.5320

* Fri Mar 30 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5268-alt1
- Version 0.15.5268

* Sat Mar 24 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5242-alt1
- Version 0.15.5242

* Tue Mar 06 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5225-alt1
- Version 0.15.5225

* Sun Feb 12 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5195-alt1
- Version 0.15.5195

* Sun Jan 29 2012 Nazarov Denis <nenderus@altlinux.org> 0.15.5185-alt1
- Version 0.15.5185

* Wed Nov 23 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5145-alt1
- Version 0.15.5145

* Sun Oct 30 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5130-alt1
- Version 0.15.5130

* Tue Oct 04 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5122-alt0.M60T.1
- Build for branch t6

* Mon Oct 03 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5122-alt1
- Version 0.15.5122

* Wed Sep 14 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5116-alt0.M60T.1.svn4128
- Build for branch t6

* Tue Sep 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5116-alt1.svn4128
- Version 0.15.5116
- SVN revision 4128

* Sun Sep 04 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5106-alt0.M60P.1.svn4127
- Build for branch p6

* Fri Sep 02 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5106-alt0.M60T.1.svn4127
- Build for branch t6

* Thu Sep 01 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5106-alt1.svn4127
- SVN revision 4127

* Tue Aug 30 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5106-alt0.M60T.1.svn4126
- Build for branch t6

* Mon Aug 29 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5106-alt1.svn4126
- Version 0.15.5106
- SVN revision 4126
- Add qca2-gnupg in reqires

* Thu Aug 25 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5091-alt0.M60T.1.svn4125
- Build for branch t6

* Wed Aug 24 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5091-alt1.svn4125
- Version 0.15.5091
- SVN revision 4125
- Add qca2-ossl in reqires

* Thu Aug 18 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5074-alt0.M60T.1.svn4124
- Build for branch t6

* Wed Aug 17 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5074-alt1.svn4124
- SVN revision 4124

* Mon Aug 08 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5074-alt1.svn4123
- Version 0.15.5074
- SVN revision 4123

* Mon Jul 18 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5062-alt0.M60T.1.svn4122
- Build for branch t6

* Mon Jul 18 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5062-alt1.svn4122
- Version 0.15.5062
- SVN revision 4122
- Change profile location from ~/.psi to ~/.config/Psi+

* Tue Jul 05 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5031-alt0.M60T.1.svn4120
- Build for branch t6

* Tue Jul 05 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.5031-alt1.svn4120
- Version 0.15.5031
- SVN revision 4120

* Fri Jul 01 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.4062-alt0.svn4118.M60T.1
- Build for branch t6

* Fri Jul 01 2011 Nazarov Denis <nenderus@altlinux.org> 0.15.4062-alt1.svn4118
- SVN revision 4118

* Tue Jun 21 2011 Nazarov Denis <nenderus@altlinux.org> 0.15-alt4.svn4062
- SVN revision 4062
- Add plugins:
  - captcha forms
  - chess
  - client switcher
  - content downloader
  - extended menu
  - gomoku game
  - history keeper
  - jabber disk
  - null
  - pep change notify
  - qip x-statuses

* Wed Mar 30 2011 Grigory Milev <week@altlinux.ru> 0.15-alt3.r3755
- new version 3755
- auto patch from psi to psi+

* Fri Jan 28 2011 Grigory Milev <week@altlinux.ru> 0.15-alt2.r3624
- new git version
- gmailnotifyplugin -> gmailserviceplugin

* Sat Oct 30 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r3133
- new nightly revision

* Tue Oct 26 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r3125
- new nightly revision

* Sun Oct 24 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r3123
- new nightly revision

* Wed Oct 13 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r3086
- new nightly revision

* Sat Jul 24 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2747
- new nightly revision

* Mon Jul 19 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2702
- new nightly revision

* Sun Jul 18 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2693
- new nightly revision

* Sun Jul 18 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2690
- new nightly revision

* Sun Jul 18 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2689
- new nightly revision
- enable webkit

* Sat Jul 17 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2687
- new nightly revision

* Mon May 31 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2486
- new nightly revision
- disable webkit

* Wed Apr 21 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2180
- new nightly revision

* Sun Apr 11 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2122
- new nightly revision

* Mon Apr 05 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt1.r2102
- new nightly revision

* Sat Mar 27 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r2049.1
- new nightly revision
- add skinsplugin
- with "--enable-qtwebkit"

* Mon Mar 22 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r2024.1
- new nightly revision

* Sun Mar 14 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1988.1
- new nightly revision

* Wed Mar 10 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1972.1
- new nightly revision

* Mon Mar 08 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1961.1
- new nightly revision

* Sun Feb 28 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1934.1
- new nightly revision

* Tue Feb 23 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1903.1
- new nightly revision

* Tue Feb 23 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1901.1
- new nightly revision
- add storagenotesplugin

* Mon Feb 22 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1900.1
- new nightly revision

* Sun Feb 14 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1860.1
- new nightly revision
- fixup plugins location (hope it's work)

* Sat Feb 06 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1818
- new nightly revision

* Fri Feb 05 2010 Anton A. Vinogradov <arc@altlinux.org> 0.15-alt0.r1813
- Initial build for ALT Linux
