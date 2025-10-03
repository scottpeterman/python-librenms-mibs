# SNMP MIB module (DLINKSW-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-POE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:42 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(pethMainPseGroupIndex,
 pethPsePortIndex,
 pethPsePortOverLoadCounter,
 pethPsePortPowerDeniedCounter,
 pethPsePortShortCounter) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseGroupIndex",
    "pethPsePortIndex",
    "pethPsePortOverLoadCounter",
    "pethPsePortPowerDeniedCounter",
    "pethPsePortShortCounter")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwPoeExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 24)
)
if mibBuilder.loadTexts:
    dlinkSwPoeExtMIB.setRevisions(
        ("2013-05-29 00:00",
         "2013-09-24 00:00",
         "2017-03-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DPoeMIBNotifications_ObjectIdentity = ObjectIdentity
dPoeMIBNotifications = _DPoeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 0)
)
_DPoeMIBObjects_ObjectIdentity = ObjectIdentity
dPoeMIBObjects = _DPoeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1)
)
_DPoeGroupCfgTable_Object = MibTable
dPoeGroupCfgTable = _DPoeGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 1)
)
if mibBuilder.loadTexts:
    dPoeGroupCfgTable.setStatus("current")
_DPoeGroupCfgEntry_Object = MibTableRow
dPoeGroupCfgEntry = _DPoeGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 1, 1)
)
dPoeGroupCfgEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    dPoeGroupCfgEntry.setStatus("current")


class _DPoeGroupPolicyPreempt_Type(TruthValue):
    """Custom type dPoeGroupPolicyPreempt based on TruthValue"""
    defaultValue = 2


_DPoeGroupPolicyPreempt_Type.__name__ = "TruthValue"
_DPoeGroupPolicyPreempt_Object = MibTableColumn
dPoeGroupPolicyPreempt = _DPoeGroupPolicyPreempt_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 1, 1, 1),
    _DPoeGroupPolicyPreempt_Type()
)
dPoeGroupPolicyPreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeGroupPolicyPreempt.setStatus("current")
_DPoeGroupClearIfStatistic_Type = PortList
_DPoeGroupClearIfStatistic_Object = MibTableColumn
dPoeGroupClearIfStatistic = _DPoeGroupClearIfStatistic_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 1, 1, 2),
    _DPoeGroupClearIfStatistic_Type()
)
dPoeGroupClearIfStatistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeGroupClearIfStatistic.setStatus("current")


class _DPoeGroupIfLedMode_Type(Integer32):
    """Custom type dPoeGroupIfLedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("poeMode", 1),
          ("linkMode", 2),
          ("invalid", 3))
    )


_DPoeGroupIfLedMode_Type.__name__ = "Integer32"
_DPoeGroupIfLedMode_Object = MibTableColumn
dPoeGroupIfLedMode = _DPoeGroupIfLedMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 1, 1, 3),
    _DPoeGroupIfLedMode_Type()
)
dPoeGroupIfLedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeGroupIfLedMode.setStatus("current")
_DPoeGroupInfoTable_Object = MibTable
dPoeGroupInfoTable = _DPoeGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 2)
)
if mibBuilder.loadTexts:
    dPoeGroupInfoTable.setStatus("current")
_DPoeGroupInfoEntry_Object = MibTableRow
dPoeGroupInfoEntry = _DPoeGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 2, 1)
)
dPoeGroupInfoEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    dPoeGroupInfoEntry.setStatus("current")
_DPoeGroupMaxPorts_Type = Integer32
_DPoeGroupMaxPorts_Object = MibTableColumn
dPoeGroupMaxPorts = _DPoeGroupMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 2, 1, 1),
    _DPoeGroupMaxPorts_Type()
)
dPoeGroupMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPoeGroupMaxPorts.setStatus("current")
_DPoeGroupHWVersion_Type = DisplayString
_DPoeGroupHWVersion_Object = MibTableColumn
dPoeGroupHWVersion = _DPoeGroupHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 2, 1, 2),
    _DPoeGroupHWVersion_Type()
)
dPoeGroupHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPoeGroupHWVersion.setStatus("current")
_DPoeGroupSWVersion_Type = DisplayString
_DPoeGroupSWVersion_Object = MibTableColumn
dPoeGroupSWVersion = _DPoeGroupSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 2, 1, 3),
    _DPoeGroupSWVersion_Type()
)
dPoeGroupSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPoeGroupSWVersion.setStatus("current")
_DPoeIfObjects_ObjectIdentity = ObjectIdentity
dPoeIfObjects = _DPoeIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3)
)
_DPoeIfCfgTable_Object = MibTable
dPoeIfCfgTable = _DPoeIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dPoeIfCfgTable.setStatus("current")
_DPoeIfCfgEntry_Object = MibTableRow
dPoeIfCfgEntry = _DPoeIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 1, 1)
)
dPoeIfCfgEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    dPoeIfCfgEntry.setStatus("current")


class _DPoeIfState_Type(Integer32):
    """Custom type dPoeIfState based on Integer32"""
    defaultValue = 1

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
          ("never", 2),
          ("static", 3))
    )


_DPoeIfState_Type.__name__ = "Integer32"
_DPoeIfState_Object = MibTableColumn
dPoeIfState = _DPoeIfState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 1, 1, 1),
    _DPoeIfState_Type()
)
dPoeIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfState.setStatus("current")


class _DPoeIfMaxPower_Type(Integer32):
    """Custom type dPoeIfMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 30000),
    )


_DPoeIfMaxPower_Type.__name__ = "Integer32"
_DPoeIfMaxPower_Object = MibTableColumn
dPoeIfMaxPower = _DPoeIfMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 1, 1, 2),
    _DPoeIfMaxPower_Type()
)
dPoeIfMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    dPoeIfMaxPower.setUnits("milliwatts")


class _DPoeIfTimeRange_Type(DisplayString):
    """Custom type dPoeIfTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DPoeIfTimeRange_Type.__name__ = "DisplayString"
_DPoeIfTimeRange_Object = MibTableColumn
dPoeIfTimeRange = _DPoeIfTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 1, 1, 3),
    _DPoeIfTimeRange_Type()
)
dPoeIfTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfTimeRange.setStatus("current")


class _DPoeIfLegacyPdEnabled_Type(TruthValue):
    """Custom type dPoeIfLegacyPdEnabled based on TruthValue"""
    defaultValue = 2


_DPoeIfLegacyPdEnabled_Type.__name__ = "TruthValue"
_DPoeIfLegacyPdEnabled_Object = MibTableColumn
dPoeIfLegacyPdEnabled = _DPoeIfLegacyPdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 1, 1, 4),
    _DPoeIfLegacyPdEnabled_Type()
)
dPoeIfLegacyPdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfLegacyPdEnabled.setStatus("current")
_DPoeIfInfoObjects_ObjectIdentity = ObjectIdentity
dPoeIfInfoObjects = _DPoeIfInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2)
)
_DPoeIfStatusTable_Object = MibTable
dPoeIfStatusTable = _DPoeIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dPoeIfStatusTable.setStatus("current")
_DPoeIfStatusEntry_Object = MibTableRow
dPoeIfStatusEntry = _DPoeIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2, 1, 1)
)
dPoeIfStatusEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    dPoeIfStatusEntry.setStatus("current")


class _DPoeIfDetectStatus_Type(Integer32):
    """Custom type dPoeIfDetectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("searching", 2),
          ("requesting", 3),
          ("delivering", 4),
          ("faulty", 5))
    )


_DPoeIfDetectStatus_Type.__name__ = "Integer32"
_DPoeIfDetectStatus_Object = MibTableColumn
dPoeIfDetectStatus = _DPoeIfDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2, 1, 1, 1),
    _DPoeIfDetectStatus_Type()
)
dPoeIfDetectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPoeIfDetectStatus.setStatus("current")


class _DPoeIfFaultyType_Type(Integer32):
    """Custom type dPoeIfFaultyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("mpsAbsent", 1),
          ("pdShort", 2),
          ("overload", 3),
          ("powerDenied", 4),
          ("thermalShutdown", 5),
          ("startupFailure", 6),
          ("classificationFailure", 7))
    )


_DPoeIfFaultyType_Type.__name__ = "Integer32"
_DPoeIfFaultyType_Object = MibTableColumn
dPoeIfFaultyType = _DPoeIfFaultyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2, 1, 1, 2),
    _DPoeIfFaultyType_Type()
)
dPoeIfFaultyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPoeIfFaultyType.setStatus("current")
_DPoeIfMeasurementTable_Object = MibTable
dPoeIfMeasurementTable = _DPoeIfMeasurementTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    dPoeIfMeasurementTable.setStatus("current")
_DPoeIfMeasurementEntry_Object = MibTableRow
dPoeIfMeasurementEntry = _DPoeIfMeasurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2, 2, 1)
)
dPoeIfMeasurementEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    dPoeIfMeasurementEntry.setStatus("current")
_DPoeIfVoltage_Type = Integer32
_DPoeIfVoltage_Object = MibTableColumn
dPoeIfVoltage = _DPoeIfVoltage_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2, 2, 1, 1),
    _DPoeIfVoltage_Type()
)
dPoeIfVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPoeIfVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dPoeIfVoltage.setUnits("millivolts")
_DPoeIfCurrent_Type = Integer32
_DPoeIfCurrent_Object = MibTableColumn
dPoeIfCurrent = _DPoeIfCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2, 2, 1, 2),
    _DPoeIfCurrent_Type()
)
dPoeIfCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPoeIfCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dPoeIfCurrent.setUnits("milliamperes")
_DPoeIfTemperature_Type = Integer32
_DPoeIfTemperature_Object = MibTableColumn
dPoeIfTemperature = _DPoeIfTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2, 2, 1, 3),
    _DPoeIfTemperature_Type()
)
dPoeIfTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPoeIfTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dPoeIfTemperature.setUnits("Degree Centigrade")
_DPoeIfPower_Type = Integer32
_DPoeIfPower_Object = MibTableColumn
dPoeIfPower = _DPoeIfPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 2, 2, 1, 4),
    _DPoeIfPower_Type()
)
dPoeIfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPoeIfPower.setStatus("current")
_DPoeIfPdAliveCfgTable_Object = MibTable
dPoeIfPdAliveCfgTable = _DPoeIfPdAliveCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgTable.setStatus("current")
_DPoeIfPdAliveCfgEntry_Object = MibTableRow
dPoeIfPdAliveCfgEntry = _DPoeIfPdAliveCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 3, 1)
)
dPoeIfPdAliveCfgEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgEntry.setStatus("current")


class _DPoeIfPdAliveCfgState_Type(Integer32):
    """Custom type dPoeIfPdAliveCfgState based on Integer32"""
    defaultValue = 2

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


_DPoeIfPdAliveCfgState_Type.__name__ = "Integer32"
_DPoeIfPdAliveCfgState_Object = MibTableColumn
dPoeIfPdAliveCfgState = _DPoeIfPdAliveCfgState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 3, 1, 1),
    _DPoeIfPdAliveCfgState_Type()
)
dPoeIfPdAliveCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgState.setStatus("current")
_DPoeIfPdAliveCfgPdIpType_Type = InetAddressType
_DPoeIfPdAliveCfgPdIpType_Object = MibTableColumn
dPoeIfPdAliveCfgPdIpType = _DPoeIfPdAliveCfgPdIpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 3, 1, 2),
    _DPoeIfPdAliveCfgPdIpType_Type()
)
dPoeIfPdAliveCfgPdIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgPdIpType.setStatus("current")
_DPoeIfPdAliveCfgPdIpAddr_Type = InetAddress
_DPoeIfPdAliveCfgPdIpAddr_Object = MibTableColumn
dPoeIfPdAliveCfgPdIpAddr = _DPoeIfPdAliveCfgPdIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 3, 1, 3),
    _DPoeIfPdAliveCfgPdIpAddr_Type()
)
dPoeIfPdAliveCfgPdIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgPdIpAddr.setStatus("current")


class _DPoeIfPdAliveCfgInterval_Type(Unsigned32):
    """Custom type dPoeIfPdAliveCfgInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_DPoeIfPdAliveCfgInterval_Type.__name__ = "Unsigned32"
_DPoeIfPdAliveCfgInterval_Object = MibTableColumn
dPoeIfPdAliveCfgInterval = _DPoeIfPdAliveCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 3, 1, 4),
    _DPoeIfPdAliveCfgInterval_Type()
)
dPoeIfPdAliveCfgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgInterval.setStatus("current")
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgInterval.setUnits("seconds")


class _DPoeIfPdAliveCfgRetry_Type(Unsigned32):
    """Custom type dPoeIfPdAliveCfgRetry based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DPoeIfPdAliveCfgRetry_Type.__name__ = "Unsigned32"
_DPoeIfPdAliveCfgRetry_Object = MibTableColumn
dPoeIfPdAliveCfgRetry = _DPoeIfPdAliveCfgRetry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 3, 1, 5),
    _DPoeIfPdAliveCfgRetry_Type()
)
dPoeIfPdAliveCfgRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgRetry.setStatus("current")
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgRetry.setUnits("times")


class _DPoeIfPdAliveCfgWaitTime_Type(Unsigned32):
    """Custom type dPoeIfPdAliveCfgWaitTime based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_DPoeIfPdAliveCfgWaitTime_Type.__name__ = "Unsigned32"
_DPoeIfPdAliveCfgWaitTime_Object = MibTableColumn
dPoeIfPdAliveCfgWaitTime = _DPoeIfPdAliveCfgWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 3, 1, 6),
    _DPoeIfPdAliveCfgWaitTime_Type()
)
dPoeIfPdAliveCfgWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgWaitTime.setUnits("seconds")


class _DPoeIfPdAliveCfgAction_Type(Integer32):
    """Custom type dPoeIfPdAliveCfgAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("notify", 2),
          ("both", 3))
    )


_DPoeIfPdAliveCfgAction_Type.__name__ = "Integer32"
_DPoeIfPdAliveCfgAction_Object = MibTableColumn
dPoeIfPdAliveCfgAction = _DPoeIfPdAliveCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 1, 3, 3, 1, 7),
    _DPoeIfPdAliveCfgAction_Type()
)
dPoeIfPdAliveCfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgAction.setStatus("current")
_DPoeMIBConformance_ObjectIdentity = ObjectIdentity
dPoeMIBConformance = _DPoeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 2)
)
_DPoeMIBCompliances_ObjectIdentity = ObjectIdentity
dPoeMIBCompliances = _DPoeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 2, 1)
)
_DPoeMIBGroups_ObjectIdentity = ObjectIdentity
dPoeMIBGroups = _DPoeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 2, 2)
)

# Managed Objects groups

dPoeGroupCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 2, 2, 1)
)
dPoeGroupCfgGroup.setObjects(
      *(("DLINKSW-POE-MIB", "dPoeGroupPolicyPreempt"),
        ("DLINKSW-POE-MIB", "dPoeGroupIfLedMode"))
)
if mibBuilder.loadTexts:
    dPoeGroupCfgGroup.setStatus("current")

dPoeIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 2, 2, 2)
)
dPoeIfCfgGroup.setObjects(
      *(("DLINKSW-POE-MIB", "dPoeGroupClearIfStatistic"),
        ("DLINKSW-POE-MIB", "dPoeIfState"),
        ("DLINKSW-POE-MIB", "dPoeIfMaxPower"),
        ("DLINKSW-POE-MIB", "dPoeIfTimeRange"),
        ("DLINKSW-POE-MIB", "dPoeIfLegacyPdEnabled"))
)
if mibBuilder.loadTexts:
    dPoeIfCfgGroup.setStatus("current")

dPoeGroupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 2, 2, 3)
)
dPoeGroupInfoGroup.setObjects(
      *(("DLINKSW-POE-MIB", "dPoeGroupMaxPorts"),
        ("DLINKSW-POE-MIB", "dPoeGroupHWVersion"),
        ("DLINKSW-POE-MIB", "dPoeGroupSWVersion"))
)
if mibBuilder.loadTexts:
    dPoeGroupInfoGroup.setStatus("current")

dPoeIfInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 2, 2, 4)
)
dPoeIfInfoGroup.setObjects(
      *(("DLINKSW-POE-MIB", "dPoeIfDetectStatus"),
        ("DLINKSW-POE-MIB", "dPoeIfFaultyType"),
        ("DLINKSW-POE-MIB", "dPoeIfVoltage"),
        ("DLINKSW-POE-MIB", "dPoeIfCurrent"),
        ("DLINKSW-POE-MIB", "dPoeIfTemperature"),
        ("DLINKSW-POE-MIB", "dPoeIfPower"))
)
if mibBuilder.loadTexts:
    dPoeIfInfoGroup.setStatus("current")

dPoeIfPdAliveCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 2, 2, 6)
)
dPoeIfPdAliveCfgGroup.setObjects(
      *(("DLINKSW-POE-MIB", "dPoeIfPdAliveCfgState"),
        ("DLINKSW-POE-MIB", "dPoeIfPdAliveCfgPdIpType"),
        ("DLINKSW-POE-MIB", "dPoeIfPdAliveCfgPdIpAddr"),
        ("DLINKSW-POE-MIB", "dPoeIfPdAliveCfgInterval"),
        ("DLINKSW-POE-MIB", "dPoeIfPdAliveCfgRetry"),
        ("DLINKSW-POE-MIB", "dPoeIfPdAliveCfgWaitTime"),
        ("DLINKSW-POE-MIB", "dPoeIfPdAliveCfgAction"))
)
if mibBuilder.loadTexts:
    dPoeIfPdAliveCfgGroup.setStatus("current")


# Notification objects

dPoeIfPowerDeniedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 0, 1)
)
dPoeIfPowerDeniedNotification.setObjects(
    ("POWER-ETHERNET-MIB", "pethPsePortPowerDeniedCounter")
)
if mibBuilder.loadTexts:
    dPoeIfPowerDeniedNotification.setStatus(
        "current"
    )

dPoeIfPowerOverLoadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 0, 2)
)
dPoeIfPowerOverLoadNotification.setObjects(
    ("POWER-ETHERNET-MIB", "pethPsePortOverLoadCounter")
)
if mibBuilder.loadTexts:
    dPoeIfPowerOverLoadNotification.setStatus(
        "current"
    )

dPoeIfPowerShortCircuitNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 0, 3)
)
dPoeIfPowerShortCircuitNotification.setObjects(
    ("POWER-ETHERNET-MIB", "pethPsePortShortCounter")
)
if mibBuilder.loadTexts:
    dPoeIfPowerShortCircuitNotification.setStatus(
        "current"
    )

dPoeIfPdAliveFailOccurNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 0, 4)
)
dPoeIfPdAliveFailOccurNotification.setObjects(
      *(("POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
        ("POWER-ETHERNET-MIB", "pethPsePortIndex"),
        ("DLINKSW-POE-MIB", "dPoeIfPdAliveCfgPdIpType"),
        ("DLINKSW-POE-MIB", "dPoeIfPdAliveCfgPdIpAddr"))
)
if mibBuilder.loadTexts:
    dPoeIfPdAliveFailOccurNotification.setStatus(
        "current"
    )


# Notifications groups

dPoeIfErrorStateNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 2, 2, 5)
)
dPoeIfErrorStateNotificationGroup.setObjects(
      *(("DLINKSW-POE-MIB", "dPoeIfPowerDeniedNotification"),
        ("DLINKSW-POE-MIB", "dPoeIfPowerOverLoadNotification"),
        ("DLINKSW-POE-MIB", "dPoeIfPowerShortCircuitNotification"))
)
if mibBuilder.loadTexts:
    dPoeIfErrorStateNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dPoeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 24, 2, 1, 1)
)
dPoeMIBCompliance.setObjects(
      *(("DLINKSW-POE-MIB", "dPoeGroupCfgGroup"),
        ("DLINKSW-POE-MIB", "dPoeIfCfgGroup"),
        ("DLINKSW-POE-MIB", "dPoeGroupInfoGroup"),
        ("DLINKSW-POE-MIB", "dPoeIfInfoGroup"),
        ("DLINKSW-POE-MIB", "dPoeIfErrorStateNotificationGroup"),
        ("DLINKSW-POE-MIB", "dPoeIfPdAliveCfgGroup"))
)
if mibBuilder.loadTexts:
    dPoeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-POE-MIB",
    **{"dlinkSwPoeExtMIB": dlinkSwPoeExtMIB,
       "dPoeMIBNotifications": dPoeMIBNotifications,
       "dPoeIfPowerDeniedNotification": dPoeIfPowerDeniedNotification,
       "dPoeIfPowerOverLoadNotification": dPoeIfPowerOverLoadNotification,
       "dPoeIfPowerShortCircuitNotification": dPoeIfPowerShortCircuitNotification,
       "dPoeIfPdAliveFailOccurNotification": dPoeIfPdAliveFailOccurNotification,
       "dPoeMIBObjects": dPoeMIBObjects,
       "dPoeGroupCfgTable": dPoeGroupCfgTable,
       "dPoeGroupCfgEntry": dPoeGroupCfgEntry,
       "dPoeGroupPolicyPreempt": dPoeGroupPolicyPreempt,
       "dPoeGroupClearIfStatistic": dPoeGroupClearIfStatistic,
       "dPoeGroupIfLedMode": dPoeGroupIfLedMode,
       "dPoeGroupInfoTable": dPoeGroupInfoTable,
       "dPoeGroupInfoEntry": dPoeGroupInfoEntry,
       "dPoeGroupMaxPorts": dPoeGroupMaxPorts,
       "dPoeGroupHWVersion": dPoeGroupHWVersion,
       "dPoeGroupSWVersion": dPoeGroupSWVersion,
       "dPoeIfObjects": dPoeIfObjects,
       "dPoeIfCfgTable": dPoeIfCfgTable,
       "dPoeIfCfgEntry": dPoeIfCfgEntry,
       "dPoeIfState": dPoeIfState,
       "dPoeIfMaxPower": dPoeIfMaxPower,
       "dPoeIfTimeRange": dPoeIfTimeRange,
       "dPoeIfLegacyPdEnabled": dPoeIfLegacyPdEnabled,
       "dPoeIfInfoObjects": dPoeIfInfoObjects,
       "dPoeIfStatusTable": dPoeIfStatusTable,
       "dPoeIfStatusEntry": dPoeIfStatusEntry,
       "dPoeIfDetectStatus": dPoeIfDetectStatus,
       "dPoeIfFaultyType": dPoeIfFaultyType,
       "dPoeIfMeasurementTable": dPoeIfMeasurementTable,
       "dPoeIfMeasurementEntry": dPoeIfMeasurementEntry,
       "dPoeIfVoltage": dPoeIfVoltage,
       "dPoeIfCurrent": dPoeIfCurrent,
       "dPoeIfTemperature": dPoeIfTemperature,
       "dPoeIfPower": dPoeIfPower,
       "dPoeIfPdAliveCfgTable": dPoeIfPdAliveCfgTable,
       "dPoeIfPdAliveCfgEntry": dPoeIfPdAliveCfgEntry,
       "dPoeIfPdAliveCfgState": dPoeIfPdAliveCfgState,
       "dPoeIfPdAliveCfgPdIpType": dPoeIfPdAliveCfgPdIpType,
       "dPoeIfPdAliveCfgPdIpAddr": dPoeIfPdAliveCfgPdIpAddr,
       "dPoeIfPdAliveCfgInterval": dPoeIfPdAliveCfgInterval,
       "dPoeIfPdAliveCfgRetry": dPoeIfPdAliveCfgRetry,
       "dPoeIfPdAliveCfgWaitTime": dPoeIfPdAliveCfgWaitTime,
       "dPoeIfPdAliveCfgAction": dPoeIfPdAliveCfgAction,
       "dPoeMIBConformance": dPoeMIBConformance,
       "dPoeMIBCompliances": dPoeMIBCompliances,
       "dPoeMIBCompliance": dPoeMIBCompliance,
       "dPoeMIBGroups": dPoeMIBGroups,
       "dPoeGroupCfgGroup": dPoeGroupCfgGroup,
       "dPoeIfCfgGroup": dPoeIfCfgGroup,
       "dPoeGroupInfoGroup": dPoeGroupInfoGroup,
       "dPoeIfInfoGroup": dPoeIfInfoGroup,
       "dPoeIfErrorStateNotificationGroup": dPoeIfErrorStateNotificationGroup,
       "dPoeIfPdAliveCfgGroup": dPoeIfPdAliveCfgGroup}
)
