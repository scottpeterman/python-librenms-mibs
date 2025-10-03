# SNMP MIB module (TN-QOS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-QOS-EXT
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:18 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnQosExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9)
)
if mibBuilder.loadTexts:
    tnQosExtMIB.setRevisions(
        ("2012-05-31 00:00",
         "1970-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnQosExtRateUnitType(TextualConvention, Integer32):
    status = "current"
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
        *(("kbps", 1),
          ("fps", 2),
          ("mbps", 3),
          ("kfps", 4))
    )



class TnQosExtRateInFps(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("fps1", 1),
          ("fps2", 2),
          ("fps4", 3),
          ("fps8", 4),
          ("fps16", 5),
          ("fps32", 6),
          ("fps64", 7),
          ("fps128", 8),
          ("fps256", 9),
          ("fps512", 10),
          ("fps1k", 11),
          ("fps2k", 12),
          ("fps4k", 13),
          ("fps8k", 14),
          ("fps16k", 15),
          ("fps32k", 16),
          ("fps64k", 17),
          ("fps128k", 18),
          ("fps256k", 19),
          ("fps512k", 20),
          ("fps1024k", 21),
          ("fps2048k", 22),
          ("fps4096k", 23),
          ("fps8192k", 24),
          ("fps16384k", 25),
          ("fps32768k", 26))
    )



# MIB Managed Objects in the order of their OIDs

_TnQosExtMIBObjects_ObjectIdentity = ObjectIdentity
tnQosExtMIBObjects = _TnQosExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1)
)
_TnQosExtPortMgmt_ObjectIdentity = ObjectIdentity
tnQosExtPortMgmt = _TnQosExtPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1)
)
_TnQosExtPortPolicerTable_Object = MibTable
tnQosExtPortPolicerTable = _TnQosExtPortPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnQosExtPortPolicerTable.setStatus("current")
_TnQosExtPortPolicerEntry_Object = MibTableRow
tnQosExtPortPolicerEntry = _TnQosExtPortPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 1, 1)
)
tnQosExtPortPolicerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtPortPolicerEntry.setStatus("current")


class _TnQosExtPortPolicerStatus_Type(Integer32):
    """Custom type tnQosExtPortPolicerStatus based on Integer32"""
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


_TnQosExtPortPolicerStatus_Type.__name__ = "Integer32"
_TnQosExtPortPolicerStatus_Object = MibTableColumn
tnQosExtPortPolicerStatus = _TnQosExtPortPolicerStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 1, 1, 1),
    _TnQosExtPortPolicerStatus_Type()
)
tnQosExtPortPolicerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortPolicerStatus.setStatus("current")
_TnQosExtPortPolicerRate_Type = Integer32
_TnQosExtPortPolicerRate_Object = MibTableColumn
tnQosExtPortPolicerRate = _TnQosExtPortPolicerRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 1, 1, 2),
    _TnQosExtPortPolicerRate_Type()
)
tnQosExtPortPolicerRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortPolicerRate.setStatus("current")
_TnQosExtPortPolicerUnit_Type = TnQosExtRateUnitType
_TnQosExtPortPolicerUnit_Object = MibTableColumn
tnQosExtPortPolicerUnit = _TnQosExtPortPolicerUnit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 1, 1, 3),
    _TnQosExtPortPolicerUnit_Type()
)
tnQosExtPortPolicerUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortPolicerUnit.setStatus("current")


class _TnQosExtPortPolicerFlowControl_Type(Integer32):
    """Custom type tnQosExtPortPolicerFlowControl based on Integer32"""
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


_TnQosExtPortPolicerFlowControl_Type.__name__ = "Integer32"
_TnQosExtPortPolicerFlowControl_Object = MibTableColumn
tnQosExtPortPolicerFlowControl = _TnQosExtPortPolicerFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 1, 1, 4),
    _TnQosExtPortPolicerFlowControl_Type()
)
tnQosExtPortPolicerFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortPolicerFlowControl.setStatus("current")
_TnQosExtPortQueuePolicerTable_Object = MibTable
tnQosExtPortQueuePolicerTable = _TnQosExtPortQueuePolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnQosExtPortQueuePolicerTable.setStatus("current")
_TnQosExtPortQueuePolicerEntry_Object = MibTableRow
tnQosExtPortQueuePolicerEntry = _TnQosExtPortQueuePolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 2, 1)
)
tnQosExtPortQueuePolicerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtPortQueuePolicerQid"),
)
if mibBuilder.loadTexts:
    tnQosExtPortQueuePolicerEntry.setStatus("current")


class _TnQosExtPortQueuePolicerQid_Type(Integer32):
    """Custom type tnQosExtPortQueuePolicerQid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtPortQueuePolicerQid_Type.__name__ = "Integer32"
_TnQosExtPortQueuePolicerQid_Object = MibTableColumn
tnQosExtPortQueuePolicerQid = _TnQosExtPortQueuePolicerQid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 2, 1, 1),
    _TnQosExtPortQueuePolicerQid_Type()
)
tnQosExtPortQueuePolicerQid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtPortQueuePolicerQid.setStatus("current")


class _TnQosExtPortQueuePolicerStatus_Type(Integer32):
    """Custom type tnQosExtPortQueuePolicerStatus based on Integer32"""
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


_TnQosExtPortQueuePolicerStatus_Type.__name__ = "Integer32"
_TnQosExtPortQueuePolicerStatus_Object = MibTableColumn
tnQosExtPortQueuePolicerStatus = _TnQosExtPortQueuePolicerStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 2, 1, 2),
    _TnQosExtPortQueuePolicerStatus_Type()
)
tnQosExtPortQueuePolicerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortQueuePolicerStatus.setStatus("current")
_TnQosExtPortQueuePolicerRate_Type = Integer32
_TnQosExtPortQueuePolicerRate_Object = MibTableColumn
tnQosExtPortQueuePolicerRate = _TnQosExtPortQueuePolicerRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 2, 1, 3),
    _TnQosExtPortQueuePolicerRate_Type()
)
tnQosExtPortQueuePolicerRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortQueuePolicerRate.setStatus("current")
_TnQosExtPortQueuePolicerUnit_Type = TnQosExtRateUnitType
_TnQosExtPortQueuePolicerUnit_Object = MibTableColumn
tnQosExtPortQueuePolicerUnit = _TnQosExtPortQueuePolicerUnit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 2, 1, 4),
    _TnQosExtPortQueuePolicerUnit_Type()
)
tnQosExtPortQueuePolicerUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortQueuePolicerUnit.setStatus("current")
_TnQosExtPortSchedulerTable_Object = MibTable
tnQosExtPortSchedulerTable = _TnQosExtPortSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnQosExtPortSchedulerTable.setStatus("current")
_TnQosExtPortSchedulerEntry_Object = MibTableRow
tnQosExtPortSchedulerEntry = _TnQosExtPortSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 3, 1)
)
tnQosExtPortSchedulerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtPortSchedulerEntry.setStatus("current")


class _TnQosExtPortSchedulerMode_Type(Integer32):
    """Custom type tnQosExtPortSchedulerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("weighted", 2))
    )


_TnQosExtPortSchedulerMode_Type.__name__ = "Integer32"
_TnQosExtPortSchedulerMode_Object = MibTableColumn
tnQosExtPortSchedulerMode = _TnQosExtPortSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 3, 1, 1),
    _TnQosExtPortSchedulerMode_Type()
)
tnQosExtPortSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortSchedulerMode.setStatus("current")


class _TnQosExtPortSchedulerQueueMask_Type(Bits):
    """Custom type tnQosExtPortSchedulerQueueMask based on Bits"""
    namedValues = NamedValues(
        ("none", 0)
    )

_TnQosExtPortSchedulerQueueMask_Type.__name__ = "Bits"
_TnQosExtPortSchedulerQueueMask_Object = MibTableColumn
tnQosExtPortSchedulerQueueMask = _TnQosExtPortSchedulerQueueMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 3, 1, 2),
    _TnQosExtPortSchedulerQueueMask_Type()
)
tnQosExtPortSchedulerQueueMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortSchedulerQueueMask.setStatus("current")
_TnQosExtPortSchedulerWeightTable_Object = MibTable
tnQosExtPortSchedulerWeightTable = _TnQosExtPortSchedulerWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tnQosExtPortSchedulerWeightTable.setStatus("current")
_TnQosExtPortSchedulerWeightEntry_Object = MibTableRow
tnQosExtPortSchedulerWeightEntry = _TnQosExtPortSchedulerWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 4, 1)
)
tnQosExtPortSchedulerWeightEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtPortSchedulerWeightQid"),
)
if mibBuilder.loadTexts:
    tnQosExtPortSchedulerWeightEntry.setStatus("current")


class _TnQosExtPortSchedulerWeightQid_Type(Integer32):
    """Custom type tnQosExtPortSchedulerWeightQid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtPortSchedulerWeightQid_Type.__name__ = "Integer32"
_TnQosExtPortSchedulerWeightQid_Object = MibTableColumn
tnQosExtPortSchedulerWeightQid = _TnQosExtPortSchedulerWeightQid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 4, 1, 1),
    _TnQosExtPortSchedulerWeightQid_Type()
)
tnQosExtPortSchedulerWeightQid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtPortSchedulerWeightQid.setStatus("current")


class _TnQosExtPortSchedulerWeightVal_Type(Integer32):
    """Custom type tnQosExtPortSchedulerWeightVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TnQosExtPortSchedulerWeightVal_Type.__name__ = "Integer32"
_TnQosExtPortSchedulerWeightVal_Object = MibTableColumn
tnQosExtPortSchedulerWeightVal = _TnQosExtPortSchedulerWeightVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 4, 1, 2),
    _TnQosExtPortSchedulerWeightVal_Type()
)
tnQosExtPortSchedulerWeightVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortSchedulerWeightVal.setStatus("current")
_TnQosExtPortSchedulerWeightPercent_Type = Integer32
_TnQosExtPortSchedulerWeightPercent_Object = MibTableColumn
tnQosExtPortSchedulerWeightPercent = _TnQosExtPortSchedulerWeightPercent_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 4, 1, 3),
    _TnQosExtPortSchedulerWeightPercent_Type()
)
tnQosExtPortSchedulerWeightPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnQosExtPortSchedulerWeightPercent.setStatus("current")
_TnQosExtPortShaperTable_Object = MibTable
tnQosExtPortShaperTable = _TnQosExtPortShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tnQosExtPortShaperTable.setStatus("current")
_TnQosExtPortShaperEntry_Object = MibTableRow
tnQosExtPortShaperEntry = _TnQosExtPortShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 5, 1)
)
tnQosExtPortShaperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtPortShaperEntry.setStatus("current")


class _TnQosExtPortShaperStatus_Type(Integer32):
    """Custom type tnQosExtPortShaperStatus based on Integer32"""
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


_TnQosExtPortShaperStatus_Type.__name__ = "Integer32"
_TnQosExtPortShaperStatus_Object = MibTableColumn
tnQosExtPortShaperStatus = _TnQosExtPortShaperStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 5, 1, 1),
    _TnQosExtPortShaperStatus_Type()
)
tnQosExtPortShaperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortShaperStatus.setStatus("current")
_TnQosExtPortShaperRate_Type = Integer32
_TnQosExtPortShaperRate_Object = MibTableColumn
tnQosExtPortShaperRate = _TnQosExtPortShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 5, 1, 2),
    _TnQosExtPortShaperRate_Type()
)
tnQosExtPortShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortShaperRate.setStatus("current")
_TnQosExtPortShaperUnit_Type = TnQosExtRateUnitType
_TnQosExtPortShaperUnit_Object = MibTableColumn
tnQosExtPortShaperUnit = _TnQosExtPortShaperUnit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 5, 1, 3),
    _TnQosExtPortShaperUnit_Type()
)
tnQosExtPortShaperUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortShaperUnit.setStatus("current")
_TnQosExtPortQueueShaperTable_Object = MibTable
tnQosExtPortQueueShaperTable = _TnQosExtPortQueueShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tnQosExtPortQueueShaperTable.setStatus("current")
_TnQosExtPortQueueShaperEntry_Object = MibTableRow
tnQosExtPortQueueShaperEntry = _TnQosExtPortQueueShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 6, 1)
)
tnQosExtPortQueueShaperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtPortQueueShaperQid"),
)
if mibBuilder.loadTexts:
    tnQosExtPortQueueShaperEntry.setStatus("current")


class _TnQosExtPortQueueShaperQid_Type(Integer32):
    """Custom type tnQosExtPortQueueShaperQid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtPortQueueShaperQid_Type.__name__ = "Integer32"
_TnQosExtPortQueueShaperQid_Object = MibTableColumn
tnQosExtPortQueueShaperQid = _TnQosExtPortQueueShaperQid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 6, 1, 1),
    _TnQosExtPortQueueShaperQid_Type()
)
tnQosExtPortQueueShaperQid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtPortQueueShaperQid.setStatus("current")


class _TnQosExtPortQueueShaperStatus_Type(Integer32):
    """Custom type tnQosExtPortQueueShaperStatus based on Integer32"""
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


_TnQosExtPortQueueShaperStatus_Type.__name__ = "Integer32"
_TnQosExtPortQueueShaperStatus_Object = MibTableColumn
tnQosExtPortQueueShaperStatus = _TnQosExtPortQueueShaperStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 6, 1, 2),
    _TnQosExtPortQueueShaperStatus_Type()
)
tnQosExtPortQueueShaperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortQueueShaperStatus.setStatus("current")
_TnQosExtPortQueueShaperRate_Type = Integer32
_TnQosExtPortQueueShaperRate_Object = MibTableColumn
tnQosExtPortQueueShaperRate = _TnQosExtPortQueueShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 6, 1, 3),
    _TnQosExtPortQueueShaperRate_Type()
)
tnQosExtPortQueueShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortQueueShaperRate.setStatus("current")
_TnQosExtPortQueueShaperUnit_Type = TnQosExtRateUnitType
_TnQosExtPortQueueShaperUnit_Object = MibTableColumn
tnQosExtPortQueueShaperUnit = _TnQosExtPortQueueShaperUnit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 6, 1, 4),
    _TnQosExtPortQueueShaperUnit_Type()
)
tnQosExtPortQueueShaperUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortQueueShaperUnit.setStatus("current")


class _TnQosExtPortQueueShaperExcess_Type(Integer32):
    """Custom type tnQosExtPortQueueShaperExcess based on Integer32"""
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


_TnQosExtPortQueueShaperExcess_Type.__name__ = "Integer32"
_TnQosExtPortQueueShaperExcess_Object = MibTableColumn
tnQosExtPortQueueShaperExcess = _TnQosExtPortQueueShaperExcess_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 6, 1, 5),
    _TnQosExtPortQueueShaperExcess_Type()
)
tnQosExtPortQueueShaperExcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortQueueShaperExcess.setStatus("current")
_TnQosExtPortStormControlTable_Object = MibTable
tnQosExtPortStormControlTable = _TnQosExtPortStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tnQosExtPortStormControlTable.setStatus("current")
_TnQosExtPortStormControlEntry_Object = MibTableRow
tnQosExtPortStormControlEntry = _TnQosExtPortStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 7, 1)
)
tnQosExtPortStormControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtPortStormControlEntry.setStatus("current")


class _TnQosExtPortStormControlUnicastStatus_Type(Integer32):
    """Custom type tnQosExtPortStormControlUnicastStatus based on Integer32"""
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


_TnQosExtPortStormControlUnicastStatus_Type.__name__ = "Integer32"
_TnQosExtPortStormControlUnicastStatus_Object = MibTableColumn
tnQosExtPortStormControlUnicastStatus = _TnQosExtPortStormControlUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 7, 1, 1),
    _TnQosExtPortStormControlUnicastStatus_Type()
)
tnQosExtPortStormControlUnicastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortStormControlUnicastStatus.setStatus("current")
_TnQosExtPortStormControlUnicastRate_Type = TnQosExtRateInFps
_TnQosExtPortStormControlUnicastRate_Object = MibTableColumn
tnQosExtPortStormControlUnicastRate = _TnQosExtPortStormControlUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 7, 1, 2),
    _TnQosExtPortStormControlUnicastRate_Type()
)
tnQosExtPortStormControlUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortStormControlUnicastRate.setStatus("current")


class _TnQosExtPortStormControlMulticastStatus_Type(Integer32):
    """Custom type tnQosExtPortStormControlMulticastStatus based on Integer32"""
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


_TnQosExtPortStormControlMulticastStatus_Type.__name__ = "Integer32"
_TnQosExtPortStormControlMulticastStatus_Object = MibTableColumn
tnQosExtPortStormControlMulticastStatus = _TnQosExtPortStormControlMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 7, 1, 3),
    _TnQosExtPortStormControlMulticastStatus_Type()
)
tnQosExtPortStormControlMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortStormControlMulticastStatus.setStatus("current")
_TnQosExtPortStormControlMulticastRate_Type = TnQosExtRateInFps
_TnQosExtPortStormControlMulticastRate_Object = MibTableColumn
tnQosExtPortStormControlMulticastRate = _TnQosExtPortStormControlMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 7, 1, 4),
    _TnQosExtPortStormControlMulticastRate_Type()
)
tnQosExtPortStormControlMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortStormControlMulticastRate.setStatus("current")


class _TnQosExtPortStormControlBroadcastStatus_Type(Integer32):
    """Custom type tnQosExtPortStormControlBroadcastStatus based on Integer32"""
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


_TnQosExtPortStormControlBroadcastStatus_Type.__name__ = "Integer32"
_TnQosExtPortStormControlBroadcastStatus_Object = MibTableColumn
tnQosExtPortStormControlBroadcastStatus = _TnQosExtPortStormControlBroadcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 7, 1, 5),
    _TnQosExtPortStormControlBroadcastStatus_Type()
)
tnQosExtPortStormControlBroadcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortStormControlBroadcastStatus.setStatus("current")
_TnQosExtPortStormControlBroadcastRate_Type = TnQosExtRateInFps
_TnQosExtPortStormControlBroadcastRate_Object = MibTableColumn
tnQosExtPortStormControlBroadcastRate = _TnQosExtPortStormControlBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 7, 1, 6),
    _TnQosExtPortStormControlBroadcastRate_Type()
)
tnQosExtPortStormControlBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortStormControlBroadcastRate.setStatus("current")
_TnQosExtPortStormControl2Table_Object = MibTable
tnQosExtPortStormControl2Table = _TnQosExtPortStormControl2Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tnQosExtPortStormControl2Table.setStatus("current")
_TnQosExtPortStormControl2Entry_Object = MibTableRow
tnQosExtPortStormControl2Entry = _TnQosExtPortStormControl2Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 8, 1)
)
tnQosExtPortStormControl2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtPortStormControl2FrameType"),
)
if mibBuilder.loadTexts:
    tnQosExtPortStormControl2Entry.setStatus("current")


class _TnQosExtPortStormControl2FrameType_Type(Integer32):
    """Custom type tnQosExtPortStormControl2FrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("broadcast", 2),
          ("unknown", 3))
    )


_TnQosExtPortStormControl2FrameType_Type.__name__ = "Integer32"
_TnQosExtPortStormControl2FrameType_Object = MibTableColumn
tnQosExtPortStormControl2FrameType = _TnQosExtPortStormControl2FrameType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 8, 1, 1),
    _TnQosExtPortStormControl2FrameType_Type()
)
tnQosExtPortStormControl2FrameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtPortStormControl2FrameType.setStatus("current")
_TnQosExtPortStormControl2Rate_Type = Integer32
_TnQosExtPortStormControl2Rate_Object = MibTableColumn
tnQosExtPortStormControl2Rate = _TnQosExtPortStormControl2Rate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 8, 1, 2),
    _TnQosExtPortStormControl2Rate_Type()
)
tnQosExtPortStormControl2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortStormControl2Rate.setStatus("current")
_TnQosExtPortStormControl2RateUnit_Type = TnQosExtRateUnitType
_TnQosExtPortStormControl2RateUnit_Object = MibTableColumn
tnQosExtPortStormControl2RateUnit = _TnQosExtPortStormControl2RateUnit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 8, 1, 3),
    _TnQosExtPortStormControl2RateUnit_Type()
)
tnQosExtPortStormControl2RateUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortStormControl2RateUnit.setStatus("current")
_TnQosExtPortStormControl2Status_Type = TruthValue
_TnQosExtPortStormControl2Status_Object = MibTableColumn
tnQosExtPortStormControl2Status = _TnQosExtPortStormControl2Status_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 8, 1, 4),
    _TnQosExtPortStormControl2Status_Type()
)
tnQosExtPortStormControl2Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortStormControl2Status.setStatus("current")
_TnQosExtPortWredTable_Object = MibTable
tnQosExtPortWredTable = _TnQosExtPortWredTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tnQosExtPortWredTable.setStatus("current")
_TnQosExtPortWredEntry_Object = MibTableRow
tnQosExtPortWredEntry = _TnQosExtPortWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 9, 1)
)
tnQosExtPortWredEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtPortWredQid"),
)
if mibBuilder.loadTexts:
    tnQosExtPortWredEntry.setStatus("current")


class _TnQosExtPortWredQid_Type(Integer32):
    """Custom type tnQosExtPortWredQid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtPortWredQid_Type.__name__ = "Integer32"
_TnQosExtPortWredQid_Object = MibTableColumn
tnQosExtPortWredQid = _TnQosExtPortWredQid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 9, 1, 1),
    _TnQosExtPortWredQid_Type()
)
tnQosExtPortWredQid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtPortWredQid.setStatus("current")
_TnQosExtPortWredEnable_Type = TruthValue
_TnQosExtPortWredEnable_Object = MibTableColumn
tnQosExtPortWredEnable = _TnQosExtPortWredEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 9, 1, 2),
    _TnQosExtPortWredEnable_Type()
)
tnQosExtPortWredEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortWredEnable.setStatus("current")
_TnQosExtPortWredThresholdMin_Type = Integer32
_TnQosExtPortWredThresholdMin_Object = MibTableColumn
tnQosExtPortWredThresholdMin = _TnQosExtPortWredThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 9, 1, 3),
    _TnQosExtPortWredThresholdMin_Type()
)
tnQosExtPortWredThresholdMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortWredThresholdMin.setStatus("current")
_TnQosExtPortWredMaxDp1_Type = Integer32
_TnQosExtPortWredMaxDp1_Object = MibTableColumn
tnQosExtPortWredMaxDp1 = _TnQosExtPortWredMaxDp1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 9, 1, 4),
    _TnQosExtPortWredMaxDp1_Type()
)
tnQosExtPortWredMaxDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortWredMaxDp1.setStatus("current")
_TnQosExtPortWredMaxDp2_Type = Integer32
_TnQosExtPortWredMaxDp2_Object = MibTableColumn
tnQosExtPortWredMaxDp2 = _TnQosExtPortWredMaxDp2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 9, 1, 5),
    _TnQosExtPortWredMaxDp2_Type()
)
tnQosExtPortWredMaxDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortWredMaxDp2.setStatus("current")
_TnQosExtPortWredMaxDp3_Type = Integer32
_TnQosExtPortWredMaxDp3_Object = MibTableColumn
tnQosExtPortWredMaxDp3 = _TnQosExtPortWredMaxDp3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 9, 1, 6),
    _TnQosExtPortWredMaxDp3_Type()
)
tnQosExtPortWredMaxDp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortWredMaxDp3.setStatus("current")
_TnQosExtPortWredMaxThresh_Type = Integer32
_TnQosExtPortWredMaxThresh_Object = MibTableColumn
tnQosExtPortWredMaxThresh = _TnQosExtPortWredMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 9, 1, 7),
    _TnQosExtPortWredMaxThresh_Type()
)
tnQosExtPortWredMaxThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortWredMaxThresh.setStatus("current")


class _TnQosExtPortWredMaxUnit_Type(Integer32):
    """Custom type tnQosExtPortWredMaxUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("fill", 2))
    )


_TnQosExtPortWredMaxUnit_Type.__name__ = "Integer32"
_TnQosExtPortWredMaxUnit_Object = MibTableColumn
tnQosExtPortWredMaxUnit = _TnQosExtPortWredMaxUnit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 9, 1, 8),
    _TnQosExtPortWredMaxUnit_Type()
)
tnQosExtPortWredMaxUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortWredMaxUnit.setStatus("current")
_TnQosExtPortPolicerOrderTable_Object = MibTable
tnQosExtPortPolicerOrderTable = _TnQosExtPortPolicerOrderTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tnQosExtPortPolicerOrderTable.setStatus("current")
_TnQosExtPortPolicerOrderEntry_Object = MibTableRow
tnQosExtPortPolicerOrderEntry = _TnQosExtPortPolicerOrderEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 10, 1)
)
tnQosExtPortPolicerOrderEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtPortPolicerOrderEntry.setStatus("current")


class _TnQosExtPortPolicerOrder_Type(Integer32):
    """Custom type tnQosExtPortPolicerOrder based on Integer32"""
    defaultValue = 1


_TnQosExtPortPolicerOrder_Type.__name__ = "Integer32"
_TnQosExtPortPolicerOrder_Object = MibTableColumn
tnQosExtPortPolicerOrder = _TnQosExtPortPolicerOrder_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 1, 10, 1, 1),
    _TnQosExtPortPolicerOrder_Type()
)
tnQosExtPortPolicerOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtPortPolicerOrder.setStatus("current")
_TnQosExtL2CosMgmt_ObjectIdentity = ObjectIdentity
tnQosExtL2CosMgmt = _TnQosExtL2CosMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2)
)
_TnQosExtL2CosIfClassifDefaultTable_Object = MibTable
tnQosExtL2CosIfClassifDefaultTable = _TnQosExtL2CosIfClassifDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifDefaultTable.setStatus("current")
_TnQosExtL2CosIfClassifDefaultEntry_Object = MibTableRow
tnQosExtL2CosIfClassifDefaultEntry = _TnQosExtL2CosIfClassifDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 1, 1)
)
tnQosExtL2CosIfClassifDefaultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifDefaultEntry.setStatus("current")
_TnQosExtL2CosIfClassifDefaultClass_Type = Integer32
_TnQosExtL2CosIfClassifDefaultClass_Object = MibTableColumn
tnQosExtL2CosIfClassifDefaultClass = _TnQosExtL2CosIfClassifDefaultClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 1, 1, 1),
    _TnQosExtL2CosIfClassifDefaultClass_Type()
)
tnQosExtL2CosIfClassifDefaultClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifDefaultClass.setStatus("current")
_TnQosExtL2CosIfClassifDefaultDpl_Type = Integer32
_TnQosExtL2CosIfClassifDefaultDpl_Object = MibTableColumn
tnQosExtL2CosIfClassifDefaultDpl = _TnQosExtL2CosIfClassifDefaultDpl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 1, 1, 2),
    _TnQosExtL2CosIfClassifDefaultDpl_Type()
)
tnQosExtL2CosIfClassifDefaultDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifDefaultDpl.setStatus("current")


class _TnQosExtL2CosIfClassifDefaultPcp_Type(Integer32):
    """Custom type tnQosExtL2CosIfClassifDefaultPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnQosExtL2CosIfClassifDefaultPcp_Type.__name__ = "Integer32"
_TnQosExtL2CosIfClassifDefaultPcp_Object = MibTableColumn
tnQosExtL2CosIfClassifDefaultPcp = _TnQosExtL2CosIfClassifDefaultPcp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 1, 1, 3),
    _TnQosExtL2CosIfClassifDefaultPcp_Type()
)
tnQosExtL2CosIfClassifDefaultPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifDefaultPcp.setStatus("current")


class _TnQosExtL2CosIfClassifDefaultDei_Type(Integer32):
    """Custom type tnQosExtL2CosIfClassifDefaultDei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnQosExtL2CosIfClassifDefaultDei_Type.__name__ = "Integer32"
_TnQosExtL2CosIfClassifDefaultDei_Object = MibTableColumn
tnQosExtL2CosIfClassifDefaultDei = _TnQosExtL2CosIfClassifDefaultDei_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 1, 1, 4),
    _TnQosExtL2CosIfClassifDefaultDei_Type()
)
tnQosExtL2CosIfClassifDefaultDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifDefaultDei.setStatus("current")
_TnQosExtL2CosIfClassifTagTable_Object = MibTable
tnQosExtL2CosIfClassifTagTable = _TnQosExtL2CosIfClassifTagTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifTagTable.setStatus("current")
_TnQosExtL2CosIfClassifTagEntry_Object = MibTableRow
tnQosExtL2CosIfClassifTagEntry = _TnQosExtL2CosIfClassifTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 2, 1)
)
tnQosExtL2CosIfClassifTagEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifTagEntry.setStatus("current")


class _TnQosExtL2CosIfClassifTagMode_Type(Integer32):
    """Custom type tnQosExtL2CosIfClassifTagMode based on Integer32"""
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


_TnQosExtL2CosIfClassifTagMode_Type.__name__ = "Integer32"
_TnQosExtL2CosIfClassifTagMode_Object = MibTableColumn
tnQosExtL2CosIfClassifTagMode = _TnQosExtL2CosIfClassifTagMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 2, 1, 1),
    _TnQosExtL2CosIfClassifTagMode_Type()
)
tnQosExtL2CosIfClassifTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifTagMode.setStatus("current")
_TnQosExtL2CosIfClassifTagMapTable_Object = MibTable
tnQosExtL2CosIfClassifTagMapTable = _TnQosExtL2CosIfClassifTagMapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifTagMapTable.setStatus("current")
_TnQosExtL2CosIfClassifTagMapEntry_Object = MibTableRow
tnQosExtL2CosIfClassifTagMapEntry = _TnQosExtL2CosIfClassifTagMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 3, 1)
)
tnQosExtL2CosIfClassifTagMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtL2CosIfClassifTagMapPcp"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtL2CosIfClassifTagMapDei"),
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifTagMapEntry.setStatus("current")


class _TnQosExtL2CosIfClassifTagMapPcp_Type(Integer32):
    """Custom type tnQosExtL2CosIfClassifTagMapPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnQosExtL2CosIfClassifTagMapPcp_Type.__name__ = "Integer32"
_TnQosExtL2CosIfClassifTagMapPcp_Object = MibTableColumn
tnQosExtL2CosIfClassifTagMapPcp = _TnQosExtL2CosIfClassifTagMapPcp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 3, 1, 1),
    _TnQosExtL2CosIfClassifTagMapPcp_Type()
)
tnQosExtL2CosIfClassifTagMapPcp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifTagMapPcp.setStatus("current")


class _TnQosExtL2CosIfClassifTagMapDei_Type(Integer32):
    """Custom type tnQosExtL2CosIfClassifTagMapDei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnQosExtL2CosIfClassifTagMapDei_Type.__name__ = "Integer32"
_TnQosExtL2CosIfClassifTagMapDei_Object = MibTableColumn
tnQosExtL2CosIfClassifTagMapDei = _TnQosExtL2CosIfClassifTagMapDei_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 3, 1, 2),
    _TnQosExtL2CosIfClassifTagMapDei_Type()
)
tnQosExtL2CosIfClassifTagMapDei.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifTagMapDei.setStatus("current")
_TnQosExtL2CosIfClassifTagMapClass_Type = Integer32
_TnQosExtL2CosIfClassifTagMapClass_Object = MibTableColumn
tnQosExtL2CosIfClassifTagMapClass = _TnQosExtL2CosIfClassifTagMapClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 3, 1, 3),
    _TnQosExtL2CosIfClassifTagMapClass_Type()
)
tnQosExtL2CosIfClassifTagMapClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifTagMapClass.setStatus("current")
_TnQosExtL2CosIfClassifTagMapDpl_Type = Integer32
_TnQosExtL2CosIfClassifTagMapDpl_Object = MibTableColumn
tnQosExtL2CosIfClassifTagMapDpl = _TnQosExtL2CosIfClassifTagMapDpl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 3, 1, 4),
    _TnQosExtL2CosIfClassifTagMapDpl_Type()
)
tnQosExtL2CosIfClassifTagMapDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfClassifTagMapDpl.setStatus("current")
_TnQosExtL2CosIfTagRemarkingModeTable_Object = MibTable
tnQosExtL2CosIfTagRemarkingModeTable = _TnQosExtL2CosIfTagRemarkingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingModeTable.setStatus("current")
_TnQosExtL2CosIfTagRemarkingModeEntry_Object = MibTableRow
tnQosExtL2CosIfTagRemarkingModeEntry = _TnQosExtL2CosIfTagRemarkingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 4, 1)
)
tnQosExtL2CosIfTagRemarkingModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingModeEntry.setStatus("current")


class _TnQosExtL2CosIfTagRemarkingMode_Type(Integer32):
    """Custom type tnQosExtL2CosIfTagRemarkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classified", 1),
          ("default", 2),
          ("mapped", 3))
    )


_TnQosExtL2CosIfTagRemarkingMode_Type.__name__ = "Integer32"
_TnQosExtL2CosIfTagRemarkingMode_Object = MibTableColumn
tnQosExtL2CosIfTagRemarkingMode = _TnQosExtL2CosIfTagRemarkingMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 4, 1, 1),
    _TnQosExtL2CosIfTagRemarkingMode_Type()
)
tnQosExtL2CosIfTagRemarkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingMode.setStatus("current")
_TnQosExtL2CosIfTagRemarkingDefaultTable_Object = MibTable
tnQosExtL2CosIfTagRemarkingDefaultTable = _TnQosExtL2CosIfTagRemarkingDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingDefaultTable.setStatus("current")
_TnQosExtL2CosIfTagRemarkingDefaultEntry_Object = MibTableRow
tnQosExtL2CosIfTagRemarkingDefaultEntry = _TnQosExtL2CosIfTagRemarkingDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 5, 1)
)
tnQosExtL2CosIfTagRemarkingDefaultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingDefaultEntry.setStatus("current")


class _TnQosExtL2CosIfTagRemarkingDefaultPcp_Type(Integer32):
    """Custom type tnQosExtL2CosIfTagRemarkingDefaultPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnQosExtL2CosIfTagRemarkingDefaultPcp_Type.__name__ = "Integer32"
_TnQosExtL2CosIfTagRemarkingDefaultPcp_Object = MibTableColumn
tnQosExtL2CosIfTagRemarkingDefaultPcp = _TnQosExtL2CosIfTagRemarkingDefaultPcp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 5, 1, 1),
    _TnQosExtL2CosIfTagRemarkingDefaultPcp_Type()
)
tnQosExtL2CosIfTagRemarkingDefaultPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingDefaultPcp.setStatus("current")


class _TnQosExtL2CosIfTagRemarkingDefaultDei_Type(Integer32):
    """Custom type tnQosExtL2CosIfTagRemarkingDefaultDei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnQosExtL2CosIfTagRemarkingDefaultDei_Type.__name__ = "Integer32"
_TnQosExtL2CosIfTagRemarkingDefaultDei_Object = MibTableColumn
tnQosExtL2CosIfTagRemarkingDefaultDei = _TnQosExtL2CosIfTagRemarkingDefaultDei_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 5, 1, 2),
    _TnQosExtL2CosIfTagRemarkingDefaultDei_Type()
)
tnQosExtL2CosIfTagRemarkingDefaultDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingDefaultDei.setStatus("current")
_TnQosExtL2CosIfTagRemarkingMappingTable_Object = MibTable
tnQosExtL2CosIfTagRemarkingMappingTable = _TnQosExtL2CosIfTagRemarkingMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingMappingTable.setStatus("current")
_TnQosExtL2CosIfTagRemarkingMappingEntry_Object = MibTableRow
tnQosExtL2CosIfTagRemarkingMappingEntry = _TnQosExtL2CosIfTagRemarkingMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 6, 1)
)
tnQosExtL2CosIfTagRemarkingMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtL2CosIfTagRemarkingClass"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtL2CosIfTagRemarkingDpl"),
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingMappingEntry.setStatus("current")


class _TnQosExtL2CosIfTagRemarkingClass_Type(Integer32):
    """Custom type tnQosExtL2CosIfTagRemarkingClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtL2CosIfTagRemarkingClass_Type.__name__ = "Integer32"
_TnQosExtL2CosIfTagRemarkingClass_Object = MibTableColumn
tnQosExtL2CosIfTagRemarkingClass = _TnQosExtL2CosIfTagRemarkingClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 6, 1, 1),
    _TnQosExtL2CosIfTagRemarkingClass_Type()
)
tnQosExtL2CosIfTagRemarkingClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingClass.setStatus("current")


class _TnQosExtL2CosIfTagRemarkingDpl_Type(Integer32):
    """Custom type tnQosExtL2CosIfTagRemarkingDpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtL2CosIfTagRemarkingDpl_Type.__name__ = "Integer32"
_TnQosExtL2CosIfTagRemarkingDpl_Object = MibTableColumn
tnQosExtL2CosIfTagRemarkingDpl = _TnQosExtL2CosIfTagRemarkingDpl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 6, 1, 2),
    _TnQosExtL2CosIfTagRemarkingDpl_Type()
)
tnQosExtL2CosIfTagRemarkingDpl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingDpl.setStatus("current")


class _TnQosExtL2CosIfTagRemarkingPcp_Type(Integer32):
    """Custom type tnQosExtL2CosIfTagRemarkingPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnQosExtL2CosIfTagRemarkingPcp_Type.__name__ = "Integer32"
_TnQosExtL2CosIfTagRemarkingPcp_Object = MibTableColumn
tnQosExtL2CosIfTagRemarkingPcp = _TnQosExtL2CosIfTagRemarkingPcp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 6, 1, 3),
    _TnQosExtL2CosIfTagRemarkingPcp_Type()
)
tnQosExtL2CosIfTagRemarkingPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingPcp.setStatus("current")


class _TnQosExtL2CosIfTagRemarkingDei_Type(Integer32):
    """Custom type tnQosExtL2CosIfTagRemarkingDei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnQosExtL2CosIfTagRemarkingDei_Type.__name__ = "Integer32"
_TnQosExtL2CosIfTagRemarkingDei_Object = MibTableColumn
tnQosExtL2CosIfTagRemarkingDei = _TnQosExtL2CosIfTagRemarkingDei_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 6, 1, 4),
    _TnQosExtL2CosIfTagRemarkingDei_Type()
)
tnQosExtL2CosIfTagRemarkingDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingDei.setStatus("current")
_TnQosExtL2CosIfTagRemarkingDplMappingTable_Object = MibTable
tnQosExtL2CosIfTagRemarkingDplMappingTable = _TnQosExtL2CosIfTagRemarkingDplMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingDplMappingTable.setStatus("current")
_TnQosExtL2CosIfTagRemarkingDplMappingEntry_Object = MibTableRow
tnQosExtL2CosIfTagRemarkingDplMappingEntry = _TnQosExtL2CosIfTagRemarkingDplMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 7, 1)
)
tnQosExtL2CosIfTagRemarkingDplMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtL2CosIfTagRemarkingDplMappingClassifDpl"),
)
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingDplMappingEntry.setStatus("current")


class _TnQosExtL2CosIfTagRemarkingDplMappingClassifDpl_Type(Integer32):
    """Custom type tnQosExtL2CosIfTagRemarkingDplMappingClassifDpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtL2CosIfTagRemarkingDplMappingClassifDpl_Type.__name__ = "Integer32"
_TnQosExtL2CosIfTagRemarkingDplMappingClassifDpl_Object = MibTableColumn
tnQosExtL2CosIfTagRemarkingDplMappingClassifDpl = _TnQosExtL2CosIfTagRemarkingDplMappingClassifDpl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 7, 1, 1),
    _TnQosExtL2CosIfTagRemarkingDplMappingClassifDpl_Type()
)
tnQosExtL2CosIfTagRemarkingDplMappingClassifDpl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingDplMappingClassifDpl.setStatus("current")
_TnQosExtL2CosIfTagRemarkingDplMappingDpl_Type = Integer32
_TnQosExtL2CosIfTagRemarkingDplMappingDpl_Object = MibTableColumn
tnQosExtL2CosIfTagRemarkingDplMappingDpl = _TnQosExtL2CosIfTagRemarkingDplMappingDpl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 2, 7, 1, 2),
    _TnQosExtL2CosIfTagRemarkingDplMappingDpl_Type()
)
tnQosExtL2CosIfTagRemarkingDplMappingDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtL2CosIfTagRemarkingDplMappingDpl.setStatus("current")
_TnQosExtDscpMgmt_ObjectIdentity = ObjectIdentity
tnQosExtDscpMgmt = _TnQosExtDscpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3)
)
_TnQosExtDscpIfClassifBaseTable_Object = MibTable
tnQosExtDscpIfClassifBaseTable = _TnQosExtDscpIfClassifBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifBaseTable.setStatus("current")
_TnQosExtDscpIfClassifBaseEntry_Object = MibTableRow
tnQosExtDscpIfClassifBaseEntry = _TnQosExtDscpIfClassifBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 1, 1)
)
tnQosExtDscpIfClassifBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifBaseEntry.setStatus("current")


class _TnQosExtDscpIfClassifBaseDscp_Type(Integer32):
    """Custom type tnQosExtDscpIfClassifBaseDscp based on Integer32"""
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


_TnQosExtDscpIfClassifBaseDscp_Type.__name__ = "Integer32"
_TnQosExtDscpIfClassifBaseDscp_Object = MibTableColumn
tnQosExtDscpIfClassifBaseDscp = _TnQosExtDscpIfClassifBaseDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 1, 1, 1),
    _TnQosExtDscpIfClassifBaseDscp_Type()
)
tnQosExtDscpIfClassifBaseDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifBaseDscp.setStatus("current")
_TnQosExtDscpIfTransTable_Object = MibTable
tnQosExtDscpIfTransTable = _TnQosExtDscpIfTransTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfTransTable.setStatus("current")
_TnQosExtDscpIfTransEntry_Object = MibTableRow
tnQosExtDscpIfTransEntry = _TnQosExtDscpIfTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 2, 1)
)
tnQosExtDscpIfTransEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfTransEntry.setStatus("current")


class _TnQosExtDscpIfTransMode_Type(Integer32):
    """Custom type tnQosExtDscpIfTransMode based on Integer32"""
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


_TnQosExtDscpIfTransMode_Type.__name__ = "Integer32"
_TnQosExtDscpIfTransMode_Object = MibTableColumn
tnQosExtDscpIfTransMode = _TnQosExtDscpIfTransMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 2, 1, 1),
    _TnQosExtDscpIfTransMode_Type()
)
tnQosExtDscpIfTransMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpIfTransMode.setStatus("current")
_TnQosExtDscpIfTransMapTable_Object = MibTable
tnQosExtDscpIfTransMapTable = _TnQosExtDscpIfTransMapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfTransMapTable.setStatus("current")
_TnQosExtDscpIfTransMapEntry_Object = MibTableRow
tnQosExtDscpIfTransMapEntry = _TnQosExtDscpIfTransMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 3, 1)
)
tnQosExtDscpIfTransMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtDscpIfTransMapDscp"),
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfTransMapEntry.setStatus("current")


class _TnQosExtDscpIfTransMapDscp_Type(Integer32):
    """Custom type tnQosExtDscpIfTransMapDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtDscpIfTransMapDscp_Type.__name__ = "Integer32"
_TnQosExtDscpIfTransMapDscp_Object = MibTableColumn
tnQosExtDscpIfTransMapDscp = _TnQosExtDscpIfTransMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 3, 1, 1),
    _TnQosExtDscpIfTransMapDscp_Type()
)
tnQosExtDscpIfTransMapDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtDscpIfTransMapDscp.setStatus("current")


class _TnQosExtDscpIfTransMapToDscp_Type(Integer32):
    """Custom type tnQosExtDscpIfTransMapToDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtDscpIfTransMapToDscp_Type.__name__ = "Integer32"
_TnQosExtDscpIfTransMapToDscp_Object = MibTableColumn
tnQosExtDscpIfTransMapToDscp = _TnQosExtDscpIfTransMapToDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 3, 1, 2),
    _TnQosExtDscpIfTransMapToDscp_Type()
)
tnQosExtDscpIfTransMapToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpIfTransMapToDscp.setStatus("current")
_TnQosExtDscpClassifMapTable_Object = MibTable
tnQosExtDscpClassifMapTable = _TnQosExtDscpClassifMapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tnQosExtDscpClassifMapTable.setStatus("current")
_TnQosExtDscpClassifMapEntry_Object = MibTableRow
tnQosExtDscpClassifMapEntry = _TnQosExtDscpClassifMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 4, 1)
)
tnQosExtDscpClassifMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtDscpClassifMapDscp"),
)
if mibBuilder.loadTexts:
    tnQosExtDscpClassifMapEntry.setStatus("current")


class _TnQosExtDscpClassifMapDscp_Type(Integer32):
    """Custom type tnQosExtDscpClassifMapDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtDscpClassifMapDscp_Type.__name__ = "Integer32"
_TnQosExtDscpClassifMapDscp_Object = MibTableColumn
tnQosExtDscpClassifMapDscp = _TnQosExtDscpClassifMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 4, 1, 1),
    _TnQosExtDscpClassifMapDscp_Type()
)
tnQosExtDscpClassifMapDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtDscpClassifMapDscp.setStatus("current")


class _TnQosExtDscpClassifMapTrust_Type(Integer32):
    """Custom type tnQosExtDscpClassifMapTrust based on Integer32"""
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


_TnQosExtDscpClassifMapTrust_Type.__name__ = "Integer32"
_TnQosExtDscpClassifMapTrust_Object = MibTableColumn
tnQosExtDscpClassifMapTrust = _TnQosExtDscpClassifMapTrust_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 4, 1, 2),
    _TnQosExtDscpClassifMapTrust_Type()
)
tnQosExtDscpClassifMapTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpClassifMapTrust.setStatus("current")
_TnQosExtDscpClassifMapClass_Type = Integer32
_TnQosExtDscpClassifMapClass_Object = MibTableColumn
tnQosExtDscpClassifMapClass = _TnQosExtDscpClassifMapClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 4, 1, 3),
    _TnQosExtDscpClassifMapClass_Type()
)
tnQosExtDscpClassifMapClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpClassifMapClass.setStatus("current")
_TnQosExtDscpClassifMapDpl_Type = Integer32
_TnQosExtDscpClassifMapDpl_Object = MibTableColumn
tnQosExtDscpClassifMapDpl = _TnQosExtDscpClassifMapDpl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 4, 1, 4),
    _TnQosExtDscpClassifMapDpl_Type()
)
tnQosExtDscpClassifMapDpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpClassifMapDpl.setStatus("current")
_TnQosExtDscpIfClassifExtTable_Object = MibTable
tnQosExtDscpIfClassifExtTable = _TnQosExtDscpIfClassifExtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtTable.setStatus("current")
_TnQosExtDscpIfClassifExtEntry_Object = MibTableRow
tnQosExtDscpIfClassifExtEntry = _TnQosExtDscpIfClassifExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 5, 1)
)
tnQosExtDscpIfClassifExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtEntry.setStatus("current")


class _TnQosExtDscpIfClassifExtMode_Type(Integer32):
    """Custom type tnQosExtDscpIfClassifExtMode based on Integer32"""
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
        *(("disable", 1),
          ("dscp0", 2),
          ("selected", 3),
          ("all", 4))
    )


_TnQosExtDscpIfClassifExtMode_Type.__name__ = "Integer32"
_TnQosExtDscpIfClassifExtMode_Object = MibTableColumn
tnQosExtDscpIfClassifExtMode = _TnQosExtDscpIfClassifExtMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 5, 1, 1),
    _TnQosExtDscpIfClassifExtMode_Type()
)
tnQosExtDscpIfClassifExtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtMode.setStatus("current")
_TnQosExtDscpIfClassifExtDscpTable_Object = MibTable
tnQosExtDscpIfClassifExtDscpTable = _TnQosExtDscpIfClassifExtDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtDscpTable.setStatus("current")
_TnQosExtDscpIfClassifExtDscpEntry_Object = MibTableRow
tnQosExtDscpIfClassifExtDscpEntry = _TnQosExtDscpIfClassifExtDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 6, 1)
)
tnQosExtDscpIfClassifExtDscpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtDscpIfClassifExtDscp"),
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtDscpEntry.setStatus("current")


class _TnQosExtDscpIfClassifExtDscp_Type(Integer32):
    """Custom type tnQosExtDscpIfClassifExtDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtDscpIfClassifExtDscp_Type.__name__ = "Integer32"
_TnQosExtDscpIfClassifExtDscp_Object = MibTableColumn
tnQosExtDscpIfClassifExtDscp = _TnQosExtDscpIfClassifExtDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 6, 1, 1),
    _TnQosExtDscpIfClassifExtDscp_Type()
)
tnQosExtDscpIfClassifExtDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtDscp.setStatus("current")


class _TnQosExtDscpIfClassifExtDscpMode_Type(Integer32):
    """Custom type tnQosExtDscpIfClassifExtDscpMode based on Integer32"""
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


_TnQosExtDscpIfClassifExtDscpMode_Type.__name__ = "Integer32"
_TnQosExtDscpIfClassifExtDscpMode_Object = MibTableColumn
tnQosExtDscpIfClassifExtDscpMode = _TnQosExtDscpIfClassifExtDscpMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 6, 1, 2),
    _TnQosExtDscpIfClassifExtDscpMode_Type()
)
tnQosExtDscpIfClassifExtDscpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtDscpMode.setStatus("current")
_TnQosExtDscpIfClassifExtMapTable_Object = MibTable
tnQosExtDscpIfClassifExtMapTable = _TnQosExtDscpIfClassifExtMapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtMapTable.setStatus("current")
_TnQosExtDscpIfClassifExtMapEntry_Object = MibTableRow
tnQosExtDscpIfClassifExtMapEntry = _TnQosExtDscpIfClassifExtMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 7, 1)
)
tnQosExtDscpIfClassifExtMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtDscpIfClassifExtMapClass"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtDscpIfClassifExtMapDpl"),
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtMapEntry.setStatus("current")


class _TnQosExtDscpIfClassifExtMapClass_Type(Integer32):
    """Custom type tnQosExtDscpIfClassifExtMapClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtDscpIfClassifExtMapClass_Type.__name__ = "Integer32"
_TnQosExtDscpIfClassifExtMapClass_Object = MibTableColumn
tnQosExtDscpIfClassifExtMapClass = _TnQosExtDscpIfClassifExtMapClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 7, 1, 1),
    _TnQosExtDscpIfClassifExtMapClass_Type()
)
tnQosExtDscpIfClassifExtMapClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtMapClass.setStatus("current")


class _TnQosExtDscpIfClassifExtMapDpl_Type(Integer32):
    """Custom type tnQosExtDscpIfClassifExtMapDpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtDscpIfClassifExtMapDpl_Type.__name__ = "Integer32"
_TnQosExtDscpIfClassifExtMapDpl_Object = MibTableColumn
tnQosExtDscpIfClassifExtMapDpl = _TnQosExtDscpIfClassifExtMapDpl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 7, 1, 2),
    _TnQosExtDscpIfClassifExtMapDpl_Type()
)
tnQosExtDscpIfClassifExtMapDpl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtMapDpl.setStatus("current")


class _TnQosExtDscpIfClassifExtMapDscp_Type(Integer32):
    """Custom type tnQosExtDscpIfClassifExtMapDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtDscpIfClassifExtMapDscp_Type.__name__ = "Integer32"
_TnQosExtDscpIfClassifExtMapDscp_Object = MibTableColumn
tnQosExtDscpIfClassifExtMapDscp = _TnQosExtDscpIfClassifExtMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 7, 1, 3),
    _TnQosExtDscpIfClassifExtMapDscp_Type()
)
tnQosExtDscpIfClassifExtMapDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpIfClassifExtMapDscp.setStatus("current")
_TnQosExtDscpIfEgressRemarkTable_Object = MibTable
tnQosExtDscpIfEgressRemarkTable = _TnQosExtDscpIfEgressRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 8)
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfEgressRemarkTable.setStatus("current")
_TnQosExtDscpIfEgressRemarkEntry_Object = MibTableRow
tnQosExtDscpIfEgressRemarkEntry = _TnQosExtDscpIfEgressRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 8, 1)
)
tnQosExtDscpIfEgressRemarkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfEgressRemarkEntry.setStatus("current")


class _TnQosExtDscpIfEgressRemarkMode_Type(Integer32):
    """Custom type tnQosExtDscpIfEgressRemarkMode based on Integer32"""
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
        *(("disable", 1),
          ("enable", 2),
          ("remapDpUnaware", 3),
          ("remapDpAware", 4))
    )


_TnQosExtDscpIfEgressRemarkMode_Type.__name__ = "Integer32"
_TnQosExtDscpIfEgressRemarkMode_Object = MibTableColumn
tnQosExtDscpIfEgressRemarkMode = _TnQosExtDscpIfEgressRemarkMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 8, 1, 1),
    _TnQosExtDscpIfEgressRemarkMode_Type()
)
tnQosExtDscpIfEgressRemarkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpIfEgressRemarkMode.setStatus("current")
_TnQosExtDscpIfEgressRemarkMapTable_Object = MibTable
tnQosExtDscpIfEgressRemarkMapTable = _TnQosExtDscpIfEgressRemarkMapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 9)
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfEgressRemarkMapTable.setStatus("current")
_TnQosExtDscpIfEgressRemarkMapEntry_Object = MibTableRow
tnQosExtDscpIfEgressRemarkMapEntry = _TnQosExtDscpIfEgressRemarkMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 9, 1)
)
tnQosExtDscpIfEgressRemarkMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtDscpIfEgressRemarkMapDscp"),
    (0, "TN-QOS-EXT-MIB", "tnQosExtDscpIfEgressRemarkMapDpl"),
)
if mibBuilder.loadTexts:
    tnQosExtDscpIfEgressRemarkMapEntry.setStatus("current")


class _TnQosExtDscpIfEgressRemarkMapDscp_Type(Integer32):
    """Custom type tnQosExtDscpIfEgressRemarkMapDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtDscpIfEgressRemarkMapDscp_Type.__name__ = "Integer32"
_TnQosExtDscpIfEgressRemarkMapDscp_Object = MibTableColumn
tnQosExtDscpIfEgressRemarkMapDscp = _TnQosExtDscpIfEgressRemarkMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 9, 1, 1),
    _TnQosExtDscpIfEgressRemarkMapDscp_Type()
)
tnQosExtDscpIfEgressRemarkMapDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtDscpIfEgressRemarkMapDscp.setStatus("current")


class _TnQosExtDscpIfEgressRemarkMapDpl_Type(Integer32):
    """Custom type tnQosExtDscpIfEgressRemarkMapDpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtDscpIfEgressRemarkMapDpl_Type.__name__ = "Integer32"
_TnQosExtDscpIfEgressRemarkMapDpl_Object = MibTableColumn
tnQosExtDscpIfEgressRemarkMapDpl = _TnQosExtDscpIfEgressRemarkMapDpl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 9, 1, 2),
    _TnQosExtDscpIfEgressRemarkMapDpl_Type()
)
tnQosExtDscpIfEgressRemarkMapDpl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtDscpIfEgressRemarkMapDpl.setStatus("current")


class _TnQosExtDscpIfEgressRemarkMapToDscp_Type(Integer32):
    """Custom type tnQosExtDscpIfEgressRemarkMapToDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtDscpIfEgressRemarkMapToDscp_Type.__name__ = "Integer32"
_TnQosExtDscpIfEgressRemarkMapToDscp_Object = MibTableColumn
tnQosExtDscpIfEgressRemarkMapToDscp = _TnQosExtDscpIfEgressRemarkMapToDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 3, 9, 1, 3),
    _TnQosExtDscpIfEgressRemarkMapToDscp_Type()
)
tnQosExtDscpIfEgressRemarkMapToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtDscpIfEgressRemarkMapToDscp.setStatus("current")
_TnQosExtQclMgmt_ObjectIdentity = ObjectIdentity
tnQosExtQclMgmt = _TnQosExtQclMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4)
)
_TnQosExtQclTable_Object = MibTable
tnQosExtQclTable = _TnQosExtQclTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnQosExtQclTable.setStatus("current")
_TnQosExtQclEntry_Object = MibTableRow
tnQosExtQclEntry = _TnQosExtQclEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1)
)
tnQosExtQclEntry.setIndexNames(
    (0, "TN-QOS-EXT-MIB", "tnQosExtQclIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtQclEntry.setStatus("current")


class _TnQosExtQclIndex_Type(Integer32):
    """Custom type tnQosExtQclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11111),
    )


_TnQosExtQclIndex_Type.__name__ = "Integer32"
_TnQosExtQclIndex_Object = MibTableColumn
tnQosExtQclIndex = _TnQosExtQclIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 1),
    _TnQosExtQclIndex_Type()
)
tnQosExtQclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnQosExtQclIndex.setStatus("current")
_TnQosExtQclId_Type = Integer32
_TnQosExtQclId_Object = MibTableColumn
tnQosExtQclId = _TnQosExtQclId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 2),
    _TnQosExtQclId_Type()
)
tnQosExtQclId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnQosExtQclId.setStatus("current")
_TnQosExtQclNextQclId_Type = Integer32
_TnQosExtQclNextQclId_Object = MibTableColumn
tnQosExtQclNextQclId = _TnQosExtQclNextQclId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 3),
    _TnQosExtQclNextQclId_Type()
)
tnQosExtQclNextQclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclNextQclId.setStatus("current")
_TnQosExtQclPortList_Type = PortList
_TnQosExtQclPortList_Object = MibTableColumn
tnQosExtQclPortList = _TnQosExtQclPortList_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 4),
    _TnQosExtQclPortList_Type()
)
tnQosExtQclPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclPortList.setStatus("current")


class _TnQosExtQclTagType_Type(Integer32):
    """Custom type tnQosExtQclTagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2),
          ("any", 3))
    )


_TnQosExtQclTagType_Type.__name__ = "Integer32"
_TnQosExtQclTagType_Object = MibTableColumn
tnQosExtQclTagType = _TnQosExtQclTagType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 5),
    _TnQosExtQclTagType_Type()
)
tnQosExtQclTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclTagType.setStatus("current")


class _TnQosExtQclTagVlanType_Type(Integer32):
    """Custom type tnQosExtQclTagVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnQosExtQclTagVlanType_Type.__name__ = "Integer32"
_TnQosExtQclTagVlanType_Object = MibTableColumn
tnQosExtQclTagVlanType = _TnQosExtQclTagVlanType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 6),
    _TnQosExtQclTagVlanType_Type()
)
tnQosExtQclTagVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclTagVlanType.setStatus("current")
_TnQosExtQclTagVlanVal_Type = VlanIndex
_TnQosExtQclTagVlanVal_Object = MibTableColumn
tnQosExtQclTagVlanVal = _TnQosExtQclTagVlanVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 7),
    _TnQosExtQclTagVlanVal_Type()
)
tnQosExtQclTagVlanVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclTagVlanVal.setStatus("current")
_TnQosExtQclTagVlanMin_Type = VlanIndex
_TnQosExtQclTagVlanMin_Object = MibTableColumn
tnQosExtQclTagVlanMin = _TnQosExtQclTagVlanMin_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 8),
    _TnQosExtQclTagVlanMin_Type()
)
tnQosExtQclTagVlanMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclTagVlanMin.setStatus("current")
_TnQosExtQclTagVlanMax_Type = VlanIndex
_TnQosExtQclTagVlanMax_Object = MibTableColumn
tnQosExtQclTagVlanMax = _TnQosExtQclTagVlanMax_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 9),
    _TnQosExtQclTagVlanMax_Type()
)
tnQosExtQclTagVlanMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclTagVlanMax.setStatus("current")


class _TnQosExtQclTagPcp_Type(Bits):
    """Custom type tnQosExtQclTagPcp based on Bits"""
    namedValues = NamedValues(
        ("none", 0)
    )

_TnQosExtQclTagPcp_Type.__name__ = "Bits"
_TnQosExtQclTagPcp_Object = MibTableColumn
tnQosExtQclTagPcp = _TnQosExtQclTagPcp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 10),
    _TnQosExtQclTagPcp_Type()
)
tnQosExtQclTagPcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclTagPcp.setStatus("current")


class _TnQosExtQclTagDei_Type(Integer32):
    """Custom type tnQosExtQclTagDei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("dei0", 2),
          ("dei1", 3))
    )


_TnQosExtQclTagDei_Type.__name__ = "Integer32"
_TnQosExtQclTagDei_Object = MibTableColumn
tnQosExtQclTagDei = _TnQosExtQclTagDei_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 11),
    _TnQosExtQclTagDei_Type()
)
tnQosExtQclTagDei.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclTagDei.setStatus("current")


class _TnQosExtQclSMacType_Type(Integer32):
    """Custom type tnQosExtQclSMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnQosExtQclSMacType_Type.__name__ = "Integer32"
_TnQosExtQclSMacType_Object = MibTableColumn
tnQosExtQclSMacType = _TnQosExtQclSMacType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 12),
    _TnQosExtQclSMacType_Type()
)
tnQosExtQclSMacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclSMacType.setStatus("current")
_TnQosExtQclSMac_Type = MacAddress
_TnQosExtQclSMac_Object = MibTableColumn
tnQosExtQclSMac = _TnQosExtQclSMac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 13),
    _TnQosExtQclSMac_Type()
)
tnQosExtQclSMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclSMac.setStatus("current")


class _TnQosExtQclDMacType_Type(Integer32):
    """Custom type tnQosExtQclDMacType based on Integer32"""
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
        *(("any", 1),
          ("unicast", 2),
          ("multicast", 3),
          ("broadcast", 4))
    )


_TnQosExtQclDMacType_Type.__name__ = "Integer32"
_TnQosExtQclDMacType_Object = MibTableColumn
tnQosExtQclDMacType = _TnQosExtQclDMacType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 14),
    _TnQosExtQclDMacType_Type()
)
tnQosExtQclDMacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclDMacType.setStatus("current")


class _TnQosExtQclFrameType_Type(Integer32):
    """Custom type tnQosExtQclFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("ethernet", 2),
          ("llc", 3),
          ("snap", 4),
          ("ipv4", 5),
          ("ipv6", 6))
    )


_TnQosExtQclFrameType_Type.__name__ = "Integer32"
_TnQosExtQclFrameType_Object = MibTableColumn
tnQosExtQclFrameType = _TnQosExtQclFrameType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 15),
    _TnQosExtQclFrameType_Type()
)
tnQosExtQclFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclFrameType.setStatus("current")


class _TnQosExtQclActClassDefault_Type(Integer32):
    """Custom type tnQosExtQclActClassDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("specific", 2))
    )


_TnQosExtQclActClassDefault_Type.__name__ = "Integer32"
_TnQosExtQclActClassDefault_Object = MibTableColumn
tnQosExtQclActClassDefault = _TnQosExtQclActClassDefault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 16),
    _TnQosExtQclActClassDefault_Type()
)
tnQosExtQclActClassDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclActClassDefault.setStatus("current")
_TnQosExtQclActClass_Type = Integer32
_TnQosExtQclActClass_Object = MibTableColumn
tnQosExtQclActClass = _TnQosExtQclActClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 17),
    _TnQosExtQclActClass_Type()
)
tnQosExtQclActClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclActClass.setStatus("current")


class _TnQosExtQclActDplDefault_Type(Integer32):
    """Custom type tnQosExtQclActDplDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("specific", 2))
    )


_TnQosExtQclActDplDefault_Type.__name__ = "Integer32"
_TnQosExtQclActDplDefault_Object = MibTableColumn
tnQosExtQclActDplDefault = _TnQosExtQclActDplDefault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 18),
    _TnQosExtQclActDplDefault_Type()
)
tnQosExtQclActDplDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclActDplDefault.setStatus("current")
_TnQosExtQclActDpl_Type = Integer32
_TnQosExtQclActDpl_Object = MibTableColumn
tnQosExtQclActDpl = _TnQosExtQclActDpl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 19),
    _TnQosExtQclActDpl_Type()
)
tnQosExtQclActDpl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclActDpl.setStatus("current")


class _TnQosExtQclActDscpDefault_Type(Integer32):
    """Custom type tnQosExtQclActDscpDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("specific", 2))
    )


_TnQosExtQclActDscpDefault_Type.__name__ = "Integer32"
_TnQosExtQclActDscpDefault_Object = MibTableColumn
tnQosExtQclActDscpDefault = _TnQosExtQclActDscpDefault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 20),
    _TnQosExtQclActDscpDefault_Type()
)
tnQosExtQclActDscpDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclActDscpDefault.setStatus("current")


class _TnQosExtQclActDscp_Type(Integer32):
    """Custom type tnQosExtQclActDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtQclActDscp_Type.__name__ = "Integer32"
_TnQosExtQclActDscp_Object = MibTableColumn
tnQosExtQclActDscp = _TnQosExtQclActDscp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 21),
    _TnQosExtQclActDscp_Type()
)
tnQosExtQclActDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclActDscp.setStatus("current")


class _TnQosExtQclConflict_Type(Integer32):
    """Custom type tnQosExtQclConflict based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_TnQosExtQclConflict_Type.__name__ = "Integer32"
_TnQosExtQclConflict_Object = MibTableColumn
tnQosExtQclConflict = _TnQosExtQclConflict_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 22),
    _TnQosExtQclConflict_Type()
)
tnQosExtQclConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnQosExtQclConflict.setStatus("current")
_TnQosExtQclStatus_Type = RowStatus
_TnQosExtQclStatus_Object = MibTableColumn
tnQosExtQclStatus = _TnQosExtQclStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 1, 1, 23),
    _TnQosExtQclStatus_Type()
)
tnQosExtQclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnQosExtQclStatus.setStatus("current")
_TnQosExtQclL2Table_Object = MibTable
tnQosExtQclL2Table = _TnQosExtQclL2Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tnQosExtQclL2Table.setStatus("current")
_TnQosExtQclL2Entry_Object = MibTableRow
tnQosExtQclL2Entry = _TnQosExtQclL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1)
)
tnQosExtQclL2Entry.setIndexNames(
    (0, "TN-QOS-EXT-MIB", "tnQosExtQclIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtQclL2Entry.setStatus("current")


class _TnQosExtQclEtherType_Type(Integer32):
    """Custom type tnQosExtQclEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnQosExtQclEtherType_Type.__name__ = "Integer32"
_TnQosExtQclEtherType_Object = MibTableColumn
tnQosExtQclEtherType = _TnQosExtQclEtherType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1, 1),
    _TnQosExtQclEtherType_Type()
)
tnQosExtQclEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclEtherType.setStatus("current")


class _TnQosExtQclEtherVal_Type(Integer32):
    """Custom type tnQosExtQclEtherVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnQosExtQclEtherVal_Type.__name__ = "Integer32"
_TnQosExtQclEtherVal_Object = MibTableColumn
tnQosExtQclEtherVal = _TnQosExtQclEtherVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1, 2),
    _TnQosExtQclEtherVal_Type()
)
tnQosExtQclEtherVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclEtherVal.setStatus("current")


class _TnQosExtQclLlcSsapType_Type(Integer32):
    """Custom type tnQosExtQclLlcSsapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnQosExtQclLlcSsapType_Type.__name__ = "Integer32"
_TnQosExtQclLlcSsapType_Object = MibTableColumn
tnQosExtQclLlcSsapType = _TnQosExtQclLlcSsapType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1, 3),
    _TnQosExtQclLlcSsapType_Type()
)
tnQosExtQclLlcSsapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclLlcSsapType.setStatus("current")


class _TnQosExtQclLlcSsapVal_Type(Integer32):
    """Custom type tnQosExtQclLlcSsapVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnQosExtQclLlcSsapVal_Type.__name__ = "Integer32"
_TnQosExtQclLlcSsapVal_Object = MibTableColumn
tnQosExtQclLlcSsapVal = _TnQosExtQclLlcSsapVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1, 4),
    _TnQosExtQclLlcSsapVal_Type()
)
tnQosExtQclLlcSsapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclLlcSsapVal.setStatus("current")


class _TnQosExtQclLlcDsapType_Type(Integer32):
    """Custom type tnQosExtQclLlcDsapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnQosExtQclLlcDsapType_Type.__name__ = "Integer32"
_TnQosExtQclLlcDsapType_Object = MibTableColumn
tnQosExtQclLlcDsapType = _TnQosExtQclLlcDsapType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1, 5),
    _TnQosExtQclLlcDsapType_Type()
)
tnQosExtQclLlcDsapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclLlcDsapType.setStatus("current")


class _TnQosExtQclLlcDsapVal_Type(Integer32):
    """Custom type tnQosExtQclLlcDsapVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnQosExtQclLlcDsapVal_Type.__name__ = "Integer32"
_TnQosExtQclLlcDsapVal_Object = MibTableColumn
tnQosExtQclLlcDsapVal = _TnQosExtQclLlcDsapVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1, 6),
    _TnQosExtQclLlcDsapVal_Type()
)
tnQosExtQclLlcDsapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclLlcDsapVal.setStatus("current")


class _TnQosExtQclLlcControlType_Type(Integer32):
    """Custom type tnQosExtQclLlcControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnQosExtQclLlcControlType_Type.__name__ = "Integer32"
_TnQosExtQclLlcControlType_Object = MibTableColumn
tnQosExtQclLlcControlType = _TnQosExtQclLlcControlType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1, 7),
    _TnQosExtQclLlcControlType_Type()
)
tnQosExtQclLlcControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclLlcControlType.setStatus("current")


class _TnQosExtQclLlcControlVal_Type(Integer32):
    """Custom type tnQosExtQclLlcControlVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnQosExtQclLlcControlVal_Type.__name__ = "Integer32"
_TnQosExtQclLlcControlVal_Object = MibTableColumn
tnQosExtQclLlcControlVal = _TnQosExtQclLlcControlVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1, 8),
    _TnQosExtQclLlcControlVal_Type()
)
tnQosExtQclLlcControlVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclLlcControlVal.setStatus("current")


class _TnQosExtQclSnapPidType_Type(Integer32):
    """Custom type tnQosExtQclSnapPidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnQosExtQclSnapPidType_Type.__name__ = "Integer32"
_TnQosExtQclSnapPidType_Object = MibTableColumn
tnQosExtQclSnapPidType = _TnQosExtQclSnapPidType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1, 9),
    _TnQosExtQclSnapPidType_Type()
)
tnQosExtQclSnapPidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclSnapPidType.setStatus("current")


class _TnQosExtQclSnapPidVal_Type(Integer32):
    """Custom type tnQosExtQclSnapPidVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnQosExtQclSnapPidVal_Type.__name__ = "Integer32"
_TnQosExtQclSnapPidVal_Object = MibTableColumn
tnQosExtQclSnapPidVal = _TnQosExtQclSnapPidVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 2, 1, 10),
    _TnQosExtQclSnapPidVal_Type()
)
tnQosExtQclSnapPidVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclSnapPidVal.setStatus("current")
_TnQosExtQclIpTable_Object = MibTable
tnQosExtQclIpTable = _TnQosExtQclIpTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tnQosExtQclIpTable.setStatus("current")
_TnQosExtQclIpEntry_Object = MibTableRow
tnQosExtQclIpEntry = _TnQosExtQclIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1)
)
tnQosExtQclIpEntry.setIndexNames(
    (0, "TN-QOS-EXT-MIB", "tnQosExtQclIndex"),
)
if mibBuilder.loadTexts:
    tnQosExtQclIpEntry.setStatus("current")


class _TnQosExtQclProtoType_Type(Integer32):
    """Custom type tnQosExtQclProtoType based on Integer32"""
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
        *(("any", 1),
          ("udp", 2),
          ("tcp", 3),
          ("specific", 4))
    )


_TnQosExtQclProtoType_Type.__name__ = "Integer32"
_TnQosExtQclProtoType_Object = MibTableColumn
tnQosExtQclProtoType = _TnQosExtQclProtoType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 1),
    _TnQosExtQclProtoType_Type()
)
tnQosExtQclProtoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclProtoType.setStatus("current")


class _TnQosExtQclProtoVal_Type(Integer32):
    """Custom type tnQosExtQclProtoVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnQosExtQclProtoVal_Type.__name__ = "Integer32"
_TnQosExtQclProtoVal_Object = MibTableColumn
tnQosExtQclProtoVal = _TnQosExtQclProtoVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 2),
    _TnQosExtQclProtoVal_Type()
)
tnQosExtQclProtoVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclProtoVal.setStatus("current")


class _TnQosExtQclDscpType_Type(Integer32):
    """Custom type tnQosExtQclDscpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnQosExtQclDscpType_Type.__name__ = "Integer32"
_TnQosExtQclDscpType_Object = MibTableColumn
tnQosExtQclDscpType = _TnQosExtQclDscpType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 3),
    _TnQosExtQclDscpType_Type()
)
tnQosExtQclDscpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclDscpType.setStatus("current")


class _TnQosExtQclDscpVal_Type(Integer32):
    """Custom type tnQosExtQclDscpVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtQclDscpVal_Type.__name__ = "Integer32"
_TnQosExtQclDscpVal_Object = MibTableColumn
tnQosExtQclDscpVal = _TnQosExtQclDscpVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 4),
    _TnQosExtQclDscpVal_Type()
)
tnQosExtQclDscpVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclDscpVal.setStatus("current")


class _TnQosExtQclDscpMin_Type(Integer32):
    """Custom type tnQosExtQclDscpMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtQclDscpMin_Type.__name__ = "Integer32"
_TnQosExtQclDscpMin_Object = MibTableColumn
tnQosExtQclDscpMin = _TnQosExtQclDscpMin_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 5),
    _TnQosExtQclDscpMin_Type()
)
tnQosExtQclDscpMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclDscpMin.setStatus("current")


class _TnQosExtQclDscpMax_Type(Integer32):
    """Custom type tnQosExtQclDscpMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnQosExtQclDscpMax_Type.__name__ = "Integer32"
_TnQosExtQclDscpMax_Object = MibTableColumn
tnQosExtQclDscpMax = _TnQosExtQclDscpMax_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 6),
    _TnQosExtQclDscpMax_Type()
)
tnQosExtQclDscpMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclDscpMax.setStatus("current")


class _TnQosExtQclSrcIpType_Type(Integer32):
    """Custom type tnQosExtQclSrcIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnQosExtQclSrcIpType_Type.__name__ = "Integer32"
_TnQosExtQclSrcIpType_Object = MibTableColumn
tnQosExtQclSrcIpType = _TnQosExtQclSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 7),
    _TnQosExtQclSrcIpType_Type()
)
tnQosExtQclSrcIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclSrcIpType.setStatus("current")
_TnQosExtQclSrcIpAddrType_Type = InetAddressType
_TnQosExtQclSrcIpAddrType_Object = MibTableColumn
tnQosExtQclSrcIpAddrType = _TnQosExtQclSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 8),
    _TnQosExtQclSrcIpAddrType_Type()
)
tnQosExtQclSrcIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclSrcIpAddrType.setStatus("current")
_TnQosExtQclSrcIpAddr_Type = InetAddress
_TnQosExtQclSrcIpAddr_Object = MibTableColumn
tnQosExtQclSrcIpAddr = _TnQosExtQclSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 9),
    _TnQosExtQclSrcIpAddr_Type()
)
tnQosExtQclSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclSrcIpAddr.setStatus("current")
_TnQosExtQclSrcIpMaskType_Type = InetAddressType
_TnQosExtQclSrcIpMaskType_Object = MibTableColumn
tnQosExtQclSrcIpMaskType = _TnQosExtQclSrcIpMaskType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 10),
    _TnQosExtQclSrcIpMaskType_Type()
)
tnQosExtQclSrcIpMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclSrcIpMaskType.setStatus("current")
_TnQosExtQclSrcIpMask_Type = InetAddress
_TnQosExtQclSrcIpMask_Object = MibTableColumn
tnQosExtQclSrcIpMask = _TnQosExtQclSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 11),
    _TnQosExtQclSrcIpMask_Type()
)
tnQosExtQclSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclSrcIpMask.setStatus("current")


class _TnQosExtQclIpv4Fragment_Type(Integer32):
    """Custom type tnQosExtQclIpv4Fragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("fragment", 2),
          ("nonfragment", 3))
    )


_TnQosExtQclIpv4Fragment_Type.__name__ = "Integer32"
_TnQosExtQclIpv4Fragment_Object = MibTableColumn
tnQosExtQclIpv4Fragment = _TnQosExtQclIpv4Fragment_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 12),
    _TnQosExtQclIpv4Fragment_Type()
)
tnQosExtQclIpv4Fragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclIpv4Fragment.setStatus("current")


class _TnQosExtQclTcpUdpSportType_Type(Integer32):
    """Custom type tnQosExtQclTcpUdpSportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnQosExtQclTcpUdpSportType_Type.__name__ = "Integer32"
_TnQosExtQclTcpUdpSportType_Object = MibTableColumn
tnQosExtQclTcpUdpSportType = _TnQosExtQclTcpUdpSportType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 13),
    _TnQosExtQclTcpUdpSportType_Type()
)
tnQosExtQclTcpUdpSportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclTcpUdpSportType.setStatus("current")


class _TnQosExtQclTcpUdpSportVal_Type(Integer32):
    """Custom type tnQosExtQclTcpUdpSportVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnQosExtQclTcpUdpSportVal_Type.__name__ = "Integer32"
_TnQosExtQclTcpUdpSportVal_Object = MibTableColumn
tnQosExtQclTcpUdpSportVal = _TnQosExtQclTcpUdpSportVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 14),
    _TnQosExtQclTcpUdpSportVal_Type()
)
tnQosExtQclTcpUdpSportVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclTcpUdpSportVal.setStatus("current")


class _TnQosExtQclTcpUdpSportMin_Type(Integer32):
    """Custom type tnQosExtQclTcpUdpSportMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnQosExtQclTcpUdpSportMin_Type.__name__ = "Integer32"
_TnQosExtQclTcpUdpSportMin_Object = MibTableColumn
tnQosExtQclTcpUdpSportMin = _TnQosExtQclTcpUdpSportMin_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 15),
    _TnQosExtQclTcpUdpSportMin_Type()
)
tnQosExtQclTcpUdpSportMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclTcpUdpSportMin.setStatus("current")


class _TnQosExtQclTcpUdpSportMax_Type(Integer32):
    """Custom type tnQosExtQclTcpUdpSportMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnQosExtQclTcpUdpSportMax_Type.__name__ = "Integer32"
_TnQosExtQclTcpUdpSportMax_Object = MibTableColumn
tnQosExtQclTcpUdpSportMax = _TnQosExtQclTcpUdpSportMax_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 16),
    _TnQosExtQclTcpUdpSportMax_Type()
)
tnQosExtQclTcpUdpSportMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclTcpUdpSportMax.setStatus("current")


class _TnQosExtQclTcpUdpDportType_Type(Integer32):
    """Custom type tnQosExtQclTcpUdpDportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnQosExtQclTcpUdpDportType_Type.__name__ = "Integer32"
_TnQosExtQclTcpUdpDportType_Object = MibTableColumn
tnQosExtQclTcpUdpDportType = _TnQosExtQclTcpUdpDportType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 17),
    _TnQosExtQclTcpUdpDportType_Type()
)
tnQosExtQclTcpUdpDportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclTcpUdpDportType.setStatus("current")


class _TnQosExtQclTcpUdpDportVal_Type(Integer32):
    """Custom type tnQosExtQclTcpUdpDportVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnQosExtQclTcpUdpDportVal_Type.__name__ = "Integer32"
_TnQosExtQclTcpUdpDportVal_Object = MibTableColumn
tnQosExtQclTcpUdpDportVal = _TnQosExtQclTcpUdpDportVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 18),
    _TnQosExtQclTcpUdpDportVal_Type()
)
tnQosExtQclTcpUdpDportVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclTcpUdpDportVal.setStatus("current")


class _TnQosExtQclTcpUdpDportMin_Type(Integer32):
    """Custom type tnQosExtQclTcpUdpDportMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnQosExtQclTcpUdpDportMin_Type.__name__ = "Integer32"
_TnQosExtQclTcpUdpDportMin_Object = MibTableColumn
tnQosExtQclTcpUdpDportMin = _TnQosExtQclTcpUdpDportMin_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 19),
    _TnQosExtQclTcpUdpDportMin_Type()
)
tnQosExtQclTcpUdpDportMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclTcpUdpDportMin.setStatus("current")


class _TnQosExtQclTcpUdpDportMax_Type(Integer32):
    """Custom type tnQosExtQclTcpUdpDportMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnQosExtQclTcpUdpDportMax_Type.__name__ = "Integer32"
_TnQosExtQclTcpUdpDportMax_Object = MibTableColumn
tnQosExtQclTcpUdpDportMax = _TnQosExtQclTcpUdpDportMax_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 9, 1, 4, 3, 1, 20),
    _TnQosExtQclTcpUdpDportMax_Type()
)
tnQosExtQclTcpUdpDportMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnQosExtQclTcpUdpDportMax.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-QOS-EXT-MIB",
    **{"TnQosExtRateUnitType": TnQosExtRateUnitType,
       "TnQosExtRateInFps": TnQosExtRateInFps,
       "tnQosExtMIB": tnQosExtMIB,
       "tnQosExtMIBObjects": tnQosExtMIBObjects,
       "tnQosExtPortMgmt": tnQosExtPortMgmt,
       "tnQosExtPortPolicerTable": tnQosExtPortPolicerTable,
       "tnQosExtPortPolicerEntry": tnQosExtPortPolicerEntry,
       "tnQosExtPortPolicerStatus": tnQosExtPortPolicerStatus,
       "tnQosExtPortPolicerRate": tnQosExtPortPolicerRate,
       "tnQosExtPortPolicerUnit": tnQosExtPortPolicerUnit,
       "tnQosExtPortPolicerFlowControl": tnQosExtPortPolicerFlowControl,
       "tnQosExtPortQueuePolicerTable": tnQosExtPortQueuePolicerTable,
       "tnQosExtPortQueuePolicerEntry": tnQosExtPortQueuePolicerEntry,
       "tnQosExtPortQueuePolicerQid": tnQosExtPortQueuePolicerQid,
       "tnQosExtPortQueuePolicerStatus": tnQosExtPortQueuePolicerStatus,
       "tnQosExtPortQueuePolicerRate": tnQosExtPortQueuePolicerRate,
       "tnQosExtPortQueuePolicerUnit": tnQosExtPortQueuePolicerUnit,
       "tnQosExtPortSchedulerTable": tnQosExtPortSchedulerTable,
       "tnQosExtPortSchedulerEntry": tnQosExtPortSchedulerEntry,
       "tnQosExtPortSchedulerMode": tnQosExtPortSchedulerMode,
       "tnQosExtPortSchedulerQueueMask": tnQosExtPortSchedulerQueueMask,
       "tnQosExtPortSchedulerWeightTable": tnQosExtPortSchedulerWeightTable,
       "tnQosExtPortSchedulerWeightEntry": tnQosExtPortSchedulerWeightEntry,
       "tnQosExtPortSchedulerWeightQid": tnQosExtPortSchedulerWeightQid,
       "tnQosExtPortSchedulerWeightVal": tnQosExtPortSchedulerWeightVal,
       "tnQosExtPortSchedulerWeightPercent": tnQosExtPortSchedulerWeightPercent,
       "tnQosExtPortShaperTable": tnQosExtPortShaperTable,
       "tnQosExtPortShaperEntry": tnQosExtPortShaperEntry,
       "tnQosExtPortShaperStatus": tnQosExtPortShaperStatus,
       "tnQosExtPortShaperRate": tnQosExtPortShaperRate,
       "tnQosExtPortShaperUnit": tnQosExtPortShaperUnit,
       "tnQosExtPortQueueShaperTable": tnQosExtPortQueueShaperTable,
       "tnQosExtPortQueueShaperEntry": tnQosExtPortQueueShaperEntry,
       "tnQosExtPortQueueShaperQid": tnQosExtPortQueueShaperQid,
       "tnQosExtPortQueueShaperStatus": tnQosExtPortQueueShaperStatus,
       "tnQosExtPortQueueShaperRate": tnQosExtPortQueueShaperRate,
       "tnQosExtPortQueueShaperUnit": tnQosExtPortQueueShaperUnit,
       "tnQosExtPortQueueShaperExcess": tnQosExtPortQueueShaperExcess,
       "tnQosExtPortStormControlTable": tnQosExtPortStormControlTable,
       "tnQosExtPortStormControlEntry": tnQosExtPortStormControlEntry,
       "tnQosExtPortStormControlUnicastStatus": tnQosExtPortStormControlUnicastStatus,
       "tnQosExtPortStormControlUnicastRate": tnQosExtPortStormControlUnicastRate,
       "tnQosExtPortStormControlMulticastStatus": tnQosExtPortStormControlMulticastStatus,
       "tnQosExtPortStormControlMulticastRate": tnQosExtPortStormControlMulticastRate,
       "tnQosExtPortStormControlBroadcastStatus": tnQosExtPortStormControlBroadcastStatus,
       "tnQosExtPortStormControlBroadcastRate": tnQosExtPortStormControlBroadcastRate,
       "tnQosExtPortStormControl2Table": tnQosExtPortStormControl2Table,
       "tnQosExtPortStormControl2Entry": tnQosExtPortStormControl2Entry,
       "tnQosExtPortStormControl2FrameType": tnQosExtPortStormControl2FrameType,
       "tnQosExtPortStormControl2Rate": tnQosExtPortStormControl2Rate,
       "tnQosExtPortStormControl2RateUnit": tnQosExtPortStormControl2RateUnit,
       "tnQosExtPortStormControl2Status": tnQosExtPortStormControl2Status,
       "tnQosExtPortWredTable": tnQosExtPortWredTable,
       "tnQosExtPortWredEntry": tnQosExtPortWredEntry,
       "tnQosExtPortWredQid": tnQosExtPortWredQid,
       "tnQosExtPortWredEnable": tnQosExtPortWredEnable,
       "tnQosExtPortWredThresholdMin": tnQosExtPortWredThresholdMin,
       "tnQosExtPortWredMaxDp1": tnQosExtPortWredMaxDp1,
       "tnQosExtPortWredMaxDp2": tnQosExtPortWredMaxDp2,
       "tnQosExtPortWredMaxDp3": tnQosExtPortWredMaxDp3,
       "tnQosExtPortWredMaxThresh": tnQosExtPortWredMaxThresh,
       "tnQosExtPortWredMaxUnit": tnQosExtPortWredMaxUnit,
       "tnQosExtPortPolicerOrderTable": tnQosExtPortPolicerOrderTable,
       "tnQosExtPortPolicerOrderEntry": tnQosExtPortPolicerOrderEntry,
       "tnQosExtPortPolicerOrder": tnQosExtPortPolicerOrder,
       "tnQosExtL2CosMgmt": tnQosExtL2CosMgmt,
       "tnQosExtL2CosIfClassifDefaultTable": tnQosExtL2CosIfClassifDefaultTable,
       "tnQosExtL2CosIfClassifDefaultEntry": tnQosExtL2CosIfClassifDefaultEntry,
       "tnQosExtL2CosIfClassifDefaultClass": tnQosExtL2CosIfClassifDefaultClass,
       "tnQosExtL2CosIfClassifDefaultDpl": tnQosExtL2CosIfClassifDefaultDpl,
       "tnQosExtL2CosIfClassifDefaultPcp": tnQosExtL2CosIfClassifDefaultPcp,
       "tnQosExtL2CosIfClassifDefaultDei": tnQosExtL2CosIfClassifDefaultDei,
       "tnQosExtL2CosIfClassifTagTable": tnQosExtL2CosIfClassifTagTable,
       "tnQosExtL2CosIfClassifTagEntry": tnQosExtL2CosIfClassifTagEntry,
       "tnQosExtL2CosIfClassifTagMode": tnQosExtL2CosIfClassifTagMode,
       "tnQosExtL2CosIfClassifTagMapTable": tnQosExtL2CosIfClassifTagMapTable,
       "tnQosExtL2CosIfClassifTagMapEntry": tnQosExtL2CosIfClassifTagMapEntry,
       "tnQosExtL2CosIfClassifTagMapPcp": tnQosExtL2CosIfClassifTagMapPcp,
       "tnQosExtL2CosIfClassifTagMapDei": tnQosExtL2CosIfClassifTagMapDei,
       "tnQosExtL2CosIfClassifTagMapClass": tnQosExtL2CosIfClassifTagMapClass,
       "tnQosExtL2CosIfClassifTagMapDpl": tnQosExtL2CosIfClassifTagMapDpl,
       "tnQosExtL2CosIfTagRemarkingModeTable": tnQosExtL2CosIfTagRemarkingModeTable,
       "tnQosExtL2CosIfTagRemarkingModeEntry": tnQosExtL2CosIfTagRemarkingModeEntry,
       "tnQosExtL2CosIfTagRemarkingMode": tnQosExtL2CosIfTagRemarkingMode,
       "tnQosExtL2CosIfTagRemarkingDefaultTable": tnQosExtL2CosIfTagRemarkingDefaultTable,
       "tnQosExtL2CosIfTagRemarkingDefaultEntry": tnQosExtL2CosIfTagRemarkingDefaultEntry,
       "tnQosExtL2CosIfTagRemarkingDefaultPcp": tnQosExtL2CosIfTagRemarkingDefaultPcp,
       "tnQosExtL2CosIfTagRemarkingDefaultDei": tnQosExtL2CosIfTagRemarkingDefaultDei,
       "tnQosExtL2CosIfTagRemarkingMappingTable": tnQosExtL2CosIfTagRemarkingMappingTable,
       "tnQosExtL2CosIfTagRemarkingMappingEntry": tnQosExtL2CosIfTagRemarkingMappingEntry,
       "tnQosExtL2CosIfTagRemarkingClass": tnQosExtL2CosIfTagRemarkingClass,
       "tnQosExtL2CosIfTagRemarkingDpl": tnQosExtL2CosIfTagRemarkingDpl,
       "tnQosExtL2CosIfTagRemarkingPcp": tnQosExtL2CosIfTagRemarkingPcp,
       "tnQosExtL2CosIfTagRemarkingDei": tnQosExtL2CosIfTagRemarkingDei,
       "tnQosExtL2CosIfTagRemarkingDplMappingTable": tnQosExtL2CosIfTagRemarkingDplMappingTable,
       "tnQosExtL2CosIfTagRemarkingDplMappingEntry": tnQosExtL2CosIfTagRemarkingDplMappingEntry,
       "tnQosExtL2CosIfTagRemarkingDplMappingClassifDpl": tnQosExtL2CosIfTagRemarkingDplMappingClassifDpl,
       "tnQosExtL2CosIfTagRemarkingDplMappingDpl": tnQosExtL2CosIfTagRemarkingDplMappingDpl,
       "tnQosExtDscpMgmt": tnQosExtDscpMgmt,
       "tnQosExtDscpIfClassifBaseTable": tnQosExtDscpIfClassifBaseTable,
       "tnQosExtDscpIfClassifBaseEntry": tnQosExtDscpIfClassifBaseEntry,
       "tnQosExtDscpIfClassifBaseDscp": tnQosExtDscpIfClassifBaseDscp,
       "tnQosExtDscpIfTransTable": tnQosExtDscpIfTransTable,
       "tnQosExtDscpIfTransEntry": tnQosExtDscpIfTransEntry,
       "tnQosExtDscpIfTransMode": tnQosExtDscpIfTransMode,
       "tnQosExtDscpIfTransMapTable": tnQosExtDscpIfTransMapTable,
       "tnQosExtDscpIfTransMapEntry": tnQosExtDscpIfTransMapEntry,
       "tnQosExtDscpIfTransMapDscp": tnQosExtDscpIfTransMapDscp,
       "tnQosExtDscpIfTransMapToDscp": tnQosExtDscpIfTransMapToDscp,
       "tnQosExtDscpClassifMapTable": tnQosExtDscpClassifMapTable,
       "tnQosExtDscpClassifMapEntry": tnQosExtDscpClassifMapEntry,
       "tnQosExtDscpClassifMapDscp": tnQosExtDscpClassifMapDscp,
       "tnQosExtDscpClassifMapTrust": tnQosExtDscpClassifMapTrust,
       "tnQosExtDscpClassifMapClass": tnQosExtDscpClassifMapClass,
       "tnQosExtDscpClassifMapDpl": tnQosExtDscpClassifMapDpl,
       "tnQosExtDscpIfClassifExtTable": tnQosExtDscpIfClassifExtTable,
       "tnQosExtDscpIfClassifExtEntry": tnQosExtDscpIfClassifExtEntry,
       "tnQosExtDscpIfClassifExtMode": tnQosExtDscpIfClassifExtMode,
       "tnQosExtDscpIfClassifExtDscpTable": tnQosExtDscpIfClassifExtDscpTable,
       "tnQosExtDscpIfClassifExtDscpEntry": tnQosExtDscpIfClassifExtDscpEntry,
       "tnQosExtDscpIfClassifExtDscp": tnQosExtDscpIfClassifExtDscp,
       "tnQosExtDscpIfClassifExtDscpMode": tnQosExtDscpIfClassifExtDscpMode,
       "tnQosExtDscpIfClassifExtMapTable": tnQosExtDscpIfClassifExtMapTable,
       "tnQosExtDscpIfClassifExtMapEntry": tnQosExtDscpIfClassifExtMapEntry,
       "tnQosExtDscpIfClassifExtMapClass": tnQosExtDscpIfClassifExtMapClass,
       "tnQosExtDscpIfClassifExtMapDpl": tnQosExtDscpIfClassifExtMapDpl,
       "tnQosExtDscpIfClassifExtMapDscp": tnQosExtDscpIfClassifExtMapDscp,
       "tnQosExtDscpIfEgressRemarkTable": tnQosExtDscpIfEgressRemarkTable,
       "tnQosExtDscpIfEgressRemarkEntry": tnQosExtDscpIfEgressRemarkEntry,
       "tnQosExtDscpIfEgressRemarkMode": tnQosExtDscpIfEgressRemarkMode,
       "tnQosExtDscpIfEgressRemarkMapTable": tnQosExtDscpIfEgressRemarkMapTable,
       "tnQosExtDscpIfEgressRemarkMapEntry": tnQosExtDscpIfEgressRemarkMapEntry,
       "tnQosExtDscpIfEgressRemarkMapDscp": tnQosExtDscpIfEgressRemarkMapDscp,
       "tnQosExtDscpIfEgressRemarkMapDpl": tnQosExtDscpIfEgressRemarkMapDpl,
       "tnQosExtDscpIfEgressRemarkMapToDscp": tnQosExtDscpIfEgressRemarkMapToDscp,
       "tnQosExtQclMgmt": tnQosExtQclMgmt,
       "tnQosExtQclTable": tnQosExtQclTable,
       "tnQosExtQclEntry": tnQosExtQclEntry,
       "tnQosExtQclIndex": tnQosExtQclIndex,
       "tnQosExtQclId": tnQosExtQclId,
       "tnQosExtQclNextQclId": tnQosExtQclNextQclId,
       "tnQosExtQclPortList": tnQosExtQclPortList,
       "tnQosExtQclTagType": tnQosExtQclTagType,
       "tnQosExtQclTagVlanType": tnQosExtQclTagVlanType,
       "tnQosExtQclTagVlanVal": tnQosExtQclTagVlanVal,
       "tnQosExtQclTagVlanMin": tnQosExtQclTagVlanMin,
       "tnQosExtQclTagVlanMax": tnQosExtQclTagVlanMax,
       "tnQosExtQclTagPcp": tnQosExtQclTagPcp,
       "tnQosExtQclTagDei": tnQosExtQclTagDei,
       "tnQosExtQclSMacType": tnQosExtQclSMacType,
       "tnQosExtQclSMac": tnQosExtQclSMac,
       "tnQosExtQclDMacType": tnQosExtQclDMacType,
       "tnQosExtQclFrameType": tnQosExtQclFrameType,
       "tnQosExtQclActClassDefault": tnQosExtQclActClassDefault,
       "tnQosExtQclActClass": tnQosExtQclActClass,
       "tnQosExtQclActDplDefault": tnQosExtQclActDplDefault,
       "tnQosExtQclActDpl": tnQosExtQclActDpl,
       "tnQosExtQclActDscpDefault": tnQosExtQclActDscpDefault,
       "tnQosExtQclActDscp": tnQosExtQclActDscp,
       "tnQosExtQclConflict": tnQosExtQclConflict,
       "tnQosExtQclStatus": tnQosExtQclStatus,
       "tnQosExtQclL2Table": tnQosExtQclL2Table,
       "tnQosExtQclL2Entry": tnQosExtQclL2Entry,
       "tnQosExtQclEtherType": tnQosExtQclEtherType,
       "tnQosExtQclEtherVal": tnQosExtQclEtherVal,
       "tnQosExtQclLlcSsapType": tnQosExtQclLlcSsapType,
       "tnQosExtQclLlcSsapVal": tnQosExtQclLlcSsapVal,
       "tnQosExtQclLlcDsapType": tnQosExtQclLlcDsapType,
       "tnQosExtQclLlcDsapVal": tnQosExtQclLlcDsapVal,
       "tnQosExtQclLlcControlType": tnQosExtQclLlcControlType,
       "tnQosExtQclLlcControlVal": tnQosExtQclLlcControlVal,
       "tnQosExtQclSnapPidType": tnQosExtQclSnapPidType,
       "tnQosExtQclSnapPidVal": tnQosExtQclSnapPidVal,
       "tnQosExtQclIpTable": tnQosExtQclIpTable,
       "tnQosExtQclIpEntry": tnQosExtQclIpEntry,
       "tnQosExtQclProtoType": tnQosExtQclProtoType,
       "tnQosExtQclProtoVal": tnQosExtQclProtoVal,
       "tnQosExtQclDscpType": tnQosExtQclDscpType,
       "tnQosExtQclDscpVal": tnQosExtQclDscpVal,
       "tnQosExtQclDscpMin": tnQosExtQclDscpMin,
       "tnQosExtQclDscpMax": tnQosExtQclDscpMax,
       "tnQosExtQclSrcIpType": tnQosExtQclSrcIpType,
       "tnQosExtQclSrcIpAddrType": tnQosExtQclSrcIpAddrType,
       "tnQosExtQclSrcIpAddr": tnQosExtQclSrcIpAddr,
       "tnQosExtQclSrcIpMaskType": tnQosExtQclSrcIpMaskType,
       "tnQosExtQclSrcIpMask": tnQosExtQclSrcIpMask,
       "tnQosExtQclIpv4Fragment": tnQosExtQclIpv4Fragment,
       "tnQosExtQclTcpUdpSportType": tnQosExtQclTcpUdpSportType,
       "tnQosExtQclTcpUdpSportVal": tnQosExtQclTcpUdpSportVal,
       "tnQosExtQclTcpUdpSportMin": tnQosExtQclTcpUdpSportMin,
       "tnQosExtQclTcpUdpSportMax": tnQosExtQclTcpUdpSportMax,
       "tnQosExtQclTcpUdpDportType": tnQosExtQclTcpUdpDportType,
       "tnQosExtQclTcpUdpDportVal": tnQosExtQclTcpUdpDportVal,
       "tnQosExtQclTcpUdpDportMin": tnQosExtQclTcpUdpDportMin,
       "tnQosExtQclTcpUdpDportMax": tnQosExtQclTcpUdpDportMax}
)
