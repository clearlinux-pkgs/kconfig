#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: e738c51
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kconfig
Version  : 6.0.0
Release  : 83
URL      : https://download.kde.org/stable/frameworks/6.0/kconfig-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/kconfig-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/kconfig-6.0.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kconfig-bin = %{version}-%{release}
Requires: kconfig-data = %{version}-%{release}
Requires: kconfig-lib = %{version}-%{release}
Requires: kconfig-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KConfig
Persistent platform-independent application settings.
## Introduction
KConfig provides an advanced configuration system. It is made of two parts:
KConfigCore and KConfigGui.

%package bin
Summary: bin components for the kconfig package.
Group: Binaries
Requires: kconfig-data = %{version}-%{release}
Requires: kconfig-license = %{version}-%{release}

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
Requires: kconfig-lib = %{version}-%{release}
Requires: kconfig-bin = %{version}-%{release}
Requires: kconfig-data = %{version}-%{release}
Provides: kconfig-devel = %{version}-%{release}
Requires: kconfig = %{version}-%{release}

%description dev
dev components for the kconfig package.


%package lib
Summary: lib components for the kconfig package.
Group: Libraries
Requires: kconfig-data = %{version}-%{release}
Requires: kconfig-license = %{version}-%{release}

%description lib
lib components for the kconfig package.


%package license
Summary: license components for the kconfig package.
Group: Default

%description license
license components for the kconfig package.


%prep
%setup -q -n kconfig-6.0.0
cd %{_builddir}/kconfig-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709223958
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709223958
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kconfig
cp %{_builddir}/kconfig-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kconfig/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/kconfig-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kconfig/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kconfig-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kconfig/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kconfig-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kconfig/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kconfig-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kconfig/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kconfig-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kconfig/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kconfig-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kconfig/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kconfig-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kconfig/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kconfig-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kconfig/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kconfig-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kconfig/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kconfig-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kconfig/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kconf_update
/V3/usr/lib64/libexec/kf6/kconfig_compiler_kf6
/usr/lib64/libexec/kf6/kconf_update
/usr/lib64/libexec/kf6/kconfig_compiler_kf6
/usr/lib64/qt6/qml/org/kde/config/kconfigqmlplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/config/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/config/qmldir

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kreadconfig6
/V3/usr/bin/kwriteconfig6
/usr/bin/kreadconfig6
/usr/bin/kwriteconfig6

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/az/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/be/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/br/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/da/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/he/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/id/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/is/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/kab/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/km/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/or/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/se/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/si/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/te/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/th/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kconfig6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kconfig6_qt.qm
/usr/share/qlogging-categories6/kconfig.categories
/usr/share/qlogging-categories6/kconfig.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KConfig/kconfig_version.h
/usr/include/KF6/KConfigCore/KAuthorized
/usr/include/KF6/KConfigCore/KConfig
/usr/include/KF6/KConfigCore/KConfigBase
/usr/include/KF6/KConfigCore/KConfigGroup
/usr/include/KF6/KConfigCore/KConfigWatcher
/usr/include/KF6/KConfigCore/KCoreConfigSkeleton
/usr/include/KF6/KConfigCore/KDesktopFile
/usr/include/KF6/KConfigCore/KDesktopFileAction
/usr/include/KF6/KConfigCore/KEMailSettings
/usr/include/KF6/KConfigCore/KSharedConfig
/usr/include/KF6/KConfigCore/kauthorized.h
/usr/include/KF6/KConfigCore/kconfig.h
/usr/include/KF6/KConfigCore/kconfigbase.h
/usr/include/KF6/KConfigCore/kconfigconversioncheck_p.h
/usr/include/KF6/KConfigCore/kconfigcore_export.h
/usr/include/KF6/KConfigCore/kconfiggroup.h
/usr/include/KF6/KConfigCore/kconfigwatcher.h
/usr/include/KF6/KConfigCore/kcoreconfigskeleton.h
/usr/include/KF6/KConfigCore/kdesktopfile.h
/usr/include/KF6/KConfigCore/kdesktopfileaction.h
/usr/include/KF6/KConfigCore/kemailsettings.h
/usr/include/KF6/KConfigCore/ksharedconfig.h
/usr/include/KF6/KConfigGui/KConfigGui
/usr/include/KF6/KConfigGui/KConfigLoader
/usr/include/KF6/KConfigGui/KConfigSkeleton
/usr/include/KF6/KConfigGui/KStandardShortcut
/usr/include/KF6/KConfigGui/KStandardShortcutWatcher
/usr/include/KF6/KConfigGui/KWindowConfig
/usr/include/KF6/KConfigGui/KWindowStateSaver
/usr/include/KF6/KConfigGui/kconfiggui.h
/usr/include/KF6/KConfigGui/kconfiggui_export.h
/usr/include/KF6/KConfigGui/kconfigguistaticinitializer.cpp
/usr/include/KF6/KConfigGui/kconfigloader.h
/usr/include/KF6/KConfigGui/kconfigskeleton.h
/usr/include/KF6/KConfigGui/kstandardshortcut.h
/usr/include/KF6/KConfigGui/kstandardshortcutwatcher.h
/usr/include/KF6/KConfigGui/kwindowconfig.h
/usr/include/KF6/KConfigGui/kwindowstatesaver.h
/usr/include/KF6/KConfigQml/KConfigPropertyMap
/usr/include/KF6/KConfigQml/kconfigpropertymap.h
/usr/include/KF6/KConfigQml/kconfigqml_export.h
/usr/lib64/cmake/KF6Config/KF6ConfigCompilerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Config/KF6ConfigCompilerTargets.cmake
/usr/lib64/cmake/KF6Config/KF6ConfigConfig.cmake
/usr/lib64/cmake/KF6Config/KF6ConfigConfigVersion.cmake
/usr/lib64/cmake/KF6Config/KF6ConfigMacros.cmake
/usr/lib64/cmake/KF6Config/KF6ConfigTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Config/KF6ConfigTargets.cmake
/usr/lib64/libKF6ConfigCore.so
/usr/lib64/libKF6ConfigGui.so
/usr/lib64/libKF6ConfigQml.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6ConfigCore.so.6.0.0
/V3/usr/lib64/libKF6ConfigGui.so.6.0.0
/V3/usr/lib64/libKF6ConfigQml.so.6.0.0
/V3/usr/lib64/qt6/qml/org/kde/config/libkconfigqmlplugin.so
/usr/lib64/libKF6ConfigCore.so.6
/usr/lib64/libKF6ConfigCore.so.6.0.0
/usr/lib64/libKF6ConfigGui.so.6
/usr/lib64/libKF6ConfigGui.so.6.0.0
/usr/lib64/libKF6ConfigQml.so.6
/usr/lib64/libKF6ConfigQml.so.6.0.0
/usr/lib64/qt6/qml/org/kde/config/libkconfigqmlplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kconfig/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kconfig/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kconfig/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kconfig/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kconfig/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kconfig/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kconfig/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kconfig/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kconfig/e712eadfab0d2357c0f50f599ef35ee0d87534cb
