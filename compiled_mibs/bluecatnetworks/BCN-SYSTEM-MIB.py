# SNMP MIB module (BCN-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\BCN-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:30 2025
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

(bcnMgmt,) = mibBuilder.importSymbols(
    "BCN-SMI-MIB",
    "bcnMgmt")

(BcnAlarmSeverity,) = mibBuilder.importSymbols(
    "BCN-TC-MIB",
    "BcnAlarmSeverity")

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

bcnSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 1)
)
if mibBuilder.loadTexts:
    bcnSystemMIB.setRevisions(
        ("2010-11-30 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcnSystem_ObjectIdentity = ObjectIdentity
bcnSystem = _BcnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2)
)
_BcnSystemObjects_ObjectIdentity = ObjectIdentity
bcnSystemObjects = _BcnSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2)
)
_BcnSysIdentification_ObjectIdentity = ObjectIdentity
bcnSysIdentification = _BcnSysIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    bcnSysIdentification.setStatus("current")
_BcnSysIdProduct_Type = ObjectIdentifier
_BcnSysIdProduct_Object = MibScalar
bcnSysIdProduct = _BcnSysIdProduct_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 1),
    _BcnSysIdProduct_Type()
)
bcnSysIdProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnSysIdProduct.setStatus("current")
_BcnSysIdOSRelease_Type = DisplayString
_BcnSysIdOSRelease_Object = MibScalar
bcnSysIdOSRelease = _BcnSysIdOSRelease_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 2),
    _BcnSysIdOSRelease_Type()
)
bcnSysIdOSRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnSysIdOSRelease.setStatus("current")
_BcnSysIdSerial_Type = DisplayString
_BcnSysIdSerial_Object = MibScalar
bcnSysIdSerial = _BcnSysIdSerial_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 3),
    _BcnSysIdSerial_Type()
)
bcnSysIdSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnSysIdSerial.setStatus("current")
_BcnSysIdServiceTag_Type = DisplayString
_BcnSysIdServiceTag_Object = MibScalar
bcnSysIdServiceTag = _BcnSysIdServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 4),
    _BcnSysIdServiceTag_Type()
)
bcnSysIdServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnSysIdServiceTag.setStatus("current")
_BcnSysIdPlatform_Type = DisplayString
_BcnSysIdPlatform_Object = MibScalar
bcnSysIdPlatform = _BcnSysIdPlatform_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 5),
    _BcnSysIdPlatform_Type()
)
bcnSysIdPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnSysIdPlatform.setStatus("current")
_BcnSysIdVendorPlatform_Type = DisplayString
_BcnSysIdVendorPlatform_Object = MibScalar
bcnSysIdVendorPlatform = _BcnSysIdVendorPlatform_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 6),
    _BcnSysIdVendorPlatform_Type()
)
bcnSysIdVendorPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnSysIdVendorPlatform.setStatus("current")
_BcnSysIdServicesTable_Object = MibTable
bcnSysIdServicesTable = _BcnSysIdServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    bcnSysIdServicesTable.setStatus("current")
_BcnSysIdServicesEntry_Object = MibTableRow
bcnSysIdServicesEntry = _BcnSysIdServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1)
)
bcnSysIdServicesEntry.setIndexNames(
    (0, "BCN-SYSTEM-MIB", "bcnSysIdServicesIndex"),
)
if mibBuilder.loadTexts:
    bcnSysIdServicesEntry.setStatus("current")
_BcnSysIdServicesIndex_Type = Unsigned32
_BcnSysIdServicesIndex_Object = MibTableColumn
bcnSysIdServicesIndex = _BcnSysIdServicesIndex_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1, 1),
    _BcnSysIdServicesIndex_Type()
)
bcnSysIdServicesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcnSysIdServicesIndex.setStatus("current")
_BcnSysIdServicesOID_Type = ObjectIdentifier
_BcnSysIdServicesOID_Object = MibTableColumn
bcnSysIdServicesOID = _BcnSysIdServicesOID_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1, 2),
    _BcnSysIdServicesOID_Type()
)
bcnSysIdServicesOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnSysIdServicesOID.setStatus("current")
_BcnSysIdServicesStateTS_Type = TimeStamp
_BcnSysIdServicesStateTS_Object = MibTableColumn
bcnSysIdServicesStateTS = _BcnSysIdServicesStateTS_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1, 3),
    _BcnSysIdServicesStateTS_Type()
)
bcnSysIdServicesStateTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnSysIdServicesStateTS.setStatus("current")
_BcnSysServices_ObjectIdentity = ObjectIdentity
bcnSysServices = _BcnSysServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    bcnSysServices.setStatus("current")
_BcnSysServDNSService_ObjectIdentity = ObjectIdentity
bcnSysServDNSService = _BcnSysServDNSService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 1)
)
_BcnSysServDHCPService_ObjectIdentity = ObjectIdentity
bcnSysServDHCPService = _BcnSysServDHCPService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 2)
)
_BcnSysServTFTPService_ObjectIdentity = ObjectIdentity
bcnSysServTFTPService = _BcnSysServTFTPService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 3)
)
_BcnSysServLicensing_ObjectIdentity = ObjectIdentity
bcnSysServLicensing = _BcnSysServLicensing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 4)
)
_BcnSysServTFTP_ObjectIdentity = ObjectIdentity
bcnSysServTFTP = _BcnSysServTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 5)
)
_BcnSysServNTP_ObjectIdentity = ObjectIdentity
bcnSysServNTP = _BcnSysServNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 6)
)
_BcnSysServPowerSupply_ObjectIdentity = ObjectIdentity
bcnSysServPowerSupply = _BcnSysServPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 7)
)
_BcnSysServNetworkInterface_ObjectIdentity = ObjectIdentity
bcnSysServNetworkInterface = _BcnSysServNetworkInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 8)
)
_BcnSysServHighAvailability_ObjectIdentity = ObjectIdentity
bcnSysServHighAvailability = _BcnSysServHighAvailability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 9)
)
_BcnSysServReplication_ObjectIdentity = ObjectIdentity
bcnSysServReplication = _BcnSysServReplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 10)
)
_BcnSysServSystem_ObjectIdentity = ObjectIdentity
bcnSysServSystem = _BcnSysServSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 11)
)
_BcnSystemNotification_ObjectIdentity = ObjectIdentity
bcnSystemNotification = _BcnSystemNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 3)
)
_BcnSysNotificationEvents_ObjectIdentity = ObjectIdentity
bcnSysNotificationEvents = _BcnSysNotificationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 0)
)
_BcnSysNotificationData_ObjectIdentity = ObjectIdentity
bcnSysNotificationData = _BcnSysNotificationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 1)
)


class _BcnSysSerOperState_Type(Integer32):
    """Custom type bcnSysSerOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("reboot", 2),
          ("shutdown", 3))
    )


_BcnSysSerOperState_Type.__name__ = "Integer32"
_BcnSysSerOperState_Object = MibScalar
bcnSysSerOperState = _BcnSysSerOperState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 1, 1),
    _BcnSysSerOperState_Type()
)
bcnSysSerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnSysSerOperState.setStatus("current")
_BcnSysAlarmSeverity_Type = BcnAlarmSeverity
_BcnSysAlarmSeverity_Object = MibScalar
bcnSysAlarmSeverity = _BcnSysAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 1, 2),
    _BcnSysAlarmSeverity_Type()
)
bcnSysAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnSysAlarmSeverity.setStatus("current")
_BcnSysAlarmInfo_Type = DisplayString
_BcnSysAlarmInfo_Object = MibScalar
bcnSysAlarmInfo = _BcnSysAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 1, 3),
    _BcnSysAlarmInfo_Type()
)
bcnSysAlarmInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnSysAlarmInfo.setStatus("current")
_BcnSystemConformance_ObjectIdentity = ObjectIdentity
bcnSystemConformance = _BcnSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 4)
)
_BcnSysServliances_ObjectIdentity = ObjectIdentity
bcnSysServliances = _BcnSysServliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 1)
)
_BcnSysGroups_ObjectIdentity = ObjectIdentity
bcnSysGroups = _BcnSysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2)
)

# Managed Objects groups

bcnSysIdentificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2, 1)
)
bcnSysIdentificationGroup.setObjects(
      *(("BCN-SYSTEM-MIB", "bcnSysIdProduct"),
        ("BCN-SYSTEM-MIB", "bcnSysIdOSRelease"),
        ("BCN-SYSTEM-MIB", "bcnSysIdSerial"),
        ("BCN-SYSTEM-MIB", "bcnSysIdServiceTag"),
        ("BCN-SYSTEM-MIB", "bcnSysIdPlatform"),
        ("BCN-SYSTEM-MIB", "bcnSysIdVendorPlatform"),
        ("BCN-SYSTEM-MIB", "bcnSysIdServicesOID"),
        ("BCN-SYSTEM-MIB", "bcnSysIdServicesStateTS"))
)
if mibBuilder.loadTexts:
    bcnSysIdentificationGroup.setStatus("current")

bcnSysNotificationDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2, 3)
)
bcnSysNotificationDataGroup.setObjects(
      *(("BCN-SYSTEM-MIB", "bcnSysSerOperState"),
        ("BCN-SYSTEM-MIB", "bcnSysAlarmSeverity"),
        ("BCN-SYSTEM-MIB", "bcnSysAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnSysNotificationDataGroup.setStatus("current")


# Notification objects

bcnSysAlarmNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 0, 1)
)
bcnSysAlarmNotif.setObjects(
      *(("BCN-SYSTEM-MIB", "bcnSysSerOperState"),
        ("BCN-SYSTEM-MIB", "bcnSysAlarmSeverity"),
        ("BCN-SYSTEM-MIB", "bcnSysAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnSysAlarmNotif.setStatus(
        "current"
    )


# Notifications groups

bcnSysNotificationEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2, 2)
)
bcnSysNotificationEventGroup.setObjects(
    ("BCN-SYSTEM-MIB", "bcnSysAlarmNotif")
)
if mibBuilder.loadTexts:
    bcnSysNotificationEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bcnSysServliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 1, 1)
)
bcnSysServliance.setObjects(
      *(("BCN-SYSTEM-MIB", "bcnSysIdentificationGroup"),
        ("BCN-SYSTEM-MIB", "bcnSysNotificationEventGroup"),
        ("BCN-SYSTEM-MIB", "bcnSysNotificationDataGroup"))
)
if mibBuilder.loadTexts:
    bcnSysServliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCN-SYSTEM-MIB",
    **{"bcnSystem": bcnSystem,
       "bcnSystemMIB": bcnSystemMIB,
       "bcnSystemObjects": bcnSystemObjects,
       "bcnSysIdentification": bcnSysIdentification,
       "bcnSysIdProduct": bcnSysIdProduct,
       "bcnSysIdOSRelease": bcnSysIdOSRelease,
       "bcnSysIdSerial": bcnSysIdSerial,
       "bcnSysIdServiceTag": bcnSysIdServiceTag,
       "bcnSysIdPlatform": bcnSysIdPlatform,
       "bcnSysIdVendorPlatform": bcnSysIdVendorPlatform,
       "bcnSysIdServicesTable": bcnSysIdServicesTable,
       "bcnSysIdServicesEntry": bcnSysIdServicesEntry,
       "bcnSysIdServicesIndex": bcnSysIdServicesIndex,
       "bcnSysIdServicesOID": bcnSysIdServicesOID,
       "bcnSysIdServicesStateTS": bcnSysIdServicesStateTS,
       "bcnSysServices": bcnSysServices,
       "bcnSysServDNSService": bcnSysServDNSService,
       "bcnSysServDHCPService": bcnSysServDHCPService,
       "bcnSysServTFTPService": bcnSysServTFTPService,
       "bcnSysServLicensing": bcnSysServLicensing,
       "bcnSysServTFTP": bcnSysServTFTP,
       "bcnSysServNTP": bcnSysServNTP,
       "bcnSysServPowerSupply": bcnSysServPowerSupply,
       "bcnSysServNetworkInterface": bcnSysServNetworkInterface,
       "bcnSysServHighAvailability": bcnSysServHighAvailability,
       "bcnSysServReplication": bcnSysServReplication,
       "bcnSysServSystem": bcnSysServSystem,
       "bcnSystemNotification": bcnSystemNotification,
       "bcnSysNotificationEvents": bcnSysNotificationEvents,
       "bcnSysAlarmNotif": bcnSysAlarmNotif,
       "bcnSysNotificationData": bcnSysNotificationData,
       "bcnSysSerOperState": bcnSysSerOperState,
       "bcnSysAlarmSeverity": bcnSysAlarmSeverity,
       "bcnSysAlarmInfo": bcnSysAlarmInfo,
       "bcnSystemConformance": bcnSystemConformance,
       "bcnSysServliances": bcnSysServliances,
       "bcnSysServliance": bcnSysServliance,
       "bcnSysGroups": bcnSysGroups,
       "bcnSysIdentificationGroup": bcnSysIdentificationGroup,
       "bcnSysNotificationEventGroup": bcnSysNotificationEventGroup,
       "bcnSysNotificationDataGroup": bcnSysNotificationDataGroup}
)
