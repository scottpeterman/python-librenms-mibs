# SNMP MIB module (WESTERMO-WEOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\westermo\WESTERMO-WEOS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:09 2025
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

(entPhysicalName,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalName")

(entPhySensorPrecision,
 entPhySensorScale,
 entPhySensorType,
 entPhySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "entPhySensorPrecision",
    "entPhySensorScale",
    "entPhySensorType",
    "entPhySensorValue")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(common,) = mibBuilder.importSymbols(
    "WESTERMO-OID-MIB",
    "common")


# MODULE-IDENTITY

weos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1)
)
if mibBuilder.loadTexts:
    weos.setRevisions(
        ("2018-10-30 00:00",
         "2018-03-12 00:00",
         "2017-10-03 00:00",
         "2017-03-28 00:00",
         "2017-01-23 00:00",
         "2016-12-16 00:00",
         "2016-06-14 00:00",
         "2015-12-16 00:00",
         "2015-09-09 00:00",
         "2014-10-10 00:00",
         "2013-10-17 00:00",
         "2013-05-13 00:00",
         "2012-01-03 00:00",
         "2011-05-16 00:00",
         "2010-11-15 00:00",
         "2010-08-19 00:00",
         "2009-11-12 00:00",
         "2009-10-09 00:00",
         "2009-08-26 00:00",
         "2009-05-31 00:00",
         "2009-05-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Command_ObjectIdentity = ObjectIdentity
command = _Command_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 1)
)


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 1, 1),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("current")


class _FactoryReset_Type(Integer32):
    """Custom type factoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restoreAndReboot", 1)
    )


_FactoryReset_Type.__name__ = "Integer32"
_FactoryReset_Object = MibScalar
factoryReset = _FactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 1, 2),
    _FactoryReset_Type()
)
factoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    factoryReset.setStatus("current")
_Phy_ObjectIdentity = ObjectIdentity
phy = _Phy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2)
)
_LffTable_Object = MibTable
lffTable = _LffTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lffTable.setStatus("current")
_LffEntry_Object = MibTableRow
lffEntry = _LffEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 1, 1)
)
lffEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "lffPortIfIndex"),
)
if mibBuilder.loadTexts:
    lffEntry.setStatus("current")
_LffPortIfIndex_Type = InterfaceIndex
_LffPortIfIndex_Object = MibTableColumn
lffPortIfIndex = _LffPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 1, 1, 1),
    _LffPortIfIndex_Type()
)
lffPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lffPortIfIndex.setStatus("current")
_LffPortIfName_Type = DisplayString
_LffPortIfName_Object = MibTableColumn
lffPortIfName = _LffPortIfName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 1, 1, 2),
    _LffPortIfName_Type()
)
lffPortIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lffPortIfName.setStatus("current")


class _LffStatus_Type(Integer32):
    """Custom type lffStatus based on Integer32"""
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
        *(("disabled", 1),
          ("unknown", 2),
          ("remoteDown", 3),
          ("remoteUp", 4))
    )


_LffStatus_Type.__name__ = "Integer32"
_LffStatus_Object = MibTableColumn
lffStatus = _LffStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 1, 1, 3),
    _LffStatus_Type()
)
lffStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lffStatus.setStatus("current")
_Sfp_ObjectIdentity = ObjectIdentity
sfp = _Sfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 2)
)
_SfpDdmPortTable_Object = MibTable
sfpDdmPortTable = _SfpDdmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sfpDdmPortTable.setStatus("current")
_SfpDdmPortEntry_Object = MibTableRow
sfpDdmPortEntry = _SfpDdmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 2, 1, 1)
)
sfpDdmPortEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
)
if mibBuilder.loadTexts:
    sfpDdmPortEntry.setStatus("current")
_SfpDdmPortIfIndex_Type = InterfaceIndex
_SfpDdmPortIfIndex_Object = MibTableColumn
sfpDdmPortIfIndex = _SfpDdmPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 2, 1, 1, 1),
    _SfpDdmPortIfIndex_Type()
)
sfpDdmPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sfpDdmPortIfIndex.setStatus("current")
_SfpDdmPortIfName_Type = DisplayString
_SfpDdmPortIfName_Object = MibTableColumn
sfpDdmPortIfName = _SfpDdmPortIfName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 2, 1, 1, 2),
    _SfpDdmPortIfName_Type()
)
sfpDdmPortIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDdmPortIfName.setStatus("current")


class _SfpDdmPortVoltage_Type(Integer32):
    """Custom type sfpDdmPortVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6550),
    )


_SfpDdmPortVoltage_Type.__name__ = "Integer32"
_SfpDdmPortVoltage_Object = MibTableColumn
sfpDdmPortVoltage = _SfpDdmPortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 2, 1, 1, 3),
    _SfpDdmPortVoltage_Type()
)
sfpDdmPortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDdmPortVoltage.setStatus("current")


class _SfpDdmPortTemperature_Type(Integer32):
    """Custom type sfpDdmPortTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_SfpDdmPortTemperature_Type.__name__ = "Integer32"
_SfpDdmPortTemperature_Object = MibTableColumn
sfpDdmPortTemperature = _SfpDdmPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 2, 1, 1, 4),
    _SfpDdmPortTemperature_Type()
)
sfpDdmPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDdmPortTemperature.setStatus("current")


class _SfpDdmPortBiasCurrent_Type(Integer32):
    """Custom type sfpDdmPortBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131),
    )


_SfpDdmPortBiasCurrent_Type.__name__ = "Integer32"
_SfpDdmPortBiasCurrent_Object = MibTableColumn
sfpDdmPortBiasCurrent = _SfpDdmPortBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 2, 1, 1, 5),
    _SfpDdmPortBiasCurrent_Type()
)
sfpDdmPortBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDdmPortBiasCurrent.setStatus("current")


class _SfpDdmPortTxPower_Type(Integer32):
    """Custom type sfpDdmPortTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 820),
    )


_SfpDdmPortTxPower_Type.__name__ = "Integer32"
_SfpDdmPortTxPower_Object = MibTableColumn
sfpDdmPortTxPower = _SfpDdmPortTxPower_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 2, 1, 1, 6),
    _SfpDdmPortTxPower_Type()
)
sfpDdmPortTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDdmPortTxPower.setStatus("current")


class _SfpDdmPortRxPower_Type(Integer32):
    """Custom type sfpDdmPortRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 820),
    )


_SfpDdmPortRxPower_Type.__name__ = "Integer32"
_SfpDdmPortRxPower_Object = MibTableColumn
sfpDdmPortRxPower = _SfpDdmPortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 2, 1, 1, 7),
    _SfpDdmPortRxPower_Type()
)
sfpDdmPortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDdmPortRxPower.setStatus("current")
_PhyStats_ObjectIdentity = ObjectIdentity
phyStats = _PhyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3)
)
_SummaryFCSErrors_Type = Integer32
_SummaryFCSErrors_Object = MibScalar
summaryFCSErrors = _SummaryFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 1),
    _SummaryFCSErrors_Type()
)
summaryFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryFCSErrors.setStatus("current")
_BwStatsTable_Object = MibTable
bwStatsTable = _BwStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    bwStatsTable.setStatus("current")
_BwStatsEntry_Object = MibTableRow
bwStatsEntry = _BwStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1)
)
bwStatsEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "bwStatsIndex"),
)
if mibBuilder.loadTexts:
    bwStatsEntry.setStatus("current")
_BwStatsIndex_Type = InterfaceIndex
_BwStatsIndex_Object = MibTableColumn
bwStatsIndex = _BwStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1, 1),
    _BwStatsIndex_Type()
)
bwStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwStatsIndex.setStatus("current")
_BwStatsEnabled_Type = TruthValue
_BwStatsEnabled_Object = MibTableColumn
bwStatsEnabled = _BwStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1, 2),
    _BwStatsEnabled_Type()
)
bwStatsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwStatsEnabled.setStatus("current")
_BwStatsBitrateIn10s_Type = Counter64
_BwStatsBitrateIn10s_Object = MibTableColumn
bwStatsBitrateIn10s = _BwStatsBitrateIn10s_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1, 3),
    _BwStatsBitrateIn10s_Type()
)
bwStatsBitrateIn10s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwStatsBitrateIn10s.setStatus("current")
if mibBuilder.loadTexts:
    bwStatsBitrateIn10s.setUnits("Bits per second")
_BwStatsBitrateOut10s_Type = Counter64
_BwStatsBitrateOut10s_Object = MibTableColumn
bwStatsBitrateOut10s = _BwStatsBitrateOut10s_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1, 4),
    _BwStatsBitrateOut10s_Type()
)
bwStatsBitrateOut10s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwStatsBitrateOut10s.setStatus("current")
if mibBuilder.loadTexts:
    bwStatsBitrateOut10s.setUnits("Bits per second")
_BwStatsBitrateIn1m_Type = Counter64
_BwStatsBitrateIn1m_Object = MibTableColumn
bwStatsBitrateIn1m = _BwStatsBitrateIn1m_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1, 5),
    _BwStatsBitrateIn1m_Type()
)
bwStatsBitrateIn1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwStatsBitrateIn1m.setStatus("current")
if mibBuilder.loadTexts:
    bwStatsBitrateIn1m.setUnits("Bits per second")
_BwStatsBitrateOut1m_Type = Counter64
_BwStatsBitrateOut1m_Object = MibTableColumn
bwStatsBitrateOut1m = _BwStatsBitrateOut1m_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1, 6),
    _BwStatsBitrateOut1m_Type()
)
bwStatsBitrateOut1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwStatsBitrateOut1m.setStatus("current")
if mibBuilder.loadTexts:
    bwStatsBitrateOut1m.setUnits("Bits per second")
_BwStatsBitrateIn10m_Type = Counter64
_BwStatsBitrateIn10m_Object = MibTableColumn
bwStatsBitrateIn10m = _BwStatsBitrateIn10m_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1, 7),
    _BwStatsBitrateIn10m_Type()
)
bwStatsBitrateIn10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwStatsBitrateIn10m.setStatus("current")
if mibBuilder.loadTexts:
    bwStatsBitrateIn10m.setUnits("Bits per second")
_BwStatsBitrateOut10m_Type = Counter64
_BwStatsBitrateOut10m_Object = MibTableColumn
bwStatsBitrateOut10m = _BwStatsBitrateOut10m_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1, 8),
    _BwStatsBitrateOut10m_Type()
)
bwStatsBitrateOut10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwStatsBitrateOut10m.setStatus("current")
if mibBuilder.loadTexts:
    bwStatsBitrateOut10m.setUnits("Bits per second")
_BwStatsBitrateIn1h_Type = Counter64
_BwStatsBitrateIn1h_Object = MibTableColumn
bwStatsBitrateIn1h = _BwStatsBitrateIn1h_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1, 9),
    _BwStatsBitrateIn1h_Type()
)
bwStatsBitrateIn1h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwStatsBitrateIn1h.setStatus("current")
if mibBuilder.loadTexts:
    bwStatsBitrateIn1h.setUnits("Bits per second")
_BwStatsBitrateOut1h_Type = Counter64
_BwStatsBitrateOut1h_Object = MibTableColumn
bwStatsBitrateOut1h = _BwStatsBitrateOut1h_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 2, 3, 2, 1, 10),
    _BwStatsBitrateOut1h_Type()
)
bwStatsBitrateOut1h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwStatsBitrateOut1h.setStatus("current")
if mibBuilder.loadTexts:
    bwStatsBitrateOut1h.setUnits("Bits per second")
_Link_ObjectIdentity = ObjectIdentity
link = _Link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3)
)
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 1)
)
_L2Qos_ObjectIdentity = ObjectIdentity
l2Qos = _L2Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2)
)
_L2QosVlanTable_Object = MibTable
l2QosVlanTable = _L2QosVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    l2QosVlanTable.setStatus("current")
_L2QosVlanEntry_Object = MibTableRow
l2QosVlanEntry = _L2QosVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 1, 1)
)
l2QosVlanEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "l2QosVlanId"),
)
if mibBuilder.loadTexts:
    l2QosVlanEntry.setStatus("current")
_L2QosVlanId_Type = VlanId
_L2QosVlanId_Object = MibTableColumn
l2QosVlanId = _L2QosVlanId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 1, 1, 1),
    _L2QosVlanId_Type()
)
l2QosVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2QosVlanId.setStatus("current")
_VlanPriorityEnabled_Type = TruthValue
_VlanPriorityEnabled_Object = MibTableColumn
vlanPriorityEnabled = _VlanPriorityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 1, 1, 2),
    _VlanPriorityEnabled_Type()
)
vlanPriorityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPriorityEnabled.setStatus("current")


class _VlanPriorityLevel_Type(Integer32):
    """Custom type vlanPriorityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanPriorityLevel_Type.__name__ = "Integer32"
_VlanPriorityLevel_Object = MibTableColumn
vlanPriorityLevel = _VlanPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 1, 1, 3),
    _VlanPriorityLevel_Type()
)
vlanPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPriorityLevel.setStatus("current")
_L2QosPortTable_Object = MibTable
l2QosPortTable = _L2QosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    l2QosPortTable.setStatus("current")
_L2QosPortEntry_Object = MibTableRow
l2QosPortEntry = _L2QosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 2, 1)
)
l2QosPortEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "l2QosPortIfIndex"),
)
if mibBuilder.loadTexts:
    l2QosPortEntry.setStatus("current")
_L2QosPortIfIndex_Type = InterfaceIndex
_L2QosPortIfIndex_Object = MibTableColumn
l2QosPortIfIndex = _L2QosPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 2, 1, 1),
    _L2QosPortIfIndex_Type()
)
l2QosPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2QosPortIfIndex.setStatus("current")
_L2QosPortIfName_Type = DisplayString
_L2QosPortIfName_Object = MibTableColumn
l2QosPortIfName = _L2QosPortIfName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 2, 1, 2),
    _L2QosPortIfName_Type()
)
l2QosPortIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2QosPortIfName.setStatus("current")


class _L2QosPortPriorityMode_Type(Integer32):
    """Custom type l2QosPortPriorityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("ip", 2),
          ("port", 3))
    )


_L2QosPortPriorityMode_Type.__name__ = "Integer32"
_L2QosPortPriorityMode_Object = MibTableColumn
l2QosPortPriorityMode = _L2QosPortPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 2, 1, 3),
    _L2QosPortPriorityMode_Type()
)
l2QosPortPriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2QosPortPriorityMode.setStatus("current")


class _L2QosPortPriorityLevel_Type(Integer32):
    """Custom type l2QosPortPriorityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_L2QosPortPriorityLevel_Type.__name__ = "Integer32"
_L2QosPortPriorityLevel_Object = MibTableColumn
l2QosPortPriorityLevel = _L2QosPortPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 2, 2, 1, 4),
    _L2QosPortPriorityLevel_Type()
)
l2QosPortPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2QosPortPriorityLevel.setStatus("current")
_Frnt_ObjectIdentity = ObjectIdentity
frnt = _Frnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3)
)
_Frntv0_ObjectIdentity = ObjectIdentity
frntv0 = _Frntv0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1)
)
_Frntv0Table_Object = MibTable
frntv0Table = _Frntv0Table_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    frntv0Table.setStatus("current")
_Frntv0Entry_Object = MibTableRow
frntv0Entry = _Frntv0Entry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1)
)
frntv0Entry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "frntv0InstanceId"),
)
if mibBuilder.loadTexts:
    frntv0Entry.setStatus("current")


class _Frntv0InstanceId_Type(Integer32):
    """Custom type frntv0InstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Frntv0InstanceId_Type.__name__ = "Integer32"
_Frntv0InstanceId_Object = MibTableColumn
frntv0InstanceId = _Frntv0InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 1),
    _Frntv0InstanceId_Type()
)
frntv0InstanceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    frntv0InstanceId.setStatus("current")
_Frntv0FocalPointEnabled_Type = TruthValue
_Frntv0FocalPointEnabled_Object = MibTableColumn
frntv0FocalPointEnabled = _Frntv0FocalPointEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 2),
    _Frntv0FocalPointEnabled_Type()
)
frntv0FocalPointEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frntv0FocalPointEnabled.setStatus("current")
_Frntv0Port1_Type = DisplayString
_Frntv0Port1_Object = MibTableColumn
frntv0Port1 = _Frntv0Port1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 3),
    _Frntv0Port1_Type()
)
frntv0Port1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frntv0Port1.setStatus("current")
_Frntv0Port2_Type = DisplayString
_Frntv0Port2_Object = MibTableColumn
frntv0Port2 = _Frntv0Port2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 4),
    _Frntv0Port2_Type()
)
frntv0Port2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frntv0Port2.setStatus("current")


class _Frntv0Port1State_Type(Integer32):
    """Custom type frntv0Port1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("learning", 4),
          ("forwarding", 5))
    )


_Frntv0Port1State_Type.__name__ = "Integer32"
_Frntv0Port1State_Object = MibTableColumn
frntv0Port1State = _Frntv0Port1State_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 5),
    _Frntv0Port1State_Type()
)
frntv0Port1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntv0Port1State.setStatus("current")


class _Frntv0Port2State_Type(Integer32):
    """Custom type frntv0Port2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("learning", 4),
          ("forwarding", 5))
    )


_Frntv0Port2State_Type.__name__ = "Integer32"
_Frntv0Port2State_Object = MibTableColumn
frntv0Port2State = _Frntv0Port2State_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 6),
    _Frntv0Port2State_Type()
)
frntv0Port2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntv0Port2State.setStatus("current")


class _Frntv0RingStatus_Type(Integer32):
    """Custom type frntv0RingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ring", 1),
          ("bus", 2))
    )


_Frntv0RingStatus_Type.__name__ = "Integer32"
_Frntv0RingStatus_Object = MibTableColumn
frntv0RingStatus = _Frntv0RingStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 7),
    _Frntv0RingStatus_Type()
)
frntv0RingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntv0RingStatus.setStatus("current")
_Frntv0RowStatus_Type = RowStatus
_Frntv0RowStatus_Object = MibTableColumn
frntv0RowStatus = _Frntv0RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 8),
    _Frntv0RowStatus_Type()
)
frntv0RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frntv0RowStatus.setStatus("current")
_Frntv0TopologyChangeCount_Type = Integer32
_Frntv0TopologyChangeCount_Object = MibTableColumn
frntv0TopologyChangeCount = _Frntv0TopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 9),
    _Frntv0TopologyChangeCount_Type()
)
frntv0TopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntv0TopologyChangeCount.setStatus("current")
_Frntv0TopologyTimeSinceLastChange_Type = TimeTicks
_Frntv0TopologyTimeSinceLastChange_Object = MibTableColumn
frntv0TopologyTimeSinceLastChange = _Frntv0TopologyTimeSinceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 10),
    _Frntv0TopologyTimeSinceLastChange_Type()
)
frntv0TopologyTimeSinceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntv0TopologyTimeSinceLastChange.setStatus("current")
_Frntv0PortsSwapped_Type = TruthValue
_Frntv0PortsSwapped_Object = MibTableColumn
frntv0PortsSwapped = _Frntv0PortsSwapped_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 3, 1, 1, 1, 11),
    _Frntv0PortsSwapped_Type()
)
frntv0PortsSwapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntv0PortsSwapped.setStatus("current")
_IgmpSnooping_ObjectIdentity = ObjectIdentity
igmpSnooping = _IgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 4)
)


class _IgmpSnoopingQuerierMode_Type(Integer32):
    """Custom type igmpSnoopingQuerierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("querier", 2),
          ("proxy", 3))
    )


_IgmpSnoopingQuerierMode_Type.__name__ = "Integer32"
_IgmpSnoopingQuerierMode_Object = MibScalar
igmpSnoopingQuerierMode = _IgmpSnoopingQuerierMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 4, 1),
    _IgmpSnoopingQuerierMode_Type()
)
igmpSnoopingQuerierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingQuerierMode.setStatus("current")
_IgmpSnoopingQuerierInterval_Type = Integer32
_IgmpSnoopingQuerierInterval_Object = MibScalar
igmpSnoopingQuerierInterval = _IgmpSnoopingQuerierInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 4, 2),
    _IgmpSnoopingQuerierInterval_Type()
)
igmpSnoopingQuerierInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingQuerierInterval.setStatus("current")
_StaticMulticastRouterPorts_Type = DisplayString
_StaticMulticastRouterPorts_Object = MibScalar
staticMulticastRouterPorts = _StaticMulticastRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 4, 3),
    _StaticMulticastRouterPorts_Type()
)
staticMulticastRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMulticastRouterPorts.setStatus("current")
_CurrentMulticastRouterPorts_Type = DisplayString
_CurrentMulticastRouterPorts_Object = MibScalar
currentMulticastRouterPorts = _CurrentMulticastRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 4, 4),
    _CurrentMulticastRouterPorts_Type()
)
currentMulticastRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMulticastRouterPorts.setStatus("current")
_IgmpSnoopingVlanTable_Object = MibTable
igmpSnoopingVlanTable = _IgmpSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 4, 5)
)
if mibBuilder.loadTexts:
    igmpSnoopingVlanTable.setStatus("current")
_IgmpSnoopingVlanEntry_Object = MibTableRow
igmpSnoopingVlanEntry = _IgmpSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 4, 5, 1)
)
igmpSnoopingVlanEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "igmpSnoopingVlanId"),
)
if mibBuilder.loadTexts:
    igmpSnoopingVlanEntry.setStatus("current")
_IgmpSnoopingVlanId_Type = VlanId
_IgmpSnoopingVlanId_Object = MibTableColumn
igmpSnoopingVlanId = _IgmpSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 4, 5, 1, 1),
    _IgmpSnoopingVlanId_Type()
)
igmpSnoopingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingVlanId.setStatus("current")
_IgmpSnoopingEnabled_Type = TruthValue
_IgmpSnoopingEnabled_Object = MibTableColumn
igmpSnoopingEnabled = _IgmpSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 4, 5, 1, 2),
    _IgmpSnoopingEnabled_Type()
)
igmpSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingEnabled.setStatus("current")
_Rico_ObjectIdentity = ObjectIdentity
rico = _Rico_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5)
)
_RiCoStatusTable_Object = MibTable
riCoStatusTable = _RiCoStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    riCoStatusTable.setStatus("current")
_RiCoStatusEntry_Object = MibTableRow
riCoStatusEntry = _RiCoStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 1, 1)
)
riCoStatusEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "riCoStatusRingIdx"),
    (0, "WESTERMO-WEOS-MIB", "riCoStatusCouplingIdx"),
    (0, "WESTERMO-WEOS-MIB", "riCoStatusNodeId"),
)
if mibBuilder.loadTexts:
    riCoStatusEntry.setStatus("current")


class _RiCoStatusRingIdx_Type(Integer32):
    """Custom type riCoStatusRingIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RiCoStatusRingIdx_Type.__name__ = "Integer32"
_RiCoStatusRingIdx_Object = MibTableColumn
riCoStatusRingIdx = _RiCoStatusRingIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 1, 1, 1),
    _RiCoStatusRingIdx_Type()
)
riCoStatusRingIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    riCoStatusRingIdx.setStatus("current")


class _RiCoStatusCouplingIdx_Type(Integer32):
    """Custom type riCoStatusCouplingIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RiCoStatusCouplingIdx_Type.__name__ = "Integer32"
_RiCoStatusCouplingIdx_Object = MibTableColumn
riCoStatusCouplingIdx = _RiCoStatusCouplingIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 1, 1, 2),
    _RiCoStatusCouplingIdx_Type()
)
riCoStatusCouplingIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    riCoStatusCouplingIdx.setStatus("current")
_RiCoStatusNodeId_Type = MacAddress
_RiCoStatusNodeId_Object = MibTableColumn
riCoStatusNodeId = _RiCoStatusNodeId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 1, 1, 3),
    _RiCoStatusNodeId_Type()
)
riCoStatusNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    riCoStatusNodeId.setStatus("current")
_RiCoStatusHelloInterval_Type = Integer32
_RiCoStatusHelloInterval_Object = MibTableColumn
riCoStatusHelloInterval = _RiCoStatusHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 1, 1, 4),
    _RiCoStatusHelloInterval_Type()
)
riCoStatusHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusHelloInterval.setStatus("current")
_RiCoStatusHelloEffective_Type = Integer32
_RiCoStatusHelloEffective_Object = MibTableColumn
riCoStatusHelloEffective = _RiCoStatusHelloEffective_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 1, 1, 5),
    _RiCoStatusHelloEffective_Type()
)
riCoStatusHelloEffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusHelloEffective.setStatus("current")
_RiCoStatusUplinkTable_Object = MibTable
riCoStatusUplinkTable = _RiCoStatusUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    riCoStatusUplinkTable.setStatus("current")
_RiCoStatusUplinkEntry_Object = MibTableRow
riCoStatusUplinkEntry = _RiCoStatusUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1)
)
riCoStatusUplinkEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "riCoStatusUplinkRingIdx"),
    (0, "WESTERMO-WEOS-MIB", "riCoStatusUplinkCouplingIdx"),
    (0, "WESTERMO-WEOS-MIB", "riCoStatusUplinkNodeId"),
    (0, "WESTERMO-WEOS-MIB", "riCoStatusUplinkIfIndex"),
)
if mibBuilder.loadTexts:
    riCoStatusUplinkEntry.setStatus("current")


class _RiCoStatusUplinkRingIdx_Type(Integer32):
    """Custom type riCoStatusUplinkRingIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RiCoStatusUplinkRingIdx_Type.__name__ = "Integer32"
_RiCoStatusUplinkRingIdx_Object = MibTableColumn
riCoStatusUplinkRingIdx = _RiCoStatusUplinkRingIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 1),
    _RiCoStatusUplinkRingIdx_Type()
)
riCoStatusUplinkRingIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    riCoStatusUplinkRingIdx.setStatus("current")


class _RiCoStatusUplinkCouplingIdx_Type(Integer32):
    """Custom type riCoStatusUplinkCouplingIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RiCoStatusUplinkCouplingIdx_Type.__name__ = "Integer32"
_RiCoStatusUplinkCouplingIdx_Object = MibTableColumn
riCoStatusUplinkCouplingIdx = _RiCoStatusUplinkCouplingIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 2),
    _RiCoStatusUplinkCouplingIdx_Type()
)
riCoStatusUplinkCouplingIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    riCoStatusUplinkCouplingIdx.setStatus("current")
_RiCoStatusUplinkNodeId_Type = MacAddress
_RiCoStatusUplinkNodeId_Object = MibTableColumn
riCoStatusUplinkNodeId = _RiCoStatusUplinkNodeId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 3),
    _RiCoStatusUplinkNodeId_Type()
)
riCoStatusUplinkNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    riCoStatusUplinkNodeId.setStatus("current")
_RiCoStatusUplinkIfIndex_Type = InterfaceIndex
_RiCoStatusUplinkIfIndex_Object = MibTableColumn
riCoStatusUplinkIfIndex = _RiCoStatusUplinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 4),
    _RiCoStatusUplinkIfIndex_Type()
)
riCoStatusUplinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkIfIndex.setStatus("current")


class _RiCoStatusUplinkStatus_Type(Integer32):
    """Custom type riCoStatusUplinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2),
          ("down", 3))
    )


_RiCoStatusUplinkStatus_Type.__name__ = "Integer32"
_RiCoStatusUplinkStatus_Object = MibTableColumn
riCoStatusUplinkStatus = _RiCoStatusUplinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 5),
    _RiCoStatusUplinkStatus_Type()
)
riCoStatusUplinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkStatus.setStatus("current")
_RiCoStatusUplinkIfName_Type = DisplayString
_RiCoStatusUplinkIfName_Object = MibTableColumn
riCoStatusUplinkIfName = _RiCoStatusUplinkIfName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 6),
    _RiCoStatusUplinkIfName_Type()
)
riCoStatusUplinkIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkIfName.setStatus("current")
_RiCoStatusUplinkPrio_Type = Integer32
_RiCoStatusUplinkPrio_Object = MibTableColumn
riCoStatusUplinkPrio = _RiCoStatusUplinkPrio_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 7),
    _RiCoStatusUplinkPrio_Type()
)
riCoStatusUplinkPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkPrio.setStatus("current")
_RiCoStatusUplinkPathCost_Type = Integer32
_RiCoStatusUplinkPathCost_Object = MibTableColumn
riCoStatusUplinkPathCost = _RiCoStatusUplinkPathCost_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 8),
    _RiCoStatusUplinkPathCost_Type()
)
riCoStatusUplinkPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkPathCost.setStatus("current")
_RiCoStatusUplinkHelloInterval_Type = Integer32
_RiCoStatusUplinkHelloInterval_Object = MibTableColumn
riCoStatusUplinkHelloInterval = _RiCoStatusUplinkHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 9),
    _RiCoStatusUplinkHelloInterval_Type()
)
riCoStatusUplinkHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkHelloInterval.setStatus("current")
_RiCoStatusUplinkHelloIntervalEffective_Type = Integer32
_RiCoStatusUplinkHelloIntervalEffective_Object = MibTableColumn
riCoStatusUplinkHelloIntervalEffective = _RiCoStatusUplinkHelloIntervalEffective_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 10),
    _RiCoStatusUplinkHelloIntervalEffective_Type()
)
riCoStatusUplinkHelloIntervalEffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkHelloIntervalEffective.setStatus("current")
_RiCoStatusUplinkChangedCounter_Type = Integer32
_RiCoStatusUplinkChangedCounter_Object = MibTableColumn
riCoStatusUplinkChangedCounter = _RiCoStatusUplinkChangedCounter_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 11),
    _RiCoStatusUplinkChangedCounter_Type()
)
riCoStatusUplinkChangedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkChangedCounter.setStatus("current")


class _RiCoStatusUplinkSynchronized_Type(Integer32):
    """Custom type riCoStatusUplinkSynchronized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("synchronized", 1),
          ("notSynchronized", 2),
          ("notApplicable", 3))
    )


_RiCoStatusUplinkSynchronized_Type.__name__ = "Integer32"
_RiCoStatusUplinkSynchronized_Object = MibTableColumn
riCoStatusUplinkSynchronized = _RiCoStatusUplinkSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 12),
    _RiCoStatusUplinkSynchronized_Type()
)
riCoStatusUplinkSynchronized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkSynchronized.setStatus("current")


class _RiCoStatusUplinkPreferred_Type(Integer32):
    """Custom type riCoStatusUplinkPreferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preferred", 1),
          ("notPreferred", 2),
          ("notApplicable", 3))
    )


_RiCoStatusUplinkPreferred_Type.__name__ = "Integer32"
_RiCoStatusUplinkPreferred_Object = MibTableColumn
riCoStatusUplinkPreferred = _RiCoStatusUplinkPreferred_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 13),
    _RiCoStatusUplinkPreferred_Type()
)
riCoStatusUplinkPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkPreferred.setStatus("current")
_RiCoStatusUplinkLocal_Type = TruthValue
_RiCoStatusUplinkLocal_Object = MibTableColumn
riCoStatusUplinkLocal = _RiCoStatusUplinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 2, 1, 14),
    _RiCoStatusUplinkLocal_Type()
)
riCoStatusUplinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riCoStatusUplinkLocal.setStatus("current")
_RiCoCfgTable_Object = MibTable
riCoCfgTable = _RiCoCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    riCoCfgTable.setStatus("current")
_RiCoCfgEntry_Object = MibTableRow
riCoCfgEntry = _RiCoCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 3, 1)
)
riCoCfgEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "riCoCfgRingIdx"),
    (0, "WESTERMO-WEOS-MIB", "riCoCfgCouplingIdx"),
)
if mibBuilder.loadTexts:
    riCoCfgEntry.setStatus("current")


class _RiCoCfgRingIdx_Type(Integer32):
    """Custom type riCoCfgRingIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RiCoCfgRingIdx_Type.__name__ = "Integer32"
_RiCoCfgRingIdx_Object = MibTableColumn
riCoCfgRingIdx = _RiCoCfgRingIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 3, 1, 1),
    _RiCoCfgRingIdx_Type()
)
riCoCfgRingIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgRingIdx.setStatus("current")


class _RiCoCfgCouplingIdx_Type(Integer32):
    """Custom type riCoCfgCouplingIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RiCoCfgCouplingIdx_Type.__name__ = "Integer32"
_RiCoCfgCouplingIdx_Object = MibTableColumn
riCoCfgCouplingIdx = _RiCoCfgCouplingIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 3, 1, 2),
    _RiCoCfgCouplingIdx_Type()
)
riCoCfgCouplingIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgCouplingIdx.setStatus("current")
_RiCoCfgEnabled_Type = TruthValue
_RiCoCfgEnabled_Object = MibTableColumn
riCoCfgEnabled = _RiCoCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 3, 1, 3),
    _RiCoCfgEnabled_Type()
)
riCoCfgEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgEnabled.setStatus("current")
_RiCoCfgHelloInterval_Type = Integer32
_RiCoCfgHelloInterval_Object = MibTableColumn
riCoCfgHelloInterval = _RiCoCfgHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 3, 1, 4),
    _RiCoCfgHelloInterval_Type()
)
riCoCfgHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgHelloInterval.setStatus("current")
_RiCoCfgSynchronize_Type = TruthValue
_RiCoCfgSynchronize_Object = MibTableColumn
riCoCfgSynchronize = _RiCoCfgSynchronize_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 3, 1, 5),
    _RiCoCfgSynchronize_Type()
)
riCoCfgSynchronize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgSynchronize.setStatus("current")
_RiCoCfgRowStatus_Type = RowStatus
_RiCoCfgRowStatus_Object = MibTableColumn
riCoCfgRowStatus = _RiCoCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 3, 1, 6),
    _RiCoCfgRowStatus_Type()
)
riCoCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgRowStatus.setStatus("current")
_RiCoCfgUplinkTable_Object = MibTable
riCoCfgUplinkTable = _RiCoCfgUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    riCoCfgUplinkTable.setStatus("current")
_RiCoCfgUplinkEntry_Object = MibTableRow
riCoCfgUplinkEntry = _RiCoCfgUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 4, 1)
)
riCoCfgUplinkEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "riCoCfgRingIdx"),
    (0, "WESTERMO-WEOS-MIB", "riCoCfgCouplingIdx"),
    (0, "WESTERMO-WEOS-MIB", "riCoCfgUplinkIfIndex"),
)
if mibBuilder.loadTexts:
    riCoCfgUplinkEntry.setStatus("current")


class _RiCoCfgUplinkRingIdx_Type(Integer32):
    """Custom type riCoCfgUplinkRingIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RiCoCfgUplinkRingIdx_Type.__name__ = "Integer32"
_RiCoCfgUplinkRingIdx_Object = MibTableColumn
riCoCfgUplinkRingIdx = _RiCoCfgUplinkRingIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 4, 1, 1),
    _RiCoCfgUplinkRingIdx_Type()
)
riCoCfgUplinkRingIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgUplinkRingIdx.setStatus("current")


class _RiCoCfgUplinkCouplingIdx_Type(Integer32):
    """Custom type riCoCfgUplinkCouplingIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RiCoCfgUplinkCouplingIdx_Type.__name__ = "Integer32"
_RiCoCfgUplinkCouplingIdx_Object = MibTableColumn
riCoCfgUplinkCouplingIdx = _RiCoCfgUplinkCouplingIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 4, 1, 2),
    _RiCoCfgUplinkCouplingIdx_Type()
)
riCoCfgUplinkCouplingIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgUplinkCouplingIdx.setStatus("current")
_RiCoCfgUplinkIfIndex_Type = InterfaceIndex
_RiCoCfgUplinkIfIndex_Object = MibTableColumn
riCoCfgUplinkIfIndex = _RiCoCfgUplinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 4, 1, 3),
    _RiCoCfgUplinkIfIndex_Type()
)
riCoCfgUplinkIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgUplinkIfIndex.setStatus("current")
_RiCoCfgUplinkPrio_Type = Integer32
_RiCoCfgUplinkPrio_Object = MibTableColumn
riCoCfgUplinkPrio = _RiCoCfgUplinkPrio_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 4, 1, 4),
    _RiCoCfgUplinkPrio_Type()
)
riCoCfgUplinkPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgUplinkPrio.setStatus("current")
_RiCoCfgUplinkAdjust_Type = Integer32
_RiCoCfgUplinkAdjust_Object = MibTableColumn
riCoCfgUplinkAdjust = _RiCoCfgUplinkAdjust_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 4, 1, 5),
    _RiCoCfgUplinkAdjust_Type()
)
riCoCfgUplinkAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgUplinkAdjust.setStatus("current")
_RiCoCfgUplinkEchoTime_Type = Integer32
_RiCoCfgUplinkEchoTime_Object = MibTableColumn
riCoCfgUplinkEchoTime = _RiCoCfgUplinkEchoTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 4, 1, 6),
    _RiCoCfgUplinkEchoTime_Type()
)
riCoCfgUplinkEchoTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgUplinkEchoTime.setStatus("current")
_RiCoCfgUplinkPathCost_Type = Integer32
_RiCoCfgUplinkPathCost_Object = MibTableColumn
riCoCfgUplinkPathCost = _RiCoCfgUplinkPathCost_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 4, 1, 7),
    _RiCoCfgUplinkPathCost_Type()
)
riCoCfgUplinkPathCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgUplinkPathCost.setStatus("current")
_RiCoCfgUplinkRowStatus_Type = RowStatus
_RiCoCfgUplinkRowStatus_Object = MibTableColumn
riCoCfgUplinkRowStatus = _RiCoCfgUplinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 5, 4, 1, 8),
    _RiCoCfgUplinkRowStatus_Type()
)
riCoCfgUplinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    riCoCfgUplinkRowStatus.setStatus("current")
_LldpCtlv_ObjectIdentity = ObjectIdentity
lldpCtlv = _LldpCtlv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6)
)
_LldpCtlvTable_Object = MibTable
lldpCtlvTable = _LldpCtlvTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    lldpCtlvTable.setStatus("current")
_LldpCtlvEntry_Object = MibTableRow
lldpCtlvEntry = _LldpCtlvEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 1, 1)
)
lldpCtlvEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "lldpCtlvIdx"),
)
if mibBuilder.loadTexts:
    lldpCtlvEntry.setStatus("current")


class _LldpCtlvIdx_Type(Integer32):
    """Custom type lldpCtlvIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_LldpCtlvIdx_Type.__name__ = "Integer32"
_LldpCtlvIdx_Object = MibTableColumn
lldpCtlvIdx = _LldpCtlvIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 1, 1, 1),
    _LldpCtlvIdx_Type()
)
lldpCtlvIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpCtlvIdx.setStatus("current")
_LldpCtlvOui_Type = OctetString
_LldpCtlvOui_Object = MibTableColumn
lldpCtlvOui = _LldpCtlvOui_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 1, 1, 2),
    _LldpCtlvOui_Type()
)
lldpCtlvOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpCtlvOui.setStatus("current")


class _LldpCtlvSubType_Type(Integer32):
    """Custom type lldpCtlvSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LldpCtlvSubType_Type.__name__ = "Integer32"
_LldpCtlvSubType_Object = MibTableColumn
lldpCtlvSubType = _LldpCtlvSubType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 1, 1, 3),
    _LldpCtlvSubType_Type()
)
lldpCtlvSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpCtlvSubType.setStatus("current")
_LldpCtlvInfo_Type = OctetString
_LldpCtlvInfo_Object = MibTableColumn
lldpCtlvInfo = _LldpCtlvInfo_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 1, 1, 4),
    _LldpCtlvInfo_Type()
)
lldpCtlvInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpCtlvInfo.setStatus("current")
_LldpCtlvRowStatus_Type = RowStatus
_LldpCtlvRowStatus_Object = MibTableColumn
lldpCtlvRowStatus = _LldpCtlvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 1, 1, 5),
    _LldpCtlvRowStatus_Type()
)
lldpCtlvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpCtlvRowStatus.setStatus("current")
_LldpCtlvPortTable_Object = MibTable
lldpCtlvPortTable = _LldpCtlvPortTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 2)
)
if mibBuilder.loadTexts:
    lldpCtlvPortTable.setStatus("current")
_LldpCtlvPortEntry_Object = MibTableRow
lldpCtlvPortEntry = _LldpCtlvPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 2, 1)
)
lldpCtlvPortEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "lldpCtlvPortIdx"),
    (0, "WESTERMO-WEOS-MIB", "lldpCtlvIdx"),
)
if mibBuilder.loadTexts:
    lldpCtlvPortEntry.setStatus("current")


class _LldpCtlvPortIdx_Type(Integer32):
    """Custom type lldpCtlvPortIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LldpCtlvPortIdx_Type.__name__ = "Integer32"
_LldpCtlvPortIdx_Object = MibTableColumn
lldpCtlvPortIdx = _LldpCtlvPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 2, 1, 1),
    _LldpCtlvPortIdx_Type()
)
lldpCtlvPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpCtlvPortIdx.setStatus("current")
_LldpCtlvPortCtlvIdx_Type = Integer32
_LldpCtlvPortCtlvIdx_Object = MibTableColumn
lldpCtlvPortCtlvIdx = _LldpCtlvPortCtlvIdx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 2, 1, 2),
    _LldpCtlvPortCtlvIdx_Type()
)
lldpCtlvPortCtlvIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpCtlvPortCtlvIdx.setStatus("current")
_LldpCtlvPortRowStatus_Type = RowStatus
_LldpCtlvPortRowStatus_Object = MibTableColumn
lldpCtlvPortRowStatus = _LldpCtlvPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 2, 1, 3),
    _LldpCtlvPortRowStatus_Type()
)
lldpCtlvPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpCtlvPortRowStatus.setStatus("current")
_LldpRemCtlvTable_Object = MibTable
lldpRemCtlvTable = _LldpRemCtlvTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 3)
)
if mibBuilder.loadTexts:
    lldpRemCtlvTable.setStatus("current")
_LldpRemCtlvEntry_Object = MibTableRow
lldpRemCtlvEntry = _LldpRemCtlvEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 3, 1)
)
lldpRemCtlvEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "lldpRemCtlvLocalPort"),
    (0, "WESTERMO-WEOS-MIB", "lldpRemCtlvMacAddress"),
    (0, "WESTERMO-WEOS-MIB", "lldpRemCtlvOui"),
    (0, "WESTERMO-WEOS-MIB", "lldpRemCtlvSubType"),
)
if mibBuilder.loadTexts:
    lldpRemCtlvEntry.setStatus("current")


class _LldpRemCtlvLocalPort_Type(Integer32):
    """Custom type lldpRemCtlvLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LldpRemCtlvLocalPort_Type.__name__ = "Integer32"
_LldpRemCtlvLocalPort_Object = MibTableColumn
lldpRemCtlvLocalPort = _LldpRemCtlvLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 3, 1, 1),
    _LldpRemCtlvLocalPort_Type()
)
lldpRemCtlvLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemCtlvLocalPort.setStatus("current")
_LldpRemCtlvMacAddress_Type = MacAddress
_LldpRemCtlvMacAddress_Object = MibTableColumn
lldpRemCtlvMacAddress = _LldpRemCtlvMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 3, 1, 2),
    _LldpRemCtlvMacAddress_Type()
)
lldpRemCtlvMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemCtlvMacAddress.setStatus("current")


class _LldpRemCtlvOui_Type(OctetString):
    """Custom type lldpRemCtlvOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_LldpRemCtlvOui_Type.__name__ = "OctetString"
_LldpRemCtlvOui_Object = MibTableColumn
lldpRemCtlvOui = _LldpRemCtlvOui_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 3, 1, 3),
    _LldpRemCtlvOui_Type()
)
lldpRemCtlvOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemCtlvOui.setStatus("current")


class _LldpRemCtlvSubType_Type(Integer32):
    """Custom type lldpRemCtlvSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LldpRemCtlvSubType_Type.__name__ = "Integer32"
_LldpRemCtlvSubType_Object = MibTableColumn
lldpRemCtlvSubType = _LldpRemCtlvSubType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 3, 1, 4),
    _LldpRemCtlvSubType_Type()
)
lldpRemCtlvSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemCtlvSubType.setStatus("current")
_LldpRemCtlvInfo_Type = OctetString
_LldpRemCtlvInfo_Object = MibTableColumn
lldpRemCtlvInfo = _LldpRemCtlvInfo_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 3, 6, 3, 1, 5),
    _LldpRemCtlvInfo_Type()
)
lldpRemCtlvInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemCtlvInfo.setStatus("current")
_Net_ObjectIdentity = ObjectIdentity
net = _Net_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4)
)
_Iface_ObjectIdentity = ObjectIdentity
iface = _Iface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1)
)
_IfaceCommon_ObjectIdentity = ObjectIdentity
ifaceCommon = _IfaceCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 1)
)
_IfaceInet4_ObjectIdentity = ObjectIdentity
ifaceInet4 = _IfaceInet4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2)
)
_Inet4StaticDefaultGatewayAddress_Type = IpAddress
_Inet4StaticDefaultGatewayAddress_Object = MibScalar
inet4StaticDefaultGatewayAddress = _Inet4StaticDefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 1),
    _Inet4StaticDefaultGatewayAddress_Type()
)
inet4StaticDefaultGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inet4StaticDefaultGatewayAddress.setStatus("current")
_Inet4BaseIfaceTable_Object = MibTable
inet4BaseIfaceTable = _Inet4BaseIfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    inet4BaseIfaceTable.setStatus("current")
_Inet4BaseIfaceEntry_Object = MibTableRow
inet4BaseIfaceEntry = _Inet4BaseIfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 2, 1)
)
inet4BaseIfaceEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "inet4BaseIfIndex"),
)
if mibBuilder.loadTexts:
    inet4BaseIfaceEntry.setStatus("current")
_Inet4BaseIfIndex_Type = InterfaceIndex
_Inet4BaseIfIndex_Object = MibTableColumn
inet4BaseIfIndex = _Inet4BaseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 2, 1, 1),
    _Inet4BaseIfIndex_Type()
)
inet4BaseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inet4BaseIfIndex.setStatus("current")
_Inet4BaseIfName_Type = DisplayString
_Inet4BaseIfName_Object = MibTableColumn
inet4BaseIfName = _Inet4BaseIfName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 2, 1, 2),
    _Inet4BaseIfName_Type()
)
inet4BaseIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inet4BaseIfName.setStatus("current")


class _Inet4BaseAddressMode_Type(Integer32):
    """Custom type inet4BaseAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_Inet4BaseAddressMode_Type.__name__ = "Integer32"
_Inet4BaseAddressMode_Object = MibTableColumn
inet4BaseAddressMode = _Inet4BaseAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 2, 1, 3),
    _Inet4BaseAddressMode_Type()
)
inet4BaseAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inet4BaseAddressMode.setStatus("current")
_Inet4StaticTable_Object = MibTable
inet4StaticTable = _Inet4StaticTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    inet4StaticTable.setStatus("current")
_Inet4StaticEntry_Object = MibTableRow
inet4StaticEntry = _Inet4StaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 3, 1)
)
inet4StaticEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "inet4StatIfIndex"),
)
if mibBuilder.loadTexts:
    inet4StaticEntry.setStatus("current")
_Inet4StatIfIndex_Type = InterfaceIndex
_Inet4StatIfIndex_Object = MibTableColumn
inet4StatIfIndex = _Inet4StatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 3, 1, 1),
    _Inet4StatIfIndex_Type()
)
inet4StatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inet4StatIfIndex.setStatus("current")
_Inet4StatIfName_Type = DisplayString
_Inet4StatIfName_Object = MibTableColumn
inet4StatIfName = _Inet4StatIfName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 3, 1, 2),
    _Inet4StatIfName_Type()
)
inet4StatIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inet4StatIfName.setStatus("current")
_Inet4StatAddress_Type = IpAddress
_Inet4StatAddress_Object = MibTableColumn
inet4StatAddress = _Inet4StatAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 3, 1, 3),
    _Inet4StatAddress_Type()
)
inet4StatAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inet4StatAddress.setStatus("current")
_Inet4StatNetmask_Type = IpAddress
_Inet4StatNetmask_Object = MibTableColumn
inet4StatNetmask = _Inet4StatNetmask_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 3, 1, 4),
    _Inet4StatNetmask_Type()
)
inet4StatNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inet4StatNetmask.setStatus("current")
_Inet4DhcpTable_Object = MibTable
inet4DhcpTable = _Inet4DhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    inet4DhcpTable.setStatus("current")
_Inet4DhcpEntry_Object = MibTableRow
inet4DhcpEntry = _Inet4DhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 4, 1)
)
inet4DhcpEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "inet4DhcpIfIndex"),
)
if mibBuilder.loadTexts:
    inet4DhcpEntry.setStatus("current")
_Inet4DhcpIfIndex_Type = InterfaceIndex
_Inet4DhcpIfIndex_Object = MibTableColumn
inet4DhcpIfIndex = _Inet4DhcpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 4, 1, 1),
    _Inet4DhcpIfIndex_Type()
)
inet4DhcpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inet4DhcpIfIndex.setStatus("current")
_Inet4DhcpIfName_Type = DisplayString
_Inet4DhcpIfName_Object = MibTableColumn
inet4DhcpIfName = _Inet4DhcpIfName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 4, 1, 2),
    _Inet4DhcpIfName_Type()
)
inet4DhcpIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inet4DhcpIfName.setStatus("current")
_Inet4DhcpClientId_Type = DisplayString
_Inet4DhcpClientId_Object = MibTableColumn
inet4DhcpClientId = _Inet4DhcpClientId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 2, 4, 1, 3),
    _Inet4DhcpClientId_Type()
)
inet4DhcpClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inet4DhcpClientId.setStatus("current")
_AddressConflict_ObjectIdentity = ObjectIdentity
addressConflict = _AddressConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4)
)
_AddressConflictExists_Type = TruthValue
_AddressConflictExists_Object = MibScalar
addressConflictExists = _AddressConflictExists_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4, 1),
    _AddressConflictExists_Type()
)
addressConflictExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressConflictExists.setStatus("current")
_AddressConflictTable_Object = MibTable
addressConflictTable = _AddressConflictTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    addressConflictTable.setStatus("current")
_AddressConflictEntry_Object = MibTableRow
addressConflictEntry = _AddressConflictEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4, 2, 1)
)
addressConflictEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "addressConflictIndex"),
)
if mibBuilder.loadTexts:
    addressConflictEntry.setStatus("current")


class _AddressConflictIndex_Type(Integer32):
    """Custom type addressConflictIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AddressConflictIndex_Type.__name__ = "Integer32"
_AddressConflictIndex_Object = MibTableColumn
addressConflictIndex = _AddressConflictIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4, 2, 1, 1),
    _AddressConflictIndex_Type()
)
addressConflictIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressConflictIndex.setStatus("current")
_AddressConflictIfIndex_Type = InterfaceIndex
_AddressConflictIfIndex_Object = MibTableColumn
addressConflictIfIndex = _AddressConflictIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4, 2, 1, 2),
    _AddressConflictIfIndex_Type()
)
addressConflictIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressConflictIfIndex.setStatus("current")
_AddressConflictIfName_Type = DisplayString
_AddressConflictIfName_Object = MibTableColumn
addressConflictIfName = _AddressConflictIfName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4, 2, 1, 3),
    _AddressConflictIfName_Type()
)
addressConflictIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressConflictIfName.setStatus("current")


class _AddressConflictType_Type(Integer32):
    """Custom type addressConflictType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2),
          ("ipAndMac", 3))
    )


_AddressConflictType_Type.__name__ = "Integer32"
_AddressConflictType_Object = MibTableColumn
addressConflictType = _AddressConflictType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4, 2, 1, 4),
    _AddressConflictType_Type()
)
addressConflictType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressConflictType.setStatus("current")
_AddressConflictMacAddress_Type = PhysAddress
_AddressConflictMacAddress_Object = MibTableColumn
addressConflictMacAddress = _AddressConflictMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4, 2, 1, 5),
    _AddressConflictMacAddress_Type()
)
addressConflictMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressConflictMacAddress.setStatus("current")
_AddressConflictIPv4Address_Type = IpAddress
_AddressConflictIPv4Address_Object = MibTableColumn
addressConflictIPv4Address = _AddressConflictIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4, 2, 1, 6),
    _AddressConflictIPv4Address_Type()
)
addressConflictIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressConflictIPv4Address.setStatus("current")
_AddressConflictTime_Type = TimeTicks
_AddressConflictTime_Object = MibTableColumn
addressConflictTime = _AddressConflictTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 1, 4, 2, 1, 7),
    _AddressConflictTime_Type()
)
addressConflictTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressConflictTime.setStatus("current")
_Ttdp_ObjectIdentity = ObjectIdentity
ttdp = _Ttdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 2)
)
_EtbnInhibitionEnabled_Type = TruthValue
_EtbnInhibitionEnabled_Object = MibScalar
etbnInhibitionEnabled = _EtbnInhibitionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 4, 2, 1),
    _EtbnInhibitionEnabled_Type()
)
etbnInhibitionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etbnInhibitionEnabled.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5)
)
_Services_ObjectIdentity = ObjectIdentity
services = _Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 1)
)
_TrapCommunity_Type = DisplayString
_TrapCommunity_Object = MibScalar
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 1, 1),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("current")
_TrapHostTable_Object = MibTable
trapHostTable = _TrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    trapHostTable.setStatus("current")
_TrapHostEntry_Object = MibTableRow
trapHostEntry = _TrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 1, 2, 1)
)
trapHostEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "trapHostId"),
)
if mibBuilder.loadTexts:
    trapHostEntry.setStatus("current")


class _TrapHostId_Type(Integer32):
    """Custom type trapHostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TrapHostId_Type.__name__ = "Integer32"
_TrapHostId_Object = MibTableColumn
trapHostId = _TrapHostId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 1, 2, 1, 1),
    _TrapHostId_Type()
)
trapHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapHostId.setStatus("current")
_TrapHostAddressType_Type = InetAddressType
_TrapHostAddressType_Object = MibTableColumn
trapHostAddressType = _TrapHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 1, 2, 1, 2),
    _TrapHostAddressType_Type()
)
trapHostAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapHostAddressType.setStatus("current")
_TrapHostAddress_Type = DisplayString
_TrapHostAddress_Object = MibTableColumn
trapHostAddress = _TrapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 1, 2, 1, 3),
    _TrapHostAddress_Type()
)
trapHostAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapHostAddress.setStatus("current")
_TrapHostRowStatus_Type = RowStatus
_TrapHostRowStatus_Object = MibTableColumn
trapHostRowStatus = _TrapHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 1, 2, 1, 4),
    _TrapHostRowStatus_Type()
)
trapHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapHostRowStatus.setStatus("current")
_RoCommunity_Type = DisplayString
_RoCommunity_Object = MibScalar
roCommunity = _RoCommunity_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 1, 3),
    _RoCommunity_Type()
)
roCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roCommunity.setStatus("current")
_RwCommunity_Type = DisplayString
_RwCommunity_Object = MibScalar
rwCommunity = _RwCommunity_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 1, 4),
    _RwCommunity_Type()
)
rwCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rwCommunity.setStatus("current")
_Web_ObjectIdentity = ObjectIdentity
web = _Web_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 2)
)
_WebEnabled_Type = TruthValue
_WebEnabled_Object = MibScalar
webEnabled = _WebEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 2, 1),
    _WebEnabled_Type()
)
webEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webEnabled.setStatus("current")
_Ipconfig_ObjectIdentity = ObjectIdentity
ipconfig = _Ipconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 3)
)
_IpconfigEnabled_Type = TruthValue
_IpconfigEnabled_Object = MibScalar
ipconfigEnabled = _IpconfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 3, 1),
    _IpconfigEnabled_Type()
)
ipconfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipconfigEnabled.setStatus("current")
_Ssh_ObjectIdentity = ObjectIdentity
ssh = _Ssh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 4)
)
_SshEnabled_Type = TruthValue
_SshEnabled_Object = MibScalar
sshEnabled = _SshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 4, 1),
    _SshEnabled_Type()
)
sshEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshEnabled.setStatus("current")
_Lldp_ObjectIdentity = ObjectIdentity
lldp = _Lldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 5)
)
_LldpEnabled_Type = TruthValue
_LldpEnabled_Object = MibScalar
lldpEnabled = _LldpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 5, 1),
    _LldpEnabled_Type()
)
lldpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpEnabled.setStatus("current")
_LldpActivated_Type = TruthValue
_LldpActivated_Object = MibScalar
lldpActivated = _LldpActivated_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 1, 5, 2),
    _LldpActivated_Type()
)
lldpActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpActivated.setStatus("current")
_EventSystem_ObjectIdentity = ObjectIdentity
eventSystem = _EventSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2)
)


class _SummaryAlarmStatus_Type(Integer32):
    """Custom type summaryAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("ok", 2))
    )


_SummaryAlarmStatus_Type.__name__ = "Integer32"
_SummaryAlarmStatus_Object = MibScalar
summaryAlarmStatus = _SummaryAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2, 1),
    _SummaryAlarmStatus_Type()
)
summaryAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryAlarmStatus.setStatus("current")
_SummaryAlarmTrapEnabled_Type = TruthValue
_SummaryAlarmTrapEnabled_Object = MibScalar
summaryAlarmTrapEnabled = _SummaryAlarmTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2, 2),
    _SummaryAlarmTrapEnabled_Type()
)
summaryAlarmTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    summaryAlarmTrapEnabled.setStatus("current")


class _StatusRelay_Type(Integer32):
    """Custom type statusRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("ok", 2))
    )


_StatusRelay_Type.__name__ = "Integer32"
_StatusRelay_Object = MibScalar
statusRelay = _StatusRelay_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2, 3),
    _StatusRelay_Type()
)
statusRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRelay.setStatus("current")
_AlarmStatusTable_Object = MibTable
alarmStatusTable = _AlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    alarmStatusTable.setStatus("current")
_AlarmStatusEntry_Object = MibTableRow
alarmStatusEntry = _AlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2, 4, 1)
)
alarmStatusEntry.setIndexNames(
    (0, "WESTERMO-WEOS-MIB", "alarmStatusTriggerId"),
)
if mibBuilder.loadTexts:
    alarmStatusEntry.setStatus("current")


class _AlarmStatusTriggerId_Type(Integer32):
    """Custom type alarmStatusTriggerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmStatusTriggerId_Type.__name__ = "Integer32"
_AlarmStatusTriggerId_Object = MibTableColumn
alarmStatusTriggerId = _AlarmStatusTriggerId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2, 4, 1, 1),
    _AlarmStatusTriggerId_Type()
)
alarmStatusTriggerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusTriggerId.setStatus("current")


class _AlarmStatusTriggerType_Type(DisplayString):
    """Custom type alarmStatusTriggerType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmStatusTriggerType_Type.__name__ = "DisplayString"
_AlarmStatusTriggerType_Object = MibTableColumn
alarmStatusTriggerType = _AlarmStatusTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2, 4, 1, 2),
    _AlarmStatusTriggerType_Type()
)
alarmStatusTriggerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusTriggerType.setStatus("current")
_AlarmStatusTriggerEnabled_Type = TruthValue
_AlarmStatusTriggerEnabled_Object = MibTableColumn
alarmStatusTriggerEnabled = _AlarmStatusTriggerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2, 4, 1, 3),
    _AlarmStatusTriggerEnabled_Type()
)
alarmStatusTriggerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusTriggerEnabled.setStatus("current")


class _AlarmStatusTriggerStatus_Type(Integer32):
    """Custom type alarmStatusTriggerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("ok", 2))
    )


_AlarmStatusTriggerStatus_Type.__name__ = "Integer32"
_AlarmStatusTriggerStatus_Object = MibTableColumn
alarmStatusTriggerStatus = _AlarmStatusTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2, 4, 1, 4),
    _AlarmStatusTriggerStatus_Type()
)
alarmStatusTriggerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusTriggerStatus.setStatus("current")


class _AlarmStatusTriggerStatusReason_Type(DisplayString):
    """Custom type alarmStatusTriggerStatusReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmStatusTriggerStatusReason_Type.__name__ = "DisplayString"
_AlarmStatusTriggerStatusReason_Object = MibTableColumn
alarmStatusTriggerStatusReason = _AlarmStatusTriggerStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 2, 4, 1, 5),
    _AlarmStatusTriggerStatusReason_Type()
)
alarmStatusTriggerStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusTriggerStatusReason.setStatus("current")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 3)
)
_MemoryAvail_Type = Integer32
_MemoryAvail_Object = MibScalar
memoryAvail = _MemoryAvail_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 3, 1),
    _MemoryAvail_Type()
)
memoryAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAvail.setStatus("current")
_CpuLoadAvg_ObjectIdentity = ObjectIdentity
cpuLoadAvg = _CpuLoadAvg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 3, 2)
)
_LoadAvg1_Type = Integer32
_LoadAvg1_Object = MibScalar
loadAvg1 = _LoadAvg1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 3, 2, 1),
    _LoadAvg1_Type()
)
loadAvg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadAvg1.setStatus("current")
_LoadAvg5_Type = Integer32
_LoadAvg5_Object = MibScalar
loadAvg5 = _LoadAvg5_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 3, 2, 2),
    _LoadAvg5_Type()
)
loadAvg5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadAvg5.setStatus("current")
_LoadAvg15_Type = Integer32
_LoadAvg15_Object = MibScalar
loadAvg15 = _LoadAvg15_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 3, 2, 3),
    _LoadAvg15_Type()
)
loadAvg15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadAvg15.setStatus("current")
_Integrity_ObjectIdentity = ObjectIdentity
integrity = _Integrity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 4)
)
_StartupConfigurationHash_Type = DisplayString
_StartupConfigurationHash_Object = MibScalar
startupConfigurationHash = _StartupConfigurationHash_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 4, 1),
    _StartupConfigurationHash_Type()
)
startupConfigurationHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startupConfigurationHash.setStatus("current")
_RunningConfigurationHash_Type = DisplayString
_RunningConfigurationHash_Object = MibScalar
runningConfigurationHash = _RunningConfigurationHash_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 5, 4, 2),
    _RunningConfigurationHash_Type()
)
runningConfigurationHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runningConfigurationHash.setStatus("current")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6)
)
_SensorNotifications_ObjectIdentity = ObjectIdentity
sensorNotifications = _SensorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 1)
)
_SensorNotificationPrefix_ObjectIdentity = ObjectIdentity
sensorNotificationPrefix = _SensorNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 1, 0)
)
_FrntNotifications_ObjectIdentity = ObjectIdentity
frntNotifications = _FrntNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 2)
)
_FrntNotificationPrefix_ObjectIdentity = ObjectIdentity
frntNotificationPrefix = _FrntNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 2, 0)
)
_LffNotifications_ObjectIdentity = ObjectIdentity
lffNotifications = _LffNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 3)
)
_LffNotificationPrefix_ObjectIdentity = ObjectIdentity
lffNotificationPrefix = _LffNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 3, 0)
)
_GenericNotifications_ObjectIdentity = ObjectIdentity
genericNotifications = _GenericNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 4)
)
_GenericNotificationPrefix_ObjectIdentity = ObjectIdentity
genericNotificationPrefix = _GenericNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 4, 0)
)
_DdmNotifications_ObjectIdentity = ObjectIdentity
ddmNotifications = _DdmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5)
)
_DdmNotificationPrefix_ObjectIdentity = ObjectIdentity
ddmNotificationPrefix = _DdmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0)
)
_ConflictNotifications_ObjectIdentity = ObjectIdentity
conflictNotifications = _ConflictNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 6)
)
_ConflictNotificationPrefix_ObjectIdentity = ObjectIdentity
conflictNotificationPrefix = _ConflictNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 6, 0)
)
_OtherNotifications_ObjectIdentity = ObjectIdentity
otherNotifications = _OtherNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 7)
)
_OtherNotificationPrefix_ObjectIdentity = ObjectIdentity
otherNotificationPrefix = _OtherNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 7, 0)
)
_RiCoNotifications_ObjectIdentity = ObjectIdentity
riCoNotifications = _RiCoNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 8)
)
_RiCoNotificationPrefix_ObjectIdentity = ObjectIdentity
riCoNotificationPrefix = _RiCoNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 8, 0)
)
_PingNotifications_ObjectIdentity = ObjectIdentity
pingNotifications = _PingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 9)
)
_PingNotificationPrefix_ObjectIdentity = ObjectIdentity
pingNotificationPrefix = _PingNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 9, 0)
)

# Managed Objects groups


# Notification objects

digitalInHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 1, 0, 1)
)
digitalInHigh.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"))
)
if mibBuilder.loadTexts:
    digitalInHigh.setStatus(
        "current"
    )

digitalInLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 1, 0, 2)
)
digitalInLow.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"))
)
if mibBuilder.loadTexts:
    digitalInLow.setStatus(
        "current"
    )

powerSupplyHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 1, 0, 3)
)
powerSupplyHigh.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"))
)
if mibBuilder.loadTexts:
    powerSupplyHigh.setStatus(
        "current"
    )

powerSupplyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 1, 0, 4)
)
powerSupplyLow.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"))
)
if mibBuilder.loadTexts:
    powerSupplyLow.setStatus(
        "current"
    )

temperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 1, 0, 5)
)
temperatureHigh.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorType"),
        ("ENTITY-SENSOR-MIB", "entPhySensorScale"),
        ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"))
)
if mibBuilder.loadTexts:
    temperatureHigh.setStatus(
        "current"
    )

temperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 1, 0, 6)
)
temperatureLow.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("ENTITY-SENSOR-MIB", "entPhySensorType"),
        ("ENTITY-SENSOR-MIB", "entPhySensorScale"),
        ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"))
)
if mibBuilder.loadTexts:
    temperatureLow.setStatus(
        "current"
    )

frntv0RingUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 2, 0, 1)
)
frntv0RingUp.setObjects(
      *(("WESTERMO-WEOS-MIB", "frntv0InstanceId"),
        ("WESTERMO-WEOS-MIB", "frntv0FocalPointEnabled"),
        ("WESTERMO-WEOS-MIB", "frntv0RingStatus"),
        ("WESTERMO-WEOS-MIB", "frntv0Port1"),
        ("WESTERMO-WEOS-MIB", "frntv0Port1State"),
        ("WESTERMO-WEOS-MIB", "frntv0Port2"),
        ("WESTERMO-WEOS-MIB", "frntv0Port2State"))
)
if mibBuilder.loadTexts:
    frntv0RingUp.setStatus(
        "current"
    )

frntv0RingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 2, 0, 2)
)
frntv0RingDown.setObjects(
      *(("WESTERMO-WEOS-MIB", "frntv0InstanceId"),
        ("WESTERMO-WEOS-MIB", "frntv0FocalPointEnabled"),
        ("WESTERMO-WEOS-MIB", "frntv0RingStatus"),
        ("WESTERMO-WEOS-MIB", "frntv0Port1"),
        ("WESTERMO-WEOS-MIB", "frntv0Port1State"),
        ("WESTERMO-WEOS-MIB", "frntv0Port2"),
        ("WESTERMO-WEOS-MIB", "frntv0Port2State"))
)
if mibBuilder.loadTexts:
    frntv0RingDown.setStatus(
        "current"
    )

lffRemoteUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 3, 0, 1)
)
lffRemoteUp.setObjects(
      *(("WESTERMO-WEOS-MIB", "lffPortIfName"),
        ("WESTERMO-WEOS-MIB", "lffStatus"))
)
if mibBuilder.loadTexts:
    lffRemoteUp.setStatus(
        "current"
    )

lffRemoteFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 3, 0, 2)
)
lffRemoteFail.setObjects(
      *(("WESTERMO-WEOS-MIB", "lffPortIfName"),
        ("WESTERMO-WEOS-MIB", "lffStatus"))
)
if mibBuilder.loadTexts:
    lffRemoteFail.setStatus(
        "current"
    )

summaryStatusOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 4, 0, 1)
)
summaryStatusOK.setObjects(
    ("WESTERMO-WEOS-MIB", "summaryAlarmStatus")
)
if mibBuilder.loadTexts:
    summaryStatusOK.setStatus(
        "current"
    )

summaryStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 4, 0, 2)
)
summaryStatusWarning.setObjects(
    ("WESTERMO-WEOS-MIB", "summaryAlarmStatus")
)
if mibBuilder.loadTexts:
    summaryStatusWarning.setStatus(
        "current"
    )

ddmVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0, 1)
)
ddmVoltageHigh.setObjects(
      *(("WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortIfName"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortVoltage"))
)
if mibBuilder.loadTexts:
    ddmVoltageHigh.setStatus(
        "current"
    )

ddmVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0, 2)
)
ddmVoltageLow.setObjects(
      *(("WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortIfName"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortVoltage"))
)
if mibBuilder.loadTexts:
    ddmVoltageLow.setStatus(
        "current"
    )

ddmTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0, 3)
)
ddmTemperatureHigh.setObjects(
      *(("WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortIfName"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortTemperature"))
)
if mibBuilder.loadTexts:
    ddmTemperatureHigh.setStatus(
        "current"
    )

ddmTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0, 4)
)
ddmTemperatureLow.setObjects(
      *(("WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortIfName"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortTemperature"))
)
if mibBuilder.loadTexts:
    ddmTemperatureLow.setStatus(
        "current"
    )

ddmBiasCurrentHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0, 5)
)
ddmBiasCurrentHigh.setObjects(
      *(("WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortIfName"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortBiasCurrent"))
)
if mibBuilder.loadTexts:
    ddmBiasCurrentHigh.setStatus(
        "current"
    )

ddmBiasCurrentLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0, 6)
)
ddmBiasCurrentLow.setObjects(
      *(("WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortIfName"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortBiasCurrent"))
)
if mibBuilder.loadTexts:
    ddmBiasCurrentLow.setStatus(
        "current"
    )

ddmTxPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0, 7)
)
ddmTxPowerHigh.setObjects(
      *(("WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortIfName"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortTxPower"))
)
if mibBuilder.loadTexts:
    ddmTxPowerHigh.setStatus(
        "current"
    )

ddmTxPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0, 8)
)
ddmTxPowerLow.setObjects(
      *(("WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortIfName"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortTxPower"))
)
if mibBuilder.loadTexts:
    ddmTxPowerLow.setStatus(
        "current"
    )

ddmRxPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0, 9)
)
ddmRxPowerHigh.setObjects(
      *(("WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortIfName"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortRxPower"))
)
if mibBuilder.loadTexts:
    ddmRxPowerHigh.setStatus(
        "current"
    )

ddmRxPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 5, 0, 10)
)
ddmRxPowerLow.setObjects(
      *(("WESTERMO-WEOS-MIB", "sfpDdmPortIfIndex"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortIfName"),
        ("WESTERMO-WEOS-MIB", "sfpDdmPortRxPower"))
)
if mibBuilder.loadTexts:
    ddmRxPowerLow.setStatus(
        "current"
    )

addressConflictDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 6, 0, 1)
)
addressConflictDetected.setObjects(
      *(("WESTERMO-WEOS-MIB", "addressConflictIfIndex"),
        ("WESTERMO-WEOS-MIB", "addressConflictIfName"),
        ("WESTERMO-WEOS-MIB", "addressConflictType"),
        ("WESTERMO-WEOS-MIB", "addressConflictMacAddress"),
        ("WESTERMO-WEOS-MIB", "addressConflictIPv4Address"))
)
if mibBuilder.loadTexts:
    addressConflictDetected.setStatus(
        "current"
    )

addressConflictCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 6, 0, 2)
)
addressConflictCleared.setObjects(
      *(("WESTERMO-WEOS-MIB", "addressConflictIfIndex"),
        ("WESTERMO-WEOS-MIB", "addressConflictIfName"),
        ("WESTERMO-WEOS-MIB", "addressConflictType"),
        ("WESTERMO-WEOS-MIB", "addressConflictMacAddress"),
        ("WESTERMO-WEOS-MIB", "addressConflictIPv4Address"))
)
if mibBuilder.loadTexts:
    addressConflictCleared.setStatus(
        "current"
    )

addressConflictOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 6, 0, 3)
)
addressConflictOK.setObjects(
    ("WESTERMO-WEOS-MIB", "addressConflictExists")
)
if mibBuilder.loadTexts:
    addressConflictOK.setStatus(
        "current"
    )

addressConflictWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 6, 0, 4)
)
addressConflictWarning.setObjects(
    ("WESTERMO-WEOS-MIB", "addressConflictExists")
)
if mibBuilder.loadTexts:
    addressConflictWarning.setStatus(
        "current"
    )

mrpRingClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 7, 0, 3)
)
mrpRingClosed.setObjects(
    ("WESTERMO-WEOS-MIB", "alarmStatusTriggerId")
)
if mibBuilder.loadTexts:
    mrpRingClosed.setStatus(
        "current"
    )

mrpRingOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 7, 0, 4)
)
mrpRingOpen.setObjects(
    ("WESTERMO-WEOS-MIB", "alarmStatusTriggerId")
)
if mibBuilder.loadTexts:
    mrpRingOpen.setStatus(
        "current"
    )

riCoUplinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 8, 0, 1)
)
riCoUplinkUp.setObjects(
      *(("WESTERMO-WEOS-MIB", "riCoStatusUplinkNodeId"),
        ("WESTERMO-WEOS-MIB", "riCoStatusUplinkIfIndex"),
        ("WESTERMO-WEOS-MIB", "riCoStatusUplinkIfName"),
        ("WESTERMO-WEOS-MIB", "riCoStatusUplinkStatus"))
)
if mibBuilder.loadTexts:
    riCoUplinkUp.setStatus(
        "current"
    )

riCoUplinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 8, 0, 2)
)
riCoUplinkDown.setObjects(
      *(("WESTERMO-WEOS-MIB", "riCoStatusUplinkNodeId"),
        ("WESTERMO-WEOS-MIB", "riCoStatusUplinkIfIndex"),
        ("WESTERMO-WEOS-MIB", "riCoStatusUplinkIfName"),
        ("WESTERMO-WEOS-MIB", "riCoStatusUplinkStatus"))
)
if mibBuilder.loadTexts:
    riCoUplinkDown.setStatus(
        "current"
    )

pingTriggerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 9, 0, 1)
)
pingTriggerOk.setObjects(
    ("WESTERMO-WEOS-MIB", "alarmStatusTriggerId")
)
if mibBuilder.loadTexts:
    pingTriggerOk.setStatus(
        "current"
    )

pingTriggerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 9, 0, 2)
)
pingTriggerWarning.setObjects(
    ("WESTERMO-WEOS-MIB", "alarmStatusTriggerId")
)
if mibBuilder.loadTexts:
    pingTriggerWarning.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-WEOS-MIB",
    **{"weos": weos,
       "command": command,
       "reboot": reboot,
       "factoryReset": factoryReset,
       "phy": phy,
       "lffTable": lffTable,
       "lffEntry": lffEntry,
       "lffPortIfIndex": lffPortIfIndex,
       "lffPortIfName": lffPortIfName,
       "lffStatus": lffStatus,
       "sfp": sfp,
       "sfpDdmPortTable": sfpDdmPortTable,
       "sfpDdmPortEntry": sfpDdmPortEntry,
       "sfpDdmPortIfIndex": sfpDdmPortIfIndex,
       "sfpDdmPortIfName": sfpDdmPortIfName,
       "sfpDdmPortVoltage": sfpDdmPortVoltage,
       "sfpDdmPortTemperature": sfpDdmPortTemperature,
       "sfpDdmPortBiasCurrent": sfpDdmPortBiasCurrent,
       "sfpDdmPortTxPower": sfpDdmPortTxPower,
       "sfpDdmPortRxPower": sfpDdmPortRxPower,
       "phyStats": phyStats,
       "summaryFCSErrors": summaryFCSErrors,
       "bwStatsTable": bwStatsTable,
       "bwStatsEntry": bwStatsEntry,
       "bwStatsIndex": bwStatsIndex,
       "bwStatsEnabled": bwStatsEnabled,
       "bwStatsBitrateIn10s": bwStatsBitrateIn10s,
       "bwStatsBitrateOut10s": bwStatsBitrateOut10s,
       "bwStatsBitrateIn1m": bwStatsBitrateIn1m,
       "bwStatsBitrateOut1m": bwStatsBitrateOut1m,
       "bwStatsBitrateIn10m": bwStatsBitrateIn10m,
       "bwStatsBitrateOut10m": bwStatsBitrateOut10m,
       "bwStatsBitrateIn1h": bwStatsBitrateIn1h,
       "bwStatsBitrateOut1h": bwStatsBitrateOut1h,
       "link": link,
       "vlan": vlan,
       "l2Qos": l2Qos,
       "l2QosVlanTable": l2QosVlanTable,
       "l2QosVlanEntry": l2QosVlanEntry,
       "l2QosVlanId": l2QosVlanId,
       "vlanPriorityEnabled": vlanPriorityEnabled,
       "vlanPriorityLevel": vlanPriorityLevel,
       "l2QosPortTable": l2QosPortTable,
       "l2QosPortEntry": l2QosPortEntry,
       "l2QosPortIfIndex": l2QosPortIfIndex,
       "l2QosPortIfName": l2QosPortIfName,
       "l2QosPortPriorityMode": l2QosPortPriorityMode,
       "l2QosPortPriorityLevel": l2QosPortPriorityLevel,
       "frnt": frnt,
       "frntv0": frntv0,
       "frntv0Table": frntv0Table,
       "frntv0Entry": frntv0Entry,
       "frntv0InstanceId": frntv0InstanceId,
       "frntv0FocalPointEnabled": frntv0FocalPointEnabled,
       "frntv0Port1": frntv0Port1,
       "frntv0Port2": frntv0Port2,
       "frntv0Port1State": frntv0Port1State,
       "frntv0Port2State": frntv0Port2State,
       "frntv0RingStatus": frntv0RingStatus,
       "frntv0RowStatus": frntv0RowStatus,
       "frntv0TopologyChangeCount": frntv0TopologyChangeCount,
       "frntv0TopologyTimeSinceLastChange": frntv0TopologyTimeSinceLastChange,
       "frntv0PortsSwapped": frntv0PortsSwapped,
       "igmpSnooping": igmpSnooping,
       "igmpSnoopingQuerierMode": igmpSnoopingQuerierMode,
       "igmpSnoopingQuerierInterval": igmpSnoopingQuerierInterval,
       "staticMulticastRouterPorts": staticMulticastRouterPorts,
       "currentMulticastRouterPorts": currentMulticastRouterPorts,
       "igmpSnoopingVlanTable": igmpSnoopingVlanTable,
       "igmpSnoopingVlanEntry": igmpSnoopingVlanEntry,
       "igmpSnoopingVlanId": igmpSnoopingVlanId,
       "igmpSnoopingEnabled": igmpSnoopingEnabled,
       "rico": rico,
       "riCoStatusTable": riCoStatusTable,
       "riCoStatusEntry": riCoStatusEntry,
       "riCoStatusRingIdx": riCoStatusRingIdx,
       "riCoStatusCouplingIdx": riCoStatusCouplingIdx,
       "riCoStatusNodeId": riCoStatusNodeId,
       "riCoStatusHelloInterval": riCoStatusHelloInterval,
       "riCoStatusHelloEffective": riCoStatusHelloEffective,
       "riCoStatusUplinkTable": riCoStatusUplinkTable,
       "riCoStatusUplinkEntry": riCoStatusUplinkEntry,
       "riCoStatusUplinkRingIdx": riCoStatusUplinkRingIdx,
       "riCoStatusUplinkCouplingIdx": riCoStatusUplinkCouplingIdx,
       "riCoStatusUplinkNodeId": riCoStatusUplinkNodeId,
       "riCoStatusUplinkIfIndex": riCoStatusUplinkIfIndex,
       "riCoStatusUplinkStatus": riCoStatusUplinkStatus,
       "riCoStatusUplinkIfName": riCoStatusUplinkIfName,
       "riCoStatusUplinkPrio": riCoStatusUplinkPrio,
       "riCoStatusUplinkPathCost": riCoStatusUplinkPathCost,
       "riCoStatusUplinkHelloInterval": riCoStatusUplinkHelloInterval,
       "riCoStatusUplinkHelloIntervalEffective": riCoStatusUplinkHelloIntervalEffective,
       "riCoStatusUplinkChangedCounter": riCoStatusUplinkChangedCounter,
       "riCoStatusUplinkSynchronized": riCoStatusUplinkSynchronized,
       "riCoStatusUplinkPreferred": riCoStatusUplinkPreferred,
       "riCoStatusUplinkLocal": riCoStatusUplinkLocal,
       "riCoCfgTable": riCoCfgTable,
       "riCoCfgEntry": riCoCfgEntry,
       "riCoCfgRingIdx": riCoCfgRingIdx,
       "riCoCfgCouplingIdx": riCoCfgCouplingIdx,
       "riCoCfgEnabled": riCoCfgEnabled,
       "riCoCfgHelloInterval": riCoCfgHelloInterval,
       "riCoCfgSynchronize": riCoCfgSynchronize,
       "riCoCfgRowStatus": riCoCfgRowStatus,
       "riCoCfgUplinkTable": riCoCfgUplinkTable,
       "riCoCfgUplinkEntry": riCoCfgUplinkEntry,
       "riCoCfgUplinkRingIdx": riCoCfgUplinkRingIdx,
       "riCoCfgUplinkCouplingIdx": riCoCfgUplinkCouplingIdx,
       "riCoCfgUplinkIfIndex": riCoCfgUplinkIfIndex,
       "riCoCfgUplinkPrio": riCoCfgUplinkPrio,
       "riCoCfgUplinkAdjust": riCoCfgUplinkAdjust,
       "riCoCfgUplinkEchoTime": riCoCfgUplinkEchoTime,
       "riCoCfgUplinkPathCost": riCoCfgUplinkPathCost,
       "riCoCfgUplinkRowStatus": riCoCfgUplinkRowStatus,
       "lldpCtlv": lldpCtlv,
       "lldpCtlvTable": lldpCtlvTable,
       "lldpCtlvEntry": lldpCtlvEntry,
       "lldpCtlvIdx": lldpCtlvIdx,
       "lldpCtlvOui": lldpCtlvOui,
       "lldpCtlvSubType": lldpCtlvSubType,
       "lldpCtlvInfo": lldpCtlvInfo,
       "lldpCtlvRowStatus": lldpCtlvRowStatus,
       "lldpCtlvPortTable": lldpCtlvPortTable,
       "lldpCtlvPortEntry": lldpCtlvPortEntry,
       "lldpCtlvPortIdx": lldpCtlvPortIdx,
       "lldpCtlvPortCtlvIdx": lldpCtlvPortCtlvIdx,
       "lldpCtlvPortRowStatus": lldpCtlvPortRowStatus,
       "lldpRemCtlvTable": lldpRemCtlvTable,
       "lldpRemCtlvEntry": lldpRemCtlvEntry,
       "lldpRemCtlvLocalPort": lldpRemCtlvLocalPort,
       "lldpRemCtlvMacAddress": lldpRemCtlvMacAddress,
       "lldpRemCtlvOui": lldpRemCtlvOui,
       "lldpRemCtlvSubType": lldpRemCtlvSubType,
       "lldpRemCtlvInfo": lldpRemCtlvInfo,
       "net": net,
       "iface": iface,
       "ifaceCommon": ifaceCommon,
       "ifaceInet4": ifaceInet4,
       "inet4StaticDefaultGatewayAddress": inet4StaticDefaultGatewayAddress,
       "inet4BaseIfaceTable": inet4BaseIfaceTable,
       "inet4BaseIfaceEntry": inet4BaseIfaceEntry,
       "inet4BaseIfIndex": inet4BaseIfIndex,
       "inet4BaseIfName": inet4BaseIfName,
       "inet4BaseAddressMode": inet4BaseAddressMode,
       "inet4StaticTable": inet4StaticTable,
       "inet4StaticEntry": inet4StaticEntry,
       "inet4StatIfIndex": inet4StatIfIndex,
       "inet4StatIfName": inet4StatIfName,
       "inet4StatAddress": inet4StatAddress,
       "inet4StatNetmask": inet4StatNetmask,
       "inet4DhcpTable": inet4DhcpTable,
       "inet4DhcpEntry": inet4DhcpEntry,
       "inet4DhcpIfIndex": inet4DhcpIfIndex,
       "inet4DhcpIfName": inet4DhcpIfName,
       "inet4DhcpClientId": inet4DhcpClientId,
       "addressConflict": addressConflict,
       "addressConflictExists": addressConflictExists,
       "addressConflictTable": addressConflictTable,
       "addressConflictEntry": addressConflictEntry,
       "addressConflictIndex": addressConflictIndex,
       "addressConflictIfIndex": addressConflictIfIndex,
       "addressConflictIfName": addressConflictIfName,
       "addressConflictType": addressConflictType,
       "addressConflictMacAddress": addressConflictMacAddress,
       "addressConflictIPv4Address": addressConflictIPv4Address,
       "addressConflictTime": addressConflictTime,
       "ttdp": ttdp,
       "etbnInhibitionEnabled": etbnInhibitionEnabled,
       "system": system,
       "services": services,
       "snmp": snmp,
       "trapCommunity": trapCommunity,
       "trapHostTable": trapHostTable,
       "trapHostEntry": trapHostEntry,
       "trapHostId": trapHostId,
       "trapHostAddressType": trapHostAddressType,
       "trapHostAddress": trapHostAddress,
       "trapHostRowStatus": trapHostRowStatus,
       "roCommunity": roCommunity,
       "rwCommunity": rwCommunity,
       "web": web,
       "webEnabled": webEnabled,
       "ipconfig": ipconfig,
       "ipconfigEnabled": ipconfigEnabled,
       "ssh": ssh,
       "sshEnabled": sshEnabled,
       "lldp": lldp,
       "lldpEnabled": lldpEnabled,
       "lldpActivated": lldpActivated,
       "eventSystem": eventSystem,
       "summaryAlarmStatus": summaryAlarmStatus,
       "summaryAlarmTrapEnabled": summaryAlarmTrapEnabled,
       "statusRelay": statusRelay,
       "alarmStatusTable": alarmStatusTable,
       "alarmStatusEntry": alarmStatusEntry,
       "alarmStatusTriggerId": alarmStatusTriggerId,
       "alarmStatusTriggerType": alarmStatusTriggerType,
       "alarmStatusTriggerEnabled": alarmStatusTriggerEnabled,
       "alarmStatusTriggerStatus": alarmStatusTriggerStatus,
       "alarmStatusTriggerStatusReason": alarmStatusTriggerStatusReason,
       "statistics": statistics,
       "memoryAvail": memoryAvail,
       "cpuLoadAvg": cpuLoadAvg,
       "loadAvg1": loadAvg1,
       "loadAvg5": loadAvg5,
       "loadAvg15": loadAvg15,
       "integrity": integrity,
       "startupConfigurationHash": startupConfigurationHash,
       "runningConfigurationHash": runningConfigurationHash,
       "notifications": notifications,
       "sensorNotifications": sensorNotifications,
       "sensorNotificationPrefix": sensorNotificationPrefix,
       "digitalInHigh": digitalInHigh,
       "digitalInLow": digitalInLow,
       "powerSupplyHigh": powerSupplyHigh,
       "powerSupplyLow": powerSupplyLow,
       "temperatureHigh": temperatureHigh,
       "temperatureLow": temperatureLow,
       "frntNotifications": frntNotifications,
       "frntNotificationPrefix": frntNotificationPrefix,
       "frntv0RingUp": frntv0RingUp,
       "frntv0RingDown": frntv0RingDown,
       "lffNotifications": lffNotifications,
       "lffNotificationPrefix": lffNotificationPrefix,
       "lffRemoteUp": lffRemoteUp,
       "lffRemoteFail": lffRemoteFail,
       "genericNotifications": genericNotifications,
       "genericNotificationPrefix": genericNotificationPrefix,
       "summaryStatusOK": summaryStatusOK,
       "summaryStatusWarning": summaryStatusWarning,
       "ddmNotifications": ddmNotifications,
       "ddmNotificationPrefix": ddmNotificationPrefix,
       "ddmVoltageHigh": ddmVoltageHigh,
       "ddmVoltageLow": ddmVoltageLow,
       "ddmTemperatureHigh": ddmTemperatureHigh,
       "ddmTemperatureLow": ddmTemperatureLow,
       "ddmBiasCurrentHigh": ddmBiasCurrentHigh,
       "ddmBiasCurrentLow": ddmBiasCurrentLow,
       "ddmTxPowerHigh": ddmTxPowerHigh,
       "ddmTxPowerLow": ddmTxPowerLow,
       "ddmRxPowerHigh": ddmRxPowerHigh,
       "ddmRxPowerLow": ddmRxPowerLow,
       "conflictNotifications": conflictNotifications,
       "conflictNotificationPrefix": conflictNotificationPrefix,
       "addressConflictDetected": addressConflictDetected,
       "addressConflictCleared": addressConflictCleared,
       "addressConflictOK": addressConflictOK,
       "addressConflictWarning": addressConflictWarning,
       "otherNotifications": otherNotifications,
       "otherNotificationPrefix": otherNotificationPrefix,
       "mrpRingClosed": mrpRingClosed,
       "mrpRingOpen": mrpRingOpen,
       "riCoNotifications": riCoNotifications,
       "riCoNotificationPrefix": riCoNotificationPrefix,
       "riCoUplinkUp": riCoUplinkUp,
       "riCoUplinkDown": riCoUplinkDown,
       "pingNotifications": pingNotifications,
       "pingNotificationPrefix": pingNotificationPrefix,
       "pingTriggerOk": pingTriggerOk,
       "pingTriggerWarning": pingTriggerWarning}
)
