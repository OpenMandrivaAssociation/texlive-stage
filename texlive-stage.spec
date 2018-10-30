Name:		texlive-stage
Version:	1.00
Release:	3
Summary:	A LaTeX class for stage plays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stage
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stage.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Stage.cls is a LaTeX class for creating plays of any length in
a standard manuscript format for production and submission.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stage
%doc %{_texmfdistdir}/doc/latex/stage

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
