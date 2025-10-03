# SNMP MIB module (EXTREME-TRAPPOLL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\EXTREME-TRAPPOLL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:50 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(trapDestIndex,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "trapDestIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

extremeTrapPoll = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeSmartTrapRulesTable_Object = MibTable
extremeSmartTrapRulesTable = _ExtremeSmartTrapRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 1)
)
if mibBuilder.loadTexts:
    extremeSmartTrapRulesTable.setStatus("current")
_ExtremeSmartTrapRulesEntry_Object = MibTableRow
extremeSmartTrapRulesEntry = _ExtremeSmartTrapRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1)
)
extremeSmartTrapRulesEntry.setIndexNames(
    (0, "EXTREME-TRAPPOLL-MIB", "extremeSmartTrapRulesIndex"),
)
if mibBuilder.loadTexts:
    extremeSmartTrapRulesEntry.setStatus("current")
_ExtremeSmartTrapRulesIndex_Type = Integer32
_ExtremeSmartTrapRulesIndex_Object = MibTableColumn
extremeSmartTrapRulesIndex = _ExtremeSmartTrapRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 1),
    _ExtremeSmartTrapRulesIndex_Type()
)
extremeSmartTrapRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSmartTrapRulesIndex.setStatus("current")
_ExtremeSmartTrapRulesRowStatus_Type = RowStatus
_ExtremeSmartTrapRulesRowStatus_Object = MibTableColumn
extremeSmartTrapRulesRowStatus = _ExtremeSmartTrapRulesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 2),
    _ExtremeSmartTrapRulesRowStatus_Type()
)
extremeSmartTrapRulesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSmartTrapRulesRowStatus.setStatus("current")
_ExtremeSmartTrapRulesDesiredOID_Type = ObjectIdentifier
_ExtremeSmartTrapRulesDesiredOID_Object = MibTableColumn
extremeSmartTrapRulesDesiredOID = _ExtremeSmartTrapRulesDesiredOID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 3),
    _ExtremeSmartTrapRulesDesiredOID_Type()
)
extremeSmartTrapRulesDesiredOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSmartTrapRulesDesiredOID.setStatus("current")
_ExtremeSmartTrapRulesSupportedOID_Type = ObjectIdentifier
_ExtremeSmartTrapRulesSupportedOID_Object = MibTableColumn
extremeSmartTrapRulesSupportedOID = _ExtremeSmartTrapRulesSupportedOID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 4),
    _ExtremeSmartTrapRulesSupportedOID_Type()
)
extremeSmartTrapRulesSupportedOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSmartTrapRulesSupportedOID.setStatus("current")


class _ExtremeSmartTrapRulesOperation_Type(Integer32):
    """Custom type extremeSmartTrapRulesOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2),
          ("modify", 3),
          ("any", 4))
    )


_ExtremeSmartTrapRulesOperation_Type.__name__ = "Integer32"
_ExtremeSmartTrapRulesOperation_Object = MibTableColumn
extremeSmartTrapRulesOperation = _ExtremeSmartTrapRulesOperation_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 5),
    _ExtremeSmartTrapRulesOperation_Type()
)
extremeSmartTrapRulesOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSmartTrapRulesOperation.setStatus("current")
_ExtremeSmartTrapRulesTrapDestIndex_Type = Integer32
_ExtremeSmartTrapRulesTrapDestIndex_Object = MibTableColumn
extremeSmartTrapRulesTrapDestIndex = _ExtremeSmartTrapRulesTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 6),
    _ExtremeSmartTrapRulesTrapDestIndex_Type()
)
extremeSmartTrapRulesTrapDestIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeSmartTrapRulesTrapDestIndex.setStatus("current")
_ExtremeSmartTrapInstanceTable_Object = MibTable
extremeSmartTrapInstanceTable = _ExtremeSmartTrapInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 2)
)
if mibBuilder.loadTexts:
    extremeSmartTrapInstanceTable.setStatus("current")
_ExtremeSmartTrapInstanceEntry_Object = MibTableRow
extremeSmartTrapInstanceEntry = _ExtremeSmartTrapInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1)
)
extremeSmartTrapInstanceEntry.setIndexNames(
    (0, "RMON2-MIB", "trapDestIndex"),
    (0, "EXTREME-TRAPPOLL-MIB", "extremeSmartTrapInstanceSubindex"),
)
if mibBuilder.loadTexts:
    extremeSmartTrapInstanceEntry.setStatus("current")
_ExtremeSmartTrapInstanceSubindex_Type = Integer32
_ExtremeSmartTrapInstanceSubindex_Object = MibTableColumn
extremeSmartTrapInstanceSubindex = _ExtremeSmartTrapInstanceSubindex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 1),
    _ExtremeSmartTrapInstanceSubindex_Type()
)
extremeSmartTrapInstanceSubindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSmartTrapInstanceSubindex.setStatus("current")
_ExtremeSmartTrapInstanceRule_Type = Integer32
_ExtremeSmartTrapInstanceRule_Object = MibTableColumn
extremeSmartTrapInstanceRule = _ExtremeSmartTrapInstanceRule_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 2),
    _ExtremeSmartTrapInstanceRule_Type()
)
extremeSmartTrapInstanceRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSmartTrapInstanceRule.setStatus("current")
_ExtremeSmartTrapInstanceChangedOid_Type = ObjectIdentifier
_ExtremeSmartTrapInstanceChangedOid_Object = MibTableColumn
extremeSmartTrapInstanceChangedOid = _ExtremeSmartTrapInstanceChangedOid_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 3),
    _ExtremeSmartTrapInstanceChangedOid_Type()
)
extremeSmartTrapInstanceChangedOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSmartTrapInstanceChangedOid.setStatus("current")


class _ExtremeSmartTrapInstanceActualOperation_Type(Integer32):
    """Custom type extremeSmartTrapInstanceActualOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2),
          ("modify", 3))
    )


_ExtremeSmartTrapInstanceActualOperation_Type.__name__ = "Integer32"
_ExtremeSmartTrapInstanceActualOperation_Object = MibTableColumn
extremeSmartTrapInstanceActualOperation = _ExtremeSmartTrapInstanceActualOperation_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 4),
    _ExtremeSmartTrapInstanceActualOperation_Type()
)
extremeSmartTrapInstanceActualOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSmartTrapInstanceActualOperation.setStatus("current")
_ExtremeSmartTrapInstanceChangeTime_Type = TimeTicks
_ExtremeSmartTrapInstanceChangeTime_Object = MibTableColumn
extremeSmartTrapInstanceChangeTime = _ExtremeSmartTrapInstanceChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 5),
    _ExtremeSmartTrapInstanceChangeTime_Type()
)
extremeSmartTrapInstanceChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSmartTrapInstanceChangeTime.setStatus("current")
_ExtremeSmartTrapFlushInstanceTableIndex_Type = Integer32
_ExtremeSmartTrapFlushInstanceTableIndex_Object = MibScalar
extremeSmartTrapFlushInstanceTableIndex = _ExtremeSmartTrapFlushInstanceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6, 3),
    _ExtremeSmartTrapFlushInstanceTableIndex_Type()
)
extremeSmartTrapFlushInstanceTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeSmartTrapFlushInstanceTableIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-TRAPPOLL-MIB",
    **{"extremeTrapPoll": extremeTrapPoll,
       "extremeSmartTrapRulesTable": extremeSmartTrapRulesTable,
       "extremeSmartTrapRulesEntry": extremeSmartTrapRulesEntry,
       "extremeSmartTrapRulesIndex": extremeSmartTrapRulesIndex,
       "extremeSmartTrapRulesRowStatus": extremeSmartTrapRulesRowStatus,
       "extremeSmartTrapRulesDesiredOID": extremeSmartTrapRulesDesiredOID,
       "extremeSmartTrapRulesSupportedOID": extremeSmartTrapRulesSupportedOID,
       "extremeSmartTrapRulesOperation": extremeSmartTrapRulesOperation,
       "extremeSmartTrapRulesTrapDestIndex": extremeSmartTrapRulesTrapDestIndex,
       "extremeSmartTrapInstanceTable": extremeSmartTrapInstanceTable,
       "extremeSmartTrapInstanceEntry": extremeSmartTrapInstanceEntry,
       "extremeSmartTrapInstanceSubindex": extremeSmartTrapInstanceSubindex,
       "extremeSmartTrapInstanceRule": extremeSmartTrapInstanceRule,
       "extremeSmartTrapInstanceChangedOid": extremeSmartTrapInstanceChangedOid,
       "extremeSmartTrapInstanceActualOperation": extremeSmartTrapInstanceActualOperation,
       "extremeSmartTrapInstanceChangeTime": extremeSmartTrapInstanceChangeTime,
       "extremeSmartTrapFlushInstanceTableIndex": extremeSmartTrapFlushInstanceTableIndex}
)
