# SNMP MIB module (BCN-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\BCN-LICENSE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:27 2025
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

(bcnServices,) = mibBuilder.importSymbols(
    "BCN-SMI-MIB",
    "bcnServices")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bcnLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    bcnLicenseMIB.setRevisions(
        ("2010-11-30 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcnLicense_ObjectIdentity = ObjectIdentity
bcnLicense = _BcnLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6)
)
_BcnLicenseObjects_ObjectIdentity = ObjectIdentity
bcnLicenseObjects = _BcnLicenseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2)
)
_BcnLicenseInformation_ObjectIdentity = ObjectIdentity
bcnLicenseInformation = _BcnLicenseInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    bcnLicenseInformation.setStatus("current")
_BcnLicenseTable_Object = MibTable
bcnLicenseTable = _BcnLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    bcnLicenseTable.setStatus("current")
_BcnLicenseEntry_Object = MibTableRow
bcnLicenseEntry = _BcnLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1)
)
bcnLicenseEntry.setIndexNames(
    (0, "BCN-LICENSE-MIB", "bcnLicenseTableIndex"),
)
if mibBuilder.loadTexts:
    bcnLicenseEntry.setStatus("current")
_BcnLicenseTableIndex_Type = Unsigned32
_BcnLicenseTableIndex_Object = MibTableColumn
bcnLicenseTableIndex = _BcnLicenseTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 1),
    _BcnLicenseTableIndex_Type()
)
bcnLicenseTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcnLicenseTableIndex.setStatus("current")


class _BcnLicenseType_Type(Integer32):
    """Custom type bcnLicenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleServer", 1),
          ("multiServer", 2))
    )


_BcnLicenseType_Type.__name__ = "Integer32"
_BcnLicenseType_Object = MibTableColumn
bcnLicenseType = _BcnLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 2),
    _BcnLicenseType_Type()
)
bcnLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnLicenseType.setStatus("current")
_BcnLicenseDescription_Type = DisplayString
_BcnLicenseDescription_Object = MibTableColumn
bcnLicenseDescription = _BcnLicenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 3),
    _BcnLicenseDescription_Type()
)
bcnLicenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnLicenseDescription.setStatus("current")
_BcnLicenseInstalled_Type = DateAndTime
_BcnLicenseInstalled_Object = MibTableColumn
bcnLicenseInstalled = _BcnLicenseInstalled_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 4),
    _BcnLicenseInstalled_Type()
)
bcnLicenseInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnLicenseInstalled.setStatus("current")
_BcnLicenseExpiry_Type = DateAndTime
_BcnLicenseExpiry_Object = MibTableColumn
bcnLicenseExpiry = _BcnLicenseExpiry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 5),
    _BcnLicenseExpiry_Type()
)
bcnLicenseExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnLicenseExpiry.setStatus("current")
_BcnLicenseGracePeriod_Type = Unsigned32
_BcnLicenseGracePeriod_Object = MibTableColumn
bcnLicenseGracePeriod = _BcnLicenseGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 6),
    _BcnLicenseGracePeriod_Type()
)
bcnLicenseGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnLicenseGracePeriod.setStatus("current")
_BcnLicenseValid_Type = TruthValue
_BcnLicenseValid_Object = MibTableColumn
bcnLicenseValid = _BcnLicenseValid_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 7),
    _BcnLicenseValid_Type()
)
bcnLicenseValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnLicenseValid.setStatus("current")
_BcnLicenseItemsGranted_Type = Unsigned32
_BcnLicenseItemsGranted_Object = MibTableColumn
bcnLicenseItemsGranted = _BcnLicenseItemsGranted_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 8),
    _BcnLicenseItemsGranted_Type()
)
bcnLicenseItemsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnLicenseItemsGranted.setStatus("current")
_BcnLicenseItemsUsed_Type = Unsigned32
_BcnLicenseItemsUsed_Object = MibTableColumn
bcnLicenseItemsUsed = _BcnLicenseItemsUsed_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 9),
    _BcnLicenseItemsUsed_Type()
)
bcnLicenseItemsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnLicenseItemsUsed.setStatus("current")
_BcnLicenseNotification_ObjectIdentity = ObjectIdentity
bcnLicenseNotification = _BcnLicenseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3)
)
_BcnLicenseNotificationEvents_ObjectIdentity = ObjectIdentity
bcnLicenseNotificationEvents = _BcnLicenseNotificationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 0)
)
_BcnLicenseNotificationData_ObjectIdentity = ObjectIdentity
bcnLicenseNotificationData = _BcnLicenseNotificationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 1)
)
_BcnLicenseAlarmSeverity_Type = BcnAlarmSeverity
_BcnLicenseAlarmSeverity_Object = MibScalar
bcnLicenseAlarmSeverity = _BcnLicenseAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 1, 1),
    _BcnLicenseAlarmSeverity_Type()
)
bcnLicenseAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnLicenseAlarmSeverity.setStatus("current")
_BcnLicenseConformance_ObjectIdentity = ObjectIdentity
bcnLicenseConformance = _BcnLicenseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4)
)
_BcnLicenseServiceCompliances_ObjectIdentity = ObjectIdentity
bcnLicenseServiceCompliances = _BcnLicenseServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 1)
)
_BcnLicenseServiceGroups_ObjectIdentity = ObjectIdentity
bcnLicenseServiceGroups = _BcnLicenseServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2)
)

# Managed Objects groups

bcnLicenseServiceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2, 1)
)
bcnLicenseServiceStatusGroup.setObjects(
      *(("BCN-LICENSE-MIB", "bcnLicenseType"),
        ("BCN-LICENSE-MIB", "bcnLicenseDescription"),
        ("BCN-LICENSE-MIB", "bcnLicenseInstalled"),
        ("BCN-LICENSE-MIB", "bcnLicenseExpiry"),
        ("BCN-LICENSE-MIB", "bcnLicenseGracePeriod"),
        ("BCN-LICENSE-MIB", "bcnLicenseValid"),
        ("BCN-LICENSE-MIB", "bcnLicenseItemsGranted"),
        ("BCN-LICENSE-MIB", "bcnLicenseItemsUsed"))
)
if mibBuilder.loadTexts:
    bcnLicenseServiceStatusGroup.setStatus("current")

bcnLicenseNotificationDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2, 3)
)
bcnLicenseNotificationDataGroup.setObjects(
    ("BCN-LICENSE-MIB", "bcnLicenseAlarmSeverity")
)
if mibBuilder.loadTexts:
    bcnLicenseNotificationDataGroup.setStatus("current")


# Notification objects

bcnLicenseExpiryNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 0, 1)
)
bcnLicenseExpiryNotif.setObjects(
      *(("BCN-LICENSE-MIB", "bcnLicenseType"),
        ("BCN-LICENSE-MIB", "bcnLicenseAlarmSeverity"),
        ("BCN-LICENSE-MIB", "bcnLicenseExpiry"),
        ("BCN-LICENSE-MIB", "bcnLicenseGracePeriod"),
        ("BCN-LICENSE-MIB", "bcnLicenseValid"))
)
if mibBuilder.loadTexts:
    bcnLicenseExpiryNotif.setStatus(
        "current"
    )


# Notifications groups

bcnLicenseNotificationEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2, 2)
)
bcnLicenseNotificationEventGroup.setObjects(
    ("BCN-LICENSE-MIB", "bcnLicenseExpiryNotif")
)
if mibBuilder.loadTexts:
    bcnLicenseNotificationEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bcnLicenseStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 1, 1)
)
bcnLicenseStatusCompliance.setObjects(
      *(("BCN-LICENSE-MIB", "bcnLicenseServiceStatusGroup"),
        ("BCN-LICENSE-MIB", "bcnLicenseNotificationEventGroup"),
        ("BCN-LICENSE-MIB", "bcnLicenseNotificationDataGroup"))
)
if mibBuilder.loadTexts:
    bcnLicenseStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCN-LICENSE-MIB",
    **{"bcnLicense": bcnLicense,
       "bcnLicenseMIB": bcnLicenseMIB,
       "bcnLicenseObjects": bcnLicenseObjects,
       "bcnLicenseInformation": bcnLicenseInformation,
       "bcnLicenseTable": bcnLicenseTable,
       "bcnLicenseEntry": bcnLicenseEntry,
       "bcnLicenseTableIndex": bcnLicenseTableIndex,
       "bcnLicenseType": bcnLicenseType,
       "bcnLicenseDescription": bcnLicenseDescription,
       "bcnLicenseInstalled": bcnLicenseInstalled,
       "bcnLicenseExpiry": bcnLicenseExpiry,
       "bcnLicenseGracePeriod": bcnLicenseGracePeriod,
       "bcnLicenseValid": bcnLicenseValid,
       "bcnLicenseItemsGranted": bcnLicenseItemsGranted,
       "bcnLicenseItemsUsed": bcnLicenseItemsUsed,
       "bcnLicenseNotification": bcnLicenseNotification,
       "bcnLicenseNotificationEvents": bcnLicenseNotificationEvents,
       "bcnLicenseExpiryNotif": bcnLicenseExpiryNotif,
       "bcnLicenseNotificationData": bcnLicenseNotificationData,
       "bcnLicenseAlarmSeverity": bcnLicenseAlarmSeverity,
       "bcnLicenseConformance": bcnLicenseConformance,
       "bcnLicenseServiceCompliances": bcnLicenseServiceCompliances,
       "bcnLicenseStatusCompliance": bcnLicenseStatusCompliance,
       "bcnLicenseServiceGroups": bcnLicenseServiceGroups,
       "bcnLicenseServiceStatusGroup": bcnLicenseServiceStatusGroup,
       "bcnLicenseNotificationEventGroup": bcnLicenseNotificationEventGroup,
       "bcnLicenseNotificationDataGroup": bcnLicenseNotificationDataGroup}
)
