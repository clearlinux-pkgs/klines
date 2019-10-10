#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : klines
Version  : 19.08.2
Release  : 13
URL      : https://download.kde.org/stable/applications/19.08.2/src/klines-19.08.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.2/src/klines-19.08.2.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.2/src/klines-19.08.2.tar.xz.sig
Summary  : A simple but highly addictive one player game
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: klines-bin = %{version}-%{release}
Requires: klines-data = %{version}-%{release}
Requires: klines-license = %{version}-%{release}
Requires: klines-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
This file describes how to create a new KLines theme.
(Last update: 29.05.2007 by dimsuz)

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
%setup -q -n klines-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570747151
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570747151
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/klines
cp COPYING %{buildroot}/usr/share/package-licenses/klines/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/klines/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang klines

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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

%files doc
%defattr(0644,root,root,0755)
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
/usr/share/doc/HTML/it/klines/index.cache.bz2
/usr/share/doc/HTML/it/klines/index.docbook
/usr/share/doc/HTML/nl/klines/index.cache.bz2
/usr/share/doc/HTML/nl/klines/index.docbook
/usr/share/doc/HTML/pt/klines/index.cache.bz2
/usr/share/doc/HTML/pt/klines/index.docbook
/usr/share/doc/HTML/pt_BR/klines/index.cache.bz2
/usr/share/doc/HTML/pt_BR/klines/index.docbook
/usr/share/doc/HTML/sv/klines/index.cache.bz2
/usr/share/doc/HTML/sv/klines/index.docbook
/usr/share/doc/HTML/uk/klines/gamescreen.png
/usr/share/doc/HTML/uk/klines/index.cache.bz2
/usr/share/doc/HTML/uk/klines/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/klines/COPYING
/usr/share/package-licenses/klines/COPYING.DOC

%files locales -f klines.lang
%defattr(-,root,root,-)

