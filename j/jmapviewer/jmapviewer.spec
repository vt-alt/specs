# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# (daviddavid) Please do not update this package otherwise it break
# freemind build and freemind is needed for freeplane.

Summary:	Java OpenStreetMap Tile Viewer
Name:		jmapviewer
Version:	1.03
Release:	alt1_6jpp8
Group:		Development/Java
License:	GPLv2
URL:		http://wiki.openstreetmap.org/wiki/JMapViewer
Source:		http://svn.openstreetmap.org/applications/viewer/jmapviewer/releases/%{version}/JMapViewer-%{version}-Source.zip

BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	maven-local
Source44: import.info

%description
JMapViewer is a java component which allows to easily integrate an OSM
map view into your Java application.

Features:
* Provides integrated zoom controls (slider and buttons) in the left
  upper corner (can be hidden)
* Switch between different tile sources: Mapnik, Tiles@Home, Cyclemap,
  ... (other tiled maps can be used, too)
* Configurable in-memory and file-based caching of loaded map tiles
* A list of map markers can be added. Map markers of different shape
  can be easily added by implementing the MapMarker interface.
* Configurable/Extentable/Replaceable controller (code part that
  manages mouse interaction and how the map reacts to it)


%package javadoc
Summary:	API documentation for JMapViewer %{name}
Group:		Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# remove all binary libs, just in case
find -name '*.class' -delete
find -name '*.jar' -delete

#fix error "unmappable character for encoding ASCII"
sed -i "s|ö|o|g" ./src/org/openstreetmap/gui/jmapviewer/interfaces/TileJob.java

# fix line endings
sed -i 's/\r$//' Readme.txt Gpl.txt

sed -i '/<\/javac>/a \
<javadoc sourcepath="src" destdir="target/site/apidocs/" encoding="UTF-8"\/>
' build.xml

%build
%ant clean build pack

%mvn_artifact org.openstreetmap:%{name}:%{version} JMapViewer.jar
%mvn_file :%{name} JMapViewer %{name}

%install
%mvn_install

%files -f .mfiles
%doc Readme.txt Gpl.txt

%files javadoc -f .mfiles-javadoc
%doc Gpl.txt


%changelog
* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_6jpp8
- sisyphus build

