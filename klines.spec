#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 94c6be0
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : klines
Version  : 24.12.2
Release  : 78
URL      : https://download.kde.org/stable/release-service/24.12.2/src/klines-24.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.2/src/klines-24.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.2/src/klines-24.12.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: klines-bin = %{version}-%{release}
Requires: klines-data = %{version}-%{release}
Requires: klines-license = %{version}-%{release}
Requires: klines-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
EXTENDED

%package bin
Summary: bin components for the klines package.
Group: Binaries
Requires: klines-data = %{version}-%{release}
Requires: klines-license = %{version}-%{release}

%description bin
bin components for the klines package.


%package data
Summary: data components for the klines package.
Group: Data

%description data
data components for the klines package.


%package doc
Summary: doc components for the klines package.
Group: Documentation

%description doc
doc components for the klines package.


%package license
Summary: license components for the klines package.
Group: Default

%description license
license components for the klines package.


%package locales
Summary: locales components for the klines package.
Group: Default

%description locales
locales components for the klines package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n klines-24.12.2
cd %{_builddir}/klines-24.12.2
pushd ..
cp -a klines-24.12.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738969402
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1738969402
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/klines
cp %{_builddir}/klines-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/klines/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/klines-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/klines/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/klines-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/klines/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/klines-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/klines/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/klines-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/klines/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang klines
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/klines
/usr/bin/klines

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.klines.desktop
/usr/share/config.kcfg/klines.kcfg
/usr/share/icons/hicolor/128x128/apps/klines.png
/usr/share/icons/hicolor/16x16/apps/klines.png
/usr/share/icons/hicolor/22x22/apps/klines.png
/usr/share/icons/hicolor/32x32/apps/klines.png
/usr/share/icons/hicolor/48x48/apps/klines.png
/usr/share/icons/hicolor/64x64/apps/klines.png
/usr/share/klines/themes/crystal.desktop
/usr/share/klines/themes/crystal.png
/usr/share/klines/themes/egyptian.desktop
/usr/share/klines/themes/egyptian.png
/usr/share/klines/themes/egyptian.svgz
/usr/share/klines/themes/klines-gems.desktop
/usr/share/klines/themes/klines-gems.png
/usr/share/klines/themes/klines-gems.svgz
/usr/share/klines/themes/klines_crystal.svgz
/usr/share/klines/themes/metal.desktop
/usr/share/klines/themes/metal.png
/usr/share/klines/themes/metal.svgz
/usr/share/klines/themes/pool.desktop
/usr/share/klines/themes/pool.png
/usr/share/klines/themes/pool.svgz
/usr/share/metainfo/org.kde.klines.appdata.xml
/usr/share/qlogging-categories6/klines.categories
/usr/share/qlogging-categories6/klines.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/klines/gamescreen.png
/usr/share/doc/HTML/ca/klines/index.cache.bz2
/usr/share/doc/HTML/ca/klines/index.docbook
/usr/share/doc/HTML/de/klines/gamescreen.png
/usr/share/doc/HTML/de/klines/index.cache.bz2
/usr/share/doc/HTML/de/klines/index.docbook
/usr/share/doc/HTML/en/klines/gamescreen.png
/usr/share/doc/HTML/en/klines/index.cache.bz2
/usr/share/doc/HTML/en/klines/index.docbook
/usr/share/doc/HTML/es/klines/index.cache.bz2
/usr/share/doc/HTML/es/klines/index.docbook
/usr/share/doc/HTML/et/klines/index.cache.bz2
/usr/share/doc/HTML/et/klines/index.docbook
/usr/share/doc/HTML/fr/klines/index.cache.bz2
/usr/share/doc/HTML/fr/klines/index.docbook
/usr/share/doc/HTML/it/klines/index.cache.bz2
/usr/share/doc/HTML/it/klines/index.docbook
/usr/share/doc/HTML/nl/klines/index.cache.bz2
/usr/share/doc/HTML/nl/klines/index.docbook
/usr/share/doc/HTML/pt/klines/index.cache.bz2
/usr/share/doc/HTML/pt/klines/index.docbook
/usr/share/doc/HTML/pt_BR/klines/index.cache.bz2
/usr/share/doc/HTML/pt_BR/klines/index.docbook
/usr/share/doc/HTML/sl/klines/index.cache.bz2
/usr/share/doc/HTML/sl/klines/index.docbook
/usr/share/doc/HTML/sv/klines/index.cache.bz2
/usr/share/doc/HTML/sv/klines/index.docbook
/usr/share/doc/HTML/uk/klines/gamescreen.png
/usr/share/doc/HTML/uk/klines/index.cache.bz2
/usr/share/doc/HTML/uk/klines/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/klines/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/klines/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/klines/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/klines/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/klines/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f klines.lang
%defattr(-,root,root,-)

