@echo off

type %~dp0\template.cpp >> .\%1.cpp
type NUL > .\%1.inp
type NUL > .\%1.sout