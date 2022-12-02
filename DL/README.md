## error solution

* vscode include path update

1. msys2 install
https://www.msys2.org/
2. pacman -Syu > y
3. pacman -Su
4. pacman -S mingw-w64-x86_64-gcc
   pacman -S mingw-w64-x86_64-toolchain
5. 시스템 환경 변수 편집 -> 고급탭 -> 환경변수(N) -> 사용자변수와 시스템변수 각각 path
6. msys64\mingw64\bin , msys64\usr\bin
7. cmd > gcc -v
8. includePath > intelliSense > gcc-x64
9. includePath > 항목 추가
10. git bash > gcc -v 확인 > root 접근해서 gcc 파일명 으로 접근 가능
11. a.exe 파일 실행으로 결과 확인 가능
