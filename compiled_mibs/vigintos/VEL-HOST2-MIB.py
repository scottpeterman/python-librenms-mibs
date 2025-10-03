# SNMP MIB module (VEL-HOST2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vigintos\VEL-HOST2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:56 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
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
    "NotificationType",
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

(vel,) = mibBuilder.importSymbols(
    "VEL-MIB",
    "vel")


# MODULE-IDENTITY

host2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27993, 5)
)
if mibBuilder.loadTexts:
    host2.setRevisions(
        ("2013-03-07 08:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Host2Name_Type = DisplayString
_Host2Name_Object = MibScalar
host2Name = _Host2Name_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 1),
    _Host2Name_Type()
)
host2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2Name.setStatus("current")
_Host2Version_Type = DisplayString
_Host2Version_Object = MibScalar
host2Version = _Host2Version_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 2),
    _Host2Version_Type()
)
host2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2Version.setStatus("current")
_Host2LoaderVersion_Type = DisplayString
_Host2LoaderVersion_Object = MibScalar
host2LoaderVersion = _Host2LoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 3),
    _Host2LoaderVersion_Type()
)
host2LoaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2LoaderVersion.setStatus("current")
_Host2CmdTable_Object = MibTable
host2CmdTable = _Host2CmdTable_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 4)
)
if mibBuilder.loadTexts:
    host2CmdTable.setStatus("current")
_Host2CmdEntry_Object = MibTableRow
host2CmdEntry = _Host2CmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 4, 1)
)
host2CmdEntry.setIndexNames(
    (0, "VEL-HOST2-MIB", "host2CmdIndex"),
)
if mibBuilder.loadTexts:
    host2CmdEntry.setStatus("current")


class _Host2CmdIndex_Type(Integer32):
    """Custom type host2CmdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Host2CmdIndex_Type.__name__ = "Integer32"
_Host2CmdIndex_Object = MibTableColumn
host2CmdIndex = _Host2CmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 4, 1, 1),
    _Host2CmdIndex_Type()
)
host2CmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2CmdIndex.setStatus("current")


class _Host2CmdName_Type(DisplayString):
    """Custom type host2CmdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Host2CmdName_Type.__name__ = "DisplayString"
_Host2CmdName_Object = MibTableColumn
host2CmdName = _Host2CmdName_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 4, 1, 2),
    _Host2CmdName_Type()
)
host2CmdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2CmdName.setStatus("current")


class _Host2CmdExecute_Type(Integer32):
    """Custom type host2CmdExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Host2CmdExecute_Type.__name__ = "Integer32"
_Host2CmdExecute_Object = MibTableColumn
host2CmdExecute = _Host2CmdExecute_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 4, 1, 3),
    _Host2CmdExecute_Type()
)
host2CmdExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    host2CmdExecute.setStatus("current")
_Host2HistoryTable_Object = MibTable
host2HistoryTable = _Host2HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 5)
)
if mibBuilder.loadTexts:
    host2HistoryTable.setStatus("current")
_Host2HistoryEntry_Object = MibTableRow
host2HistoryEntry = _Host2HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 5, 1)
)
host2HistoryEntry.setIndexNames(
    (0, "VEL-HOST2-MIB", "host2HisIndex"),
)
if mibBuilder.loadTexts:
    host2HistoryEntry.setStatus("current")


class _Host2HisIndex_Type(Integer32):
    """Custom type host2HisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1008),
    )


_Host2HisIndex_Type.__name__ = "Integer32"
_Host2HisIndex_Object = MibTableColumn
host2HisIndex = _Host2HisIndex_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 5, 1, 1),
    _Host2HisIndex_Type()
)
host2HisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2HisIndex.setStatus("current")


class _Host2HisRecord_Type(DisplayString):
    """Custom type host2HisRecord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Host2HisRecord_Type.__name__ = "DisplayString"
_Host2HisRecord_Object = MibTableColumn
host2HisRecord = _Host2HisRecord_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 5, 1, 2),
    _Host2HisRecord_Type()
)
host2HisRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2HisRecord.setStatus("current")
_Host2DevAttrTable_Object = MibTable
host2DevAttrTable = _Host2DevAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 6)
)
if mibBuilder.loadTexts:
    host2DevAttrTable.setStatus("current")
_Host2DevAttrEntry_Object = MibTableRow
host2DevAttrEntry = _Host2DevAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 6, 1)
)
host2DevAttrEntry.setIndexNames(
    (0, "VEL-HOST2-MIB", "host2DevIndex"),
)
if mibBuilder.loadTexts:
    host2DevAttrEntry.setStatus("current")


class _Host2DevIndex_Type(Integer32):
    """Custom type host2DevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Host2DevIndex_Type.__name__ = "Integer32"
_Host2DevIndex_Object = MibTableColumn
host2DevIndex = _Host2DevIndex_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 6, 1, 1),
    _Host2DevIndex_Type()
)
host2DevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevIndex.setStatus("current")


class _Host2DevLocalAddr_Type(Integer32):
    """Custom type host2DevLocalAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_Host2DevLocalAddr_Type.__name__ = "Integer32"
_Host2DevLocalAddr_Object = MibTableColumn
host2DevLocalAddr = _Host2DevLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 6, 1, 2),
    _Host2DevLocalAddr_Type()
)
host2DevLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevLocalAddr.setStatus("current")


class _Host2DevTypeNumber_Type(Integer32):
    """Custom type host2DevTypeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Host2DevTypeNumber_Type.__name__ = "Integer32"
_Host2DevTypeNumber_Object = MibTableColumn
host2DevTypeNumber = _Host2DevTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 6, 1, 3),
    _Host2DevTypeNumber_Type()
)
host2DevTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevTypeNumber.setStatus("current")


class _Host2DevLanState_Type(Integer32):
    """Custom type host2DevLanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_Host2DevLanState_Type.__name__ = "Integer32"
_Host2DevLanState_Object = MibTableColumn
host2DevLanState = _Host2DevLanState_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 6, 1, 4),
    _Host2DevLanState_Type()
)
host2DevLanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevLanState.setStatus("current")
_Host2DevTxtTable_Object = MibTable
host2DevTxtTable = _Host2DevTxtTable_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 7)
)
if mibBuilder.loadTexts:
    host2DevTxtTable.setStatus("current")
_Host2DevTxtEntry_Object = MibTableRow
host2DevTxtEntry = _Host2DevTxtEntry_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 7, 1)
)
host2DevTxtEntry.setIndexNames(
    (0, "VEL-HOST2-MIB", "host2DevIndex"),
    (0, "VEL-HOST2-MIB", "host2DevTxtIndex"),
)
if mibBuilder.loadTexts:
    host2DevTxtEntry.setStatus("current")


class _Host2DevTxtIndex_Type(Integer32):
    """Custom type host2DevTxtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Host2DevTxtIndex_Type.__name__ = "Integer32"
_Host2DevTxtIndex_Object = MibTableColumn
host2DevTxtIndex = _Host2DevTxtIndex_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 7, 1, 1),
    _Host2DevTxtIndex_Type()
)
host2DevTxtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevTxtIndex.setStatus("current")


class _Host2DevTxtName_Type(DisplayString):
    """Custom type host2DevTxtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Host2DevTxtName_Type.__name__ = "DisplayString"
_Host2DevTxtName_Object = MibTableColumn
host2DevTxtName = _Host2DevTxtName_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 7, 1, 2),
    _Host2DevTxtName_Type()
)
host2DevTxtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevTxtName.setStatus("current")


class _Host2DevTxtValue_Type(DisplayString):
    """Custom type host2DevTxtValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Host2DevTxtValue_Type.__name__ = "DisplayString"
_Host2DevTxtValue_Object = MibTableColumn
host2DevTxtValue = _Host2DevTxtValue_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 7, 1, 3),
    _Host2DevTxtValue_Type()
)
host2DevTxtValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevTxtValue.setStatus("current")
_Host2DevEvtTable_Object = MibTable
host2DevEvtTable = _Host2DevEvtTable_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 8)
)
if mibBuilder.loadTexts:
    host2DevEvtTable.setStatus("current")
_Host2DevEvtEntry_Object = MibTableRow
host2DevEvtEntry = _Host2DevEvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 8, 1)
)
host2DevEvtEntry.setIndexNames(
    (0, "VEL-HOST2-MIB", "host2DevIndex"),
    (0, "VEL-HOST2-MIB", "host2DevEvtIndex"),
)
if mibBuilder.loadTexts:
    host2DevEvtEntry.setStatus("current")


class _Host2DevEvtIndex_Type(Integer32):
    """Custom type host2DevEvtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Host2DevEvtIndex_Type.__name__ = "Integer32"
_Host2DevEvtIndex_Object = MibTableColumn
host2DevEvtIndex = _Host2DevEvtIndex_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 8, 1, 1),
    _Host2DevEvtIndex_Type()
)
host2DevEvtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevEvtIndex.setStatus("current")


class _Host2DevEvtName_Type(DisplayString):
    """Custom type host2DevEvtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Host2DevEvtName_Type.__name__ = "DisplayString"
_Host2DevEvtName_Object = MibTableColumn
host2DevEvtName = _Host2DevEvtName_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 8, 1, 2),
    _Host2DevEvtName_Type()
)
host2DevEvtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevEvtName.setStatus("current")


class _Host2DevEvtType_Type(Integer32):
    """Custom type host2DevEvtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notice", 0),
          ("warning", 1),
          ("alarm", 2))
    )


_Host2DevEvtType_Type.__name__ = "Integer32"
_Host2DevEvtType_Object = MibTableColumn
host2DevEvtType = _Host2DevEvtType_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 8, 1, 3),
    _Host2DevEvtType_Type()
)
host2DevEvtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevEvtType.setStatus("current")


class _Host2DevEvtState_Type(Integer32):
    """Custom type host2DevEvtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Host2DevEvtState_Type.__name__ = "Integer32"
_Host2DevEvtState_Object = MibTableColumn
host2DevEvtState = _Host2DevEvtState_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 8, 1, 4),
    _Host2DevEvtState_Type()
)
host2DevEvtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevEvtState.setStatus("current")
_Host2DevParTable_Object = MibTable
host2DevParTable = _Host2DevParTable_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 9)
)
if mibBuilder.loadTexts:
    host2DevParTable.setStatus("current")
_Host2DevParEntry_Object = MibTableRow
host2DevParEntry = _Host2DevParEntry_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 9, 1)
)
host2DevParEntry.setIndexNames(
    (0, "VEL-HOST2-MIB", "host2DevIndex"),
    (0, "VEL-HOST2-MIB", "host2DevParIndex"),
)
if mibBuilder.loadTexts:
    host2DevParEntry.setStatus("current")


class _Host2DevParIndex_Type(Integer32):
    """Custom type host2DevParIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Host2DevParIndex_Type.__name__ = "Integer32"
_Host2DevParIndex_Object = MibTableColumn
host2DevParIndex = _Host2DevParIndex_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 1),
    _Host2DevParIndex_Type()
)
host2DevParIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevParIndex.setStatus("current")


class _Host2DevParName_Type(DisplayString):
    """Custom type host2DevParName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Host2DevParName_Type.__name__ = "DisplayString"
_Host2DevParName_Object = MibTableColumn
host2DevParName = _Host2DevParName_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 2),
    _Host2DevParName_Type()
)
host2DevParName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevParName.setStatus("current")


class _Host2DevParValue_Type(DisplayString):
    """Custom type host2DevParValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Host2DevParValue_Type.__name__ = "DisplayString"
_Host2DevParValue_Object = MibTableColumn
host2DevParValue = _Host2DevParValue_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 3),
    _Host2DevParValue_Type()
)
host2DevParValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevParValue.setStatus("current")


class _Host2DevParUnit_Type(DisplayString):
    """Custom type host2DevParUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Host2DevParUnit_Type.__name__ = "DisplayString"
_Host2DevParUnit_Object = MibTableColumn
host2DevParUnit = _Host2DevParUnit_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 4),
    _Host2DevParUnit_Type()
)
host2DevParUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevParUnit.setStatus("current")


class _Host2DevParStateType_Type(Integer32):
    """Custom type host2DevParStateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notice", 0),
          ("warning", 1),
          ("alarm", 2))
    )


_Host2DevParStateType_Type.__name__ = "Integer32"
_Host2DevParStateType_Object = MibTableColumn
host2DevParStateType = _Host2DevParStateType_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 5),
    _Host2DevParStateType_Type()
)
host2DevParStateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevParStateType.setStatus("current")


class _Host2DevParState_Type(Integer32):
    """Custom type host2DevParState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("lessThanMin", 1),
          ("greatherThanMax", 2),
          ("blocked", 3))
    )


_Host2DevParState_Type.__name__ = "Integer32"
_Host2DevParState_Object = MibTableColumn
host2DevParState = _Host2DevParState_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 6),
    _Host2DevParState_Type()
)
host2DevParState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevParState.setStatus("current")
_Host2DevQntTable_Object = MibTable
host2DevQntTable = _Host2DevQntTable_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 10)
)
if mibBuilder.loadTexts:
    host2DevQntTable.setStatus("current")
_Host2DevQntEntry_Object = MibTableRow
host2DevQntEntry = _Host2DevQntEntry_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 10, 1)
)
host2DevQntEntry.setIndexNames(
    (0, "VEL-HOST2-MIB", "host2DevIndex"),
    (0, "VEL-HOST2-MIB", "host2DevQntIndex"),
)
if mibBuilder.loadTexts:
    host2DevQntEntry.setStatus("current")


class _Host2DevQntIndex_Type(Integer32):
    """Custom type host2DevQntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Host2DevQntIndex_Type.__name__ = "Integer32"
_Host2DevQntIndex_Object = MibTableColumn
host2DevQntIndex = _Host2DevQntIndex_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 1),
    _Host2DevQntIndex_Type()
)
host2DevQntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevQntIndex.setStatus("current")


class _Host2DevQntName_Type(DisplayString):
    """Custom type host2DevQntName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Host2DevQntName_Type.__name__ = "DisplayString"
_Host2DevQntName_Object = MibTableColumn
host2DevQntName = _Host2DevQntName_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 2),
    _Host2DevQntName_Type()
)
host2DevQntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevQntName.setStatus("current")


class _Host2DevQntValue_Type(DisplayString):
    """Custom type host2DevQntValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Host2DevQntValue_Type.__name__ = "DisplayString"
_Host2DevQntValue_Object = MibTableColumn
host2DevQntValue = _Host2DevQntValue_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 3),
    _Host2DevQntValue_Type()
)
host2DevQntValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    host2DevQntValue.setStatus("current")


class _Host2DevQntMin_Type(DisplayString):
    """Custom type host2DevQntMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Host2DevQntMin_Type.__name__ = "DisplayString"
_Host2DevQntMin_Object = MibTableColumn
host2DevQntMin = _Host2DevQntMin_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 4),
    _Host2DevQntMin_Type()
)
host2DevQntMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevQntMin.setStatus("current")


class _Host2DevQntMax_Type(DisplayString):
    """Custom type host2DevQntMax based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Host2DevQntMax_Type.__name__ = "DisplayString"
_Host2DevQntMax_Object = MibTableColumn
host2DevQntMax = _Host2DevQntMax_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 5),
    _Host2DevQntMax_Type()
)
host2DevQntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevQntMax.setStatus("current")


class _Host2DevQntAccess_Type(Integer32):
    """Custom type host2DevQntAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 0),
          ("read-write", 1))
    )


_Host2DevQntAccess_Type.__name__ = "Integer32"
_Host2DevQntAccess_Object = MibTableColumn
host2DevQntAccess = _Host2DevQntAccess_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 6),
    _Host2DevQntAccess_Type()
)
host2DevQntAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevQntAccess.setStatus("current")
_Host2DevCmdTable_Object = MibTable
host2DevCmdTable = _Host2DevCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 11)
)
if mibBuilder.loadTexts:
    host2DevCmdTable.setStatus("current")
_Host2DevCmdEntry_Object = MibTableRow
host2DevCmdEntry = _Host2DevCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 11, 1)
)
host2DevCmdEntry.setIndexNames(
    (0, "VEL-HOST2-MIB", "host2DevIndex"),
    (0, "VEL-HOST2-MIB", "host2DevCmdIndex"),
)
if mibBuilder.loadTexts:
    host2DevCmdEntry.setStatus("current")


class _Host2DevCmdIndex_Type(Integer32):
    """Custom type host2DevCmdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Host2DevCmdIndex_Type.__name__ = "Integer32"
_Host2DevCmdIndex_Object = MibTableColumn
host2DevCmdIndex = _Host2DevCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 11, 1, 1),
    _Host2DevCmdIndex_Type()
)
host2DevCmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevCmdIndex.setStatus("current")


class _Host2DevCmdName_Type(DisplayString):
    """Custom type host2DevCmdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Host2DevCmdName_Type.__name__ = "DisplayString"
_Host2DevCmdName_Object = MibTableColumn
host2DevCmdName = _Host2DevCmdName_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 11, 1, 2),
    _Host2DevCmdName_Type()
)
host2DevCmdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host2DevCmdName.setStatus("current")


class _Host2DevCmdExecute_Type(Integer32):
    """Custom type host2DevCmdExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Host2DevCmdExecute_Type.__name__ = "Integer32"
_Host2DevCmdExecute_Object = MibTableColumn
host2DevCmdExecute = _Host2DevCmdExecute_Object(
    (1, 3, 6, 1, 4, 1, 27993, 5, 11, 1, 3),
    _Host2DevCmdExecute_Type()
)
host2DevCmdExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    host2DevCmdExecute.setStatus("current")

# Managed Objects groups


# Notification objects

host2DevConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27993, 5, 0, 5001)
)
host2DevConnectionTrap.setObjects(
    ("VEL-HOST2-MIB", "host2DevLanState")
)
if mibBuilder.loadTexts:
    host2DevConnectionTrap.setStatus(
        ""
    )

host2DevEvtStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27993, 5, 0, 5002)
)
host2DevEvtStateTrap.setObjects(
    ("VEL-HOST2-MIB", "host2DevEvtState")
)
if mibBuilder.loadTexts:
    host2DevEvtStateTrap.setStatus(
        ""
    )

host2DevParStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27993, 5, 0, 5003)
)
host2DevParStateTrap.setObjects(
    ("VEL-HOST2-MIB", "host2DevParState")
)
if mibBuilder.loadTexts:
    host2DevParStateTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VEL-HOST2-MIB",
    **{"host2": host2,
       "host2DevConnectionTrap": host2DevConnectionTrap,
       "host2DevEvtStateTrap": host2DevEvtStateTrap,
       "host2DevParStateTrap": host2DevParStateTrap,
       "host2Name": host2Name,
       "host2Version": host2Version,
       "host2LoaderVersion": host2LoaderVersion,
       "host2CmdTable": host2CmdTable,
       "host2CmdEntry": host2CmdEntry,
       "host2CmdIndex": host2CmdIndex,
       "host2CmdName": host2CmdName,
       "host2CmdExecute": host2CmdExecute,
       "host2HistoryTable": host2HistoryTable,
       "host2HistoryEntry": host2HistoryEntry,
       "host2HisIndex": host2HisIndex,
       "host2HisRecord": host2HisRecord,
       "host2DevAttrTable": host2DevAttrTable,
       "host2DevAttrEntry": host2DevAttrEntry,
       "host2DevIndex": host2DevIndex,
       "host2DevLocalAddr": host2DevLocalAddr,
       "host2DevTypeNumber": host2DevTypeNumber,
       "host2DevLanState": host2DevLanState,
       "host2DevTxtTable": host2DevTxtTable,
       "host2DevTxtEntry": host2DevTxtEntry,
       "host2DevTxtIndex": host2DevTxtIndex,
       "host2DevTxtName": host2DevTxtName,
       "host2DevTxtValue": host2DevTxtValue,
       "host2DevEvtTable": host2DevEvtTable,
       "host2DevEvtEntry": host2DevEvtEntry,
       "host2DevEvtIndex": host2DevEvtIndex,
       "host2DevEvtName": host2DevEvtName,
       "host2DevEvtType": host2DevEvtType,
       "host2DevEvtState": host2DevEvtState,
       "host2DevParTable": host2DevParTable,
       "host2DevParEntry": host2DevParEntry,
       "host2DevParIndex": host2DevParIndex,
       "host2DevParName": host2DevParName,
       "host2DevParValue": host2DevParValue,
       "host2DevParUnit": host2DevParUnit,
       "host2DevParStateType": host2DevParStateType,
       "host2DevParState": host2DevParState,
       "host2DevQntTable": host2DevQntTable,
       "host2DevQntEntry": host2DevQntEntry,
       "host2DevQntIndex": host2DevQntIndex,
       "host2DevQntName": host2DevQntName,
       "host2DevQntValue": host2DevQntValue,
       "host2DevQntMin": host2DevQntMin,
       "host2DevQntMax": host2DevQntMax,
       "host2DevQntAccess": host2DevQntAccess,
       "host2DevCmdTable": host2DevCmdTable,
       "host2DevCmdEntry": host2DevCmdEntry,
       "host2DevCmdIndex": host2DevCmdIndex,
       "host2DevCmdName": host2DevCmdName,
       "host2DevCmdExecute": host2DevCmdExecute}
)
