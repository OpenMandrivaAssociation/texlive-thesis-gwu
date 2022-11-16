Name:		texlive-thesis-gwu
Version:	54287
Release:	1
Summary:	Thesis class for George Washington University School of Engineering and Applied Science
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thesis-gwu
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-gwu.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-gwu.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class is an attempt to create a standard format for GWU
SEAS dissertations/theses. It automatically handles many of the
complicated formatting requirements and includes many useful
packages. An example thesis is provided serving as a user guide
and a demonstration of the thesis.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/thesis-gwu
%doc %{_texmfdistdir}/doc/latex/thesis-gwu

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
