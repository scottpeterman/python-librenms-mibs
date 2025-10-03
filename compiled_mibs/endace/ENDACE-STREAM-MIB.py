# SNMP MIB module (ENDACE-STREAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\endace\ENDACE-STREAM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:59 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

(ModuleIndex,) = mibBuilder.importSymbols(
    "ENDACE-MODULE-MIB",
    "ModuleIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

streamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 10)
)
if mibBuilder.loadTexts:
    streamMIB.setRevisions(
        ("2019-08-22 01:47",
         "2017-11-01 23:51",
         "2013-10-08 19:34",
         "2009-05-21 23:46")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class StreamIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_StreamEvents_ObjectIdentity = ObjectIdentity
streamEvents = _StreamEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 10, 0)
)
_StreamObjects_ObjectIdentity = ObjectIdentity
streamObjects = _StreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1)
)
_StreamDropTable_Object = MibTable
streamDropTable = _StreamDropTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 1)
)
if mibBuilder.loadTexts:
    streamDropTable.setStatus("current")
_StreamDropEntry_Object = MibTableRow
streamDropEntry = _StreamDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 1, 1)
)
streamDropEntry.setIndexNames(
    (0, "ENDACE-STREAM-MIB", "streamDropModIndex"),
)
if mibBuilder.loadTexts:
    streamDropEntry.setStatus("current")
_StreamDropModIndex_Type = Unsigned32
_StreamDropModIndex_Object = MibTableColumn
streamDropModIndex = _StreamDropModIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 1, 1, 1),
    _StreamDropModIndex_Type()
)
streamDropModIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    streamDropModIndex.setStatus("current")


class _StreamDropModule_Type(ModuleIndex):
    """Custom type streamDropModule based on ModuleIndex"""
    subtypeSpec = ModuleIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StreamDropModule_Type.__name__ = "ModuleIndex"
_StreamDropModule_Object = MibTableColumn
streamDropModule = _StreamDropModule_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 1, 1, 2),
    _StreamDropModule_Type()
)
streamDropModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamDropModule.setStatus("current")


class _StreamDropEnabled_Type(Integer32):
    """Custom type streamDropEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_StreamDropEnabled_Type.__name__ = "Integer32"
_StreamDropEnabled_Object = MibTableColumn
streamDropEnabled = _StreamDropEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 1, 1, 3),
    _StreamDropEnabled_Type()
)
streamDropEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamDropEnabled.setStatus("current")
_StreamInDropThreshold_Type = Gauge32
_StreamInDropThreshold_Object = MibTableColumn
streamInDropThreshold = _StreamInDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 1, 1, 4),
    _StreamInDropThreshold_Type()
)
streamInDropThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInDropThreshold.setStatus("current")
_StreamInTable_Object = MibTable
streamInTable = _StreamInTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2)
)
if mibBuilder.loadTexts:
    streamInTable.setStatus("current")
_StreamInEntry_Object = MibTableRow
streamInEntry = _StreamInEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1)
)
streamInEntry.setIndexNames(
    (0, "ENDACE-STREAM-MIB", "streamInIndex"),
)
if mibBuilder.loadTexts:
    streamInEntry.setStatus("current")


class _StreamInIndex_Type(StreamIndex):
    """Custom type streamInIndex based on StreamIndex"""
    subtypeSpec = StreamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StreamInIndex_Type.__name__ = "StreamIndex"
_StreamInIndex_Object = MibTableColumn
streamInIndex = _StreamInIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 1),
    _StreamInIndex_Type()
)
streamInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    streamInIndex.setStatus("current")


class _StreamInNum_Type(StreamIndex):
    """Custom type streamInNum based on StreamIndex"""
    subtypeSpec = StreamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StreamInNum_Type.__name__ = "StreamIndex"
_StreamInNum_Object = MibTableColumn
streamInNum = _StreamInNum_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 2),
    _StreamInNum_Type()
)
streamInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInNum.setStatus("current")


class _StreamInName_Type(DisplayString):
    """Custom type streamInName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StreamInName_Type.__name__ = "DisplayString"
_StreamInName_Object = MibTableColumn
streamInName = _StreamInName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 3),
    _StreamInName_Type()
)
streamInName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInName.setStatus("current")
_StreamInModule_Type = ModuleIndex
_StreamInModule_Object = MibTableColumn
streamInModule = _StreamInModule_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 4),
    _StreamInModule_Type()
)
streamInModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInModule.setStatus("current")


class _StreamInLabel_Type(DisplayString):
    """Custom type streamInLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StreamInLabel_Type.__name__ = "DisplayString"
_StreamInLabel_Object = MibTableColumn
streamInLabel = _StreamInLabel_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 5),
    _StreamInLabel_Type()
)
streamInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInLabel.setStatus("current")


class _StreamInAdminStatus_Type(Integer32):
    """Custom type streamInAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_StreamInAdminStatus_Type.__name__ = "Integer32"
_StreamInAdminStatus_Object = MibTableColumn
streamInAdminStatus = _StreamInAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 6),
    _StreamInAdminStatus_Type()
)
streamInAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInAdminStatus.setStatus("obsolete")


class _StreamInOperStatus_Type(Integer32):
    """Custom type streamInOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_StreamInOperStatus_Type.__name__ = "Integer32"
_StreamInOperStatus_Object = MibTableColumn
streamInOperStatus = _StreamInOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 7),
    _StreamInOperStatus_Type()
)
streamInOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInOperStatus.setStatus("current")


class _StreamInMem_Type(Unsigned32):
    """Custom type streamInMem based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_StreamInMem_Type.__name__ = "Unsigned32"
_StreamInMem_Object = MibTableColumn
streamInMem = _StreamInMem_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 8),
    _StreamInMem_Type()
)
streamInMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInMem.setStatus("current")


class _StreamInMemBytes_Type(Unsigned32):
    """Custom type streamInMemBytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_StreamInMemBytes_Type.__name__ = "Unsigned32"
_StreamInMemBytes_Object = MibTableColumn
streamInMemBytes = _StreamInMemBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 9),
    _StreamInMemBytes_Type()
)
streamInMemBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInMemBytes.setStatus("deprecated")


class _StreamInSnapLen_Type(Unsigned32):
    """Custom type streamInSnapLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_StreamInSnapLen_Type.__name__ = "Unsigned32"
_StreamInSnapLen_Object = MibTableColumn
streamInSnapLen = _StreamInSnapLen_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 10),
    _StreamInSnapLen_Type()
)
streamInSnapLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInSnapLen.setStatus("obsolete")
_StreamInPackets_Type = Counter32
_StreamInPackets_Object = MibTableColumn
streamInPackets = _StreamInPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 11),
    _StreamInPackets_Type()
)
streamInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInPackets.setStatus("obsolete")
_StreamInOctets_Type = Counter32
_StreamInOctets_Object = MibTableColumn
streamInOctets = _StreamInOctets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 12),
    _StreamInOctets_Type()
)
streamInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInOctets.setStatus("obsolete")
_StreamInHCPackets_Type = Counter64
_StreamInHCPackets_Object = MibTableColumn
streamInHCPackets = _StreamInHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 13),
    _StreamInHCPackets_Type()
)
streamInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInHCPackets.setStatus("obsolete")
_StreamInHCOctets_Type = Counter64
_StreamInHCOctets_Object = MibTableColumn
streamInHCOctets = _StreamInHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 14),
    _StreamInHCOctets_Type()
)
streamInHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInHCOctets.setStatus("obsolete")
_StreamInDropPackets_Type = Counter32
_StreamInDropPackets_Object = MibTableColumn
streamInDropPackets = _StreamInDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 15),
    _StreamInDropPackets_Type()
)
streamInDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInDropPackets.setStatus("current")
_StreamInHCDropPackets_Type = Counter64
_StreamInHCDropPackets_Object = MibTableColumn
streamInHCDropPackets = _StreamInHCDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 2, 1, 16),
    _StreamInHCDropPackets_Type()
)
streamInHCDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamInHCDropPackets.setStatus("current")
_StreamOutTable_Object = MibTable
streamOutTable = _StreamOutTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3)
)
if mibBuilder.loadTexts:
    streamOutTable.setStatus("current")
_StreamOutEntry_Object = MibTableRow
streamOutEntry = _StreamOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1)
)
streamOutEntry.setIndexNames(
    (0, "ENDACE-STREAM-MIB", "streamOutIndex"),
)
if mibBuilder.loadTexts:
    streamOutEntry.setStatus("current")


class _StreamOutIndex_Type(StreamIndex):
    """Custom type streamOutIndex based on StreamIndex"""
    subtypeSpec = StreamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StreamOutIndex_Type.__name__ = "StreamIndex"
_StreamOutIndex_Object = MibTableColumn
streamOutIndex = _StreamOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 1),
    _StreamOutIndex_Type()
)
streamOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    streamOutIndex.setStatus("current")


class _StreamOutNum_Type(StreamIndex):
    """Custom type streamOutNum based on StreamIndex"""
    subtypeSpec = StreamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StreamOutNum_Type.__name__ = "StreamIndex"
_StreamOutNum_Object = MibTableColumn
streamOutNum = _StreamOutNum_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 2),
    _StreamOutNum_Type()
)
streamOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutNum.setStatus("current")


class _StreamOutName_Type(DisplayString):
    """Custom type streamOutName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StreamOutName_Type.__name__ = "DisplayString"
_StreamOutName_Object = MibTableColumn
streamOutName = _StreamOutName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 3),
    _StreamOutName_Type()
)
streamOutName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutName.setStatus("current")
_StreamOutModule_Type = ModuleIndex
_StreamOutModule_Object = MibTableColumn
streamOutModule = _StreamOutModule_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 4),
    _StreamOutModule_Type()
)
streamOutModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutModule.setStatus("current")


class _StreamOutLabel_Type(DisplayString):
    """Custom type streamOutLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_StreamOutLabel_Type.__name__ = "DisplayString"
_StreamOutLabel_Object = MibTableColumn
streamOutLabel = _StreamOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 5),
    _StreamOutLabel_Type()
)
streamOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutLabel.setStatus("current")


class _StreamOutAdminStatus_Type(Integer32):
    """Custom type streamOutAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_StreamOutAdminStatus_Type.__name__ = "Integer32"
_StreamOutAdminStatus_Object = MibTableColumn
streamOutAdminStatus = _StreamOutAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 6),
    _StreamOutAdminStatus_Type()
)
streamOutAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutAdminStatus.setStatus("current")


class _StreamOutOperStatus_Type(Integer32):
    """Custom type streamOutOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_StreamOutOperStatus_Type.__name__ = "Integer32"
_StreamOutOperStatus_Object = MibTableColumn
streamOutOperStatus = _StreamOutOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 7),
    _StreamOutOperStatus_Type()
)
streamOutOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutOperStatus.setStatus("current")


class _StreamOutMem_Type(Unsigned32):
    """Custom type streamOutMem based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_StreamOutMem_Type.__name__ = "Unsigned32"
_StreamOutMem_Object = MibTableColumn
streamOutMem = _StreamOutMem_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 8),
    _StreamOutMem_Type()
)
streamOutMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutMem.setStatus("current")


class _StreamOutMemBytes_Type(Unsigned32):
    """Custom type streamOutMemBytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_StreamOutMemBytes_Type.__name__ = "Unsigned32"
_StreamOutMemBytes_Object = MibTableColumn
streamOutMemBytes = _StreamOutMemBytes_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 9),
    _StreamOutMemBytes_Type()
)
streamOutMemBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutMemBytes.setStatus("current")


class _StreamOutSnapLen_Type(Unsigned32):
    """Custom type streamOutSnapLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_StreamOutSnapLen_Type.__name__ = "Unsigned32"
_StreamOutSnapLen_Object = MibTableColumn
streamOutSnapLen = _StreamOutSnapLen_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 10),
    _StreamOutSnapLen_Type()
)
streamOutSnapLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutSnapLen.setStatus("current")
_StreamOutPackets_Type = Counter32
_StreamOutPackets_Object = MibTableColumn
streamOutPackets = _StreamOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 11),
    _StreamOutPackets_Type()
)
streamOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutPackets.setStatus("current")
_StreamOutOctets_Type = Counter32
_StreamOutOctets_Object = MibTableColumn
streamOutOctets = _StreamOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 12),
    _StreamOutOctets_Type()
)
streamOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutOctets.setStatus("current")
_StreamOutHCPackets_Type = Counter64
_StreamOutHCPackets_Object = MibTableColumn
streamOutHCPackets = _StreamOutHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 13),
    _StreamOutHCPackets_Type()
)
streamOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutHCPackets.setStatus("current")
_StreamOutHCOctets_Type = Counter64
_StreamOutHCOctets_Object = MibTableColumn
streamOutHCOctets = _StreamOutHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 10, 1, 3, 1, 14),
    _StreamOutHCOctets_Type()
)
streamOutHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamOutHCOctets.setStatus("current")
_StreamConf_ObjectIdentity = ObjectIdentity
streamConf = _StreamConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2)
)
_StreamGroups_ObjectIdentity = ObjectIdentity
streamGroups = _StreamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 1)
)
_StreamCompls_ObjectIdentity = ObjectIdentity
streamCompls = _StreamCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 2)
)

# Managed Objects groups

streamModuleAttributes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 1, 1)
)
streamModuleAttributes.setObjects(
      *(("ENDACE-STREAM-MIB", "streamDropModule"),
        ("ENDACE-STREAM-MIB", "streamDropEnabled"),
        ("ENDACE-STREAM-MIB", "streamInDropThreshold"))
)
if mibBuilder.loadTexts:
    streamModuleAttributes.setStatus("current")

streamInDetail = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 1, 2)
)
streamInDetail.setObjects(
      *(("ENDACE-STREAM-MIB", "streamInNum"),
        ("ENDACE-STREAM-MIB", "streamInName"),
        ("ENDACE-STREAM-MIB", "streamInModule"),
        ("ENDACE-STREAM-MIB", "streamInLabel"))
)
if mibBuilder.loadTexts:
    streamInDetail.setStatus("current")

streamInAttributes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 1, 3)
)
streamInAttributes.setObjects(
      *(("ENDACE-STREAM-MIB", "streamInAdminStatus"),
        ("ENDACE-STREAM-MIB", "streamInOperStatus"),
        ("ENDACE-STREAM-MIB", "streamInMem"),
        ("ENDACE-STREAM-MIB", "streamInMemBytes"),
        ("ENDACE-STREAM-MIB", "streamInSnapLen"))
)
if mibBuilder.loadTexts:
    streamInAttributes.setStatus("current")

streamInCounters = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 1, 4)
)
streamInCounters.setObjects(
      *(("ENDACE-STREAM-MIB", "streamInPackets"),
        ("ENDACE-STREAM-MIB", "streamInOctets"),
        ("ENDACE-STREAM-MIB", "streamInHCPackets"),
        ("ENDACE-STREAM-MIB", "streamInHCOctets"),
        ("ENDACE-STREAM-MIB", "streamInDropPackets"),
        ("ENDACE-STREAM-MIB", "streamInHCDropPackets"))
)
if mibBuilder.loadTexts:
    streamInCounters.setStatus("current")

streamOutDetails = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 1, 5)
)
streamOutDetails.setObjects(
      *(("ENDACE-STREAM-MIB", "streamOutNum"),
        ("ENDACE-STREAM-MIB", "streamOutLabel"),
        ("ENDACE-STREAM-MIB", "streamOutModule"),
        ("ENDACE-STREAM-MIB", "streamOutName"))
)
if mibBuilder.loadTexts:
    streamOutDetails.setStatus("current")

streamOutAttributes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 1, 6)
)
streamOutAttributes.setObjects(
      *(("ENDACE-STREAM-MIB", "streamOutAdminStatus"),
        ("ENDACE-STREAM-MIB", "streamOutOperStatus"),
        ("ENDACE-STREAM-MIB", "streamOutMem"),
        ("ENDACE-STREAM-MIB", "streamOutMemBytes"),
        ("ENDACE-STREAM-MIB", "streamOutSnapLen"))
)
if mibBuilder.loadTexts:
    streamOutAttributes.setStatus("current")

streamOutCounters = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 1, 7)
)
streamOutCounters.setObjects(
      *(("ENDACE-STREAM-MIB", "streamOutPackets"),
        ("ENDACE-STREAM-MIB", "streamOutOctets"),
        ("ENDACE-STREAM-MIB", "streamOutHCPackets"),
        ("ENDACE-STREAM-MIB", "streamOutHCOctets"))
)
if mibBuilder.loadTexts:
    streamOutCounters.setStatus("current")


# Notification objects

streamInDropFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 10, 0, 1)
)
streamInDropFault.setObjects(
      *(("ENDACE-STREAM-MIB", "streamInNum"),
        ("ENDACE-STREAM-MIB", "streamInName"))
)
if mibBuilder.loadTexts:
    streamInDropFault.setStatus(
        "current"
    )

streamInDropNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 10, 0, 2)
)
streamInDropNormal.setObjects(
      *(("ENDACE-STREAM-MIB", "streamInNum"),
        ("ENDACE-STREAM-MIB", "streamInName"))
)
if mibBuilder.loadTexts:
    streamInDropNormal.setStatus(
        "current"
    )


# Notifications groups

streamInEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 1, 8)
)
streamInEvents.setObjects(
      *(("ENDACE-STREAM-MIB", "streamInDropFault"),
        ("ENDACE-STREAM-MIB", "streamInDropNormal"))
)
if mibBuilder.loadTexts:
    streamInEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

streamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18418, 10, 2, 2, 1)
)
streamCompliance.setObjects(
      *(("ENDACE-STREAM-MIB", "streamModuleAttributes"),
        ("ENDACE-STREAM-MIB", "streamInDetail"),
        ("ENDACE-STREAM-MIB", "streamOutDetails"),
        ("ENDACE-STREAM-MIB", "streamInEvents"))
)
if mibBuilder.loadTexts:
    streamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-STREAM-MIB",
    **{"StreamIndex": StreamIndex,
       "streamMIB": streamMIB,
       "streamEvents": streamEvents,
       "streamInDropFault": streamInDropFault,
       "streamInDropNormal": streamInDropNormal,
       "streamObjects": streamObjects,
       "streamDropTable": streamDropTable,
       "streamDropEntry": streamDropEntry,
       "streamDropModIndex": streamDropModIndex,
       "streamDropModule": streamDropModule,
       "streamDropEnabled": streamDropEnabled,
       "streamInDropThreshold": streamInDropThreshold,
       "streamInTable": streamInTable,
       "streamInEntry": streamInEntry,
       "streamInIndex": streamInIndex,
       "streamInNum": streamInNum,
       "streamInName": streamInName,
       "streamInModule": streamInModule,
       "streamInLabel": streamInLabel,
       "streamInAdminStatus": streamInAdminStatus,
       "streamInOperStatus": streamInOperStatus,
       "streamInMem": streamInMem,
       "streamInMemBytes": streamInMemBytes,
       "streamInSnapLen": streamInSnapLen,
       "streamInPackets": streamInPackets,
       "streamInOctets": streamInOctets,
       "streamInHCPackets": streamInHCPackets,
       "streamInHCOctets": streamInHCOctets,
       "streamInDropPackets": streamInDropPackets,
       "streamInHCDropPackets": streamInHCDropPackets,
       "streamOutTable": streamOutTable,
       "streamOutEntry": streamOutEntry,
       "streamOutIndex": streamOutIndex,
       "streamOutNum": streamOutNum,
       "streamOutName": streamOutName,
       "streamOutModule": streamOutModule,
       "streamOutLabel": streamOutLabel,
       "streamOutAdminStatus": streamOutAdminStatus,
       "streamOutOperStatus": streamOutOperStatus,
       "streamOutMem": streamOutMem,
       "streamOutMemBytes": streamOutMemBytes,
       "streamOutSnapLen": streamOutSnapLen,
       "streamOutPackets": streamOutPackets,
       "streamOutOctets": streamOutOctets,
       "streamOutHCPackets": streamOutHCPackets,
       "streamOutHCOctets": streamOutHCOctets,
       "streamConf": streamConf,
       "streamGroups": streamGroups,
       "streamModuleAttributes": streamModuleAttributes,
       "streamInDetail": streamInDetail,
       "streamInAttributes": streamInAttributes,
       "streamInCounters": streamInCounters,
       "streamOutDetails": streamOutDetails,
       "streamOutAttributes": streamOutAttributes,
       "streamOutCounters": streamOutCounters,
       "streamInEvents": streamInEvents,
       "streamCompls": streamCompls,
       "streamCompliance": streamCompliance}
)
