#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v18
# autospec commit: f35655a
#
Name     : grass
Version  : 8.4.0
Release  : 67
URL      : https://github.com/OSGeo/grass/archive/8.4.0/grass-8.4.0.tar.gz
Source0  : https://github.com/OSGeo/grass/archive/8.4.0/grass-8.4.0.tar.gz
Summary  : Multi-producer-multi-consumer signal dispatching mechanism
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC-BY-SA-3.0 GPL-2.0 GPL-2.0+ LGPL-2.1 MIT
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : buildreq-kde
BuildRequires : bzip2-dev
BuildRequires : cairo-dev
BuildRequires : fftw-dev
BuildRequires : flex
BuildRequires : freetype-dev
BuildRequires : gdal-dev
BuildRequires : geos
BuildRequires : geos-dev
BuildRequires : gfortran
BuildRequires : glu-dev
BuildRequires : libpng-dev
BuildRequires : mesa-dev
BuildRequires : netcdf
BuildRequires : netcdf-dev
BuildRequires : openblas
BuildRequires : pkgconfig(pdal)
BuildRequires : pkgconfig(x11)
BuildRequires : proj-dev
BuildRequires : pypi-wxPython
BuildRequires : sqlite-autoconf-dev
BuildRequires : tiff-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
PyDispatcher is an enhanced version of Patrick K. O'Brien's
        original dispatcher.py module.  It provides the Python
        programmer with a robust mechanism for event routing within
        various application contexts.

        Included in the package are the robustapply and saferef
        modules, which provide the ability to selectively apply
        arguments to callable objects and to reference instance
        methods using weak-references.

%package dev
Summary: dev components for the grass package.
Group: Development
Provides: grass-devel = %{version}-%{release}
Requires: grass = %{version}-%{release}

%description dev
dev components for the grass package.


%prep
%setup -q -n grass-8.4.0
cd %{_builddir}/grass-8.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723503687
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
%configure --disable-static --with-fftw \
--with-openmp \
--without-freetype
make  || :

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
export SOURCE_DATE_EPOCH=1723503687
rm -rf %{buildroot}
## install_prepend content
mkdir -p %{buildroot}/usr/etc
touch  %{buildroot}/usr/etc/fontcap
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/grass
cp %{_builddir}/grass-%{version}/GPL.TXT %{buildroot}/usr/share/package-licenses/grass/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/grass-%{version}/gui/icons/grass/LICENSE.TXT %{buildroot}/usr/share/package-licenses/grass/095127a16b456be28e180b85c739535e9de42ec2 || :
cp %{_builddir}/grass-%{version}/lib/external/ccmath/lgpl.license %{buildroot}/usr/share/package-licenses/grass/85b6c317814eb04c6ef5f0090037358e1be06b12 || :
cp %{_builddir}/grass-%{version}/lib/external/parson/LICENSE %{buildroot}/usr/share/package-licenses/grass/1518f228adf46f7d96f40a5d08059d24360ed9f2 || :
cp %{_builddir}/grass-%{version}/lib/vector/dglib/COPYING %{buildroot}/usr/share/package-licenses/grass/6e3c11e241d01ccacf94f5c138f9150bd8a5b65f || :
cp %{_builddir}/grass-%{version}/mswindows/external/rbatch/COPYING %{buildroot}/usr/share/package-licenses/grass/b9e28040de9d8773c5b0cc8108869e8f3f287798 || :
cp %{_builddir}/grass-%{version}/mswindows/external/rbatch/LICENSE %{buildroot}/usr/share/package-licenses/grass/3e214f9d2536757b88a59d2d5a05f5e38d660e46 || :
cp %{_builddir}/grass-%{version}/python/grass/pydispatch/license.txt %{buildroot}/usr/share/package-licenses/grass/59d4a2706b04976b460f78fb96c232ceeb155302 || :
cp %{_builddir}/grass-%{version}/python/libgrass_interface_generator/LICENSE %{buildroot}/usr/share/package-licenses/grass/083f420d5cabd4e87c1cced4399546adf61c03bd || :
cp %{_builddir}/grass-%{version}/vector/v.lrs/LICENSE %{buildroot}/usr/share/package-licenses/grass/0dffcc72bb327ff5b4dc2158e1723f334779543b || :
export GOAMD64=v2
GOAMD64=v2
%make_install prefix=%{buildroot}%{_libdir} UNIX_BIN=%{buildroot}%{_bindir} || :
## install_append content
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/include/grass/dgl
mkdir -p %{buildroot}/usr/lib64
# Copy headers.
cp -r include/* %{buildroot}/usr/include/grass/
# Copy DGLib headers.
cp lib/vector/dglib/*.h %{buildroot}/usr/include/grass/dgl/
mv %{buildroot}/usr/include/grass/dgl/dgl.h %{buildroot}/usr/include/grass/
# Copy RTree headers.
cp lib/vector/rtree/*.h %{buildroot}/usr/include/grass/
# Copy shapefil header.
cp lib/external/shapelib/shapefil.h %{buildroot}/usr/include/grass/
# Rest grass headers.
cp -a dist.x86_64-generic-linux-gnu/include/grass/*.h %{buildroot}/usr/include/grass/
# Copy Libraries.
cp dist.x86_64-generic-linux-gnu/lib/* %{buildroot}/usr/lib64
# Fixup the pc file
sed 's|/usr/grass-[0-9\.]\+/lib|/usr/lib64|g' -i grass.pc
sed 's|/usr/grass-[0-9\.]\+/include|/usr/include/grass|g' -i grass.pc
sed 's|/usr/grass-[0-9\.]\+|/usr|g' -i grass.pc
mkdir -p %{buildroot}/usr/lib64/pkgconfig
cp -a grass.pc %{buildroot}/usr/lib64/pkgconfig
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/grass/Make/Compile.make
/usr/include/grass/Make/DB.make
/usr/include/grass/Make/Dir.make
/usr/include/grass/Make/Docs.make
/usr/include/grass/Make/Doxyfile_arch_html
/usr/include/grass/Make/Doxyfile_arch_html.in
/usr/include/grass/Make/Doxyfile_arch_latex
/usr/include/grass/Make/Doxyfile_arch_latex.in
/usr/include/grass/Make/Doxygen.make
/usr/include/grass/Make/Etc.make
/usr/include/grass/Make/Grass.make
/usr/include/grass/Make/GuiScript.make
/usr/include/grass/Make/Html.make
/usr/include/grass/Make/HtmlRules.make
/usr/include/grass/Make/Install.make
/usr/include/grass/Make/Lib.make
/usr/include/grass/Make/Module.make
/usr/include/grass/Make/Multi.make
/usr/include/grass/Make/NoHtml.make
/usr/include/grass/Make/Other.make
/usr/include/grass/Make/Platform.make
/usr/include/grass/Make/Platform.make.in
/usr/include/grass/Make/Python.make
/usr/include/grass/Make/Rules.make
/usr/include/grass/Make/Script.make
/usr/include/grass/Make/ScriptRules.make
/usr/include/grass/Make/ShScript.make
/usr/include/grass/Make/ShScriptRules.make
/usr/include/grass/Make/Shlib.make
/usr/include/grass/Make/Sphinx.make
/usr/include/grass/Make/Stlib.make
/usr/include/grass/Make/Vars.make
/usr/include/grass/Makefile
/usr/include/grass/N_gwflow.h
/usr/include/grass/N_heatflow.h
/usr/include/grass/N_pde.h
/usr/include/grass/N_solute_transport.h
/usr/include/grass/VERSION
/usr/include/grass/arraystats.h
/usr/include/grass/bitmap.h
/usr/include/grass/blas.h
/usr/include/grass/btree.h
/usr/include/grass/calc.h
/usr/include/grass/card.h
/usr/include/grass/ccmath_grass.h
/usr/include/grass/cdhc.h
/usr/include/grass/citing.h
/usr/include/grass/cluster.h
/usr/include/grass/colors.h
/usr/include/grass/config.h
/usr/include/grass/confparms.h
/usr/include/grass/copying.h
/usr/include/grass/dataquad.h
/usr/include/grass/datetime.h
/usr/include/grass/dbmi.h
/usr/include/grass/dbstubs.h
/usr/include/grass/dgl.h
/usr/include/grass/dgl/avl.h
/usr/include/grass/dgl/graph.h
/usr/include/grass/dgl/graph_v1.h
/usr/include/grass/dgl/graph_v2.h
/usr/include/grass/dgl/heap.h
/usr/include/grass/dgl/helpers.h
/usr/include/grass/dgl/tavl.h
/usr/include/grass/dgl/tree.h
/usr/include/grass/dgl/type.h
/usr/include/grass/dgl/v1-defs.h
/usr/include/grass/dgl/v2-defs.h
/usr/include/grass/display.h
/usr/include/grass/fontcap.h
/usr/include/grass/form.h
/usr/include/grass/gis.h
/usr/include/grass/glocale.h
/usr/include/grass/gmath.h
/usr/include/grass/gprojects.h
/usr/include/grass/grass/Makefile
/usr/include/grass/grass/arraystats.h
/usr/include/grass/grass/bitmap.h
/usr/include/grass/grass/blas.h
/usr/include/grass/grass/btree.h
/usr/include/grass/grass/calc.h
/usr/include/grass/grass/cdhc.h
/usr/include/grass/grass/cluster.h
/usr/include/grass/grass/colors.h
/usr/include/grass/grass/config.h
/usr/include/grass/grass/config.h.in
/usr/include/grass/grass/datetime.h
/usr/include/grass/grass/dbmi.h
/usr/include/grass/grass/defs/Paintlib.h
/usr/include/grass/grass/defs/arraystats.h
/usr/include/grass/grass/defs/bitmap.h
/usr/include/grass/grass/defs/btree.h
/usr/include/grass/grass/defs/calc.h
/usr/include/grass/grass/defs/cdhc.h
/usr/include/grass/grass/defs/cluster.h
/usr/include/grass/grass/defs/colors.h
/usr/include/grass/grass/defs/datetime.h
/usr/include/grass/grass/defs/dbmi.h
/usr/include/grass/grass/defs/devlib.h
/usr/include/grass/grass/defs/dig_atts.h
/usr/include/grass/grass/defs/display.h
/usr/include/grass/grass/defs/form.h
/usr/include/grass/grass/defs/gis.h
/usr/include/grass/grass/defs/glocale.h
/usr/include/grass/grass/defs/gmath.h
/usr/include/grass/grass/defs/gprojects.h
/usr/include/grass/grass/defs/imagery.h
/usr/include/grass/grass/defs/la.h
/usr/include/grass/grass/defs/linkm.h
/usr/include/grass/grass/defs/manage.h
/usr/include/grass/grass/defs/neta.h
/usr/include/grass/grass/defs/nviz.h
/usr/include/grass/grass/defs/ogsf.h
/usr/include/grass/grass/defs/ortholib.h
/usr/include/grass/grass/defs/raster.h
/usr/include/grass/grass/defs/raster3d.h
/usr/include/grass/grass/defs/rbtree.h
/usr/include/grass/grass/defs/rowio.h
/usr/include/grass/grass/defs/segment.h
/usr/include/grass/grass/defs/spawn.h
/usr/include/grass/grass/defs/sqlp.h
/usr/include/grass/grass/defs/stats.h
/usr/include/grass/grass/defs/symbol.h
/usr/include/grass/grass/defs/vector.h
/usr/include/grass/grass/defs/vedit.h
/usr/include/grass/grass/display.h
/usr/include/grass/grass/fontcap.h
/usr/include/grass/grass/form.h
/usr/include/grass/grass/gis.h
/usr/include/grass/grass/glocale.h
/usr/include/grass/grass/gmath.h
/usr/include/grass/grass/gprojects.h
/usr/include/grass/grass/imagery.h
/usr/include/grass/grass/iostream/ami.h
/usr/include/grass/grass/iostream/ami_config.h
/usr/include/grass/grass/iostream/ami_sort.h
/usr/include/grass/grass/iostream/ami_sort_impl.h
/usr/include/grass/grass/iostream/ami_stream.h
/usr/include/grass/grass/iostream/embuffer.h
/usr/include/grass/grass/iostream/empq.h
/usr/include/grass/grass/iostream/empq_adaptive.h
/usr/include/grass/grass/iostream/empq_adaptive_impl.h
/usr/include/grass/grass/iostream/empq_impl.h
/usr/include/grass/grass/iostream/imbuffer.h
/usr/include/grass/grass/iostream/mem_stream.h
/usr/include/grass/grass/iostream/minmaxheap.h
/usr/include/grass/grass/iostream/mm.h
/usr/include/grass/grass/iostream/mm_utils.h
/usr/include/grass/grass/iostream/pqheap.h
/usr/include/grass/grass/iostream/queue.h
/usr/include/grass/grass/iostream/quicksort.h
/usr/include/grass/grass/iostream/replacementHeap.h
/usr/include/grass/grass/iostream/replacementHeapBlock.h
/usr/include/grass/grass/iostream/rtimer.h
/usr/include/grass/grass/la.h
/usr/include/grass/grass/lapack.h
/usr/include/grass/grass/linkm.h
/usr/include/grass/grass/manage.h
/usr/include/grass/grass/neta.h
/usr/include/grass/grass/nviz.h
/usr/include/grass/grass/ogsf.h
/usr/include/grass/grass/ortholib.h
/usr/include/grass/grass/raster.h
/usr/include/grass/grass/raster3d.h
/usr/include/grass/grass/rbtree.h
/usr/include/grass/grass/rowio.h
/usr/include/grass/grass/segment.h
/usr/include/grass/grass/spawn.h
/usr/include/grass/grass/sqlp.h
/usr/include/grass/grass/stats.h
/usr/include/grass/grass/symbol.h
/usr/include/grass/grass/temporal.h
/usr/include/grass/grass/vect/dig_defines.h
/usr/include/grass/grass/vect/dig_externs.h
/usr/include/grass/grass/vect/dig_macros.h
/usr/include/grass/grass/vect/dig_structs.h
/usr/include/grass/grass/vect/digit.h
/usr/include/grass/grass/vector.h
/usr/include/grass/grass/vedit.h
/usr/include/grass/grass/version.h
/usr/include/grass/grass/version.h.in
/usr/include/grass/imagery.h
/usr/include/grass/index.h
/usr/include/grass/interpf.h
/usr/include/grass/kdtree.h
/usr/include/grass/la.h
/usr/include/grass/lapack.h
/usr/include/grass/lidar.h
/usr/include/grass/linkm.h
/usr/include/grass/lrs.h
/usr/include/grass/manage.h
/usr/include/grass/neta.h
/usr/include/grass/nviz.h
/usr/include/grass/ogsf.h
/usr/include/grass/ortholib.h
/usr/include/grass/parson.h
/usr/include/grass/qtree.h
/usr/include/grass/raster.h
/usr/include/grass/raster3d.h
/usr/include/grass/rbtree.h
/usr/include/grass/rowio.h
/usr/include/grass/rtree.h
/usr/include/grass/segment.h
/usr/include/grass/shapefil.h
/usr/include/grass/simlib.h
/usr/include/grass/spawn.h
/usr/include/grass/split.h
/usr/include/grass/sqlp.h
/usr/include/grass/stats.h
/usr/include/grass/symbol.h
/usr/include/grass/temporal.h
/usr/include/grass/vector.h
/usr/include/grass/vedit.h
/usr/include/grass/version.h
/usr/include/grass/waterglobs.h
/usr/lib64/libgrass_arraystats.8.4.so
/usr/lib64/libgrass_arraystats.so
/usr/lib64/libgrass_bitmap.8.4.so
/usr/lib64/libgrass_bitmap.so
/usr/lib64/libgrass_btree.8.4.so
/usr/lib64/libgrass_btree.so
/usr/lib64/libgrass_btree2.8.4.so
/usr/lib64/libgrass_btree2.so
/usr/lib64/libgrass_cairodriver.8.4.so
/usr/lib64/libgrass_cairodriver.so
/usr/lib64/libgrass_calc.8.4.so
/usr/lib64/libgrass_calc.so
/usr/lib64/libgrass_ccmath.8.4.so
/usr/lib64/libgrass_ccmath.so
/usr/lib64/libgrass_cdhc.8.4.so
/usr/lib64/libgrass_cdhc.so
/usr/lib64/libgrass_cluster.8.4.so
/usr/lib64/libgrass_cluster.so
/usr/lib64/libgrass_datetime.8.4.so
/usr/lib64/libgrass_datetime.so
/usr/lib64/libgrass_dbmibase.8.4.so
/usr/lib64/libgrass_dbmibase.so
/usr/lib64/libgrass_dbmiclient.8.4.so
/usr/lib64/libgrass_dbmiclient.so
/usr/lib64/libgrass_dbmidriver.8.4.so
/usr/lib64/libgrass_dbmidriver.so
/usr/lib64/libgrass_dbstubs.8.4.so
/usr/lib64/libgrass_dbstubs.so
/usr/lib64/libgrass_dgl.8.4.so
/usr/lib64/libgrass_dgl.so
/usr/lib64/libgrass_dig2.8.4.so
/usr/lib64/libgrass_dig2.so
/usr/lib64/libgrass_display.8.4.so
/usr/lib64/libgrass_display.so
/usr/lib64/libgrass_driver.8.4.so
/usr/lib64/libgrass_driver.so
/usr/lib64/libgrass_dspf.8.4.so
/usr/lib64/libgrass_dspf.so
/usr/lib64/libgrass_g3d.8.4.so
/usr/lib64/libgrass_g3d.so
/usr/lib64/libgrass_gis.8.4.so
/usr/lib64/libgrass_gis.so
/usr/lib64/libgrass_gmath.8.4.so
/usr/lib64/libgrass_gmath.so
/usr/lib64/libgrass_gpde.8.4.so
/usr/lib64/libgrass_gpde.so
/usr/lib64/libgrass_gproj.8.4.so
/usr/lib64/libgrass_gproj.so
/usr/lib64/libgrass_htmldriver.8.4.so
/usr/lib64/libgrass_htmldriver.so
/usr/lib64/libgrass_imagery.8.4.so
/usr/lib64/libgrass_imagery.so
/usr/lib64/libgrass_interpdata.8.4.so
/usr/lib64/libgrass_interpdata.so
/usr/lib64/libgrass_interpfl.8.4.so
/usr/lib64/libgrass_interpfl.so
/usr/lib64/libgrass_iortho.8.4.so
/usr/lib64/libgrass_iortho.so
/usr/lib64/libgrass_iostream.8.4.so
/usr/lib64/libgrass_iostream.so
/usr/lib64/libgrass_lidar.8.4.so
/usr/lib64/libgrass_lidar.so
/usr/lib64/libgrass_linkm.8.4.so
/usr/lib64/libgrass_linkm.so
/usr/lib64/libgrass_lrs.8.4.so
/usr/lib64/libgrass_lrs.so
/usr/lib64/libgrass_manage.8.4.so
/usr/lib64/libgrass_manage.so
/usr/lib64/libgrass_neta.8.4.so
/usr/lib64/libgrass_neta.so
/usr/lib64/libgrass_nviz.8.4.so
/usr/lib64/libgrass_nviz.so
/usr/lib64/libgrass_ogsf.8.4.so
/usr/lib64/libgrass_ogsf.so
/usr/lib64/libgrass_parson.8.4.so
/usr/lib64/libgrass_parson.so
/usr/lib64/libgrass_pngdriver.8.4.so
/usr/lib64/libgrass_pngdriver.so
/usr/lib64/libgrass_psdriver.8.4.so
/usr/lib64/libgrass_psdriver.so
/usr/lib64/libgrass_qtree.8.4.so
/usr/lib64/libgrass_qtree.so
/usr/lib64/libgrass_raster.8.4.so
/usr/lib64/libgrass_raster.so
/usr/lib64/libgrass_rli.8.4.so
/usr/lib64/libgrass_rli.so
/usr/lib64/libgrass_rowio.8.4.so
/usr/lib64/libgrass_rowio.so
/usr/lib64/libgrass_rtree.8.4.so
/usr/lib64/libgrass_rtree.so
/usr/lib64/libgrass_segment.8.4.so
/usr/lib64/libgrass_segment.so
/usr/lib64/libgrass_shape.8.4.so
/usr/lib64/libgrass_shape.so
/usr/lib64/libgrass_sim.8.4.so
/usr/lib64/libgrass_sim.so
/usr/lib64/libgrass_sqlp.8.4.so
/usr/lib64/libgrass_sqlp.so
/usr/lib64/libgrass_stats.8.4.so
/usr/lib64/libgrass_stats.so
/usr/lib64/libgrass_symb.8.4.so
/usr/lib64/libgrass_symb.so
/usr/lib64/libgrass_temporal.8.4.so
/usr/lib64/libgrass_temporal.so
/usr/lib64/libgrass_vector.8.4.so
/usr/lib64/libgrass_vector.so
/usr/lib64/libgrass_vedit.8.4.so
/usr/lib64/libgrass_vedit.so
/usr/lib64/pkgconfig/grass.pc
