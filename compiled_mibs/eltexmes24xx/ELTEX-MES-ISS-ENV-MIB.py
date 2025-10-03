# SNMP MIB module (ELTEX-MES-ISS-ENV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eltexmes24xx\ELTEX-MES-ISS-ENV-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:49 2025
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

(issSwitchFanEntry,
 issSwitchFanIndex,
 issSwitchFanStatus) = mibBuilder.importSymbols(
    "ARICENT-ISS-MIB",
    "issSwitchFanEntry",
    "issSwitchFanIndex",
    "issSwitchFanStatus")

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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

eltMesIssEnvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12)
)
if mibBuilder.loadTexts:
    eltMesIssEnvMIB.setRevisions(
        ("2019-04-04 00:00",
         "2020-11-25 00:00",
         "2021-04-01 00:00",
         "2021-06-23 00:00",
         "2024-12-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesIssBatteryState(TextualConvention, Integer32):
    status = "current"
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
        *(("notoperational", 1),
          ("notpresent", 2),
          ("recharge", 3),
          ("low", 4),
          ("discharge", 5),
          ("operational", 6))
    )



class EltMesIssOverheatState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overheat", 1),
          ("cooldown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssEnvObjects_ObjectIdentity = ObjectIdentity
eltMesIssEnvObjects = _EltMesIssEnvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1)
)
_EltMesIssEnvDryContacts_ObjectIdentity = ObjectIdentity
eltMesIssEnvDryContacts = _EltMesIssEnvDryContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 1)
)


class _EltMesIssEnvDryContactsNotificationEnable_Type(TruthValue):
    """Custom type eltMesIssEnvDryContactsNotificationEnable based on TruthValue"""
    defaultValue = 2


_EltMesIssEnvDryContactsNotificationEnable_Type.__name__ = "TruthValue"
_EltMesIssEnvDryContactsNotificationEnable_Object = MibScalar
eltMesIssEnvDryContactsNotificationEnable = _EltMesIssEnvDryContactsNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 1, 1),
    _EltMesIssEnvDryContactsNotificationEnable_Type()
)
eltMesIssEnvDryContactsNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssEnvDryContactsNotificationEnable.setStatus("current")
_EltMesIssEnvDryContactsStateTable_Object = MibTable
eltMesIssEnvDryContactsStateTable = _EltMesIssEnvDryContactsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltMesIssEnvDryContactsStateTable.setStatus("current")
_EltMesIssEnvDryContactsStateEntry_Object = MibTableRow
eltMesIssEnvDryContactsStateEntry = _EltMesIssEnvDryContactsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 1, 2, 1)
)
eltMesIssEnvDryContactsStateEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvDryContactsGroup"),
    (0, "ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvDryContactsIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssEnvDryContactsStateEntry.setStatus("current")


class _EltMesIssEnvDryContactsGroup_Type(Integer32):
    """Custom type eltMesIssEnvDryContactsGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssEnvDryContactsGroup_Type.__name__ = "Integer32"
_EltMesIssEnvDryContactsGroup_Object = MibTableColumn
eltMesIssEnvDryContactsGroup = _EltMesIssEnvDryContactsGroup_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 1, 2, 1, 1),
    _EltMesIssEnvDryContactsGroup_Type()
)
eltMesIssEnvDryContactsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssEnvDryContactsGroup.setStatus("current")


class _EltMesIssEnvDryContactsIndex_Type(Integer32):
    """Custom type eltMesIssEnvDryContactsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssEnvDryContactsIndex_Type.__name__ = "Integer32"
_EltMesIssEnvDryContactsIndex_Object = MibTableColumn
eltMesIssEnvDryContactsIndex = _EltMesIssEnvDryContactsIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 1, 2, 1, 2),
    _EltMesIssEnvDryContactsIndex_Type()
)
eltMesIssEnvDryContactsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssEnvDryContactsIndex.setStatus("current")


class _EltMesIssEnvDryContactsState_Type(Integer32):
    """Custom type eltMesIssEnvDryContactsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opened", 1),
          ("closed", 2))
    )


_EltMesIssEnvDryContactsState_Type.__name__ = "Integer32"
_EltMesIssEnvDryContactsState_Object = MibTableColumn
eltMesIssEnvDryContactsState = _EltMesIssEnvDryContactsState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 1, 2, 1, 3),
    _EltMesIssEnvDryContactsState_Type()
)
eltMesIssEnvDryContactsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssEnvDryContactsState.setStatus("current")
_EltMesIssEnvResetButton_ObjectIdentity = ObjectIdentity
eltMesIssEnvResetButton = _EltMesIssEnvResetButton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 2)
)


class _EltEnvResetButtonMode_Type(Integer32):
    """Custom type eltEnvResetButtonMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1),
          ("reset-only", 2))
    )


_EltEnvResetButtonMode_Type.__name__ = "Integer32"
_EltEnvResetButtonMode_Object = MibScalar
eltEnvResetButtonMode = _EltEnvResetButtonMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 2, 1),
    _EltEnvResetButtonMode_Type()
)
eltEnvResetButtonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltEnvResetButtonMode.setStatus("current")
_EltMesIssEnvBattery_ObjectIdentity = ObjectIdentity
eltMesIssEnvBattery = _EltMesIssEnvBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 3)
)
_EltMesIssBatteryStatusTable_Object = MibTable
eltMesIssBatteryStatusTable = _EltMesIssBatteryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltMesIssBatteryStatusTable.setStatus("current")
_EltMesIssBatteryStatusEntry_Object = MibTableRow
eltMesIssBatteryStatusEntry = _EltMesIssBatteryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 3, 1, 1)
)
eltMesIssBatteryStatusEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-ENV-MIB", "eltMesIssBatteryStatusIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssBatteryStatusEntry.setStatus("current")
_EltMesIssBatteryStatusIndex_Type = Integer32
_EltMesIssBatteryStatusIndex_Object = MibTableColumn
eltMesIssBatteryStatusIndex = _EltMesIssBatteryStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 3, 1, 1, 1),
    _EltMesIssBatteryStatusIndex_Type()
)
eltMesIssBatteryStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssBatteryStatusIndex.setStatus("current")
_EltMesIssBatteryStatus_Type = EltMesIssBatteryState
_EltMesIssBatteryStatus_Object = MibTableColumn
eltMesIssBatteryStatus = _EltMesIssBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 3, 1, 1, 2),
    _EltMesIssBatteryStatus_Type()
)
eltMesIssBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssBatteryStatus.setStatus("current")


class _EltMesIssBatteryLevel_Type(Integer32):
    """Custom type eltMesIssBatteryLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(255, 255),
    )


_EltMesIssBatteryLevel_Type.__name__ = "Integer32"
_EltMesIssBatteryLevel_Object = MibTableColumn
eltMesIssBatteryLevel = _EltMesIssBatteryLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 3, 1, 1, 3),
    _EltMesIssBatteryLevel_Type()
)
eltMesIssBatteryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssBatteryLevel.setStatus("current")


class _EltMesIssBatteryMonitorEnable_Type(TruthValue):
    """Custom type eltMesIssBatteryMonitorEnable based on TruthValue"""
    defaultValue = 1


_EltMesIssBatteryMonitorEnable_Type.__name__ = "TruthValue"
_EltMesIssBatteryMonitorEnable_Object = MibScalar
eltMesIssBatteryMonitorEnable = _EltMesIssBatteryMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 3, 2),
    _EltMesIssBatteryMonitorEnable_Type()
)
eltMesIssBatteryMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssBatteryMonitorEnable.setStatus("current")
_EltMesIssEnvDyingGasp_ObjectIdentity = ObjectIdentity
eltMesIssEnvDyingGasp = _EltMesIssEnvDyingGasp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 4)
)


class _EltMesIssDyingGaspStatus_Type(Integer32):
    """Custom type eltMesIssDyingGaspStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EltMesIssDyingGaspStatus_Type.__name__ = "Integer32"
_EltMesIssDyingGaspStatus_Object = MibScalar
eltMesIssDyingGaspStatus = _EltMesIssDyingGaspStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 4, 1),
    _EltMesIssDyingGaspStatus_Type()
)
eltMesIssDyingGaspStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDyingGaspStatus.setStatus("current")
_EltMesIssEnvFan_ObjectIdentity = ObjectIdentity
eltMesIssEnvFan = _EltMesIssEnvFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 5)
)
_EltMesIssEnvFanTable_Object = MibTable
eltMesIssEnvFanTable = _EltMesIssEnvFanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 5, 1)
)
if mibBuilder.loadTexts:
    eltMesIssEnvFanTable.setStatus("current")
_EltMesIssEnvFanEntry_Object = MibTableRow
eltMesIssEnvFanEntry = _EltMesIssEnvFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssEnvFanEntry.setStatus("current")


class _EltMesIssEnvFanSpeed_Type(Integer32):
    """Custom type eltMesIssEnvFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltMesIssEnvFanSpeed_Type.__name__ = "Integer32"
_EltMesIssEnvFanSpeed_Object = MibTableColumn
eltMesIssEnvFanSpeed = _EltMesIssEnvFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 5, 1, 1, 1),
    _EltMesIssEnvFanSpeed_Type()
)
eltMesIssEnvFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssEnvFanSpeed.setStatus("current")


class _EltMesIssEnvFanSpeedLevel_Type(Integer32):
    """Custom type eltMesIssEnvFanSpeedLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_EltMesIssEnvFanSpeedLevel_Type.__name__ = "Integer32"
_EltMesIssEnvFanSpeedLevel_Object = MibTableColumn
eltMesIssEnvFanSpeedLevel = _EltMesIssEnvFanSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 5, 1, 1, 2),
    _EltMesIssEnvFanSpeedLevel_Type()
)
eltMesIssEnvFanSpeedLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssEnvFanSpeedLevel.setStatus("current")
_EltMesIssEnvFanThresholdTable_Object = MibTable
eltMesIssEnvFanThresholdTable = _EltMesIssEnvFanThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 5, 2)
)
if mibBuilder.loadTexts:
    eltMesIssEnvFanThresholdTable.setStatus("current")
_EltMesIssEnvFanThresholdEntry_Object = MibTableRow
eltMesIssEnvFanThresholdEntry = _EltMesIssEnvFanThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 5, 2, 1)
)
eltMesIssEnvFanThresholdEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issSwitchFanIndex"),
    (0, "ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvFanThresholdLevel"),
)
if mibBuilder.loadTexts:
    eltMesIssEnvFanThresholdEntry.setStatus("current")
_EltMesIssEnvFanThresholdLevel_Type = Integer32
_EltMesIssEnvFanThresholdLevel_Object = MibTableColumn
eltMesIssEnvFanThresholdLevel = _EltMesIssEnvFanThresholdLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 5, 2, 1, 1),
    _EltMesIssEnvFanThresholdLevel_Type()
)
eltMesIssEnvFanThresholdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssEnvFanThresholdLevel.setStatus("current")
_EltMesIssEnvFanThresholdMin_Type = Integer32
_EltMesIssEnvFanThresholdMin_Object = MibTableColumn
eltMesIssEnvFanThresholdMin = _EltMesIssEnvFanThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 5, 2, 1, 2),
    _EltMesIssEnvFanThresholdMin_Type()
)
eltMesIssEnvFanThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssEnvFanThresholdMin.setStatus("current")
_EltMesIssEnvFanThresholdMax_Type = Integer32
_EltMesIssEnvFanThresholdMax_Object = MibTableColumn
eltMesIssEnvFanThresholdMax = _EltMesIssEnvFanThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 5, 2, 1, 3),
    _EltMesIssEnvFanThresholdMax_Type()
)
eltMesIssEnvFanThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssEnvFanThresholdMax.setStatus("current")
_EltMesIssEnvPowerSource_ObjectIdentity = ObjectIdentity
eltMesIssEnvPowerSource = _EltMesIssEnvPowerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 6)
)
_EltMesIssEnvPowerSourceTable_Object = MibTable
eltMesIssEnvPowerSourceTable = _EltMesIssEnvPowerSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 6, 1)
)
if mibBuilder.loadTexts:
    eltMesIssEnvPowerSourceTable.setStatus("current")
_EltMesIssEnvPowerSourceEntry_Object = MibTableRow
eltMesIssEnvPowerSourceEntry = _EltMesIssEnvPowerSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 6, 1, 1)
)
eltMesIssEnvPowerSourceEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvPowerSourceIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssEnvPowerSourceEntry.setStatus("current")


class _EltMesIssEnvPowerSourceIndex_Type(Integer32):
    """Custom type eltMesIssEnvPowerSourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssEnvPowerSourceIndex_Type.__name__ = "Integer32"
_EltMesIssEnvPowerSourceIndex_Object = MibTableColumn
eltMesIssEnvPowerSourceIndex = _EltMesIssEnvPowerSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 6, 1, 1, 1),
    _EltMesIssEnvPowerSourceIndex_Type()
)
eltMesIssEnvPowerSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssEnvPowerSourceIndex.setStatus("current")


class _EltMesIssEnvPowerSourceType_Type(Integer32):
    """Custom type eltMesIssEnvPowerSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("redundant", 2))
    )


_EltMesIssEnvPowerSourceType_Type.__name__ = "Integer32"
_EltMesIssEnvPowerSourceType_Object = MibTableColumn
eltMesIssEnvPowerSourceType = _EltMesIssEnvPowerSourceType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 6, 1, 1, 2),
    _EltMesIssEnvPowerSourceType_Type()
)
eltMesIssEnvPowerSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssEnvPowerSourceType.setStatus("current")


class _EltMesIssEnvPowerSourceState_Type(Integer32):
    """Custom type eltMesIssEnvPowerSourceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("not-operational", 2),
          ("not-present", 3))
    )


_EltMesIssEnvPowerSourceState_Type.__name__ = "Integer32"
_EltMesIssEnvPowerSourceState_Object = MibTableColumn
eltMesIssEnvPowerSourceState = _EltMesIssEnvPowerSourceState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 6, 1, 1, 3),
    _EltMesIssEnvPowerSourceState_Type()
)
eltMesIssEnvPowerSourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssEnvPowerSourceState.setStatus("current")
_EltMesIssEnvTempSensor_ObjectIdentity = ObjectIdentity
eltMesIssEnvTempSensor = _EltMesIssEnvTempSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 7)
)
_EltMesIssEnvOverheatStatus_Type = EltMesIssOverheatState
_EltMesIssEnvOverheatStatus_Object = MibScalar
eltMesIssEnvOverheatStatus = _EltMesIssEnvOverheatStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 7, 2),
    _EltMesIssEnvOverheatStatus_Type()
)
eltMesIssEnvOverheatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssEnvOverheatStatus.setStatus("current")
_EltMesIssEnvOverheatDeviceTemp_Type = Integer32
_EltMesIssEnvOverheatDeviceTemp_Object = MibScalar
eltMesIssEnvOverheatDeviceTemp = _EltMesIssEnvOverheatDeviceTemp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 7, 3),
    _EltMesIssEnvOverheatDeviceTemp_Type()
)
eltMesIssEnvOverheatDeviceTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssEnvOverheatDeviceTemp.setStatus("current")
_EltMesIssEnvOverheatThreshold_Type = Integer32
_EltMesIssEnvOverheatThreshold_Object = MibScalar
eltMesIssEnvOverheatThreshold = _EltMesIssEnvOverheatThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 1, 7, 4),
    _EltMesIssEnvOverheatThreshold_Type()
)
eltMesIssEnvOverheatThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssEnvOverheatThreshold.setStatus("current")
_EltMesIssEnvNotifications_ObjectIdentity = ObjectIdentity
eltMesIssEnvNotifications = _EltMesIssEnvNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 2)
)
_EltMesIssEnvNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltMesIssEnvNotificationsPrefix = _EltMesIssEnvNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 2, 0)
)
issSwitchFanEntry.registerAugmentions(
    ("ELTEX-MES-ISS-ENV-MIB",
     "eltMesIssEnvFanEntry")
)
eltMesIssEnvFanEntry.setIndexNames(*issSwitchFanEntry.getIndexNames())

# Managed Objects groups


# Notification objects

eltMesIssEnvDryContactsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 2, 0, 1)
)
eltMesIssEnvDryContactsTrap.setObjects(
      *(("ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvDryContactsGroup"),
        ("ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvDryContactsIndex"),
        ("ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvDryContactsState"))
)
if mibBuilder.loadTexts:
    eltMesIssEnvDryContactsTrap.setStatus(
        "current"
    )

eltMesIssBatteryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 2, 0, 2)
)
eltMesIssBatteryTrap.setObjects(
      *(("ELTEX-MES-ISS-ENV-MIB", "eltMesIssBatteryStatus"),
        ("ELTEX-MES-ISS-ENV-MIB", "eltMesIssBatteryLevel"))
)
if mibBuilder.loadTexts:
    eltMesIssBatteryTrap.setStatus(
        "current"
    )

eltMesIssEnvFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 2, 0, 3)
)
eltMesIssEnvFanStatusTrap.setObjects(
      *(("ARICENT-ISS-MIB", "issSwitchFanIndex"),
        ("ARICENT-ISS-MIB", "issSwitchFanStatus"),
        ("ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvFanSpeed"),
        ("ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvFanSpeedLevel"))
)
if mibBuilder.loadTexts:
    eltMesIssEnvFanStatusTrap.setStatus(
        "current"
    )

eltMesIssEnvOverheatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12, 2, 0, 5)
)
eltMesIssEnvOverheatTrap.setObjects(
      *(("ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvOverheatStatus"),
        ("ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvOverheatDeviceTemp"),
        ("ELTEX-MES-ISS-ENV-MIB", "eltMesIssEnvOverheatThreshold"))
)
if mibBuilder.loadTexts:
    eltMesIssEnvOverheatTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-ENV-MIB",
    **{"EltMesIssBatteryState": EltMesIssBatteryState,
       "EltMesIssOverheatState": EltMesIssOverheatState,
       "eltMesIssEnvMIB": eltMesIssEnvMIB,
       "eltMesIssEnvObjects": eltMesIssEnvObjects,
       "eltMesIssEnvDryContacts": eltMesIssEnvDryContacts,
       "eltMesIssEnvDryContactsNotificationEnable": eltMesIssEnvDryContactsNotificationEnable,
       "eltMesIssEnvDryContactsStateTable": eltMesIssEnvDryContactsStateTable,
       "eltMesIssEnvDryContactsStateEntry": eltMesIssEnvDryContactsStateEntry,
       "eltMesIssEnvDryContactsGroup": eltMesIssEnvDryContactsGroup,
       "eltMesIssEnvDryContactsIndex": eltMesIssEnvDryContactsIndex,
       "eltMesIssEnvDryContactsState": eltMesIssEnvDryContactsState,
       "eltMesIssEnvResetButton": eltMesIssEnvResetButton,
       "eltEnvResetButtonMode": eltEnvResetButtonMode,
       "eltMesIssEnvBattery": eltMesIssEnvBattery,
       "eltMesIssBatteryStatusTable": eltMesIssBatteryStatusTable,
       "eltMesIssBatteryStatusEntry": eltMesIssBatteryStatusEntry,
       "eltMesIssBatteryStatusIndex": eltMesIssBatteryStatusIndex,
       "eltMesIssBatteryStatus": eltMesIssBatteryStatus,
       "eltMesIssBatteryLevel": eltMesIssBatteryLevel,
       "eltMesIssBatteryMonitorEnable": eltMesIssBatteryMonitorEnable,
       "eltMesIssEnvDyingGasp": eltMesIssEnvDyingGasp,
       "eltMesIssDyingGaspStatus": eltMesIssDyingGaspStatus,
       "eltMesIssEnvFan": eltMesIssEnvFan,
       "eltMesIssEnvFanTable": eltMesIssEnvFanTable,
       "eltMesIssEnvFanEntry": eltMesIssEnvFanEntry,
       "eltMesIssEnvFanSpeed": eltMesIssEnvFanSpeed,
       "eltMesIssEnvFanSpeedLevel": eltMesIssEnvFanSpeedLevel,
       "eltMesIssEnvFanThresholdTable": eltMesIssEnvFanThresholdTable,
       "eltMesIssEnvFanThresholdEntry": eltMesIssEnvFanThresholdEntry,
       "eltMesIssEnvFanThresholdLevel": eltMesIssEnvFanThresholdLevel,
       "eltMesIssEnvFanThresholdMin": eltMesIssEnvFanThresholdMin,
       "eltMesIssEnvFanThresholdMax": eltMesIssEnvFanThresholdMax,
       "eltMesIssEnvPowerSource": eltMesIssEnvPowerSource,
       "eltMesIssEnvPowerSourceTable": eltMesIssEnvPowerSourceTable,
       "eltMesIssEnvPowerSourceEntry": eltMesIssEnvPowerSourceEntry,
       "eltMesIssEnvPowerSourceIndex": eltMesIssEnvPowerSourceIndex,
       "eltMesIssEnvPowerSourceType": eltMesIssEnvPowerSourceType,
       "eltMesIssEnvPowerSourceState": eltMesIssEnvPowerSourceState,
       "eltMesIssEnvTempSensor": eltMesIssEnvTempSensor,
       "eltMesIssEnvOverheatStatus": eltMesIssEnvOverheatStatus,
       "eltMesIssEnvOverheatDeviceTemp": eltMesIssEnvOverheatDeviceTemp,
       "eltMesIssEnvOverheatThreshold": eltMesIssEnvOverheatThreshold,
       "eltMesIssEnvNotifications": eltMesIssEnvNotifications,
       "eltMesIssEnvNotificationsPrefix": eltMesIssEnvNotificationsPrefix,
       "eltMesIssEnvDryContactsTrap": eltMesIssEnvDryContactsTrap,
       "eltMesIssBatteryTrap": eltMesIssBatteryTrap,
       "eltMesIssEnvFanStatusTrap": eltMesIssEnvFanStatusTrap,
       "eltMesIssEnvOverheatTrap": eltMesIssEnvOverheatTrap}
)
