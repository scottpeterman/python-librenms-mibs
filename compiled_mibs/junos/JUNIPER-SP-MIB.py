# SNMP MIB module (JUNIPER-SP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-SP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:02:42 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(jnxMibs,
 jnxSpNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxSpNotifications")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxSpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32)
)
if mibBuilder.loadTexts:
    jnxSpMIB.setRevisions(
        ("2005-04-02 00:00",
         "2013-02-23 00:00",
         "2016-05-31 00:00",
         "2018-10-22 00:00",
         "2019-08-10 00:00",
         "2019-09-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxSpSvcSet_ObjectIdentity = ObjectIdentity
jnxSpSvcSet = _JnxSpSvcSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1)
)
if mibBuilder.loadTexts:
    jnxSpSvcSet.setStatus("current")
_JnxSpSvcSetTable_Object = MibTable
jnxSpSvcSetTable = _JnxSpSvcSetTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSpSvcSetTable.setStatus("current")
_JnxSpSvcSetEntry_Object = MibTableRow
jnxSpSvcSetEntry = _JnxSpSvcSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1)
)
jnxSpSvcSetEntry.setIndexNames(
    (0, "JUNIPER-SP-MIB", "jnxSpSvcSetName"),
)
if mibBuilder.loadTexts:
    jnxSpSvcSetEntry.setStatus("current")


class _JnxSpSvcSetName_Type(DisplayString):
    """Custom type jnxSpSvcSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_JnxSpSvcSetName_Type.__name__ = "DisplayString"
_JnxSpSvcSetName_Object = MibTableColumn
jnxSpSvcSetName = _JnxSpSvcSetName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 1),
    _JnxSpSvcSetName_Type()
)
jnxSpSvcSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSpSvcSetName.setStatus("current")
_JnxSpSvcSetSvcType_Type = DisplayString
_JnxSpSvcSetSvcType_Object = MibTableColumn
jnxSpSvcSetSvcType = _JnxSpSvcSetSvcType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 2),
    _JnxSpSvcSetSvcType_Type()
)
jnxSpSvcSetSvcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcType.setStatus("current")


class _JnxSpSvcSetTypeIndex_Type(Integer32):
    """Custom type jnxSpSvcSetTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxSpSvcSetTypeIndex_Type.__name__ = "Integer32"
_JnxSpSvcSetTypeIndex_Object = MibTableColumn
jnxSpSvcSetTypeIndex = _JnxSpSvcSetTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 3),
    _JnxSpSvcSetTypeIndex_Type()
)
jnxSpSvcSetTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetTypeIndex.setStatus("current")
_JnxSpSvcSetIfName_Type = DisplayString
_JnxSpSvcSetIfName_Object = MibTableColumn
jnxSpSvcSetIfName = _JnxSpSvcSetIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 4),
    _JnxSpSvcSetIfName_Type()
)
jnxSpSvcSetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfName.setStatus("current")
_JnxSpSvcSetIfIndex_Type = InterfaceIndex
_JnxSpSvcSetIfIndex_Object = MibTableColumn
jnxSpSvcSetIfIndex = _JnxSpSvcSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 5),
    _JnxSpSvcSetIfIndex_Type()
)
jnxSpSvcSetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfIndex.setStatus("current")
_JnxSpSvcSetMemoryUsage_Type = Gauge32
_JnxSpSvcSetMemoryUsage_Object = MibTableColumn
jnxSpSvcSetMemoryUsage = _JnxSpSvcSetMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 6),
    _JnxSpSvcSetMemoryUsage_Type()
)
jnxSpSvcSetMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetMemoryUsage.setUnits("bytes")
_JnxSpSvcSetCpuUtil_Type = Gauge32
_JnxSpSvcSetCpuUtil_Object = MibTableColumn
jnxSpSvcSetCpuUtil = _JnxSpSvcSetCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 7),
    _JnxSpSvcSetCpuUtil_Type()
)
jnxSpSvcSetCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuUtil.setUnits("percent")


class _JnxSpSvcSetSvcStyle_Type(Integer32):
    """Custom type jnxSpSvcSetSvcStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("interface-service", 2),
          ("next-hop-service", 3))
    )


_JnxSpSvcSetSvcStyle_Type.__name__ = "Integer32"
_JnxSpSvcSetSvcStyle_Object = MibTableColumn
jnxSpSvcSetSvcStyle = _JnxSpSvcSetSvcStyle_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 8),
    _JnxSpSvcSetSvcStyle_Type()
)
jnxSpSvcSetSvcStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcStyle.setStatus("current")
_JnxSpSvcSetMemLimitPktDrops_Type = Counter32
_JnxSpSvcSetMemLimitPktDrops_Object = MibTableColumn
jnxSpSvcSetMemLimitPktDrops = _JnxSpSvcSetMemLimitPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 9),
    _JnxSpSvcSetMemLimitPktDrops_Type()
)
jnxSpSvcSetMemLimitPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetMemLimitPktDrops.setStatus("current")
_JnxSpSvcSetCpuLimitPktDrops_Type = Counter32
_JnxSpSvcSetCpuLimitPktDrops_Object = MibTableColumn
jnxSpSvcSetCpuLimitPktDrops = _JnxSpSvcSetCpuLimitPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 10),
    _JnxSpSvcSetCpuLimitPktDrops_Type()
)
jnxSpSvcSetCpuLimitPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuLimitPktDrops.setStatus("current")
_JnxSpSvcSetFlowLimitPktDrops_Type = Counter32
_JnxSpSvcSetFlowLimitPktDrops_Object = MibTableColumn
jnxSpSvcSetFlowLimitPktDrops = _JnxSpSvcSetFlowLimitPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 11),
    _JnxSpSvcSetFlowLimitPktDrops_Type()
)
jnxSpSvcSetFlowLimitPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetFlowLimitPktDrops.setStatus("current")
_JnxSpSvcSetMemoryUsage64_Type = CounterBasedGauge64
_JnxSpSvcSetMemoryUsage64_Object = MibTableColumn
jnxSpSvcSetMemoryUsage64 = _JnxSpSvcSetMemoryUsage64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 12),
    _JnxSpSvcSetMemoryUsage64_Type()
)
jnxSpSvcSetMemoryUsage64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetMemoryUsage64.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetMemoryUsage64.setUnits("bytes")
_JnxSpSvcSetMemLimitPktDrops64_Type = CounterBasedGauge64
_JnxSpSvcSetMemLimitPktDrops64_Object = MibTableColumn
jnxSpSvcSetMemLimitPktDrops64 = _JnxSpSvcSetMemLimitPktDrops64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 13),
    _JnxSpSvcSetMemLimitPktDrops64_Type()
)
jnxSpSvcSetMemLimitPktDrops64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetMemLimitPktDrops64.setStatus("current")
_JnxSpSvcSetCpuLimitPktDrops64_Type = CounterBasedGauge64
_JnxSpSvcSetCpuLimitPktDrops64_Object = MibTableColumn
jnxSpSvcSetCpuLimitPktDrops64 = _JnxSpSvcSetCpuLimitPktDrops64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 14),
    _JnxSpSvcSetCpuLimitPktDrops64_Type()
)
jnxSpSvcSetCpuLimitPktDrops64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuLimitPktDrops64.setStatus("current")
_JnxSpSvcSetFlowLimitPktDrops64_Type = CounterBasedGauge64
_JnxSpSvcSetFlowLimitPktDrops64_Object = MibTableColumn
jnxSpSvcSetFlowLimitPktDrops64 = _JnxSpSvcSetFlowLimitPktDrops64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 15),
    _JnxSpSvcSetFlowLimitPktDrops64_Type()
)
jnxSpSvcSetFlowLimitPktDrops64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetFlowLimitPktDrops64.setStatus("current")
_JnxSpSvcSetSessCount_Type = Counter32
_JnxSpSvcSetSessCount_Object = MibTableColumn
jnxSpSvcSetSessCount = _JnxSpSvcSetSessCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 16),
    _JnxSpSvcSetSessCount_Type()
)
jnxSpSvcSetSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSessCount.setStatus("current")
_JnxSpSvcSetSvcTypeTable_Object = MibTable
jnxSpSvcSetSvcTypeTable = _JnxSpSvcSetSvcTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2)
)
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeTable.setStatus("current")
_JnxSpSvcSetSvcTypeEntry_Object = MibTableRow
jnxSpSvcSetSvcTypeEntry = _JnxSpSvcSetSvcTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1)
)
jnxSpSvcSetSvcTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-SP-MIB", "jnxSpSvcSetSvcTypeIndex"),
)
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeEntry.setStatus("current")


class _JnxSpSvcSetSvcTypeIndex_Type(Integer32):
    """Custom type jnxSpSvcSetSvcTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxSpSvcSetSvcTypeIndex_Type.__name__ = "Integer32"
_JnxSpSvcSetSvcTypeIndex_Object = MibTableColumn
jnxSpSvcSetSvcTypeIndex = _JnxSpSvcSetSvcTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 1),
    _JnxSpSvcSetSvcTypeIndex_Type()
)
jnxSpSvcSetSvcTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeIndex.setStatus("current")
_JnxSpSvcSetSvcTypeIfName_Type = DisplayString
_JnxSpSvcSetSvcTypeIfName_Object = MibTableColumn
jnxSpSvcSetSvcTypeIfName = _JnxSpSvcSetSvcTypeIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 2),
    _JnxSpSvcSetSvcTypeIfName_Type()
)
jnxSpSvcSetSvcTypeIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeIfName.setStatus("current")
_JnxSpSvcSetSvcTypeName_Type = DisplayString
_JnxSpSvcSetSvcTypeName_Object = MibTableColumn
jnxSpSvcSetSvcTypeName = _JnxSpSvcSetSvcTypeName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 3),
    _JnxSpSvcSetSvcTypeName_Type()
)
jnxSpSvcSetSvcTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeName.setStatus("current")
_JnxSpSvcSetSvcTypeSvcSets_Type = Gauge32
_JnxSpSvcSetSvcTypeSvcSets_Object = MibTableColumn
jnxSpSvcSetSvcTypeSvcSets = _JnxSpSvcSetSvcTypeSvcSets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 4),
    _JnxSpSvcSetSvcTypeSvcSets_Type()
)
jnxSpSvcSetSvcTypeSvcSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeSvcSets.setStatus("current")
_JnxSpSvcSetSvcTypeMemoryUsage_Type = Gauge32
_JnxSpSvcSetSvcTypeMemoryUsage_Object = MibTableColumn
jnxSpSvcSetSvcTypeMemoryUsage = _JnxSpSvcSetSvcTypeMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 5),
    _JnxSpSvcSetSvcTypeMemoryUsage_Type()
)
jnxSpSvcSetSvcTypeMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeMemoryUsage.setUnits("bytes")
_JnxSpSvcSetSvcTypePctMemoryUsage_Type = Gauge32
_JnxSpSvcSetSvcTypePctMemoryUsage_Object = MibTableColumn
jnxSpSvcSetSvcTypePctMemoryUsage = _JnxSpSvcSetSvcTypePctMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 6),
    _JnxSpSvcSetSvcTypePctMemoryUsage_Type()
)
jnxSpSvcSetSvcTypePctMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypePctMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypePctMemoryUsage.setUnits("percent")
_JnxSpSvcSetSvcTypeCpuUtil_Type = Gauge32
_JnxSpSvcSetSvcTypeCpuUtil_Object = MibTableColumn
jnxSpSvcSetSvcTypeCpuUtil = _JnxSpSvcSetSvcTypeCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 7),
    _JnxSpSvcSetSvcTypeCpuUtil_Type()
)
jnxSpSvcSetSvcTypeCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeCpuUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeCpuUtil.setUnits("percent")
_JnxSpSvcSetSvcTypeMemoryUsage64_Type = CounterBasedGauge64
_JnxSpSvcSetSvcTypeMemoryUsage64_Object = MibTableColumn
jnxSpSvcSetSvcTypeMemoryUsage64 = _JnxSpSvcSetSvcTypeMemoryUsage64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 8),
    _JnxSpSvcSetSvcTypeMemoryUsage64_Type()
)
jnxSpSvcSetSvcTypeMemoryUsage64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeMemoryUsage64.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetSvcTypeMemoryUsage64.setUnits("bytes")
_JnxSpSvcSetIfTable_Object = MibTable
jnxSpSvcSetIfTable = _JnxSpSvcSetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3)
)
if mibBuilder.loadTexts:
    jnxSpSvcSetIfTable.setStatus("current")
_JnxSpSvcSetIfEntry_Object = MibTableRow
jnxSpSvcSetIfEntry = _JnxSpSvcSetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1)
)
jnxSpSvcSetIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxSpSvcSetIfEntry.setStatus("current")
_JnxSpSvcSetIfTableName_Type = DisplayString
_JnxSpSvcSetIfTableName_Object = MibTableColumn
jnxSpSvcSetIfTableName = _JnxSpSvcSetIfTableName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 1),
    _JnxSpSvcSetIfTableName_Type()
)
jnxSpSvcSetIfTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfTableName.setStatus("current")
_JnxSpSvcSetIfSvcSets_Type = Gauge32
_JnxSpSvcSetIfSvcSets_Object = MibTableColumn
jnxSpSvcSetIfSvcSets = _JnxSpSvcSetIfSvcSets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 2),
    _JnxSpSvcSetIfSvcSets_Type()
)
jnxSpSvcSetIfSvcSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfSvcSets.setStatus("current")
_JnxSpSvcSetIfMemoryUsage_Type = Gauge32
_JnxSpSvcSetIfMemoryUsage_Object = MibTableColumn
jnxSpSvcSetIfMemoryUsage = _JnxSpSvcSetIfMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 3),
    _JnxSpSvcSetIfMemoryUsage_Type()
)
jnxSpSvcSetIfMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMemoryUsage.setUnits("bytes")
_JnxSpSvcSetIfPctMemoryUsage_Type = Gauge32
_JnxSpSvcSetIfPctMemoryUsage_Object = MibTableColumn
jnxSpSvcSetIfPctMemoryUsage = _JnxSpSvcSetIfPctMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 4),
    _JnxSpSvcSetIfPctMemoryUsage_Type()
)
jnxSpSvcSetIfPctMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPctMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPctMemoryUsage.setUnits("percent")
_JnxSpSvcSetIfPolMemoryUsage_Type = Gauge32
_JnxSpSvcSetIfPolMemoryUsage_Object = MibTableColumn
jnxSpSvcSetIfPolMemoryUsage = _JnxSpSvcSetIfPolMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 5),
    _JnxSpSvcSetIfPolMemoryUsage_Type()
)
jnxSpSvcSetIfPolMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPolMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPolMemoryUsage.setUnits("bytes")
_JnxSpSvcSetIfPctPolMemoryUsage_Type = Gauge32
_JnxSpSvcSetIfPctPolMemoryUsage_Object = MibTableColumn
jnxSpSvcSetIfPctPolMemoryUsage = _JnxSpSvcSetIfPctPolMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 6),
    _JnxSpSvcSetIfPctPolMemoryUsage_Type()
)
jnxSpSvcSetIfPctPolMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPctPolMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPctPolMemoryUsage.setUnits("percent")


class _JnxSpSvcSetIfMemoryZone_Type(Integer32):
    """Custom type jnxSpSvcSetIfMemoryZone based on Integer32"""
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
        *(("green", 1),
          ("yellow", 2),
          ("orange", 3),
          ("red", 4))
    )


_JnxSpSvcSetIfMemoryZone_Type.__name__ = "Integer32"
_JnxSpSvcSetIfMemoryZone_Object = MibTableColumn
jnxSpSvcSetIfMemoryZone = _JnxSpSvcSetIfMemoryZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 7),
    _JnxSpSvcSetIfMemoryZone_Type()
)
jnxSpSvcSetIfMemoryZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMemoryZone.setStatus("current")
_JnxSpSvcSetIfCpuUtil_Type = Gauge32
_JnxSpSvcSetIfCpuUtil_Object = MibTableColumn
jnxSpSvcSetIfCpuUtil = _JnxSpSvcSetIfCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 8),
    _JnxSpSvcSetIfCpuUtil_Type()
)
jnxSpSvcSetIfCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfCpuUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfCpuUtil.setUnits("percent")
_JnxSpSvcSetIfMemoryUsage64_Type = CounterBasedGauge64
_JnxSpSvcSetIfMemoryUsage64_Object = MibTableColumn
jnxSpSvcSetIfMemoryUsage64 = _JnxSpSvcSetIfMemoryUsage64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 9),
    _JnxSpSvcSetIfMemoryUsage64_Type()
)
jnxSpSvcSetIfMemoryUsage64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMemoryUsage64.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMemoryUsage64.setUnits("bytes")
_JnxSpSvcSetIfPolMemoryUsage64_Type = CounterBasedGauge64
_JnxSpSvcSetIfPolMemoryUsage64_Object = MibTableColumn
jnxSpSvcSetIfPolMemoryUsage64 = _JnxSpSvcSetIfPolMemoryUsage64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 10),
    _JnxSpSvcSetIfPolMemoryUsage64_Type()
)
jnxSpSvcSetIfPolMemoryUsage64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPolMemoryUsage64.setStatus("current")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPolMemoryUsage64.setUnits("bytes")
_JnxSpSvcSetIfNumTotalSessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalSessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalSessActive = _JnxSpSvcSetIfNumTotalSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 11),
    _JnxSpSvcSetIfNumTotalSessActive_Type()
)
jnxSpSvcSetIfNumTotalSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalSessActive.setStatus("current")
_JnxSpSvcSetIfPeakTotalSessActive_Type = Integer32
_JnxSpSvcSetIfPeakTotalSessActive_Object = MibTableColumn
jnxSpSvcSetIfPeakTotalSessActive = _JnxSpSvcSetIfPeakTotalSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 12),
    _JnxSpSvcSetIfPeakTotalSessActive_Type()
)
jnxSpSvcSetIfPeakTotalSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPeakTotalSessActive.setStatus("current")
_JnxSpSvcSetIfNumCreatedSessPerSec_Type = Integer32
_JnxSpSvcSetIfNumCreatedSessPerSec_Object = MibTableColumn
jnxSpSvcSetIfNumCreatedSessPerSec = _JnxSpSvcSetIfNumCreatedSessPerSec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 13),
    _JnxSpSvcSetIfNumCreatedSessPerSec_Type()
)
jnxSpSvcSetIfNumCreatedSessPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumCreatedSessPerSec.setStatus("current")
_JnxSpSvcSetIfNumDeletedSessPerSec_Type = Integer32
_JnxSpSvcSetIfNumDeletedSessPerSec_Object = MibTableColumn
jnxSpSvcSetIfNumDeletedSessPerSec = _JnxSpSvcSetIfNumDeletedSessPerSec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 14),
    _JnxSpSvcSetIfNumDeletedSessPerSec_Type()
)
jnxSpSvcSetIfNumDeletedSessPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumDeletedSessPerSec.setStatus("current")
_JnxSpSvcSetIfNumTotalTcpSessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalTcpSessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalTcpSessActive = _JnxSpSvcSetIfNumTotalTcpSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 15),
    _JnxSpSvcSetIfNumTotalTcpSessActive_Type()
)
jnxSpSvcSetIfNumTotalTcpSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalTcpSessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalUdpSessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalUdpSessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalUdpSessActive = _JnxSpSvcSetIfNumTotalUdpSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 16),
    _JnxSpSvcSetIfNumTotalUdpSessActive_Type()
)
jnxSpSvcSetIfNumTotalUdpSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalUdpSessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalOtherSessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalOtherSessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalOtherSessActive = _JnxSpSvcSetIfNumTotalOtherSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 17),
    _JnxSpSvcSetIfNumTotalOtherSessActive_Type()
)
jnxSpSvcSetIfNumTotalOtherSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalOtherSessActive.setStatus("current")
_JnxSpSvcSetIfPeakTotalTcpSessActive_Type = Integer32
_JnxSpSvcSetIfPeakTotalTcpSessActive_Object = MibTableColumn
jnxSpSvcSetIfPeakTotalTcpSessActive = _JnxSpSvcSetIfPeakTotalTcpSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 18),
    _JnxSpSvcSetIfPeakTotalTcpSessActive_Type()
)
jnxSpSvcSetIfPeakTotalTcpSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPeakTotalTcpSessActive.setStatus("current")
_JnxSpSvcSetIfPeakTotalUdpSessActive_Type = Integer32
_JnxSpSvcSetIfPeakTotalUdpSessActive_Object = MibTableColumn
jnxSpSvcSetIfPeakTotalUdpSessActive = _JnxSpSvcSetIfPeakTotalUdpSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 19),
    _JnxSpSvcSetIfPeakTotalUdpSessActive_Type()
)
jnxSpSvcSetIfPeakTotalUdpSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPeakTotalUdpSessActive.setStatus("current")
_JnxSpSvcSetIfPeakTotalOtherSessActive_Type = Integer32
_JnxSpSvcSetIfPeakTotalOtherSessActive_Object = MibTableColumn
jnxSpSvcSetIfPeakTotalOtherSessActive = _JnxSpSvcSetIfPeakTotalOtherSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 20),
    _JnxSpSvcSetIfPeakTotalOtherSessActive_Type()
)
jnxSpSvcSetIfPeakTotalOtherSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPeakTotalOtherSessActive.setStatus("current")
_JnxSpSvcSetIfPeakCreatedSessPerSec_Type = Integer32
_JnxSpSvcSetIfPeakCreatedSessPerSec_Object = MibTableColumn
jnxSpSvcSetIfPeakCreatedSessPerSec = _JnxSpSvcSetIfPeakCreatedSessPerSec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 21),
    _JnxSpSvcSetIfPeakCreatedSessPerSec_Type()
)
jnxSpSvcSetIfPeakCreatedSessPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPeakCreatedSessPerSec.setStatus("current")
_JnxSpSvcSetIfPeakDeletedSessPerSec_Type = Integer32
_JnxSpSvcSetIfPeakDeletedSessPerSec_Object = MibTableColumn
jnxSpSvcSetIfPeakDeletedSessPerSec = _JnxSpSvcSetIfPeakDeletedSessPerSec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 22),
    _JnxSpSvcSetIfPeakDeletedSessPerSec_Type()
)
jnxSpSvcSetIfPeakDeletedSessPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfPeakDeletedSessPerSec.setStatus("current")
_JnxSpSvcSetIfNumTotalTcpIpv4SessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalTcpIpv4SessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalTcpIpv4SessActive = _JnxSpSvcSetIfNumTotalTcpIpv4SessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 23),
    _JnxSpSvcSetIfNumTotalTcpIpv4SessActive_Type()
)
jnxSpSvcSetIfNumTotalTcpIpv4SessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalTcpIpv4SessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalTcpIpv6SessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalTcpIpv6SessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalTcpIpv6SessActive = _JnxSpSvcSetIfNumTotalTcpIpv6SessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 24),
    _JnxSpSvcSetIfNumTotalTcpIpv6SessActive_Type()
)
jnxSpSvcSetIfNumTotalTcpIpv6SessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalTcpIpv6SessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalUdpIpv4SessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalUdpIpv4SessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalUdpIpv4SessActive = _JnxSpSvcSetIfNumTotalUdpIpv4SessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 25),
    _JnxSpSvcSetIfNumTotalUdpIpv4SessActive_Type()
)
jnxSpSvcSetIfNumTotalUdpIpv4SessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalUdpIpv4SessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalUdpIpv6SessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalUdpIpv6SessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalUdpIpv6SessActive = _JnxSpSvcSetIfNumTotalUdpIpv6SessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 26),
    _JnxSpSvcSetIfNumTotalUdpIpv6SessActive_Type()
)
jnxSpSvcSetIfNumTotalUdpIpv6SessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalUdpIpv6SessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalOtherIpv4SessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalOtherIpv4SessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalOtherIpv4SessActive = _JnxSpSvcSetIfNumTotalOtherIpv4SessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 27),
    _JnxSpSvcSetIfNumTotalOtherIpv4SessActive_Type()
)
jnxSpSvcSetIfNumTotalOtherIpv4SessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalOtherIpv4SessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalOtherIpv6SessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalOtherIpv6SessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalOtherIpv6SessActive = _JnxSpSvcSetIfNumTotalOtherIpv6SessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 28),
    _JnxSpSvcSetIfNumTotalOtherIpv6SessActive_Type()
)
jnxSpSvcSetIfNumTotalOtherIpv6SessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalOtherIpv6SessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalTcpGatedSessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalTcpGatedSessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalTcpGatedSessActive = _JnxSpSvcSetIfNumTotalTcpGatedSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 29),
    _JnxSpSvcSetIfNumTotalTcpGatedSessActive_Type()
)
jnxSpSvcSetIfNumTotalTcpGatedSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalTcpGatedSessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalUdpGatedSessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalUdpGatedSessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalUdpGatedSessActive = _JnxSpSvcSetIfNumTotalUdpGatedSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 30),
    _JnxSpSvcSetIfNumTotalUdpGatedSessActive_Type()
)
jnxSpSvcSetIfNumTotalUdpGatedSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalUdpGatedSessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalTcpRegSessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalTcpRegSessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalTcpRegSessActive = _JnxSpSvcSetIfNumTotalTcpRegSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 31),
    _JnxSpSvcSetIfNumTotalTcpRegSessActive_Type()
)
jnxSpSvcSetIfNumTotalTcpRegSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalTcpRegSessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalUdpRegSessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalUdpRegSessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalUdpRegSessActive = _JnxSpSvcSetIfNumTotalUdpRegSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 32),
    _JnxSpSvcSetIfNumTotalUdpRegSessActive_Type()
)
jnxSpSvcSetIfNumTotalUdpRegSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalUdpRegSessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalTcpTunSessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalTcpTunSessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalTcpTunSessActive = _JnxSpSvcSetIfNumTotalTcpTunSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 33),
    _JnxSpSvcSetIfNumTotalTcpTunSessActive_Type()
)
jnxSpSvcSetIfNumTotalTcpTunSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalTcpTunSessActive.setStatus("current")
_JnxSpSvcSetIfNumTotalUdpTunSessActive_Type = Integer32
_JnxSpSvcSetIfNumTotalUdpTunSessActive_Object = MibTableColumn
jnxSpSvcSetIfNumTotalUdpTunSessActive = _JnxSpSvcSetIfNumTotalUdpTunSessActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 34),
    _JnxSpSvcSetIfNumTotalUdpTunSessActive_Type()
)
jnxSpSvcSetIfNumTotalUdpTunSessActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfNumTotalUdpTunSessActive.setStatus("current")
_JnxSpSvcSetIfSessPktRecv_Type = CounterBasedGauge64
_JnxSpSvcSetIfSessPktRecv_Object = MibTableColumn
jnxSpSvcSetIfSessPktRecv = _JnxSpSvcSetIfSessPktRecv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 35),
    _JnxSpSvcSetIfSessPktRecv_Type()
)
jnxSpSvcSetIfSessPktRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfSessPktRecv.setStatus("current")
_JnxSpSvcSetIfSessPktXmit_Type = CounterBasedGauge64
_JnxSpSvcSetIfSessPktXmit_Object = MibTableColumn
jnxSpSvcSetIfSessPktXmit = _JnxSpSvcSetIfSessPktXmit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 36),
    _JnxSpSvcSetIfSessPktXmit_Type()
)
jnxSpSvcSetIfSessPktXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfSessPktXmit.setStatus("current")
_JnxSpSvcSetIfSessSlowPathDiscard_Type = CounterBasedGauge64
_JnxSpSvcSetIfSessSlowPathDiscard_Object = MibTableColumn
jnxSpSvcSetIfSessSlowPathDiscard = _JnxSpSvcSetIfSessSlowPathDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 37),
    _JnxSpSvcSetIfSessSlowPathDiscard_Type()
)
jnxSpSvcSetIfSessSlowPathDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfSessSlowPathDiscard.setStatus("current")
_JnxSpSvcSetIfSessSlowPathForward_Type = CounterBasedGauge64
_JnxSpSvcSetIfSessSlowPathForward_Object = MibTableColumn
jnxSpSvcSetIfSessSlowPathForward = _JnxSpSvcSetIfSessSlowPathForward_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 38),
    _JnxSpSvcSetIfSessSlowPathForward_Type()
)
jnxSpSvcSetIfSessSlowPathForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfSessSlowPathForward.setStatus("current")
_JnxSpSvcSetIfMspNumCreatedSubsPerSec_Type = Integer32
_JnxSpSvcSetIfMspNumCreatedSubsPerSec_Object = MibTableColumn
jnxSpSvcSetIfMspNumCreatedSubsPerSec = _JnxSpSvcSetIfMspNumCreatedSubsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 39),
    _JnxSpSvcSetIfMspNumCreatedSubsPerSec_Type()
)
jnxSpSvcSetIfMspNumCreatedSubsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMspNumCreatedSubsPerSec.setStatus("current")
_JnxSpSvcSetIfMspNumDeletedSubsPerSec_Type = Integer32
_JnxSpSvcSetIfMspNumDeletedSubsPerSec_Object = MibTableColumn
jnxSpSvcSetIfMspNumDeletedSubsPerSec = _JnxSpSvcSetIfMspNumDeletedSubsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 40),
    _JnxSpSvcSetIfMspNumDeletedSubsPerSec_Type()
)
jnxSpSvcSetIfMspNumDeletedSubsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMspNumDeletedSubsPerSec.setStatus("current")
_JnxSpSvcSetIfMspNumTotalSubsActive_Type = Integer32
_JnxSpSvcSetIfMspNumTotalSubsActive_Object = MibTableColumn
jnxSpSvcSetIfMspNumTotalSubsActive = _JnxSpSvcSetIfMspNumTotalSubsActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 41),
    _JnxSpSvcSetIfMspNumTotalSubsActive_Type()
)
jnxSpSvcSetIfMspNumTotalSubsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMspNumTotalSubsActive.setStatus("current")
_JnxSpSvcSetIfMspPeakCreatedSubsPerSec_Type = Integer32
_JnxSpSvcSetIfMspPeakCreatedSubsPerSec_Object = MibTableColumn
jnxSpSvcSetIfMspPeakCreatedSubsPerSec = _JnxSpSvcSetIfMspPeakCreatedSubsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 42),
    _JnxSpSvcSetIfMspPeakCreatedSubsPerSec_Type()
)
jnxSpSvcSetIfMspPeakCreatedSubsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMspPeakCreatedSubsPerSec.setStatus("current")
_JnxSpSvcSetIfMspPeakDeletedSubsPerSec_Type = Integer32
_JnxSpSvcSetIfMspPeakDeletedSubsPerSec_Object = MibTableColumn
jnxSpSvcSetIfMspPeakDeletedSubsPerSec = _JnxSpSvcSetIfMspPeakDeletedSubsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 43),
    _JnxSpSvcSetIfMspPeakDeletedSubsPerSec_Type()
)
jnxSpSvcSetIfMspPeakDeletedSubsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMspPeakDeletedSubsPerSec.setStatus("current")
_JnxSpSvcSetIfMspPeakTotalSubsActive_Type = Integer32
_JnxSpSvcSetIfMspPeakTotalSubsActive_Object = MibTableColumn
jnxSpSvcSetIfMspPeakTotalSubsActive = _JnxSpSvcSetIfMspPeakTotalSubsActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 44),
    _JnxSpSvcSetIfMspPeakTotalSubsActive_Type()
)
jnxSpSvcSetIfMspPeakTotalSubsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpSvcSetIfMspPeakTotalSubsActive.setStatus("current")
_JnxFlowLimitTrapVars_ObjectIdentity = ObjectIdentity
jnxFlowLimitTrapVars = _JnxFlowLimitTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 2)
)


class _JnxSpSvcSetFlowLimitUtil_Type(Integer32):
    """Custom type jnxSpSvcSetFlowLimitUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxSpSvcSetFlowLimitUtil_Type.__name__ = "Integer32"
_JnxSpSvcSetFlowLimitUtil_Object = MibScalar
jnxSpSvcSetFlowLimitUtil = _JnxSpSvcSetFlowLimitUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 2, 1),
    _JnxSpSvcSetFlowLimitUtil_Type()
)
jnxSpSvcSetFlowLimitUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSpSvcSetFlowLimitUtil.setStatus("current")


class _JnxSpSvcSetNameUtil_Type(DisplayString):
    """Custom type jnxSpSvcSetNameUtil based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 96),
    )


_JnxSpSvcSetNameUtil_Type.__name__ = "DisplayString"
_JnxSpSvcSetNameUtil_Object = MibScalar
jnxSpSvcSetNameUtil = _JnxSpSvcSetNameUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 2, 2),
    _JnxSpSvcSetNameUtil_Type()
)
jnxSpSvcSetNameUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSpSvcSetNameUtil.setStatus("current")
_JnxTcpLoggingTrapVars_ObjectIdentity = ObjectIdentity
jnxTcpLoggingTrapVars = _JnxTcpLoggingTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 3)
)


class _JnxSpTcpLoggingHostIpaddr_Type(DisplayString):
    """Custom type jnxSpTcpLoggingHostIpaddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxSpTcpLoggingHostIpaddr_Type.__name__ = "DisplayString"
_JnxSpTcpLoggingHostIpaddr_Object = MibScalar
jnxSpTcpLoggingHostIpaddr = _JnxSpTcpLoggingHostIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 3, 1),
    _JnxSpTcpLoggingHostIpaddr_Type()
)
jnxSpTcpLoggingHostIpaddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSpTcpLoggingHostIpaddr.setStatus("current")


class _JnxSpTcpLoggingHostPort_Type(Integer32):
    """Custom type jnxSpTcpLoggingHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxSpTcpLoggingHostPort_Type.__name__ = "Integer32"
_JnxSpTcpLoggingHostPort_Object = MibScalar
jnxSpTcpLoggingHostPort = _JnxSpTcpLoggingHostPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 3, 2),
    _JnxSpTcpLoggingHostPort_Type()
)
jnxSpTcpLoggingHostPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSpTcpLoggingHostPort.setStatus("current")


class _JnxSpTcpLoggingHostConnStatus_Type(DisplayString):
    """Custom type jnxSpTcpLoggingHostConnStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxSpTcpLoggingHostConnStatus_Type.__name__ = "DisplayString"
_JnxSpTcpLoggingHostConnStatus_Object = MibScalar
jnxSpTcpLoggingHostConnStatus = _JnxSpTcpLoggingHostConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 3, 3),
    _JnxSpTcpLoggingHostConnStatus_Type()
)
jnxSpTcpLoggingHostConnStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSpTcpLoggingHostConnStatus.setStatus("current")


class _JnxSpTcpLoggingHostRoutingInstance_Type(DisplayString):
    """Custom type jnxSpTcpLoggingHostRoutingInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxSpTcpLoggingHostRoutingInstance_Type.__name__ = "DisplayString"
_JnxSpTcpLoggingHostRoutingInstance_Object = MibScalar
jnxSpTcpLoggingHostRoutingInstance = _JnxSpTcpLoggingHostRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 32, 3, 4),
    _JnxSpTcpLoggingHostRoutingInstance_Type()
)
jnxSpTcpLoggingHostRoutingInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSpTcpLoggingHostRoutingInstance.setStatus("current")
_JnxSpNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxSpNotificationPrefix = _JnxSpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 10, 0)
)
if mibBuilder.loadTexts:
    jnxSpNotificationPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

jnxSpSvcSetZoneEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 10, 0, 1)
)
jnxSpSvcSetZoneEntered.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetIfMemoryZone"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetZoneEntered.setStatus(
        "current"
    )

jnxSpSvcSetZoneExited = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 10, 0, 2)
)
jnxSpSvcSetZoneExited.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetIfMemoryZone"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetZoneExited.setStatus(
        "current"
    )

jnxSpSvcSetCpuExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 10, 0, 3)
)
jnxSpSvcSetCpuExceeded.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetIfCpuUtil"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuExceeded.setStatus(
        "current"
    )

jnxSpSvcSetCpuOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 10, 0, 4)
)
jnxSpSvcSetCpuOk.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetIfCpuUtil"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetCpuOk.setStatus(
        "current"
    )

jnxSpSvcSetFlowLimitUtilised = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 10, 0, 5)
)
jnxSpSvcSetFlowLimitUtilised.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetFlowLimitUtil"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetNameUtil"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetFlowLimitUtilised.setStatus(
        "current"
    )

jnxSpTcpLoggingHostStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 10, 0, 6)
)
jnxSpTcpLoggingHostStatus.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpTcpLoggingHostIpaddr"),
        ("JUNIPER-SP-MIB", "jnxSpTcpLoggingHostPort"),
        ("JUNIPER-SP-MIB", "jnxSpTcpLoggingHostConnStatus"),
        ("JUNIPER-SP-MIB", "jnxSpTcpLoggingHostRoutingInstance"))
)
if mibBuilder.loadTexts:
    jnxSpTcpLoggingHostStatus.setStatus(
        "current"
    )

jnxSpSvcSetFlowLimitUtilized = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 10, 1)
)
jnxSpSvcSetFlowLimitUtilized.setObjects(
      *(("JUNIPER-SP-MIB", "jnxSpSvcSetFlowLimitUtil"),
        ("JUNIPER-SP-MIB", "jnxSpSvcSetNameUtil"))
)
if mibBuilder.loadTexts:
    jnxSpSvcSetFlowLimitUtilized.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SP-MIB",
    **{"jnxSpMIB": jnxSpMIB,
       "jnxSpSvcSet": jnxSpSvcSet,
       "jnxSpSvcSetTable": jnxSpSvcSetTable,
       "jnxSpSvcSetEntry": jnxSpSvcSetEntry,
       "jnxSpSvcSetName": jnxSpSvcSetName,
       "jnxSpSvcSetSvcType": jnxSpSvcSetSvcType,
       "jnxSpSvcSetTypeIndex": jnxSpSvcSetTypeIndex,
       "jnxSpSvcSetIfName": jnxSpSvcSetIfName,
       "jnxSpSvcSetIfIndex": jnxSpSvcSetIfIndex,
       "jnxSpSvcSetMemoryUsage": jnxSpSvcSetMemoryUsage,
       "jnxSpSvcSetCpuUtil": jnxSpSvcSetCpuUtil,
       "jnxSpSvcSetSvcStyle": jnxSpSvcSetSvcStyle,
       "jnxSpSvcSetMemLimitPktDrops": jnxSpSvcSetMemLimitPktDrops,
       "jnxSpSvcSetCpuLimitPktDrops": jnxSpSvcSetCpuLimitPktDrops,
       "jnxSpSvcSetFlowLimitPktDrops": jnxSpSvcSetFlowLimitPktDrops,
       "jnxSpSvcSetMemoryUsage64": jnxSpSvcSetMemoryUsage64,
       "jnxSpSvcSetMemLimitPktDrops64": jnxSpSvcSetMemLimitPktDrops64,
       "jnxSpSvcSetCpuLimitPktDrops64": jnxSpSvcSetCpuLimitPktDrops64,
       "jnxSpSvcSetFlowLimitPktDrops64": jnxSpSvcSetFlowLimitPktDrops64,
       "jnxSpSvcSetSessCount": jnxSpSvcSetSessCount,
       "jnxSpSvcSetSvcTypeTable": jnxSpSvcSetSvcTypeTable,
       "jnxSpSvcSetSvcTypeEntry": jnxSpSvcSetSvcTypeEntry,
       "jnxSpSvcSetSvcTypeIndex": jnxSpSvcSetSvcTypeIndex,
       "jnxSpSvcSetSvcTypeIfName": jnxSpSvcSetSvcTypeIfName,
       "jnxSpSvcSetSvcTypeName": jnxSpSvcSetSvcTypeName,
       "jnxSpSvcSetSvcTypeSvcSets": jnxSpSvcSetSvcTypeSvcSets,
       "jnxSpSvcSetSvcTypeMemoryUsage": jnxSpSvcSetSvcTypeMemoryUsage,
       "jnxSpSvcSetSvcTypePctMemoryUsage": jnxSpSvcSetSvcTypePctMemoryUsage,
       "jnxSpSvcSetSvcTypeCpuUtil": jnxSpSvcSetSvcTypeCpuUtil,
       "jnxSpSvcSetSvcTypeMemoryUsage64": jnxSpSvcSetSvcTypeMemoryUsage64,
       "jnxSpSvcSetIfTable": jnxSpSvcSetIfTable,
       "jnxSpSvcSetIfEntry": jnxSpSvcSetIfEntry,
       "jnxSpSvcSetIfTableName": jnxSpSvcSetIfTableName,
       "jnxSpSvcSetIfSvcSets": jnxSpSvcSetIfSvcSets,
       "jnxSpSvcSetIfMemoryUsage": jnxSpSvcSetIfMemoryUsage,
       "jnxSpSvcSetIfPctMemoryUsage": jnxSpSvcSetIfPctMemoryUsage,
       "jnxSpSvcSetIfPolMemoryUsage": jnxSpSvcSetIfPolMemoryUsage,
       "jnxSpSvcSetIfPctPolMemoryUsage": jnxSpSvcSetIfPctPolMemoryUsage,
       "jnxSpSvcSetIfMemoryZone": jnxSpSvcSetIfMemoryZone,
       "jnxSpSvcSetIfCpuUtil": jnxSpSvcSetIfCpuUtil,
       "jnxSpSvcSetIfMemoryUsage64": jnxSpSvcSetIfMemoryUsage64,
       "jnxSpSvcSetIfPolMemoryUsage64": jnxSpSvcSetIfPolMemoryUsage64,
       "jnxSpSvcSetIfNumTotalSessActive": jnxSpSvcSetIfNumTotalSessActive,
       "jnxSpSvcSetIfPeakTotalSessActive": jnxSpSvcSetIfPeakTotalSessActive,
       "jnxSpSvcSetIfNumCreatedSessPerSec": jnxSpSvcSetIfNumCreatedSessPerSec,
       "jnxSpSvcSetIfNumDeletedSessPerSec": jnxSpSvcSetIfNumDeletedSessPerSec,
       "jnxSpSvcSetIfNumTotalTcpSessActive": jnxSpSvcSetIfNumTotalTcpSessActive,
       "jnxSpSvcSetIfNumTotalUdpSessActive": jnxSpSvcSetIfNumTotalUdpSessActive,
       "jnxSpSvcSetIfNumTotalOtherSessActive": jnxSpSvcSetIfNumTotalOtherSessActive,
       "jnxSpSvcSetIfPeakTotalTcpSessActive": jnxSpSvcSetIfPeakTotalTcpSessActive,
       "jnxSpSvcSetIfPeakTotalUdpSessActive": jnxSpSvcSetIfPeakTotalUdpSessActive,
       "jnxSpSvcSetIfPeakTotalOtherSessActive": jnxSpSvcSetIfPeakTotalOtherSessActive,
       "jnxSpSvcSetIfPeakCreatedSessPerSec": jnxSpSvcSetIfPeakCreatedSessPerSec,
       "jnxSpSvcSetIfPeakDeletedSessPerSec": jnxSpSvcSetIfPeakDeletedSessPerSec,
       "jnxSpSvcSetIfNumTotalTcpIpv4SessActive": jnxSpSvcSetIfNumTotalTcpIpv4SessActive,
       "jnxSpSvcSetIfNumTotalTcpIpv6SessActive": jnxSpSvcSetIfNumTotalTcpIpv6SessActive,
       "jnxSpSvcSetIfNumTotalUdpIpv4SessActive": jnxSpSvcSetIfNumTotalUdpIpv4SessActive,
       "jnxSpSvcSetIfNumTotalUdpIpv6SessActive": jnxSpSvcSetIfNumTotalUdpIpv6SessActive,
       "jnxSpSvcSetIfNumTotalOtherIpv4SessActive": jnxSpSvcSetIfNumTotalOtherIpv4SessActive,
       "jnxSpSvcSetIfNumTotalOtherIpv6SessActive": jnxSpSvcSetIfNumTotalOtherIpv6SessActive,
       "jnxSpSvcSetIfNumTotalTcpGatedSessActive": jnxSpSvcSetIfNumTotalTcpGatedSessActive,
       "jnxSpSvcSetIfNumTotalUdpGatedSessActive": jnxSpSvcSetIfNumTotalUdpGatedSessActive,
       "jnxSpSvcSetIfNumTotalTcpRegSessActive": jnxSpSvcSetIfNumTotalTcpRegSessActive,
       "jnxSpSvcSetIfNumTotalUdpRegSessActive": jnxSpSvcSetIfNumTotalUdpRegSessActive,
       "jnxSpSvcSetIfNumTotalTcpTunSessActive": jnxSpSvcSetIfNumTotalTcpTunSessActive,
       "jnxSpSvcSetIfNumTotalUdpTunSessActive": jnxSpSvcSetIfNumTotalUdpTunSessActive,
       "jnxSpSvcSetIfSessPktRecv": jnxSpSvcSetIfSessPktRecv,
       "jnxSpSvcSetIfSessPktXmit": jnxSpSvcSetIfSessPktXmit,
       "jnxSpSvcSetIfSessSlowPathDiscard": jnxSpSvcSetIfSessSlowPathDiscard,
       "jnxSpSvcSetIfSessSlowPathForward": jnxSpSvcSetIfSessSlowPathForward,
       "jnxSpSvcSetIfMspNumCreatedSubsPerSec": jnxSpSvcSetIfMspNumCreatedSubsPerSec,
       "jnxSpSvcSetIfMspNumDeletedSubsPerSec": jnxSpSvcSetIfMspNumDeletedSubsPerSec,
       "jnxSpSvcSetIfMspNumTotalSubsActive": jnxSpSvcSetIfMspNumTotalSubsActive,
       "jnxSpSvcSetIfMspPeakCreatedSubsPerSec": jnxSpSvcSetIfMspPeakCreatedSubsPerSec,
       "jnxSpSvcSetIfMspPeakDeletedSubsPerSec": jnxSpSvcSetIfMspPeakDeletedSubsPerSec,
       "jnxSpSvcSetIfMspPeakTotalSubsActive": jnxSpSvcSetIfMspPeakTotalSubsActive,
       "jnxFlowLimitTrapVars": jnxFlowLimitTrapVars,
       "jnxSpSvcSetFlowLimitUtil": jnxSpSvcSetFlowLimitUtil,
       "jnxSpSvcSetNameUtil": jnxSpSvcSetNameUtil,
       "jnxTcpLoggingTrapVars": jnxTcpLoggingTrapVars,
       "jnxSpTcpLoggingHostIpaddr": jnxSpTcpLoggingHostIpaddr,
       "jnxSpTcpLoggingHostPort": jnxSpTcpLoggingHostPort,
       "jnxSpTcpLoggingHostConnStatus": jnxSpTcpLoggingHostConnStatus,
       "jnxSpTcpLoggingHostRoutingInstance": jnxSpTcpLoggingHostRoutingInstance,
       "jnxSpNotificationPrefix": jnxSpNotificationPrefix,
       "jnxSpSvcSetZoneEntered": jnxSpSvcSetZoneEntered,
       "jnxSpSvcSetZoneExited": jnxSpSvcSetZoneExited,
       "jnxSpSvcSetCpuExceeded": jnxSpSvcSetCpuExceeded,
       "jnxSpSvcSetCpuOk": jnxSpSvcSetCpuOk,
       "jnxSpSvcSetFlowLimitUtilised": jnxSpSvcSetFlowLimitUtilised,
       "jnxSpTcpLoggingHostStatus": jnxSpTcpLoggingHostStatus,
       "jnxSpSvcSetFlowLimitUtilized": jnxSpSvcSetFlowLimitUtilized}
)
