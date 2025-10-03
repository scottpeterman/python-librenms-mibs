from pysmi.reader import FileReader
from pysmi.searcher import StubSearcher
from pysmi.writer import PyFileWriter
from pysmi.parser import SmiStarParser
from pysmi.codegen import PySnmpCodeGen
from pysmi.compiler import MibCompiler

compiler = MibCompiler(SmiStarParser(), PySnmpCodeGen(), PyFileWriter('test_out'))
compiler.add_sources(FileReader('mibs'))
compiler.add_sources(FileReader('mibs/cisco'))
compiler.add_searchers(StubSearcher(*PySnmpCodeGen.baseMibs))

results = compiler.compile('CISCO-SMI')
print(results)