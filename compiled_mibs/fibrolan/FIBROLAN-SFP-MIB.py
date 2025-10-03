# SNMP MIB module (FIBROLAN-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-SFP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:31 2025
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

(fibrolanGeneric,) = mibBuilder.importSymbols(
    "FIBROLAN-COMMON-MIB",
    "fibrolanGeneric")

(flDeviceNotifications,) = mibBuilder.importSymbols(
    "FIBROLAN-DEVICE-MIB",
    "flDeviceNotifications")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

flSfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50)
)
if mibBuilder.loadTexts:
    flSfp.setRevisions(
        ("2014-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FlSfpMIBObjects_ObjectIdentity = ObjectIdentity
flSfpMIBObjects = _FlSfpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1)
)
_FlSfpInfoTable_Object = MibTable
flSfpInfoTable = _FlSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1)
)
if mibBuilder.loadTexts:
    flSfpInfoTable.setStatus("current")
_FlSfpInfoEntry_Object = MibTableRow
flSfpInfoEntry = _FlSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1)
)
flSfpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    flSfpInfoEntry.setStatus("current")
_FlSfpVendor_Type = DisplayString
_FlSfpVendor_Object = MibTableColumn
flSfpVendor = _FlSfpVendor_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 1),
    _FlSfpVendor_Type()
)
flSfpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpVendor.setStatus("current")
_FlSfpPartNumber_Type = DisplayString
_FlSfpPartNumber_Object = MibTableColumn
flSfpPartNumber = _FlSfpPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 2),
    _FlSfpPartNumber_Type()
)
flSfpPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpPartNumber.setStatus("current")
_FlSfpSerialNumber_Type = DisplayString
_FlSfpSerialNumber_Object = MibTableColumn
flSfpSerialNumber = _FlSfpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 3),
    _FlSfpSerialNumber_Type()
)
flSfpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpSerialNumber.setStatus("current")
_FlSfpType_Type = DisplayString
_FlSfpType_Object = MibTableColumn
flSfpType = _FlSfpType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 4),
    _FlSfpType_Type()
)
flSfpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpType.setStatus("current")
_FlSfpMaxRate_Type = Integer32
_FlSfpMaxRate_Object = MibTableColumn
flSfpMaxRate = _FlSfpMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 5),
    _FlSfpMaxRate_Type()
)
flSfpMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpMaxRate.setStatus("current")
_FlSfpRange_Type = Integer32
_FlSfpRange_Object = MibTableColumn
flSfpRange = _FlSfpRange_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 6),
    _FlSfpRange_Type()
)
flSfpRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpRange.setStatus("current")
_FlSfpTxWl_Type = Integer32
_FlSfpTxWl_Object = MibTableColumn
flSfpTxWl = _FlSfpTxWl_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 7),
    _FlSfpTxWl_Type()
)
flSfpTxWl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpTxWl.setStatus("current")
_FlSfpTxWlFraction_Type = Integer32
_FlSfpTxWlFraction_Object = MibTableColumn
flSfpTxWlFraction = _FlSfpTxWlFraction_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 8),
    _FlSfpTxWlFraction_Type()
)
flSfpTxWlFraction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpTxWlFraction.setStatus("current")
_FlSfpRxWl_Type = Integer32
_FlSfpRxWl_Object = MibTableColumn
flSfpRxWl = _FlSfpRxWl_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 9),
    _FlSfpRxWl_Type()
)
flSfpRxWl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpRxWl.setStatus("current")
_FlSfpRxWlFraction_Type = Integer32
_FlSfpRxWlFraction_Object = MibTableColumn
flSfpRxWlFraction = _FlSfpRxWlFraction_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 10),
    _FlSfpRxWlFraction_Type()
)
flSfpRxWlFraction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpRxWlFraction.setStatus("current")


class _FlSfpDdmSupport_Type(Integer32):
    """Custom type flSfpDdmSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ddmSupported", 1),
          ("ddmNotSupported", 2))
    )


_FlSfpDdmSupport_Type.__name__ = "Integer32"
_FlSfpDdmSupport_Object = MibTableColumn
flSfpDdmSupport = _FlSfpDdmSupport_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 1, 1, 11),
    _FlSfpDdmSupport_Type()
)
flSfpDdmSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDdmSupport.setStatus("current")
_FlSfpMonitoringTable_Object = MibTable
flSfpMonitoringTable = _FlSfpMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 2)
)
if mibBuilder.loadTexts:
    flSfpMonitoringTable.setStatus("current")
_FlSfpMonitoringEntry_Object = MibTableRow
flSfpMonitoringEntry = _FlSfpMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 2, 1)
)
flSfpMonitoringEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    flSfpMonitoringEntry.setStatus("current")
_FlSfpRxPower_Type = Integer32
_FlSfpRxPower_Object = MibTableColumn
flSfpRxPower = _FlSfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 2, 1, 1),
    _FlSfpRxPower_Type()
)
flSfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpRxPower.setStatus("current")
if mibBuilder.loadTexts:
    flSfpRxPower.setUnits("micro Watts")
_FlSfpTxPower_Type = Integer32
_FlSfpTxPower_Object = MibTableColumn
flSfpTxPower = _FlSfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 2, 1, 2),
    _FlSfpTxPower_Type()
)
flSfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpTxPower.setStatus("current")
if mibBuilder.loadTexts:
    flSfpTxPower.setUnits("micro Watts")
_FlSfpTemperature_Type = Integer32
_FlSfpTemperature_Object = MibTableColumn
flSfpTemperature = _FlSfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 2, 1, 3),
    _FlSfpTemperature_Type()
)
flSfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpTemperature.setStatus("current")
if mibBuilder.loadTexts:
    flSfpTemperature.setUnits("Degrees Celsius (oC)")
_FlSfpBiasCurrent_Type = Integer32
_FlSfpBiasCurrent_Object = MibTableColumn
flSfpBiasCurrent = _FlSfpBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 2, 1, 4),
    _FlSfpBiasCurrent_Type()
)
flSfpBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    flSfpBiasCurrent.setUnits("milliampere")
_FlSfpSupplyVoltage_Type = Integer32
_FlSfpSupplyVoltage_Object = MibTableColumn
flSfpSupplyVoltage = _FlSfpSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 2, 1, 5),
    _FlSfpSupplyVoltage_Type()
)
flSfpSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpSupplyVoltage.setStatus("current")
if mibBuilder.loadTexts:
    flSfpSupplyVoltage.setUnits("millivolt")


class _FlSfpAlarmStatus_Type(Integer32):
    """Custom type flSfpAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FlSfpAlarmStatus_Type.__name__ = "Integer32"
_FlSfpAlarmStatus_Object = MibTableColumn
flSfpAlarmStatus = _FlSfpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 2, 1, 6),
    _FlSfpAlarmStatus_Type()
)
flSfpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpAlarmStatus.setStatus("current")
_FlSfpStatusLastChange_Type = TimeStamp
_FlSfpStatusLastChange_Object = MibTableColumn
flSfpStatusLastChange = _FlSfpStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 1, 2, 1, 7),
    _FlSfpStatusLastChange_Type()
)
flSfpStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpStatusLastChange.setStatus("current")
_FlSfpMIBConformance_ObjectIdentity = ObjectIdentity
flSfpMIBConformance = _FlSfpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 2)
)
_FlSfpMIBCompliances_ObjectIdentity = ObjectIdentity
flSfpMIBCompliances = _FlSfpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 2, 1)
)
_FlSfpMIBGroups_ObjectIdentity = ObjectIdentity
flSfpMIBGroups = _FlSfpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 2, 2)
)
_FlSfpTraps_ObjectIdentity = ObjectIdentity
flSfpTraps = _FlSfpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 10)
)

# Managed Objects groups

flSfpDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 2, 2, 1)
)
flSfpDeviceGroup.setObjects(
      *(("FIBROLAN-SFP-MIB", "flSfpVendor"),
        ("FIBROLAN-SFP-MIB", "flSfpPartNumber"),
        ("FIBROLAN-SFP-MIB", "flSfpSerialNumber"),
        ("FIBROLAN-SFP-MIB", "flSfpType"),
        ("FIBROLAN-SFP-MIB", "flSfpMaxRate"),
        ("FIBROLAN-SFP-MIB", "flSfpRange"),
        ("FIBROLAN-SFP-MIB", "flSfpTxWl"),
        ("FIBROLAN-SFP-MIB", "flSfpTxWlFraction"),
        ("FIBROLAN-SFP-MIB", "flSfpRxWl"),
        ("FIBROLAN-SFP-MIB", "flSfpRxWlFraction"),
        ("FIBROLAN-SFP-MIB", "flSfpDdmSupport"))
)
if mibBuilder.loadTexts:
    flSfpDeviceGroup.setStatus("current")

flSfpMonitoringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 2, 2, 2)
)
flSfpMonitoringGroup.setObjects(
      *(("FIBROLAN-SFP-MIB", "flSfpRxPower"),
        ("FIBROLAN-SFP-MIB", "flSfpTxPower"),
        ("FIBROLAN-SFP-MIB", "flSfpTemperature"),
        ("FIBROLAN-SFP-MIB", "flSfpBiasCurrent"),
        ("FIBROLAN-SFP-MIB", "flSfpSupplyVoltage"),
        ("FIBROLAN-SFP-MIB", "flSfpAlarmStatus"),
        ("FIBROLAN-SFP-MIB", "flSfpStatusLastChange"))
)
if mibBuilder.loadTexts:
    flSfpMonitoringGroup.setStatus("current")


# Notification objects

flSfpPluggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 0, 17)
)
if mibBuilder.loadTexts:
    flSfpPluggedIn.setStatus(
        "current"
    )

flSfpUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 10, 0, 18)
)
if mibBuilder.loadTexts:
    flSfpUnplugged.setStatus(
        "current"
    )

flSfpAlarmStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 10, 0, 1)
)
flSfpAlarmStatusChange.setObjects(
      *(("FIBROLAN-SFP-MIB", "flSfpAlarmStatus"),
        ("FIBROLAN-SFP-MIB", "flSfpStatusLastChange"))
)
if mibBuilder.loadTexts:
    flSfpAlarmStatusChange.setStatus(
        "current"
    )


# Notifications groups

flSfpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 2, 2, 3)
)
flSfpNotificationsGroup.setObjects(
    ("FIBROLAN-SFP-MIB", "flSfpAlarmStatusChange")
)
if mibBuilder.loadTexts:
    flSfpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

flSfpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 50, 2, 1, 1)
)
flSfpMIBCompliance.setObjects(
      *(("FIBROLAN-SFP-MIB", "flSfpDeviceGroup"),
        ("FIBROLAN-SFP-MIB", "flSfpMonitoringGroup"),
        ("FIBROLAN-SFP-MIB", "flSfpNotificationsGroup"))
)
if mibBuilder.loadTexts:
    flSfpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-SFP-MIB",
    **{"flSfpPluggedIn": flSfpPluggedIn,
       "flSfpUnplugged": flSfpUnplugged,
       "flSfp": flSfp,
       "flSfpMIBObjects": flSfpMIBObjects,
       "flSfpInfoTable": flSfpInfoTable,
       "flSfpInfoEntry": flSfpInfoEntry,
       "flSfpVendor": flSfpVendor,
       "flSfpPartNumber": flSfpPartNumber,
       "flSfpSerialNumber": flSfpSerialNumber,
       "flSfpType": flSfpType,
       "flSfpMaxRate": flSfpMaxRate,
       "flSfpRange": flSfpRange,
       "flSfpTxWl": flSfpTxWl,
       "flSfpTxWlFraction": flSfpTxWlFraction,
       "flSfpRxWl": flSfpRxWl,
       "flSfpRxWlFraction": flSfpRxWlFraction,
       "flSfpDdmSupport": flSfpDdmSupport,
       "flSfpMonitoringTable": flSfpMonitoringTable,
       "flSfpMonitoringEntry": flSfpMonitoringEntry,
       "flSfpRxPower": flSfpRxPower,
       "flSfpTxPower": flSfpTxPower,
       "flSfpTemperature": flSfpTemperature,
       "flSfpBiasCurrent": flSfpBiasCurrent,
       "flSfpSupplyVoltage": flSfpSupplyVoltage,
       "flSfpAlarmStatus": flSfpAlarmStatus,
       "flSfpStatusLastChange": flSfpStatusLastChange,
       "flSfpMIBConformance": flSfpMIBConformance,
       "flSfpMIBCompliances": flSfpMIBCompliances,
       "flSfpMIBCompliance": flSfpMIBCompliance,
       "flSfpMIBGroups": flSfpMIBGroups,
       "flSfpDeviceGroup": flSfpDeviceGroup,
       "flSfpMonitoringGroup": flSfpMonitoringGroup,
       "flSfpNotificationsGroup": flSfpNotificationsGroup,
       "flSfpTraps": flSfpTraps,
       "flSfpAlarmStatusChange": flSfpAlarmStatusChange}
)
