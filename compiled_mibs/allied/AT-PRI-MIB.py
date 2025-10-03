# SNMP MIB module (AT-PRI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\allied\AT-PRI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:32 2025
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pri = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42)
)
if mibBuilder.loadTexts:
    pri.setRevisions(
        ("2006-06-28 12:22",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PriIntTable_Object = MibTable
priIntTable = _PriIntTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1)
)
if mibBuilder.loadTexts:
    priIntTable.setStatus("current")
_PriIntEntry_Object = MibTableRow
priIntEntry = _PriIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1)
)
priIntEntry.setIndexNames(
    (0, "AT-PRI-MIB", "priIntIndex"),
)
if mibBuilder.loadTexts:
    priIntEntry.setStatus("current")
_PriIntIndex_Type = Integer32
_PriIntIndex_Object = MibTableColumn
priIntIndex = _PriIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 1),
    _PriIntIndex_Type()
)
priIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntIndex.setStatus("current")
_PriIntBoardIndex_Type = Integer32
_PriIntBoardIndex_Object = MibTableColumn
priIntBoardIndex = _PriIntBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 2),
    _PriIntBoardIndex_Type()
)
priIntBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntBoardIndex.setStatus("current")
_PriIntBoardPosition_Type = Integer32
_PriIntBoardPosition_Object = MibTableColumn
priIntBoardPosition = _PriIntBoardPosition_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 3),
    _PriIntBoardPosition_Type()
)
priIntBoardPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntBoardPosition.setStatus("current")


class _PriIntMode_Type(Integer32):
    """Custom type priIntMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("tdm", 2),
          ("mixed", 3))
    )


_PriIntMode_Type.__name__ = "Integer32"
_PriIntMode_Object = MibTableColumn
priIntMode = _PriIntMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 4),
    _PriIntMode_Type()
)
priIntMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntMode.setStatus("current")
_PriIntTdmChannelMap_Type = Integer32
_PriIntTdmChannelMap_Object = MibTableColumn
priIntTdmChannelMap = _PriIntTdmChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 5),
    _PriIntTdmChannelMap_Type()
)
priIntTdmChannelMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntTdmChannelMap.setStatus("current")
_PriIntIsdnChannelMap_Type = Integer32
_PriIntIsdnChannelMap_Object = MibTableColumn
priIntIsdnChannelMap = _PriIntIsdnChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 6),
    _PriIntIsdnChannelMap_Type()
)
priIntIsdnChannelMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntIsdnChannelMap.setStatus("current")


class _PriIntType_Type(Integer32):
    """Custom type priIntType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("t1", 2),
          ("unknown", 3))
    )


_PriIntType_Type.__name__ = "Integer32"
_PriIntType_Object = MibTableColumn
priIntType = _PriIntType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 7),
    _PriIntType_Type()
)
priIntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priIntType.setStatus("current")
_PriChanTable_Object = MibTable
priChanTable = _PriChanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2)
)
if mibBuilder.loadTexts:
    priChanTable.setStatus("current")
_PriChanEntry_Object = MibTableRow
priChanEntry = _PriChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1)
)
priChanEntry.setIndexNames(
    (0, "AT-PRI-MIB", "priChanIntIndex"),
    (0, "AT-PRI-MIB", "priChanChannelIndex"),
)
if mibBuilder.loadTexts:
    priChanEntry.setStatus("current")
_PriChanIntIndex_Type = Integer32
_PriChanIntIndex_Object = MibTableColumn
priChanIntIndex = _PriChanIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 1),
    _PriChanIntIndex_Type()
)
priChanIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priChanIntIndex.setStatus("current")


class _PriChanChannelIndex_Type(Integer32):
    """Custom type priChanChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PriChanChannelIndex_Type.__name__ = "Integer32"
_PriChanChannelIndex_Object = MibTableColumn
priChanChannelIndex = _PriChanChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 2),
    _PriChanChannelIndex_Type()
)
priChanChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priChanChannelIndex.setStatus("current")


class _PriChanMode_Type(Integer32):
    """Custom type priChanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("tdm", 2),
          ("neither", 3))
    )


_PriChanMode_Type.__name__ = "Integer32"
_PriChanMode_Object = MibTableColumn
priChanMode = _PriChanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 3),
    _PriChanMode_Type()
)
priChanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priChanMode.setStatus("current")


class _PriChanState_Type(Integer32):
    """Custom type priChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_PriChanState_Type.__name__ = "Integer32"
_PriChanState_Object = MibTableColumn
priChanState = _PriChanState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 4),
    _PriChanState_Type()
)
priChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priChanState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-PRI-MIB",
    **{"pri": pri,
       "priIntTable": priIntTable,
       "priIntEntry": priIntEntry,
       "priIntIndex": priIntIndex,
       "priIntBoardIndex": priIntBoardIndex,
       "priIntBoardPosition": priIntBoardPosition,
       "priIntMode": priIntMode,
       "priIntTdmChannelMap": priIntTdmChannelMap,
       "priIntIsdnChannelMap": priIntIsdnChannelMap,
       "priIntType": priIntType,
       "priChanTable": priChanTable,
       "priChanEntry": priChanEntry,
       "priChanIntIndex": priChanIntIndex,
       "priChanChannelIndex": priChanChannelIndex,
       "priChanMode": priChanMode,
       "priChanState": priChanState}
)
