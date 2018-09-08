#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kconfig
Version  : 5.50.0
Release  : 4
URL      : https://download.kde.org/stable/frameworks/5.50/kconfig-5.50.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.50/kconfig-5.50.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.50/kconfig-5.50.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kconfig-bin
Requires: kconfig-lib
Requires: kconfig-license
Requires: kconfig-data
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev qtbase-extras mesa-dev

%description
# KConfig
Persistent platform-independent application settings.
## Introduction
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

%package bin
Summary: bin components for the kconfig package.
Group: Binaries
Requires: kconfig-data
Requires: kconfig-license

%description bin
bin components for the kconfig package.


%package data
Summary: data components for the kconfig package.
Group: Data

%description data
data components for the kconfig package.


%package dev
Summary: dev components for the kconfig package.
Group: Development
Requires: kconfig-lib
Requires: kconfig-bin
Requires: kconfig-data
Provides: kconfig-devel

%description dev
dev components for the kconfig package.


%package lib
Summary: lib components for the kconfig package.
Group: Libraries
Requires: kconfig-data
Requires: kconfig-license

%description lib
lib components for the kconfig package.


%package license
Summary: license components for the kconfig package.
Group: Default

%description license
license components for the kconfig package.


%prep
%setup -q -n kconfig-5.50.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536431015
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1536431015
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kconfig
cp COPYING.LIB %{buildroot}/usr/share/doc/kconfig/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/kconf_update
/usr/lib64/libexec/kf5/kconfig_compiler_kf5

%files bin
%defattr(-,root,root,-)
/usr/bin/kreadconfig5
/usr/bin/kwriteconfig5

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/si/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/te/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kconfig5_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KConfigCore/ConversionCheck
/usr/include/KF5/KConfigCore/KAuthorized
/usr/include/KF5/KConfigCore/KConfig
/usr/include/KF5/KConfigCore/KConfigBase
/usr/include/KF5/KConfigCore/KConfigGroup
/usr/include/KF5/KConfigCore/KCoreConfigSkeleton
/usr/include/KF5/KConfigCore/KDesktopFile
/usr/include/KF5/KConfigCore/KEMailSettings
/usr/include/KF5/KConfigCore/KSharedConfig
/usr/include/KF5/KConfigCore/conversioncheck.h
/usr/include/KF5/KConfigCore/kauthorized.h
/usr/include/KF5/KConfigCore/kconfig.h
/usr/include/KF5/KConfigCore/kconfigbase.h
/usr/include/KF5/KConfigCore/kconfigcore_export.h
/usr/include/KF5/KConfigCore/kconfiggroup.h
/usr/include/KF5/KConfigCore/kcoreconfigskeleton.h
/usr/include/KF5/KConfigCore/kdesktopfile.h
/usr/include/KF5/KConfigCore/kemailsettings.h
/usr/include/KF5/KConfigCore/ksharedconfig.h
/usr/include/KF5/KConfigGui/KConfigGui
/usr/include/KF5/KConfigGui/KConfigLoader
/usr/include/KF5/KConfigGui/KConfigSkeleton
/usr/include/KF5/KConfigGui/KStandardShortcut
/usr/include/KF5/KConfigGui/KWindowConfig
/usr/include/KF5/KConfigGui/kconfiggui.h
/usr/include/KF5/KConfigGui/kconfiggui_export.h
/usr/include/KF5/KConfigGui/kconfigloader.h
/usr/include/KF5/KConfigGui/kconfigskeleton.h
/usr/include/KF5/KConfigGui/kstandardshortcut.h
/usr/include/KF5/KConfigGui/kwindowconfig.h
/usr/include/KF5/kconfig_version.h
/usr/lib64/cmake/KF5Config/KF5ConfigCompilerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigCompilerTargets.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigConfig.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigConfigVersion.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigMacros.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigTargets.cmake
/usr/lib64/libKF5ConfigCore.so
/usr/lib64/libKF5ConfigGui.so
/usr/lib64/qt5/mkspecs/modules/qt_KConfigCore.pri
/usr/lib64/qt5/mkspecs/modules/qt_KConfigGui.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5ConfigCore.so.5
/usr/lib64/libKF5ConfigCore.so.5.50.0
/usr/lib64/libKF5ConfigGui.so.5
/usr/lib64/libKF5ConfigGui.so.5.50.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/kconfig/COPYING.LIB
