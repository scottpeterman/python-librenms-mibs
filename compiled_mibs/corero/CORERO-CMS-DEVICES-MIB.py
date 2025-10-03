# SNMP MIB module (CORERO-CMS-DEVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\corero\CORERO-CMS-DEVICES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:31 2025
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

(coreroCMSMIBCompliances,
 coreroCMSMIBGroups,
 coreroCMSMIBObjects) = mibBuilder.importSymbols(
    "CORERO-CMS-MIB",
    "coreroCMSMIBCompliances",
    "coreroCMSMIBGroups",
    "coreroCMSMIBObjects")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

devices = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2)
)
if mibBuilder.loadTexts:
    devices.setRevisions(
        ("2017-12-05 00:00",
         "2017-12-07 00:00",
         "2017-12-19 00:00",
         "2018-01-09 00:00",
         "2018-02-05 00:00",
         "2018-09-25 00:00",
         "2018-10-02 00:00",
         "2018-10-08 00:00",
         "2020-09-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("current")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1)
)
deviceEntry.setIndexNames(
    (0, "CORERO-CMS-DEVICES-MIB", "deviceIndex"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("current")


class _DeviceIndex_Type(Integer32):
    """Custom type deviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceIndex_Type.__name__ = "Integer32"
_DeviceIndex_Object = MibTableColumn
deviceIndex = _DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 1),
    _DeviceIndex_Type()
)
deviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIndex.setStatus("current")
_DeviceName_Type = OctetString
_DeviceName_Object = MibTableColumn
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_DeviceAddress_Type = OctetString
_DeviceAddress_Object = MibTableColumn
deviceAddress = _DeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 3),
    _DeviceAddress_Type()
)
deviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAddress.setStatus("current")
_DeviceDescription_Type = OctetString
_DeviceDescription_Object = MibTableColumn
deviceDescription = _DeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 4),
    _DeviceDescription_Type()
)
deviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDescription.setStatus("current")


class _DeviceDefenseMode_Type(Integer32):
    """Custom type deviceDefenseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 0),
          ("mitigate", 1),
          ("pass-through", 2),
          ("not-applicable", 10))
    )


_DeviceDefenseMode_Type.__name__ = "Integer32"
_DeviceDefenseMode_Object = MibTableColumn
deviceDefenseMode = _DeviceDefenseMode_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 5),
    _DeviceDefenseMode_Type()
)
deviceDefenseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDefenseMode.setStatus("current")


class _DeviceAdminState_Type(Integer32):
    """Custom type deviceAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DeviceAdminState_Type.__name__ = "Integer32"
_DeviceAdminState_Object = MibTableColumn
deviceAdminState = _DeviceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 6),
    _DeviceAdminState_Type()
)
deviceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAdminState.setStatus("current")


class _DeviceModel_Type(Integer32):
    """Custom type deviceModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ntd-virtual-edition", 0),
          ("ntd1100", 1),
          ("ntd120", 2),
          ("nba", 3),
          ("unknown", 4),
          ("ntd280", 5))
    )


_DeviceModel_Type.__name__ = "Integer32"
_DeviceModel_Object = MibTableColumn
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 7),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("current")
_DeviceSerialNumber_Type = OctetString
_DeviceSerialNumber_Object = MibTableColumn
deviceSerialNumber = _DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 8),
    _DeviceSerialNumber_Type()
)
deviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNumber.setStatus("current")


class _DeviceConnectionState_Type(Integer32):
    """Custom type deviceConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connected", 0),
          ("authentication-failed", 1),
          ("connection-timed-out", 2),
          ("connection-refused", 3),
          ("unknown-connection-error", 4),
          ("no-connection", 5),
          ("locked-by-user", 6))
    )


_DeviceConnectionState_Type.__name__ = "Integer32"
_DeviceConnectionState_Object = MibTableColumn
deviceConnectionState = _DeviceConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 9),
    _DeviceConnectionState_Type()
)
deviceConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceConnectionState.setStatus("current")


class _DeviceDeploymentState_Type(Integer32):
    """Custom type deviceDeploymentState based on Integer32"""
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("in-sync", 0),
          ("sync-required", 1),
          ("force-sync-required", 2),
          ("unknown", 3),
          ("not-in-cluster", 4),
          ("initial-sync-pending", 5),
          ("not-licensed", 6),
          ("unsupported-version", 7),
          ("deploy-pending", 8),
          ("unexpected-device-type", 9),
          ("invalid-modules-detected", 10),
          ("redeploy-pending", 11))
    )


_DeviceDeploymentState_Type.__name__ = "Integer32"
_DeviceDeploymentState_Object = MibTableColumn
deviceDeploymentState = _DeviceDeploymentState_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 10),
    _DeviceDeploymentState_Type()
)
deviceDeploymentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDeploymentState.setStatus("current")


class _DeviceDeploymentAction_Type(Integer32):
    """Custom type deviceDeploymentAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("deploy-in-progress", 1),
          ("sync-to-in-progress", 2),
          ("force-sync-in-progress", 3),
          ("commit-in-progress", 4),
          ("upgrade-in-progress", 5))
    )


_DeviceDeploymentAction_Type.__name__ = "Integer32"
_DeviceDeploymentAction_Object = MibTableColumn
deviceDeploymentAction = _DeviceDeploymentAction_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 11),
    _DeviceDeploymentAction_Type()
)
deviceDeploymentAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDeploymentAction.setStatus("current")
_DeviceSXOSVersion_Type = OctetString
_DeviceSXOSVersion_Object = MibTableColumn
deviceSXOSVersion = _DeviceSXOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 12),
    _DeviceSXOSVersion_Type()
)
deviceSXOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSXOSVersion.setStatus("current")
_DeviceSoftwareVersion_Type = OctetString
_DeviceSoftwareVersion_Object = MibTableColumn
deviceSoftwareVersion = _DeviceSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 13),
    _DeviceSoftwareVersion_Type()
)
deviceSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSoftwareVersion.setStatus("current")
_DeviceUptime_Type = OctetString
_DeviceUptime_Object = MibTableColumn
deviceUptime = _DeviceUptime_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 14),
    _DeviceUptime_Type()
)
deviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUptime.setStatus("current")
_DeviceStatus_Type = OctetString
_DeviceStatus_Object = MibTableColumn
deviceStatus = _DeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 15),
    _DeviceStatus_Type()
)
deviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceStatus.setStatus("current")


class _DeviceType_Type(Integer32):
    """Custom type deviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defense", 0),
          ("bypass", 1),
          ("unknown", 2))
    )


_DeviceType_Type.__name__ = "Integer32"
_DeviceType_Object = MibTableColumn
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 16),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")


class _DeviceBypassMode_Type(Integer32):
    """Custom type deviceBypassMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("automatic", 1),
          ("physical-bypass", 2),
          ("switched-bypass", 3),
          ("monitor-tap", 4),
          ("not-applicable", 10))
    )


_DeviceBypassMode_Type.__name__ = "Integer32"
_DeviceBypassMode_Object = MibTableColumn
deviceBypassMode = _DeviceBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 17),
    _DeviceBypassMode_Type()
)
deviceBypassMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceBypassMode.setStatus("current")
_DeviceHardwareVersion_Type = OctetString
_DeviceHardwareVersion_Object = MibTableColumn
deviceHardwareVersion = _DeviceHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 2, 1, 1, 18),
    _DeviceHardwareVersion_Type()
)
deviceHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardwareVersion.setStatus("current")

# Managed Objects groups

coreroDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 2, 2)
)
coreroDeviceGroup.setObjects(
      *(("CORERO-CMS-DEVICES-MIB", "deviceIndex"),
        ("CORERO-CMS-DEVICES-MIB", "deviceName"),
        ("CORERO-CMS-DEVICES-MIB", "deviceAddress"),
        ("CORERO-CMS-DEVICES-MIB", "deviceDescription"),
        ("CORERO-CMS-DEVICES-MIB", "deviceDefenseMode"),
        ("CORERO-CMS-DEVICES-MIB", "deviceAdminState"),
        ("CORERO-CMS-DEVICES-MIB", "deviceModel"),
        ("CORERO-CMS-DEVICES-MIB", "deviceSerialNumber"),
        ("CORERO-CMS-DEVICES-MIB", "deviceConnectionState"),
        ("CORERO-CMS-DEVICES-MIB", "deviceDeploymentState"),
        ("CORERO-CMS-DEVICES-MIB", "deviceDeploymentAction"),
        ("CORERO-CMS-DEVICES-MIB", "deviceSXOSVersion"),
        ("CORERO-CMS-DEVICES-MIB", "deviceSoftwareVersion"),
        ("CORERO-CMS-DEVICES-MIB", "deviceUptime"),
        ("CORERO-CMS-DEVICES-MIB", "deviceStatus"),
        ("CORERO-CMS-DEVICES-MIB", "deviceType"),
        ("CORERO-CMS-DEVICES-MIB", "deviceBypassMode"),
        ("CORERO-CMS-DEVICES-MIB", "deviceHardwareVersion"))
)
if mibBuilder.loadTexts:
    coreroDeviceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

coreroCMSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 1, 2)
)
coreroCMSMIBCompliance.setObjects(
    ("CORERO-CMS-DEVICES-MIB", "coreroDeviceGroup")
)
if mibBuilder.loadTexts:
    coreroCMSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CORERO-CMS-DEVICES-MIB",
    **{"devices": devices,
       "deviceTable": deviceTable,
       "deviceEntry": deviceEntry,
       "deviceIndex": deviceIndex,
       "deviceName": deviceName,
       "deviceAddress": deviceAddress,
       "deviceDescription": deviceDescription,
       "deviceDefenseMode": deviceDefenseMode,
       "deviceAdminState": deviceAdminState,
       "deviceModel": deviceModel,
       "deviceSerialNumber": deviceSerialNumber,
       "deviceConnectionState": deviceConnectionState,
       "deviceDeploymentState": deviceDeploymentState,
       "deviceDeploymentAction": deviceDeploymentAction,
       "deviceSXOSVersion": deviceSXOSVersion,
       "deviceSoftwareVersion": deviceSoftwareVersion,
       "deviceUptime": deviceUptime,
       "deviceStatus": deviceStatus,
       "deviceType": deviceType,
       "deviceBypassMode": deviceBypassMode,
       "deviceHardwareVersion": deviceHardwareVersion,
       "coreroCMSMIBCompliance": coreroCMSMIBCompliance,
       "coreroDeviceGroup": coreroDeviceGroup}
)
