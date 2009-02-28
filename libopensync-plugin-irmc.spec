Name: 	 	libopensync-plugin-irmc
Version: 	0.22
Epoch:		1
Release: 	%mkrel 3
Summary: 	IRMC plugin for OpenSync synchronization framework
License:	GPLv2
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	openobex-devel
Requires:	libopensync >= %{epoch}:%{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise to and from
Sony Ericsson phones.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
