Sphinx와 Read the Docs 연계하여 문서화 작업하기
=================================================

일단 다음과 같은 명령어를 통해 파이썬 가상 환경을 만들고, 필요한 패키지를 설치합니다.::

    python -m venv .vRtd # 가상환경 관련 폴더를 .vRtd로 지정함 
    source venv/bin/activate  # On Windows use `.vRtd\Scripts\activate`
    pip install sphinx sphinx_rtd_theme # sphinx 패키지와 Read the Docs 테마 설치

이후 설치된 sphinx 패키지를 이용하기 위해 아래 명령을 통해 필요한 폴더 구조 파일 등을 만든다.::

    sphinx-quickstart

이후 생성된 conf.py 파일을 열어 테마를 지정해 준다.::

    html_theme = "sphinx_rtd_theme" # conf.py 파일에서 html_theme 항목을 찾아 위와 같이 수정
   
마지막으로 빌드 명령어를 통해 HTML 문서를 생성한다.::
   
    make html

이후 생성된 HTML 문서는 _build/html/index.html 파일을 열어 확인할 수 있으며, 
github와 Read the Docs를 연계하여 자동으로 문서화 작업을 수행할 수 있다. 
또한 필요한 경우 .readthedocs.yaml 파일을 프로젝트 루트에 생성하여 빌드 과정을 
커스터마이징 할 수도 있으며, conf.py 내부에 extention 등을 추가할 수 있다. 

rst 파일에서 사용하는 다양한 방식에 대한 설명
=============================================

다음 사항은 reStructuredText(rst) 파일에서 별도의 html을 만들어 주는 toctree 방식의 예시이다. ::

  .. toctree::        # rst 파일에서 toctree 방식을 사용할 때는 다음과 같이 작성한다.
     :maxdepth: 2     # toctree의 최대 깊이를 2로 지정 
     :caption: Contents: # toctree의 캡션을 Contents로 지정

     mydoctree # rst 파일에서 mydoctree 문서를 포함시키고 2개 깊이까지 목차화 시킨다.   
     anotherfile # rst 파일에서 anotherfile 문서를 포함시키고 마찬가지로 2개 깊이까지 목차화 시킨다. 

