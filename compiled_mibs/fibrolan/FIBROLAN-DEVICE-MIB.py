# SNMP MIB module (FIBROLAN-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-DEVICE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:18 2025
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

(FlFileServerType,
 FlFileXferDirection,
 FlTemperature,
 FlUtilization,
 fibrolanGeneric) = mibBuilder.importSymbols(
    "FIBROLAN-COMMON-MIB",
    "FlFileServerType",
    "FlFileXferDirection",
    "FlTemperature",
    "FlUtilization",
    "fibrolanGeneric")

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

flDevice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10)
)
if mibBuilder.loadTexts:
    flDevice.setRevisions(
        ("2016-07-15 00:00",
         "2015-09-15 00:00",
         "2015-09-01 00:00",
         "2015-02-01 00:00",
         "2009-05-05 00:00",
         "2009-03-19 00:00",
         "2009-02-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FlDeviceNotifications_ObjectIdentity = ObjectIdentity
flDeviceNotifications = _FlDeviceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 0)
)
_FlDeviceMIBObjects_ObjectIdentity = ObjectIdentity
flDeviceMIBObjects = _FlDeviceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1)
)


class _FlDeviceReboot_Type(Integer32):
    """Custom type flDeviceReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("notReady", 1),
          ("reboot", 2))
    )


_FlDeviceReboot_Type.__name__ = "Integer32"
_FlDeviceReboot_Object = MibScalar
flDeviceReboot = _FlDeviceReboot_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 10),
    _FlDeviceReboot_Type()
)
flDeviceReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceReboot.setStatus("current")


class _FlDeviceRestoreDefaults_Type(Integer32):
    """Custom type flDeviceRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("notReady", 1),
          ("restoreDefaults", 2))
    )


_FlDeviceRestoreDefaults_Type.__name__ = "Integer32"
_FlDeviceRestoreDefaults_Object = MibScalar
flDeviceRestoreDefaults = _FlDeviceRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 11),
    _FlDeviceRestoreDefaults_Type()
)
flDeviceRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceRestoreDefaults.setStatus("current")


class _FlDeviceSaveConfig_Type(Integer32):
    """Custom type flDeviceSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("notReady", 1),
          ("saveConfig", 2))
    )


_FlDeviceSaveConfig_Type.__name__ = "Integer32"
_FlDeviceSaveConfig_Object = MibScalar
flDeviceSaveConfig = _FlDeviceSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 12),
    _FlDeviceSaveConfig_Type()
)
flDeviceSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceSaveConfig.setStatus("current")
_FlDeviceTemperature_Type = FlTemperature
_FlDeviceTemperature_Object = MibScalar
flDeviceTemperature = _FlDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 13),
    _FlDeviceTemperature_Type()
)
flDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceTemperature.setStatus("current")


class _FlDeviceTemperatureAlarmsEnable_Type(Integer32):
    """Custom type flDeviceTemperatureAlarmsEnable based on Integer32"""
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


_FlDeviceTemperatureAlarmsEnable_Type.__name__ = "Integer32"
_FlDeviceTemperatureAlarmsEnable_Object = MibScalar
flDeviceTemperatureAlarmsEnable = _FlDeviceTemperatureAlarmsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 14),
    _FlDeviceTemperatureAlarmsEnable_Type()
)
flDeviceTemperatureAlarmsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceTemperatureAlarmsEnable.setStatus("current")


class _FlDeviceTemperatureAlarmStatus_Type(Integer32):
    """Custom type flDeviceTemperatureAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("high", 2),
          ("low", 4))
    )


_FlDeviceTemperatureAlarmStatus_Type.__name__ = "Integer32"
_FlDeviceTemperatureAlarmStatus_Object = MibScalar
flDeviceTemperatureAlarmStatus = _FlDeviceTemperatureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 15),
    _FlDeviceTemperatureAlarmStatus_Type()
)
flDeviceTemperatureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceTemperatureAlarmStatus.setStatus("current")
_FlDeviceTemperatureStatusLastChange_Type = TimeTicks
_FlDeviceTemperatureStatusLastChange_Object = MibScalar
flDeviceTemperatureStatusLastChange = _FlDeviceTemperatureStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 16),
    _FlDeviceTemperatureStatusLastChange_Type()
)
flDeviceTemperatureStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceTemperatureStatusLastChange.setStatus("current")
_FlDevicePsuStatusTable_Object = MibTable
flDevicePsuStatusTable = _FlDevicePsuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 100)
)
if mibBuilder.loadTexts:
    flDevicePsuStatusTable.setStatus("current")
_FlDevicePsuStatusEntry_Object = MibTableRow
flDevicePsuStatusEntry = _FlDevicePsuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 100, 1)
)
flDevicePsuStatusEntry.setIndexNames(
    (0, "FIBROLAN-DEVICE-MIB", "flDevicePsuIndex"),
)
if mibBuilder.loadTexts:
    flDevicePsuStatusEntry.setStatus("current")


class _FlDevicePsuIndex_Type(Integer32):
    """Custom type flDevicePsuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FlDevicePsuIndex_Type.__name__ = "Integer32"
_FlDevicePsuIndex_Object = MibTableColumn
flDevicePsuIndex = _FlDevicePsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 100, 1, 1),
    _FlDevicePsuIndex_Type()
)
flDevicePsuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flDevicePsuIndex.setStatus("current")


class _FlDevicePsuInstalled_Type(Integer32):
    """Custom type flDevicePsuInstalled based on Integer32"""
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
          ("installed", 2),
          ("notInstalled", 3))
    )


_FlDevicePsuInstalled_Type.__name__ = "Integer32"
_FlDevicePsuInstalled_Object = MibTableColumn
flDevicePsuInstalled = _FlDevicePsuInstalled_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 100, 1, 2),
    _FlDevicePsuInstalled_Type()
)
flDevicePsuInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDevicePsuInstalled.setStatus("current")


class _FlDevicePsuStatus_Type(Integer32):
    """Custom type flDevicePsuStatus based on Integer32"""
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
          ("ok", 2),
          ("fail", 3))
    )


_FlDevicePsuStatus_Type.__name__ = "Integer32"
_FlDevicePsuStatus_Object = MibTableColumn
flDevicePsuStatus = _FlDevicePsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 100, 1, 3),
    _FlDevicePsuStatus_Type()
)
flDevicePsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDevicePsuStatus.setStatus("current")


class _FlDevicePsuFanStatus_Type(Integer32):
    """Custom type flDevicePsuFanStatus based on Integer32"""
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
        *(("unknown", 1),
          ("notApplicable", 2),
          ("ok", 3),
          ("fail", 4),
          ("singleFail", 5))
    )


_FlDevicePsuFanStatus_Type.__name__ = "Integer32"
_FlDevicePsuFanStatus_Object = MibTableColumn
flDevicePsuFanStatus = _FlDevicePsuFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 100, 1, 4),
    _FlDevicePsuFanStatus_Type()
)
flDevicePsuFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDevicePsuFanStatus.setStatus("current")


class _FlDevicePsuAlarmsEnable_Type(Integer32):
    """Custom type flDevicePsuAlarmsEnable based on Integer32"""
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


_FlDevicePsuAlarmsEnable_Type.__name__ = "Integer32"
_FlDevicePsuAlarmsEnable_Object = MibTableColumn
flDevicePsuAlarmsEnable = _FlDevicePsuAlarmsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 100, 1, 5),
    _FlDevicePsuAlarmsEnable_Type()
)
flDevicePsuAlarmsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDevicePsuAlarmsEnable.setStatus("current")


class _FlDevicePsuAlarmStatus_Type(Integer32):
    """Custom type flDevicePsuAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("psuNotInstalled", 2),
          ("psuDown", 4),
          ("fanDown", 8),
          ("singleFanDown", 16))
    )


_FlDevicePsuAlarmStatus_Type.__name__ = "Integer32"
_FlDevicePsuAlarmStatus_Object = MibTableColumn
flDevicePsuAlarmStatus = _FlDevicePsuAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 100, 1, 6),
    _FlDevicePsuAlarmStatus_Type()
)
flDevicePsuAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDevicePsuAlarmStatus.setStatus("current")
_FlDevicePsuStatusLastChange_Type = TimeTicks
_FlDevicePsuStatusLastChange_Object = MibTableColumn
flDevicePsuStatusLastChange = _FlDevicePsuStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 100, 1, 7),
    _FlDevicePsuStatusLastChange_Type()
)
flDevicePsuStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDevicePsuStatusLastChange.setStatus("current")
_FlDeviceUpdateTable_Object = MibTable
flDeviceUpdateTable = _FlDeviceUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110)
)
if mibBuilder.loadTexts:
    flDeviceUpdateTable.setStatus("current")
_FlDeviceUpdateEntry_Object = MibTableRow
flDeviceUpdateEntry = _FlDeviceUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1)
)
flDeviceUpdateEntry.setIndexNames(
    (0, "FIBROLAN-DEVICE-MIB", "flDeviceUpdateTableIndex"),
)
if mibBuilder.loadTexts:
    flDeviceUpdateEntry.setStatus("current")


class _FlDeviceUpdateTableIndex_Type(Unsigned32):
    """Custom type flDeviceUpdateTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_FlDeviceUpdateTableIndex_Type.__name__ = "Unsigned32"
_FlDeviceUpdateTableIndex_Object = MibTableColumn
flDeviceUpdateTableIndex = _FlDeviceUpdateTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 1),
    _FlDeviceUpdateTableIndex_Type()
)
flDeviceUpdateTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flDeviceUpdateTableIndex.setStatus("current")


class _FlDeviceUpdateType_Type(Integer32):
    """Custom type flDeviceUpdateType based on Integer32"""
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
        *(("other", 1),
          ("software", 2),
          ("firmware", 3),
          ("system", 4),
          ("config", 5),
          ("script", 6))
    )


_FlDeviceUpdateType_Type.__name__ = "Integer32"
_FlDeviceUpdateType_Object = MibTableColumn
flDeviceUpdateType = _FlDeviceUpdateType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 2),
    _FlDeviceUpdateType_Type()
)
flDeviceUpdateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceUpdateType.setStatus("current")
_FlDeviceUpdateFileServerType_Type = FlFileServerType
_FlDeviceUpdateFileServerType_Object = MibTableColumn
flDeviceUpdateFileServerType = _FlDeviceUpdateFileServerType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 3),
    _FlDeviceUpdateFileServerType_Type()
)
flDeviceUpdateFileServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceUpdateFileServerType.setStatus("current")
_FlDeviceUpdateFileServerAddress_Type = IpAddress
_FlDeviceUpdateFileServerAddress_Object = MibTableColumn
flDeviceUpdateFileServerAddress = _FlDeviceUpdateFileServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 4),
    _FlDeviceUpdateFileServerAddress_Type()
)
flDeviceUpdateFileServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceUpdateFileServerAddress.setStatus("current")
_FlDeviceUpdateFileXferDirection_Type = FlFileXferDirection
_FlDeviceUpdateFileXferDirection_Object = MibTableColumn
flDeviceUpdateFileXferDirection = _FlDeviceUpdateFileXferDirection_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 5),
    _FlDeviceUpdateFileXferDirection_Type()
)
flDeviceUpdateFileXferDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceUpdateFileXferDirection.setStatus("current")


class _FlDeviceUpdateFileName_Type(DisplayString):
    """Custom type flDeviceUpdateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FlDeviceUpdateFileName_Type.__name__ = "DisplayString"
_FlDeviceUpdateFileName_Object = MibTableColumn
flDeviceUpdateFileName = _FlDeviceUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 6),
    _FlDeviceUpdateFileName_Type()
)
flDeviceUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceUpdateFileName.setStatus("current")


class _FlDeviceUpdateStart_Type(Integer32):
    """Custom type flDeviceUpdateStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("notReady", 1),
          ("start", 2))
    )


_FlDeviceUpdateStart_Type.__name__ = "Integer32"
_FlDeviceUpdateStart_Object = MibTableColumn
flDeviceUpdateStart = _FlDeviceUpdateStart_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 7),
    _FlDeviceUpdateStart_Type()
)
flDeviceUpdateStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceUpdateStart.setStatus("current")


class _FlDeviceUpdateStatus_Type(Integer32):
    """Custom type flDeviceUpdateStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("notStarted", 2),
          ("loadingFile", 3),
          ("savingFile", 4),
          ("verifyingFile", 5),
          ("updateInProgress", 6),
          ("updateComplete", 7),
          ("updateIncomplete", 8),
          ("updateFailed", 9))
    )


_FlDeviceUpdateStatus_Type.__name__ = "Integer32"
_FlDeviceUpdateStatus_Object = MibTableColumn
flDeviceUpdateStatus = _FlDeviceUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 8),
    _FlDeviceUpdateStatus_Type()
)
flDeviceUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceUpdateStatus.setStatus("current")


class _FlDeviceUpdateErrorStatus_Type(Integer32):
    """Custom type flDeviceUpdateErrorStatus based on Integer32"""
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
        *(("noError", 1),
          ("other", 2),
          ("fileNotFound", 3),
          ("serverTimeout", 4),
          ("fileInvalid", 5),
          ("updateError", 6))
    )


_FlDeviceUpdateErrorStatus_Type.__name__ = "Integer32"
_FlDeviceUpdateErrorStatus_Object = MibTableColumn
flDeviceUpdateErrorStatus = _FlDeviceUpdateErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 9),
    _FlDeviceUpdateErrorStatus_Type()
)
flDeviceUpdateErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceUpdateErrorStatus.setStatus("current")


class _FlDeviceUpdateErrorCode_Type(Integer32):
    """Custom type flDeviceUpdateErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_FlDeviceUpdateErrorCode_Type.__name__ = "Integer32"
_FlDeviceUpdateErrorCode_Object = MibTableColumn
flDeviceUpdateErrorCode = _FlDeviceUpdateErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 10),
    _FlDeviceUpdateErrorCode_Type()
)
flDeviceUpdateErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceUpdateErrorCode.setStatus("current")


class _FlDeviceUpdateUrl_Type(DisplayString):
    """Custom type flDeviceUpdateUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FlDeviceUpdateUrl_Type.__name__ = "DisplayString"
_FlDeviceUpdateUrl_Object = MibTableColumn
flDeviceUpdateUrl = _FlDeviceUpdateUrl_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 110, 1, 11),
    _FlDeviceUpdateUrl_Type()
)
flDeviceUpdateUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceUpdateUrl.setStatus("current")
_FlDeviceCpuStatusTable_Object = MibTable
flDeviceCpuStatusTable = _FlDeviceCpuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 120)
)
if mibBuilder.loadTexts:
    flDeviceCpuStatusTable.setStatus("current")
_FlDeviceCpuStatusEntry_Object = MibTableRow
flDeviceCpuStatusEntry = _FlDeviceCpuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 120, 1)
)
flDeviceCpuStatusEntry.setIndexNames(
    (0, "FIBROLAN-DEVICE-MIB", "flDeviceCpuIndex"),
)
if mibBuilder.loadTexts:
    flDeviceCpuStatusEntry.setStatus("current")


class _FlDeviceCpuIndex_Type(Integer32):
    """Custom type flDeviceCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FlDeviceCpuIndex_Type.__name__ = "Integer32"
_FlDeviceCpuIndex_Object = MibTableColumn
flDeviceCpuIndex = _FlDeviceCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 120, 1, 1),
    _FlDeviceCpuIndex_Type()
)
flDeviceCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flDeviceCpuIndex.setStatus("current")
_FlDeviceCpuUtilization_Type = FlUtilization
_FlDeviceCpuUtilization_Object = MibTableColumn
flDeviceCpuUtilization = _FlDeviceCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 120, 1, 2),
    _FlDeviceCpuUtilization_Type()
)
flDeviceCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceCpuUtilization.setStatus("current")
_FlDeviceMemoryUtilization_Type = FlUtilization
_FlDeviceMemoryUtilization_Object = MibTableColumn
flDeviceMemoryUtilization = _FlDeviceMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 120, 1, 3),
    _FlDeviceMemoryUtilization_Type()
)
flDeviceMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceMemoryUtilization.setStatus("current")
_FlDeviceNvMemoryUtilization_Type = FlUtilization
_FlDeviceNvMemoryUtilization_Object = MibTableColumn
flDeviceNvMemoryUtilization = _FlDeviceNvMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 120, 1, 4),
    _FlDeviceNvMemoryUtilization_Type()
)
flDeviceNvMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceNvMemoryUtilization.setStatus("current")


class _FlDeviceCpuAlarmsEnable_Type(Integer32):
    """Custom type flDeviceCpuAlarmsEnable based on Integer32"""
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


_FlDeviceCpuAlarmsEnable_Type.__name__ = "Integer32"
_FlDeviceCpuAlarmsEnable_Object = MibTableColumn
flDeviceCpuAlarmsEnable = _FlDeviceCpuAlarmsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 120, 1, 5),
    _FlDeviceCpuAlarmsEnable_Type()
)
flDeviceCpuAlarmsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceCpuAlarmsEnable.setStatus("current")
_FlDeviceCpuAlarmStatus_Type = Integer32
_FlDeviceCpuAlarmStatus_Object = MibTableColumn
flDeviceCpuAlarmStatus = _FlDeviceCpuAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 120, 1, 6),
    _FlDeviceCpuAlarmStatus_Type()
)
flDeviceCpuAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceCpuAlarmStatus.setStatus("current")
_FlDeviceCpuStatusLastChange_Type = TimeTicks
_FlDeviceCpuStatusLastChange_Object = MibTableColumn
flDeviceCpuStatusLastChange = _FlDeviceCpuStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 120, 1, 7),
    _FlDeviceCpuStatusLastChange_Type()
)
flDeviceCpuStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceCpuStatusLastChange.setStatus("current")
_FlDeviceAlarmThresholdTable_Object = MibTable
flDeviceAlarmThresholdTable = _FlDeviceAlarmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 500)
)
if mibBuilder.loadTexts:
    flDeviceAlarmThresholdTable.setStatus("current")
_FlDeviceAlarmThresholdEntry_Object = MibTableRow
flDeviceAlarmThresholdEntry = _FlDeviceAlarmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 500, 1)
)
flDeviceAlarmThresholdEntry.setIndexNames(
    (0, "FIBROLAN-DEVICE-MIB", "flDeviceAlarmThresholdTableIndex"),
)
if mibBuilder.loadTexts:
    flDeviceAlarmThresholdEntry.setStatus("current")


class _FlDeviceAlarmThresholdTableIndex_Type(Unsigned32):
    """Custom type flDeviceAlarmThresholdTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_FlDeviceAlarmThresholdTableIndex_Type.__name__ = "Unsigned32"
_FlDeviceAlarmThresholdTableIndex_Object = MibTableColumn
flDeviceAlarmThresholdTableIndex = _FlDeviceAlarmThresholdTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 500, 1, 1),
    _FlDeviceAlarmThresholdTableIndex_Type()
)
flDeviceAlarmThresholdTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flDeviceAlarmThresholdTableIndex.setStatus("current")


class _FlDeviceAlarmThresholdType_Type(Integer32):
    """Custom type flDeviceAlarmThresholdType based on Integer32"""
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
        *(("other", 1),
          ("temperatureHigh", 2),
          ("temperatureLow", 3),
          ("cpuUtilHigh", 4),
          ("memoryUtilHigh", 5))
    )


_FlDeviceAlarmThresholdType_Type.__name__ = "Integer32"
_FlDeviceAlarmThresholdType_Object = MibTableColumn
flDeviceAlarmThresholdType = _FlDeviceAlarmThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 500, 1, 2),
    _FlDeviceAlarmThresholdType_Type()
)
flDeviceAlarmThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flDeviceAlarmThresholdType.setStatus("current")


class _FlDeviceAlarmThresholdValue_Type(Integer32):
    """Custom type flDeviceAlarmThresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_FlDeviceAlarmThresholdValue_Type.__name__ = "Integer32"
_FlDeviceAlarmThresholdValue_Object = MibTableColumn
flDeviceAlarmThresholdValue = _FlDeviceAlarmThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 500, 1, 3),
    _FlDeviceAlarmThresholdValue_Type()
)
flDeviceAlarmThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceAlarmThresholdValue.setStatus("current")


class _FlDeviceAlarmThresholdClearValue_Type(Integer32):
    """Custom type flDeviceAlarmThresholdClearValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_FlDeviceAlarmThresholdClearValue_Type.__name__ = "Integer32"
_FlDeviceAlarmThresholdClearValue_Object = MibTableColumn
flDeviceAlarmThresholdClearValue = _FlDeviceAlarmThresholdClearValue_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 1, 500, 1, 4),
    _FlDeviceAlarmThresholdClearValue_Type()
)
flDeviceAlarmThresholdClearValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flDeviceAlarmThresholdClearValue.setStatus("current")

# Managed Objects groups


# Notification objects

psuStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 0, 10)
)
psuStatusChange.setObjects(
      *(("FIBROLAN-DEVICE-MIB", "flDevicePsuAlarmStatus"),
        ("FIBROLAN-DEVICE-MIB", "flDevicePsuStatusLastChange"))
)
if mibBuilder.loadTexts:
    psuStatusChange.setStatus(
        "current"
    )

dyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 0, 11)
)
if mibBuilder.loadTexts:
    dyingGasp.setStatus(
        "current"
    )

temperatureStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 0, 12)
)
temperatureStatusChange.setObjects(
      *(("FIBROLAN-DEVICE-MIB", "flDeviceTemperatureAlarmStatus"),
        ("FIBROLAN-DEVICE-MIB", "flDeviceTemperatureStatusLastChange"))
)
if mibBuilder.loadTexts:
    temperatureStatusChange.setStatus(
        "current"
    )

cpuStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 0, 13)
)
cpuStatusChange.setObjects(
      *(("FIBROLAN-DEVICE-MIB", "flDeviceCpuAlarmStatus"),
        ("FIBROLAN-DEVICE-MIB", "flDeviceCpuStatusLastChange"))
)
if mibBuilder.loadTexts:
    cpuStatusChange.setStatus(
        "current"
    )

portMacLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 0, 19)
)
portMacLimit.setObjects(
    ("FIBROLAN-DEVICE-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portMacLimit.setStatus(
        "current"
    )

configChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 0, 50)
)
if mibBuilder.loadTexts:
    configChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-DEVICE-MIB",
    **{"flDevice": flDevice,
       "flDeviceNotifications": flDeviceNotifications,
       "psuStatusChange": psuStatusChange,
       "dyingGasp": dyingGasp,
       "temperatureStatusChange": temperatureStatusChange,
       "cpuStatusChange": cpuStatusChange,
       "portMacLimit": portMacLimit,
       "configChanged": configChanged,
       "flDeviceMIBObjects": flDeviceMIBObjects,
       "flDeviceReboot": flDeviceReboot,
       "flDeviceRestoreDefaults": flDeviceRestoreDefaults,
       "flDeviceSaveConfig": flDeviceSaveConfig,
       "flDeviceTemperature": flDeviceTemperature,
       "flDeviceTemperatureAlarmsEnable": flDeviceTemperatureAlarmsEnable,
       "flDeviceTemperatureAlarmStatus": flDeviceTemperatureAlarmStatus,
       "flDeviceTemperatureStatusLastChange": flDeviceTemperatureStatusLastChange,
       "flDevicePsuStatusTable": flDevicePsuStatusTable,
       "flDevicePsuStatusEntry": flDevicePsuStatusEntry,
       "flDevicePsuIndex": flDevicePsuIndex,
       "flDevicePsuInstalled": flDevicePsuInstalled,
       "flDevicePsuStatus": flDevicePsuStatus,
       "flDevicePsuFanStatus": flDevicePsuFanStatus,
       "flDevicePsuAlarmsEnable": flDevicePsuAlarmsEnable,
       "flDevicePsuAlarmStatus": flDevicePsuAlarmStatus,
       "flDevicePsuStatusLastChange": flDevicePsuStatusLastChange,
       "flDeviceUpdateTable": flDeviceUpdateTable,
       "flDeviceUpdateEntry": flDeviceUpdateEntry,
       "flDeviceUpdateTableIndex": flDeviceUpdateTableIndex,
       "flDeviceUpdateType": flDeviceUpdateType,
       "flDeviceUpdateFileServerType": flDeviceUpdateFileServerType,
       "flDeviceUpdateFileServerAddress": flDeviceUpdateFileServerAddress,
       "flDeviceUpdateFileXferDirection": flDeviceUpdateFileXferDirection,
       "flDeviceUpdateFileName": flDeviceUpdateFileName,
       "flDeviceUpdateStart": flDeviceUpdateStart,
       "flDeviceUpdateStatus": flDeviceUpdateStatus,
       "flDeviceUpdateErrorStatus": flDeviceUpdateErrorStatus,
       "flDeviceUpdateErrorCode": flDeviceUpdateErrorCode,
       "flDeviceUpdateUrl": flDeviceUpdateUrl,
       "flDeviceCpuStatusTable": flDeviceCpuStatusTable,
       "flDeviceCpuStatusEntry": flDeviceCpuStatusEntry,
       "flDeviceCpuIndex": flDeviceCpuIndex,
       "flDeviceCpuUtilization": flDeviceCpuUtilization,
       "flDeviceMemoryUtilization": flDeviceMemoryUtilization,
       "flDeviceNvMemoryUtilization": flDeviceNvMemoryUtilization,
       "flDeviceCpuAlarmsEnable": flDeviceCpuAlarmsEnable,
       "flDeviceCpuAlarmStatus": flDeviceCpuAlarmStatus,
       "flDeviceCpuStatusLastChange": flDeviceCpuStatusLastChange,
       "flDeviceAlarmThresholdTable": flDeviceAlarmThresholdTable,
       "flDeviceAlarmThresholdEntry": flDeviceAlarmThresholdEntry,
       "flDeviceAlarmThresholdTableIndex": flDeviceAlarmThresholdTableIndex,
       "flDeviceAlarmThresholdType": flDeviceAlarmThresholdType,
       "flDeviceAlarmThresholdValue": flDeviceAlarmThresholdValue,
       "flDeviceAlarmThresholdClearValue": flDeviceAlarmThresholdClearValue}
)
