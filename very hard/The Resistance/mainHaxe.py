import sys

import math as python_lib_Math
import math as Math
import inspect as python_lib_Inspect
import sys as python_lib_Sys
import functools as python_lib_Functools
import time as python_lib_Time
import timeit as python_lib_Timeit
import traceback as python_lib_Traceback
from threading import Semaphore as Lock
from threading import RLock as sys_thread__Mutex_NativeRLock
import threading


class _hx_AnonObject:
    _hx_disable_getattr = False
    def __init__(self, fields):
        self.__dict__ = fields
    def __repr__(self):
        return repr(self.__dict__)
    def __contains__(self, item):
        return item in self.__dict__
    def __getitem__(self, item):
        return self.__dict__[item]
    def __getattr__(self, name):
        if (self._hx_disable_getattr):
            raise AttributeError('field does not exist')
        else:
            return None
    def _hx_hasattr(self,field):
        self._hx_disable_getattr = True
        try:
            getattr(self, field)
            self._hx_disable_getattr = False
            return True
        except AttributeError:
            self._hx_disable_getattr = False
            return False



class Enum:
    _hx_class_name = "Enum"
    __slots__ = ("tag", "index", "params")
    _hx_fields = ["tag", "index", "params"]
    _hx_methods = ["__str__"]

    def __init__(self,tag,index,params):
        self.tag = tag
        self.index = index
        self.params = params

    def __str__(self):
        if (self.params is None):
            return self.tag
        else:
            return self.tag + '(' + (', '.join(str(v) for v in self.params)) + ')'



class Class: pass


class CodinGame:
    _hx_class_name = "CodinGame"
    __slots__ = ()
    _hx_statics = ["print", "printErr"]

    @staticmethod
    def print(output):
        print(output)

    @staticmethod
    def printErr(output):
        print(output, file=python_lib_Sys.stderr)
        return python_lib_Sys.platform


class Lambda:
    _hx_class_name = "Lambda"
    __slots__ = ()
    _hx_statics = ["iter"]

    @staticmethod
    def iter(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            f(x.next())


class _Main_Main_Fields_:
    _hx_class_name = "_Main.Main_Fields_"
    __slots__ = ()
    _hx_statics = ["encoding", "sequence", "wordCodes", "codeWords", "subResults", "codeLengths", "main", "process", "createWordCodes", "search"]
    sequence = None
    subResults = None
    codeLengths = None

    @staticmethod
    def main():
        l = '.-...-.-...--......--....------.-.....---..--.-.----...-----.-.........-..--.-.-.----....--...-.--.--.--.--...-.-..--....--.--.-....--.-.-..--..-...-..-...-.......-.......-....--.--...-.-.......----....-.-.---..-.-.-.....-.-..----.--...-....--.-..-..-...-.........---...-.-.--..-.----....-..-.....--..-.-.-...........--.-.......--...-....---...-..---..-..--.--.....-.-.-..-.-.----.......-..-..-.----.--.-.-.---.-...-.....-....---..-..-..-----.-......-.-..---.-....--.-..-..--..-....-........-.-.....--...-....----.-......-...---.-...-.....-.-.-...----..-...........-.--.-.-.-....-..-..-.....-.-...-....-....-.-.-.-..--.---..-.-..-...--.-..--..-..-.--........-.-..-.-.----...---..-...-.-..-.-..--.-.-.-......-........--.-..-.-......---.-..-..-...--.-..-.-.........-...-..-...-.....--.-..-....--.----.-.-.-..-.--..----...--..-.-.------.....-..-.....----...--...--.-..-.-........--.-..-..--..-..-.-..-.--..--.-.-....-...-.-.----...-----.-.........--.-.----......-...-.-.-.-------..-....--..-.-.-...-.-.......-.-.-......-.-.-------..--...-.-..--..----....-...---.-...--.-..-.....-..-.------..-.-.-........-...-...-----.-.........-.--..-...-.-.-....--..-.-...--.-.-..--...-........--..-.-..-......--...-....-.-...-.....-.-.-------.------.--.-.-...-.-..--....--..........----....---..-...-.-.--.-.........-...-..-...-..-......--.-..-.-...--.....-...-.-......-...-...--.---..-.-.-.-...-.-.-..-.....--..........----....-.-..-.-..--.-.-.-...-..-------.--..--.-..-..-..--....----....-.-............-..-...-...--..----...-.-....-.-..--....-.-...-.--..--...-..-.........-.--..----....--.-.-...-..--....-......--.--...-.-......-.-..-.-..--..----..-..--..-....---.-..-..-----......-------..--.-..-....---..--......-..-.-.-.---.-...--.---..-.-..-...-.....--.-..-.-........--..----.--.-.-...-..--..--..-.-.-.-...-.-.-..-....-.-..--.....--.----.-.....-.-.....-..--...-.-..-..-....--..--....-....-...--.-..-----.-......--..-.-..-..-.--.--..-....-...-.-...--.-...--.-..--....--.......--..-.-...--.-..-....-....-...---..-....-...-..-.---.-.--......--.-.....-......-..--..-....-..-......-...-----.-.........---..-.-...--.-.-.--..-..--..--.-..-.--..-.-.-.......---.--...-.-....-.-.-------.-...-.------....-....--..-.-..--....---.---.--...-.-.......-.-.---..--...-----.-........----.---.-...-.-....---..-....--..-.--..-..----.--....-.-....---..-.-.-...--...-......-....-----.-......-....---..-....--..-.-...-.-.----....--....---.-..-.-..--.....--.---.-.-...-...-..--......--.-..-.-...-..--....---.--...-.--.--..-.---.-..-..-..----..-.-...-....---..--...-.-----.-...-.-.----.-..-...-.---..--.-.----.-..-...----..-....--.-...-..-..--.--..-...-.....--.-..-..-.-...--.-.-.--....-.--..-.-.-..--..--....--.--...-.-.......----..-...-.-.-.-...--.-..-.-.-..-...-..-......--.-.-.-....-...-.-..--..-..-.--.......--.-..-.-.-.....-..-.-..-...-.---....------..-.-......--......--.-..-.-..---.-..--...--.-..-.---..-...-.......-..-....-..-...-........-....---..-....--..-.-....-...--.-..-...--..-......-....-...-...--...---.-..--..----.-....--.-.----...-----.-.........--...-.-.----....-..-......-.-..-.-..--.-.-.-.......-..-.--.-..-.-.-....-...-.-.-..--....--........--.-..-..--..-.--...-.-.----....-..-..-.....-.--.-.-...........-.-.-.........--.-..-.-.-.-......--..-....-....-..----.--...-.....-......-.-..-.-..--.-.-.-.....--.-..-...-.....-...-.-..-.-.--..-....-....-..-.-..--.-.-.--..-.-..-..-.--.--..-....-.....-...--.-..-.-......-..-.--.-..-.-.-.....--.-.----...--..-.-...--......--.--..-....--.---..-.-.-....--..-....-...-....-....-.-...----..-....-...........--.-......-.......-..--.-......-...--.-........----.-----..--....-.-.----...........-.-.--.-..-.--.-.......--.-..-..--..-.-..---.--..-..--..---.-......-.-.........-...-..-..........-.-.-.-...-.--.-.....--.-..-..--..-.-.........--.-..-.-.-.-......--..-....-....-..----.--...-....-.-.---.-..-......--.----.-...-.--.........-.-----...---.-.......-.......--..-....-....-..-.-..........--.-.....-....--.----.-.-.-..-.--..----....-.-----...---.-.......--.-..-.-..--.-.-.-.........--.-.-....-..--..-.--..-.-..-.-...-...-...--.-.-.-..--.-.----...-----.-.....-.......--....-....-...--..----....-.-.-------..-.-.-....-.-.......--..-....-....-...--...---.-.....----.---.-..-.....-.-.----...--.--.......--......-..-.......-.-.-----.--..-..-.....-...--.......-.-..--------..-.---..-.--..-....-...--.-......-......---.--..-..--...-.-....-...-.-..--..-..-.--........-.-.----....-..-.....-...-.-.-.-..---.-.....-...--...-........--.--......------...-..-.....--.-..-.-...-.------..----.-.-..-.-----..--.-.-.--..-.--.-----.-..-..-.--.-..---..-----..-...-.-....---..--.--.--....-.---..----.-----..--.----.--.....--..-.---.----.-..-....-..----..-.--.---.--.-....--.-----.-..-....-.-..-..-.---.-.----...-...-...--...-------.-..-.-..-....-.-..-..-.--.-....-.-.-.-..----.-...-.-.....-.-.----......-.-..--..---.--.-..--.......-..-...-.-.-----......-.-..--....--..........----.........-.-..-......-.-.-....-.......-.......-..--....---.---.--...-.-......--...-........-.-----..-.------..-.-....-.-...-.-.-..-....-.-.----.......-.--..--...-.....-.-.----...--.-.--.-.----...--.....-........----.-..--...-...........--..-.-..-......---.--..-..--...-.-.....-..-...-.-......-.-......--.--...-.-........-...-.---.-.--.--..----.....-.-.-...-.-..-..-.-.....--.---.-.-.--.-.--..-.-..-..-.--.--..-........-.-..-...---.-..-.-.-....--....-...-.-.....-.....----..-......-.-......--.--..--.-.-...-.....-..-.--.-..-.-.-.-......-.-......-.-..--..-..-----.....-.......--..-..--...-......-.....-.....----.....-..--....----.-..--..-..-.--.......--.-..-........--......-....-....--...-........--.-.-...-.-.----...-----.-.....-...--.-.--....--..-.....---....--..--..-......-.-..-....-..-...--.-.----...-..-..-.-.-..-...-.....-..-....-..---.-...-.....-..-...-.-..----.--...-...-.-.-..----.-...-...---.-.....-.-....--...-..--.-..-..-...-.-..-..-..--....----.-..--..-..-.--........-----.-......-.--..-..----..-...-...-.-....-.-.........-........--.-..-.-.....---...-.-.-------..-.--..--...-..-...-..-.-..........---..-...--.-..-.-..--..-....-........-.-....-.-.----...-..-..-.-.-.....------.-.....-.-......-.......-..--....----.-.-------..--...-.-..--..----....-....-...-..........-.-.-......-....--.-........--...-.........-..--.---..-.-..-......-.-.-------..--...-.-..--..----.....-.-.-..--..-..-.--........-----.-.....-....--...-......-.....-...-....-.-.....-.-...--.....-...-.-..--...-..-....-...---.....--.-...........-....-..-.-.....--.-.-...-..--....-.-.-....-.....-------......-......-.....-..-..--.-.-...--...-.------....-....--..-.-..--.-......--..--.--...----.-.--....--.-..----.-..-...-...-....-...-....-..--....----.-..--..-..-.--.......--.-..-.----....-....--..-----...-...--.-.........-......--..........----.....-.-----.-.....-.----.-----.-.-.....-.-..-...-..-..-.--.-..-.-.-.-..-...-.-....--..--.-.-...-..--..-.-.-.----..-..--..--.-..-..-.....-.-..-...-..-..-.--.-..-.-.-.-..-...-.-....--...-..-...-..-.-.-.....-..--.-..-..-...-.-.-...-..-.-.........---..--...-.--..--...-...-..-..--....----.-..--..-..-.--........-....--...-......-.......--.-.......--....-.--...---.-.......--..-...-....-....-...-.-..-.-.-------..--...-.-..--..----..--.--.--.-.--..-.......-....-...-...-......--..-.-.-...-.-...-.-..-------.-.-.-...-.-..-..-...-.-.--.-.-...-..--..-..--....----.-..--..-..-.--.......--.-..-..-.-..--....----.-...--.....----...--.-..-...--...-........--.-.-......----.-............-.---.....-.-.....-.-.-------.-.-.-..-..-.-..-....-...-..-...-.-.--.-.--.-...--..-.-...--.-...-...-..-.....-..-.-.-.---.-..-.-...------..-.-.-........-..-.--.-..-.-.-.-.......-.-..-.-..--..----..-.-.......-..-...-..-.-.-.....--..-.-..-....-..-.-...--......-...-...-.....----.-....-.........-.-..-....-...---------.-.-...-..---..-.-..--..--.-.-------..--...-.-..--..----....--.-.-...-..--.....-..-..--....----.-..--..-..-.--.........--..-.-.--..-...-..--.-.....-.-....--..-.-....--..---..--.-....--..-.-....--...--.---..-...-.--.-.-..-........-.-....--...-........--..-.-..-...-...-...--..----.-.-......-...-....-...--....--.-...-......---.-.....-.----.-----.-.-.-.....-...--...-.........--..-.-...--.....-..-.--.-.-..-..-....--..--.--...-...--.....-...------.-....--..-.-.--...-......--.-..-..-......-...-.-..--..........----..--....-..-...-.-.--..-.-..-...-...---....-.-....--...---.--..-...-.-..---..-.---..--..-...--.-.......-...-...-.-..--...--....-....--.-..-.-....--.-.----.--.----...---..-...---..--...-...-.-.---.....-...-......-.--.....--.......-....-.-..----........-....-.-.-......-.....-..-...--.-...-----.--..-...-.-.---..---.--.....-...-..-.-...-..--..----.-....-...-..........-..........------.-.---.-...-.-..-..-......-.-..........-.---.-.......-...-......--.-..-..-..--.-..-.....-..--.-...--.-..----.....--..-.....-...-.--..-....-.--..-.-.--.........-.--..----....--.-.-...-..--.....-.-.-.---.-...-..--.-.-.....-..--.--.--.-.-.--..-....-....-.-----.-.....--.-..-..-.....-.-...-.-....-.-..--....-.-...-.--..--...-...-...-.-.-..-..-...-...--.-.-.-.....-.-...-..-.--.-..-.-.-.-..-..--..........----..-..-.------..-.-.-........-..-.-...-.-.-..-.......-..-.--.-..-.-.-.-.....-......-..-......-..--.-..-..-...-.-..-.-.-..---....-...---.-.-...-..--.-.-.-.-......--.-...----.-.-.-.-.---.-....--...-..-...-..-.-.-.--..----.----........-...-......-.....----.-.--..-....-.....--...-...........--.-..-..--..-.-.--.-..-..-..--.-..-.....--..--.--....--.-.....-..-.-..--.-.--....--...-......-...-..-.....---....--..--..-......-.-..-....-.-....-....-.-.-..----.-....-...-.-...---.--...-.-..-........-......-....--..-..--..-.--....-...-.-.---..-.-...--.-.--.-.-------..--...--.-..-..-..-.-----.-......-....---..-....--..-.-.-..---.-....--.-..-..-...--.-..-.--..--.-...---.--.-..-...-..-..........--.-..-..--..-.-.....-..-..-..--...--.---..-.-.-......-.-....-.---..-...-...-.-.....-.-....-...---.-.-...-..--.-.-.-.-......--.-...-...--....-...-.------....-....--..-.--..--.--...-..----.-.-...-..-..-..--.-.-..'
        n=9444;wortList=[] #4 erg = 57.330.892.800
        _g = []
        f = open("C:\\Users\\marku\\Python\\codingame\\very hard\\The Resistance\\input4.txt","r")
        for x in f:
            _g.append(x[:-1])
        f.close()

        inputSequence = l
        
        CodinGame.print(_Main_Main_Fields_.process(inputSequence,_g))

    @staticmethod
    def process(inputSequence,words):
        start = python_lib_Timeit.default_timer()
        _Main_Main_Fields_.sequence = inputSequence
        _Main_Main_Fields_.wordCodes.h.clear()
        _Main_Main_Fields_.codeWords.h.clear()
        _g = []
        _g1 = 0
        _g2 = len(_Main_Main_Fields_.sequence)
        while (_g1 < _g2):
            _g1 = (_g1 + 1)
            _g.append(-1)
        _Main_Main_Fields_.subResults = _g
        _Main_Main_Fields_.codeLengths = []
        def _hx_local_1(word):
            _Main_Main_Fields_.createWordCodes(word)
        Lambda.iter(words,_hx_local_1)
        wordCode = _Main_Main_Fields_.wordCodes.keys()
        while wordCode.hasNext():
            wordCode1 = wordCode.next()
            if (not (len(wordCode1) in _Main_Main_Fields_.codeLengths)):
                x = len(wordCode1)
                _Main_Main_Fields_.codeLengths.append(x)
        def _hx_local_2(a,b):
            return (a - b)
        _Main_Main_Fields_.codeLengths.sort(key= python_lib_Functools.cmp_to_key(_hx_local_2))
        result = _Main_Main_Fields_.search(0)
        def _hx_local_3(v):
            if (v == -1):
                return "."
            else:
                return ("" + Std.string(v))
        _this = list(map(_hx_local_3,_Main_Main_Fields_.subResults))
        " ".join([python_Boot.toString1(x1,'') for x1 in _this])
        CodinGame.printErr((("Duration " + Std.string(Math.floor(((((python_lib_Timeit.default_timer() - start)) * 1000) + 0.5)))) + "ms"))
        return result

    @staticmethod
    def createWordCodes(word):
        wordCode = ""
        _g = 0
        _g1 = len(word)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            key = ("" if (((i < 0) or ((i >= len(word))))) else word[i])
            wordCode = (("null" if wordCode is None else wordCode) + HxOverrides.stringOrNull(_Main_Main_Fields_.encoding.h.get(key,None)))
        if (_Main_Main_Fields_.sequence.find(wordCode) == -1):
            return
        if (wordCode in _Main_Main_Fields_.wordCodes.h):
            tmp = wordCode
            tmp1 = _Main_Main_Fields_.wordCodes.h.get(tmp,None)
            _Main_Main_Fields_.wordCodes.h[tmp] = (tmp1 + 1)
            _Main_Main_Fields_.codeWords.h.get(wordCode,None).append(word)
        else:
            _Main_Main_Fields_.wordCodes.h[wordCode] = 1
            _Main_Main_Fields_.codeWords.h[wordCode] = [word]

    @staticmethod
    def search(offset):
        if (offset == len(_Main_Main_Fields_.sequence)):
            return 1
        if (python_internal_ArrayImpl._get(_Main_Main_Fields_.subResults, offset) != -1):
            return python_internal_ArrayImpl._get(_Main_Main_Fields_.subResults, offset)
        result = 0
        _g = 0
        _g1 = _Main_Main_Fields_.codeLengths
        while (_g < len(_g1)):
            i = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if ((offset + i) > len(_Main_Main_Fields_.sequence)):
                return result
            subSequence = HxString.substr(_Main_Main_Fields_.sequence,offset,i)
            if (subSequence in _Main_Main_Fields_.wordCodes.h):
                result = (result + ((_Main_Main_Fields_.wordCodes.h.get(subSequence,None) * _Main_Main_Fields_.search((offset + i)))))
        python_internal_ArrayImpl._set(_Main_Main_Fields_.subResults, offset, result)
        return result


class Std:
    _hx_class_name = "Std"
    __slots__ = ()
    _hx_statics = ["isOfType", "string", "parseInt"]

    @staticmethod
    def isOfType(v,t):
        if ((v is None) and ((t is None))):
            return False
        if (t is None):
            return False
        if ((type(t) == type) and (t == Dynamic)):
            return (v is not None)
        isBool = isinstance(v,bool)
        if (((type(t) == type) and (t == Bool)) and isBool):
            return True
        if ((((not isBool) and (not ((type(t) == type) and (t == Bool)))) and ((type(t) == type) and (t == Int))) and isinstance(v,int)):
            return True
        vIsFloat = isinstance(v,float)
        tmp = None
        tmp1 = None
        if (((not isBool) and vIsFloat) and ((type(t) == type) and (t == Int))):
            f = v
            tmp1 = (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
        else:
            tmp1 = False
        if tmp1:
            tmp1 = None
            try:
                tmp1 = int(v)
            except BaseException as _g:
                None
                tmp1 = None
            tmp = (v == tmp1)
        else:
            tmp = False
        if ((tmp and ((v <= 2147483647))) and ((v >= -2147483648))):
            return True
        if (((not isBool) and ((type(t) == type) and (t == Float))) and isinstance(v,(float, int))):
            return True
        if ((type(t) == type) and (t == str)):
            return isinstance(v,str)
        isEnumType = ((type(t) == type) and (t == Enum))
        if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
            return True
        if isEnumType:
            return False
        isClassType = ((type(t) == type) and (t == Class))
        if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
            return True
        if isClassType:
            return False
        tmp = None
        try:
            tmp = isinstance(v,t)
        except BaseException as _g:
            None
            tmp = False
        if tmp:
            return True
        if python_lib_Inspect.isclass(t):
            cls = t
            loop = None
            def _hx_local_1(intf):
                f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                if (f is not None):
                    _g = 0
                    while (_g < len(f)):
                        i = (f[_g] if _g >= 0 and _g < len(f) else None)
                        _g = (_g + 1)
                        if (i == cls):
                            return True
                        else:
                            l = loop(i)
                            if l:
                                return True
                    return False
                else:
                    return False
            loop = _hx_local_1
            currentClass = v.__class__
            result = False
            while (currentClass is not None):
                if loop(currentClass):
                    result = True
                    break
                currentClass = python_Boot.getSuperClass(currentClass)
            return result
        else:
            return False

    @staticmethod
    def string(s):
        return python_Boot.toString1(s,"")

    @staticmethod
    def parseInt(x):
        if (x is None):
            return None
        try:
            return int(x)
        except BaseException as _g:
            None
            base = 10
            _hx_len = len(x)
            foundCount = 0
            sign = 0
            firstDigitIndex = 0
            lastDigitIndex = -1
            previous = 0
            _g = 0
            while (_g < _hx_len):
                i = _g
                _g = (_g + 1)
                c = (-1 if ((i >= len(x))) else ord(x[i]))
                if (((c > 8) and ((c < 14))) or ((c == 32))):
                    if (foundCount > 0):
                        return None
                    continue
                else:
                    c1 = c
                    if (c1 == 43):
                        if (foundCount == 0):
                            sign = 1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 45):
                        if (foundCount == 0):
                            sign = -1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 48):
                        if (not (((foundCount == 0) or (((foundCount == 1) and ((sign != 0))))))):
                            if (not (((48 <= c) and ((c <= 57))))):
                                if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                    break
                    elif ((c1 == 120) or ((c1 == 88))):
                        if ((previous == 48) and ((((foundCount == 1) and ((sign == 0))) or (((foundCount == 2) and ((sign != 0))))))):
                            base = 16
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (not (((48 <= c) and ((c <= 57))))):
                        if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                            break
                if (((foundCount == 0) and ((sign == 0))) or (((foundCount == 1) and ((sign != 0))))):
                    firstDigitIndex = i
                foundCount = (foundCount + 1)
                lastDigitIndex = i
                previous = c
            if (firstDigitIndex <= lastDigitIndex):
                digits = HxString.substring(x,firstDigitIndex,(lastDigitIndex + 1))
                try:
                    return (((-1 if ((sign == -1)) else 1)) * int(digits,base))
                except BaseException as _g:
                    return None
            return None


class Float: pass


class Int: pass


class Bool: pass


class Dynamic: pass


class haxe_IMap:
    _hx_class_name = "haxe.IMap"
    __slots__ = ()


class haxe_Exception(Exception):
    _hx_class_name = "haxe.Exception"
    __slots__ = ("_hx___nativeStack", "_hx___nativeException", "_hx___previousException")
    _hx_fields = ["__nativeStack", "__nativeException", "__previousException"]
    _hx_methods = ["unwrap"]
    _hx_statics = ["caught"]
    _hx_interfaces = []
    _hx_super = Exception


    def __init__(self,message,previous = None,native = None):
        self._hx___previousException = None
        self._hx___nativeException = None
        self._hx___nativeStack = None
        super().__init__(message)
        self._hx___previousException = previous
        if ((native is not None) and Std.isOfType(native,BaseException)):
            self._hx___nativeException = native
            self._hx___nativeStack = haxe_NativeStackTrace.exceptionStack()
        else:
            self._hx___nativeException = self
            infos = python_lib_Traceback.extract_stack()
            if (len(infos) != 0):
                infos.pop()
            infos.reverse()
            self._hx___nativeStack = infos

    def unwrap(self):
        return self._hx___nativeException

    @staticmethod
    def caught(value):
        if Std.isOfType(value,haxe_Exception):
            return value
        elif Std.isOfType(value,BaseException):
            return haxe_Exception(str(value),None,value)
        else:
            return haxe_ValueException(value,None,value)



class haxe_NativeStackTrace:
    _hx_class_name = "haxe.NativeStackTrace"
    __slots__ = ()
    _hx_statics = ["saveStack", "exceptionStack"]

    @staticmethod
    def saveStack(exception):
        pass

    @staticmethod
    def exceptionStack():
        exc = python_lib_Sys.exc_info()
        if (exc[2] is not None):
            infos = python_lib_Traceback.extract_tb(exc[2])
            infos.reverse()
            return infos
        else:
            return []


class haxe_ValueException(haxe_Exception):
    _hx_class_name = "haxe.ValueException"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["unwrap"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,value,previous = None,native = None):
        self.value = None
        super().__init__(Std.string(value),previous,native)
        self.value = value

    def unwrap(self):
        return self.value



class haxe_ds_ObjectMap:
    _hx_class_name = "haxe.ds.ObjectMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value



class haxe_ds_StringMap:
    _hx_class_name = "haxe.ds.StringMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["keys"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))



class haxe_iterators_ArrayIterator:
    _hx_class_name = "haxe.iterators.ArrayIterator"
    __slots__ = ("array", "current")
    _hx_fields = ["array", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return python_internal_ArrayImpl._get(self.array, _hx_local_2())
        return _hx_local_3()



class python_Boot:
    _hx_class_name = "python.Boot"
    __slots__ = ()
    _hx_statics = ["keywords", "toString1", "fields", "simpleField", "getInstanceFields", "getSuperClass", "getClassFields", "prefixLength", "unhandleKeywords"]

    @staticmethod
    def toString1(o,s):
        if (o is None):
            return "null"
        if isinstance(o,str):
            return o
        if (s is None):
            s = ""
        if (len(s) >= 5):
            return "<...>"
        if isinstance(o,bool):
            if o:
                return "true"
            else:
                return "false"
        if (isinstance(o,int) and (not isinstance(o,bool))):
            return str(o)
        if isinstance(o,float):
            try:
                if (o == int(o)):
                    return str(Math.floor((o + 0.5)))
                else:
                    return str(o)
            except BaseException as _g:
                None
                return str(o)
        if isinstance(o,list):
            o1 = o
            l = len(o1)
            st = "["
            s = (("null" if s is None else s) + "\t")
            _g = 0
            _g1 = l
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                prefix = ""
                if (i > 0):
                    prefix = ","
                st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
            st = (("null" if st is None else st) + "]")
            return st
        try:
            if hasattr(o,"toString"):
                return o.toString()
        except BaseException as _g:
            None
        if hasattr(o,"__class__"):
            if isinstance(o,_hx_AnonObject):
                toStr = None
                try:
                    fields = python_Boot.fields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
                except BaseException as _g:
                    None
                    return "{ ... }"
                if (toStr is None):
                    return "{ ... }"
                else:
                    return toStr
            if isinstance(o,Enum):
                o1 = o
                l = len(o1.params)
                hasParams = (l > 0)
                if hasParams:
                    paramsStr = ""
                    _g = 0
                    _g1 = l
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        prefix = ""
                        if (i > 0):
                            prefix = ","
                        paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1(o1.params[i],s))))))
                    return (((HxOverrides.stringOrNull(o1.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
                else:
                    return o1.tag
            if hasattr(o,"_hx_class_name"):
                if (o.__class__.__name__ != "type"):
                    fields = python_Boot.getInstanceFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
                else:
                    fields = python_Boot.getClassFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
            if ((type(o) == type) and (o == str)):
                return "#String"
            if ((type(o) == type) and (o == list)):
                return "#Array"
            if callable(o):
                return "function"
            try:
                if hasattr(o,"__repr__"):
                    return o.__repr__()
            except BaseException as _g:
                None
            if hasattr(o,"__str__"):
                return o.__str__([])
            if hasattr(o,"__name__"):
                return o.__name__
            return "???"
        else:
            return str(o)

    @staticmethod
    def fields(o):
        a = []
        if (o is not None):
            if hasattr(o,"_hx_fields"):
                fields = o._hx_fields
                if (fields is not None):
                    return list(fields)
            if isinstance(o,_hx_AnonObject):
                d = o.__dict__
                keys = d.keys()
                handler = python_Boot.unhandleKeywords
                for k in keys:
                    if (k != '_hx_disable_getattr'):
                        a.append(handler(k))
            elif hasattr(o,"__dict__"):
                d = o.__dict__
                keys1 = d.keys()
                for k in keys1:
                    a.append(k)
        return a

    @staticmethod
    def simpleField(o,field):
        if (field is None):
            return None
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if hasattr(o,field1):
            return getattr(o,field1)
        else:
            return None

    @staticmethod
    def getInstanceFields(c):
        f = (list(c._hx_fields) if (hasattr(c,"_hx_fields")) else [])
        if hasattr(c,"_hx_methods"):
            f = (f + c._hx_methods)
        sc = python_Boot.getSuperClass(c)
        if (sc is None):
            return f
        else:
            scArr = python_Boot.getInstanceFields(sc)
            scMap = set(scArr)
            _g = 0
            while (_g < len(f)):
                f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
                _g = (_g + 1)
                if (not (f1 in scMap)):
                    scArr.append(f1)
            return scArr

    @staticmethod
    def getSuperClass(c):
        if (c is None):
            return None
        try:
            if hasattr(c,"_hx_super"):
                return c._hx_super
            return None
        except BaseException as _g:
            None
        return None

    @staticmethod
    def getClassFields(c):
        if hasattr(c,"_hx_statics"):
            x = c._hx_statics
            return list(x)
        else:
            return []

    @staticmethod
    def unhandleKeywords(name):
        if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
            real = HxString.substr(name,python_Boot.prefixLength,None)
            if (real in python_Boot.keywords):
                return real
        return name


class python_HaxeIterator:
    _hx_class_name = "python.HaxeIterator"
    __slots__ = ("it", "x", "has", "checked")
    _hx_fields = ["it", "x", "has", "checked"]
    _hx_methods = ["next", "hasNext"]

    def __init__(self,it):
        self.checked = False
        self.has = False
        self.x = None
        self.it = it

    def next(self):
        if (not self.checked):
            self.hasNext()
        self.checked = False
        return self.x

    def hasNext(self):
        if (not self.checked):
            try:
                self.x = self.it.__next__()
                self.has = True
            except BaseException as _g:
                None
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),StopIteration):
                    self.has = False
                    self.x = None
                else:
                    raise _g
            self.checked = True
        return self.has



class python_internal_ArrayImpl:
    _hx_class_name = "python.internal.ArrayImpl"
    __slots__ = ()
    _hx_statics = ["_get", "_set"]

    @staticmethod
    def _get(x,idx):
        if ((idx > -1) and ((idx < len(x)))):
            return x[idx]
        else:
            return None

    @staticmethod
    def _set(x,idx,v):
        l = len(x)
        while (l < idx):
            x.append(None)
            l = (l + 1)
        if (l == idx):
            x.append(v)
        else:
            x[idx] = v
        return v


class HxOverrides:
    _hx_class_name = "HxOverrides"
    __slots__ = ()
    _hx_statics = ["iterator", "eq", "stringOrNull"]

    @staticmethod
    def iterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayIterator(x)
        return x.iterator()

    @staticmethod
    def eq(a,b):
        if (isinstance(a,list) or isinstance(b,list)):
            return a is b
        return (a == b)

    @staticmethod
    def stringOrNull(s):
        if (s is None):
            return "null"
        else:
            return s


class python_internal_MethodClosure:
    _hx_class_name = "python.internal.MethodClosure"
    __slots__ = ("obj", "func")
    _hx_fields = ["obj", "func"]
    _hx_methods = ["__call__"]

    def __init__(self,obj,func):
        self.obj = obj
        self.func = func

    def __call__(self,*args):
        return self.func(self.obj,*args)



class HxString:
    _hx_class_name = "HxString"
    __slots__ = ()
    _hx_statics = ["substring", "substr"]

    @staticmethod
    def substring(s,startIndex,endIndex = None):
        if (startIndex < 0):
            startIndex = 0
        if (endIndex is None):
            return s[startIndex:]
        else:
            if (endIndex < 0):
                endIndex = 0
            if (endIndex < startIndex):
                return s[endIndex:startIndex]
            else:
                return s[startIndex:endIndex]

    @staticmethod
    def substr(s,startIndex,_hx_len = None):
        if (_hx_len is None):
            return s[startIndex:]
        else:
            if (_hx_len == 0):
                return ""
            if (startIndex < 0):
                startIndex = (len(s) + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            return s[startIndex:(startIndex + _hx_len)]


class sys_thread_EventLoop:
    _hx_class_name = "sys.thread.EventLoop"
    __slots__ = ("mutex", "oneTimeEvents", "oneTimeEventsIdx", "waitLock", "promisedEventsCount", "regularEvents")
    _hx_fields = ["mutex", "oneTimeEvents", "oneTimeEventsIdx", "waitLock", "promisedEventsCount", "regularEvents"]
    _hx_methods = ["loop"]

    def __init__(self):
        self.regularEvents = None
        self.promisedEventsCount = 0
        self.waitLock = sys_thread_Lock()
        self.oneTimeEventsIdx = 0
        self.oneTimeEvents = list()
        self.mutex = sys_thread_Mutex()

    def loop(self):
        recycleRegular = []
        recycleOneTimers = []
        while True:
            now = python_lib_Time.time()
            eventsToRunIdx = 0
            nextEventAt = -1
            self.mutex.lock.acquire(True)
            while self.waitLock.semaphore.acquire(True,0.0):
                pass
            current = self.regularEvents
            while (current is not None):
                if (current.nextRunTime <= now):
                    tmp = eventsToRunIdx
                    eventsToRunIdx = (eventsToRunIdx + 1)
                    python_internal_ArrayImpl._set(recycleRegular, tmp, current)
                    current.nextRunTime = (current.nextRunTime + current.interval)
                    nextEventAt = -2
                elif ((nextEventAt == -1) or ((current.nextRunTime < nextEventAt))):
                    nextEventAt = current.nextRunTime
                current = current.next
            self.mutex.lock.release()
            _g = 0
            _g1 = eventsToRunIdx
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (not (recycleRegular[i] if i >= 0 and i < len(recycleRegular) else None).cancelled):
                    (recycleRegular[i] if i >= 0 and i < len(recycleRegular) else None).run()
                python_internal_ArrayImpl._set(recycleRegular, i, None)
            eventsToRunIdx = 0
            self.mutex.lock.acquire(True)
            _this = self.oneTimeEvents
            _g2_current = 0
            while (_g2_current < len(_this)):
                _g3_value = (_this[_g2_current] if _g2_current >= 0 and _g2_current < len(_this) else None)
                _g3_key = _g2_current
                _g2_current = (_g2_current + 1)
                if (_g3_value is None):
                    break
                else:
                    tmp1 = eventsToRunIdx
                    eventsToRunIdx = (eventsToRunIdx + 1)
                    python_internal_ArrayImpl._set(recycleOneTimers, tmp1, _g3_value)
                    python_internal_ArrayImpl._set(self.oneTimeEvents, _g3_key, None)
            self.oneTimeEventsIdx = 0
            hasPromisedEvents = (self.promisedEventsCount > 0)
            self.mutex.lock.release()
            _g2 = 0
            _g3 = eventsToRunIdx
            while (_g2 < _g3):
                i1 = _g2
                _g2 = (_g2 + 1)
                (recycleOneTimers[i1] if i1 >= 0 and i1 < len(recycleOneTimers) else None)()
                python_internal_ArrayImpl._set(recycleOneTimers, i1, None)
            if (eventsToRunIdx > 0):
                nextEventAt = -2
            r_nextEventAt = nextEventAt
            if (r_nextEventAt == -2):
                pass
            elif (r_nextEventAt == -1):
                if hasPromisedEvents:
                    self.waitLock.semaphore.acquire(True,None)
                else:
                    break
            else:
                timeout = (r_nextEventAt - python_lib_Time.time())
                _this1 = self.waitLock
                timeout1 = (0 if (python_lib_Math.isnan(0)) else (timeout if (python_lib_Math.isnan(timeout)) else max(0,timeout)))
                _this1.semaphore.acquire(True,timeout1)



class sys_thread__EventLoop_RegularEvent:
    _hx_class_name = "sys.thread._EventLoop.RegularEvent"
    __slots__ = ("nextRunTime", "interval", "run", "next", "cancelled")
    _hx_fields = ["nextRunTime", "interval", "run", "next", "cancelled"]

    def __init__(self,run,nextRunTime,interval):
        self.next = None
        self.cancelled = False
        self.run = run
        self.nextRunTime = nextRunTime
        self.interval = interval



class sys_thread_Lock:
    _hx_class_name = "sys.thread.Lock"
    __slots__ = ("semaphore",)
    _hx_fields = ["semaphore"]

    def __init__(self):
        self.semaphore = Lock(0)



class sys_thread_Mutex:
    _hx_class_name = "sys.thread.Mutex"
    __slots__ = ("lock",)
    _hx_fields = ["lock"]

    def __init__(self):
        self.lock = sys_thread__Mutex_NativeRLock()



class sys_thread__Thread_Thread_Impl_:
    _hx_class_name = "sys.thread._Thread.Thread_Impl_"
    __slots__ = ()
    _hx_statics = ["processEvents"]

    @staticmethod
    def processEvents():
        sys_thread__Thread_HxThread.current().events.loop()


class sys_thread__Thread_HxThread:
    _hx_class_name = "sys.thread._Thread.HxThread"
    __slots__ = ("events", "nativeThread")
    _hx_fields = ["events", "nativeThread"]
    _hx_statics = ["threads", "threadsMutex", "mainThread", "current"]

    def __init__(self,t):
        self.events = None
        self.nativeThread = t
    threads = None
    threadsMutex = None
    mainThread = None

    @staticmethod
    def current():
        sys_thread__Thread_HxThread.threadsMutex.lock.acquire(True)
        ct = threading.current_thread()
        if (ct == threading.main_thread()):
            sys_thread__Thread_HxThread.threadsMutex.lock.release()
            return sys_thread__Thread_HxThread.mainThread
        if (not (ct in sys_thread__Thread_HxThread.threads.h)):
            sys_thread__Thread_HxThread.threads.set(ct,sys_thread__Thread_HxThread(ct))
        t = sys_thread__Thread_HxThread.threads.h.get(ct,None)
        sys_thread__Thread_HxThread.threadsMutex.lock.release()
        return t


Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi
sys_thread__Thread_HxThread.threads = haxe_ds_ObjectMap()
sys_thread__Thread_HxThread.threadsMutex = sys_thread_Mutex()
sys_thread__Thread_HxThread.mainThread = sys_thread__Thread_HxThread(threading.current_thread())
sys_thread__Thread_HxThread.mainThread.events = sys_thread_EventLoop()

def _hx_init__Main_Main_Fields__encoding():
    def _hx_local_0():
        _g = haxe_ds_StringMap()
        _g.h["A"] = ".-"
        _g.h["B"] = "-..."
        _g.h["C"] = "-.-."
        _g.h["D"] = "-.."
        _g.h["E"] = "."
        _g.h["F"] = "..-."
        _g.h["G"] = "--."
        _g.h["H"] = "...."
        _g.h["I"] = ".."
        _g.h["J"] = ".---"
        _g.h["K"] = "-.-"
        _g.h["L"] = ".-.."
        _g.h["M"] = "--"
        _g.h["N"] = "-."
        _g.h["O"] = "---"
        _g.h["P"] = ".--."
        _g.h["Q"] = "--.-"
        _g.h["R"] = ".-."
        _g.h["S"] = "..."
        _g.h["T"] = "-"
        _g.h["U"] = "..-"
        _g.h["V"] = "...-"
        _g.h["W"] = ".--"
        _g.h["X"] = "-..-"
        _g.h["Y"] = "-.--"
        _g.h["Z"] = "--.."
        return _g
    return _hx_local_0()
_Main_Main_Fields_.encoding = _hx_init__Main_Main_Fields__encoding()
_Main_Main_Fields_.wordCodes = haxe_ds_StringMap()
_Main_Main_Fields_.codeWords = haxe_ds_StringMap()
python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")

_Main_Main_Fields_.main()
sys_thread__Thread_Thread_Impl_.processEvents()
