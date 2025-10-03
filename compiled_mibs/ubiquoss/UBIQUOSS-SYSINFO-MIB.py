# SNMP MIB module (UBIQUOSS-SYSINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBIQUOSS-SYSINFO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:02 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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

(ubiMgmt,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmt")


# MODULE-IDENTITY

ubiSysInfoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiSysInfoMIBObjects_ObjectIdentity = ObjectIdentity
ubiSysInfoMIBObjects = _UbiSysInfoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1)
)
_UbiSysInfoTable_Object = MibTable
ubiSysInfoTable = _UbiSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1)
)
if mibBuilder.loadTexts:
    ubiSysInfoTable.setStatus("mandatory")
_UbiSysInfoEntry_Object = MibTableRow
ubiSysInfoEntry = _UbiSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1)
)
ubiSysInfoEntry.setIndexNames(
    (0, "UBIQUOSS-SYSINFO-MIB", "ubiSysIndex"),
)
if mibBuilder.loadTexts:
    ubiSysInfoEntry.setStatus("mandatory")
_UbiSysIndex_Type = Integer32
_UbiSysIndex_Object = MibTableColumn
ubiSysIndex = _UbiSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 1),
    _UbiSysIndex_Type()
)
ubiSysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysIndex.setStatus("current")


class _UbiSysDescr_Type(DisplayString):
    """Custom type ubiSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UbiSysDescr_Type.__name__ = "DisplayString"
_UbiSysDescr_Object = MibTableColumn
ubiSysDescr = _UbiSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 2),
    _UbiSysDescr_Type()
)
ubiSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysDescr.setStatus("mandatory")
_UbiSysObjectID_Type = ObjectIdentifier
_UbiSysObjectID_Object = MibTableColumn
ubiSysObjectID = _UbiSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 3),
    _UbiSysObjectID_Type()
)
ubiSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysObjectID.setStatus("mandatory")
_UbiSysUpTime_Type = TimeTicks
_UbiSysUpTime_Object = MibTableColumn
ubiSysUpTime = _UbiSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 4),
    _UbiSysUpTime_Type()
)
ubiSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysUpTime.setStatus("mandatory")


class _UbiSysName_Type(DisplayString):
    """Custom type ubiSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UbiSysName_Type.__name__ = "DisplayString"
_UbiSysName_Object = MibTableColumn
ubiSysName = _UbiSysName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 5),
    _UbiSysName_Type()
)
ubiSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysName.setStatus("mandatory")
_UbiSysSerialNumber_Type = DisplayString
_UbiSysSerialNumber_Object = MibTableColumn
ubiSysSerialNumber = _UbiSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 6),
    _UbiSysSerialNumber_Type()
)
ubiSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysSerialNumber.setStatus("current")
_UbiSysMacAddress_Type = PhysAddress
_UbiSysMacAddress_Object = MibTableColumn
ubiSysMacAddress = _UbiSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 7),
    _UbiSysMacAddress_Type()
)
ubiSysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysMacAddress.setStatus("current")
_UbiSysHwVersion_Type = DisplayString
_UbiSysHwVersion_Object = MibTableColumn
ubiSysHwVersion = _UbiSysHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 8),
    _UbiSysHwVersion_Type()
)
ubiSysHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysHwVersion.setStatus("current")
_UbiSysSwVersion_Type = DisplayString
_UbiSysSwVersion_Object = MibTableColumn
ubiSysSwVersion = _UbiSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 9),
    _UbiSysSwVersion_Type()
)
ubiSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysSwVersion.setStatus("current")
_UbiSysFwVersion_Type = DisplayString
_UbiSysFwVersion_Object = MibTableColumn
ubiSysFwVersion = _UbiSysFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 10),
    _UbiSysFwVersion_Type()
)
ubiSysFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysFwVersion.setStatus("current")


class _UbiSysReset_Type(Integer32):
    """Custom type ubiSysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_UbiSysReset_Type.__name__ = "Integer32"
_UbiSysReset_Object = MibTableColumn
ubiSysReset = _UbiSysReset_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 11),
    _UbiSysReset_Type()
)
ubiSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysReset.setStatus("current")


class _UbiSystemDateAndTime_Type(DisplayString):
    """Custom type ubiSystemDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UbiSystemDateAndTime_Type.__name__ = "DisplayString"
_UbiSystemDateAndTime_Object = MibTableColumn
ubiSystemDateAndTime = _UbiSystemDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 12),
    _UbiSystemDateAndTime_Type()
)
ubiSystemDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSystemDateAndTime.setStatus("current")


class _UbiTimeZoneCurrent_Type(DisplayString):
    """Custom type ubiTimeZoneCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UbiTimeZoneCurrent_Type.__name__ = "DisplayString"
_UbiTimeZoneCurrent_Object = MibTableColumn
ubiTimeZoneCurrent = _UbiTimeZoneCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 13),
    _UbiTimeZoneCurrent_Type()
)
ubiTimeZoneCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiTimeZoneCurrent.setStatus("current")


class _UbiSysDayBanner_Type(DisplayString):
    """Custom type ubiSysDayBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UbiSysDayBanner_Type.__name__ = "DisplayString"
_UbiSysDayBanner_Object = MibTableColumn
ubiSysDayBanner = _UbiSysDayBanner_Object(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 1, 1, 1, 14),
    _UbiSysDayBanner_Type()
)
ubiSysDayBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysDayBanner.setStatus("current")
_UbiSysInfoMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiSysInfoMIBNotificationPrefix = _UbiSysInfoMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 2)
)
_UbiSysInfoMIBNotifications_ObjectIdentity = ObjectIdentity
ubiSysInfoMIBNotifications = _UbiSysInfoMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 2, 0)
)
_UbiSysInfoMIBConformance_ObjectIdentity = ObjectIdentity
ubiSysInfoMIBConformance = _UbiSysInfoMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 3)
)
_UbiSysInfoMIBCompliances_ObjectIdentity = ObjectIdentity
ubiSysInfoMIBCompliances = _UbiSysInfoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 3, 1)
)
_UbiSysInfoMonMIBGroups_ObjectIdentity = ObjectIdentity
ubiSysInfoMonMIBGroups = _UbiSysInfoMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 3, 2)
)

# Managed Objects groups

ubiSysInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 3, 2, 1)
)
ubiSysInfoMIBGroup.setObjects(
      *(("UBIQUOSS-SYSINFO-MIB", "ubiSysDescr"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysObjectID"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysUpTime"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysName"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysSerialNumber"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysMacAddress"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysHwVersion"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysSwVersion"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysFwVersion"))
)
if mibBuilder.loadTexts:
    ubiSysInfoMIBGroup.setStatus("current")


# Notification objects

ubiSysAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 2, 0, 1)
)
ubiSysAlarmNotification.setObjects(
      *(("UBIQUOSS-SYSINFO-MIB", "ubiAlarmIndex"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiAlarmId"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiAlarmType"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiAlarmSeverity"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiAlarmPhysicalLoc"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiAlarmLogicalLoc"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiAlarmCurStatus"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiAlarmAuxinfo"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiAlarmDateTime"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiAlarmStatus"))
)
if mibBuilder.loadTexts:
    ubiSysAlarmNotification.setStatus(
        "current"
    )


# Notifications groups

ubiSysInfoMIBAlarmNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 3, 2, 2)
)
ubiSysInfoMIBAlarmNotifGroup.setObjects(
    ("UBIQUOSS-SYSINFO-MIB", "ubiSysAlarmNotification")
)
if mibBuilder.loadTexts:
    ubiSysInfoMIBAlarmNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ubiSysInfoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 2, 100, 3, 1, 1)
)
ubiSysInfoMIBCompliance.setObjects(
      *(("UBIQUOSS-SYSINFO-MIB", "ubiSysInfoMIBGroup"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysInfoMIBAlarmNotifGroup"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysInfoMIBGroup"),
        ("UBIQUOSS-SYSINFO-MIB", "ubiSysInfoMIBAlarmNotifGroup"))
)
if mibBuilder.loadTexts:
    ubiSysInfoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBIQUOSS-SYSINFO-MIB",
    **{"ubiSysInfoMIB": ubiSysInfoMIB,
       "ubiSysInfoMIBObjects": ubiSysInfoMIBObjects,
       "ubiSysInfoTable": ubiSysInfoTable,
       "ubiSysInfoEntry": ubiSysInfoEntry,
       "ubiSysIndex": ubiSysIndex,
       "ubiSysDescr": ubiSysDescr,
       "ubiSysObjectID": ubiSysObjectID,
       "ubiSysUpTime": ubiSysUpTime,
       "ubiSysName": ubiSysName,
       "ubiSysSerialNumber": ubiSysSerialNumber,
       "ubiSysMacAddress": ubiSysMacAddress,
       "ubiSysHwVersion": ubiSysHwVersion,
       "ubiSysSwVersion": ubiSysSwVersion,
       "ubiSysFwVersion": ubiSysFwVersion,
       "ubiSysReset": ubiSysReset,
       "ubiSystemDateAndTime": ubiSystemDateAndTime,
       "ubiTimeZoneCurrent": ubiTimeZoneCurrent,
       "ubiSysDayBanner": ubiSysDayBanner,
       "ubiSysInfoMIBNotificationPrefix": ubiSysInfoMIBNotificationPrefix,
       "ubiSysInfoMIBNotifications": ubiSysInfoMIBNotifications,
       "ubiSysAlarmNotification": ubiSysAlarmNotification,
       "ubiSysInfoMIBConformance": ubiSysInfoMIBConformance,
       "ubiSysInfoMIBCompliances": ubiSysInfoMIBCompliances,
       "ubiSysInfoMIBCompliance": ubiSysInfoMIBCompliance,
       "ubiSysInfoMonMIBGroups": ubiSysInfoMonMIBGroups,
       "ubiSysInfoMIBGroup": ubiSysInfoMIBGroup,
       "ubiSysInfoMIBAlarmNotifGroup": ubiSysInfoMIBAlarmNotifGroup}
)
