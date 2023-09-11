#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kconfig
Version  : 5.110.0
Release  : 76
URL      : https://download.kde.org/stable/frameworks/5.110/kconfig-5.110.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.110/kconfig-5.110.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.110/kconfig-5.110.0.tar.xz.sig
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
%setup -q -n kconfig-5.110.0
cd %{_builddir}/kconfig-5.110.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694443131
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1694443131
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
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf5/kconf_update
/V3/usr/lib64/libexec/kf5/kconfig_compiler_kf5
/usr/lib64/libexec/kf5/kconf_update
/usr/lib64/libexec/kf5/kconfig_compiler_kf5

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kreadconfig5
/V3/usr/bin/kwriteconfig5
/usr/bin/kreadconfig5
/usr/bin/kwriteconfig5

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kconfig5_qt.qm
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
/usr/share/locale/ka/LC_MESSAGES/kconfig5_qt.qm
/usr/share/locale/kab/LC_MESSAGES/kconfig5_qt.qm
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
/usr/share/qlogging-categories5/kconfig.categories
/usr/share/qlogging-categories5/kconfig.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KConfig/kconfig_version.h
/usr/include/KF5/KConfigCore/ConversionCheck
/usr/include/KF5/KConfigCore/KAuthorized
/usr/include/KF5/KConfigCore/KConfig
/usr/include/KF5/KConfigCore/KConfigBase
/usr/include/KF5/KConfigCore/KConfigGroup
/usr/include/KF5/KConfigCore/KConfigWatcher
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
/usr/include/KF5/KConfigCore/kconfigwatcher.h
/usr/include/KF5/KConfigCore/kcoreconfigskeleton.h
/usr/include/KF5/KConfigCore/kdesktopfile.h
/usr/include/KF5/KConfigCore/kemailsettings.h
/usr/include/KF5/KConfigCore/ksharedconfig.h
/usr/include/KF5/KConfigGui/KConfigGui
/usr/include/KF5/KConfigGui/KConfigLoader
/usr/include/KF5/KConfigGui/KConfigSkeleton
/usr/include/KF5/KConfigGui/KStandardShortcut
/usr/include/KF5/KConfigGui/KStandardShortcutWatcher
/usr/include/KF5/KConfigGui/KWindowConfig
/usr/include/KF5/KConfigGui/KWindowStateSaver
/usr/include/KF5/KConfigGui/kconfiggui.h
/usr/include/KF5/KConfigGui/kconfiggui_export.h
/usr/include/KF5/KConfigGui/kconfigguistaticinitializer.cpp
/usr/include/KF5/KConfigGui/kconfigloader.h
/usr/include/KF5/KConfigGui/kconfigskeleton.h
/usr/include/KF5/KConfigGui/kstandardshortcut.h
/usr/include/KF5/KConfigGui/kstandardshortcutwatcher.h
/usr/include/KF5/KConfigGui/kwindowconfig.h
/usr/include/KF5/KConfigGui/kwindowstatesaver.h
/usr/include/KF5/KConfigQml/KConfigPropertyMap
/usr/include/KF5/KConfigQml/kconfigpropertymap.h
/usr/include/KF5/KConfigQml/kconfigqml_export.h
/usr/lib64/cmake/KF5Config/KF5ConfigCompilerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigCompilerTargets.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigConfig.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigConfigVersion.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigMacros.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Config/KF5ConfigTargets.cmake
/usr/lib64/libKF5ConfigCore.so
/usr/lib64/libKF5ConfigGui.so
/usr/lib64/libKF5ConfigQml.so
/usr/lib64/qt5/mkspecs/modules/qt_KConfigCore.pri
/usr/lib64/qt5/mkspecs/modules/qt_KConfigGui.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5ConfigCore.so.5.110.0
/V3/usr/lib64/libKF5ConfigGui.so.5.110.0
/V3/usr/lib64/libKF5ConfigQml.so.5.110.0
/usr/lib64/libKF5ConfigCore.so.5
/usr/lib64/libKF5ConfigCore.so.5.110.0
/usr/lib64/libKF5ConfigGui.so.5
/usr/lib64/libKF5ConfigGui.so.5.110.0
/usr/lib64/libKF5ConfigQml.so.5
/usr/lib64/libKF5ConfigQml.so.5.110.0

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
