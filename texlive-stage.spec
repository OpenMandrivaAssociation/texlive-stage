# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/stage
# catalog-date 2006-11-06 12:20:58 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-stage
Version:	20061106
Release:	1
Summary:	A LaTeX class for stage plays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stage
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stage.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Stage.cls is a LaTeX class for creating plays of any length in
a standard manuscript format for production and submission.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stage/stage.cls
%doc %{_texmfdistdir}/doc/latex/stage/README
%doc %{_texmfdistdir}/doc/latex/stage/stage-documentation.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
