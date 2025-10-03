# SNMP MIB module (BLUECOAT-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecoat\BLUECOAT-LICENSE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:33 2025
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

appLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16)
)
if mibBuilder.loadTexts:
    appLicenseMIB.setRevisions(
        ("2015-01-13 03:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LicenseState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("active", 1),
          ("expired", 2))
    )



class LicenseExpireType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("perpetual", 1),
          ("subscription", 2),
          ("demo", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AppLicenseMIBObjects_ObjectIdentity = ObjectIdentity
appLicenseMIBObjects = _AppLicenseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1)
)
_AppLicense_ObjectIdentity = ObjectIdentity
appLicense = _AppLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1)
)
_AppLicenseStatusTable_Object = MibTable
appLicenseStatusTable = _AppLicenseStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    appLicenseStatusTable.setStatus("current")
_AppLicenseStatusEntry_Object = MibTableRow
appLicenseStatusEntry = _AppLicenseStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1)
)
appLicenseStatusEntry.setIndexNames(
    (0, "BLUECOAT-LICENSE-MIB", "appLicenseStatusIndex"),
)
if mibBuilder.loadTexts:
    appLicenseStatusEntry.setStatus("current")


class _AppLicenseStatusIndex_Type(Integer32):
    """Custom type appLicenseStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AppLicenseStatusIndex_Type.__name__ = "Integer32"
_AppLicenseStatusIndex_Object = MibTableColumn
appLicenseStatusIndex = _AppLicenseStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 1),
    _AppLicenseStatusIndex_Type()
)
appLicenseStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appLicenseStatusIndex.setStatus("current")
_AppLicenseStatusApplicationName_Type = DisplayString
_AppLicenseStatusApplicationName_Object = MibTableColumn
appLicenseStatusApplicationName = _AppLicenseStatusApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 2),
    _AppLicenseStatusApplicationName_Type()
)
appLicenseStatusApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLicenseStatusApplicationName.setStatus("current")
_AppLicenseStatusFeatureName_Type = DisplayString
_AppLicenseStatusFeatureName_Object = MibTableColumn
appLicenseStatusFeatureName = _AppLicenseStatusFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 3),
    _AppLicenseStatusFeatureName_Type()
)
appLicenseStatusFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLicenseStatusFeatureName.setStatus("current")
_AppLicenseStatusComponentName_Type = DisplayString
_AppLicenseStatusComponentName_Object = MibTableColumn
appLicenseStatusComponentName = _AppLicenseStatusComponentName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 4),
    _AppLicenseStatusComponentName_Type()
)
appLicenseStatusComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLicenseStatusComponentName.setStatus("current")
_AppLicenseStatusExpireType_Type = LicenseExpireType
_AppLicenseStatusExpireType_Object = MibTableColumn
appLicenseStatusExpireType = _AppLicenseStatusExpireType_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 5),
    _AppLicenseStatusExpireType_Type()
)
appLicenseStatusExpireType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLicenseStatusExpireType.setStatus("current")
_AppLicenseStatusExpireDate_Type = DateAndTime
_AppLicenseStatusExpireDate_Object = MibTableColumn
appLicenseStatusExpireDate = _AppLicenseStatusExpireDate_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 6),
    _AppLicenseStatusExpireDate_Type()
)
appLicenseStatusExpireDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLicenseStatusExpireDate.setStatus("current")
_AppLicenseStatusLicenseState_Type = LicenseState
_AppLicenseStatusLicenseState_Object = MibTableColumn
appLicenseStatusLicenseState = _AppLicenseStatusLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 7),
    _AppLicenseStatusLicenseState_Type()
)
appLicenseStatusLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLicenseStatusLicenseState.setStatus("current")
_AppLicenseMIBNotifications_ObjectIdentity = ObjectIdentity
appLicenseMIBNotifications = _AppLicenseMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 2)
)
_AppLicenseMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
appLicenseMIBNotificationsPrefix = _AppLicenseMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 2, 0)
)
_AppLicenseMIBConformance_ObjectIdentity = ObjectIdentity
appLicenseMIBConformance = _AppLicenseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 3)
)
_AppLicenseMIBCompliances_ObjectIdentity = ObjectIdentity
appLicenseMIBCompliances = _AppLicenseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 1)
)
_AppLicenseMIBGroups_ObjectIdentity = ObjectIdentity
appLicenseMIBGroups = _AppLicenseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 2)
)
_AppLicenseMIBNotifGroups_ObjectIdentity = ObjectIdentity
appLicenseMIBNotifGroups = _AppLicenseMIBNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 3)
)

# Managed Objects groups

appLicenseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 2, 1)
)
appLicenseMIBGroup.setObjects(
      *(("BLUECOAT-LICENSE-MIB", "appLicenseStatusApplicationName"),
        ("BLUECOAT-LICENSE-MIB", "appLicenseStatusFeatureName"),
        ("BLUECOAT-LICENSE-MIB", "appLicenseStatusComponentName"),
        ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireType"),
        ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireDate"),
        ("BLUECOAT-LICENSE-MIB", "appLicenseStatusLicenseState"))
)
if mibBuilder.loadTexts:
    appLicenseMIBGroup.setStatus("current")


# Notification objects

appLicenseStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 2, 0, 1)
)
appLicenseStateTrap.setObjects(
      *(("BLUECOAT-LICENSE-MIB", "appLicenseStatusApplicationName"),
        ("BLUECOAT-LICENSE-MIB", "appLicenseStatusFeatureName"),
        ("BLUECOAT-LICENSE-MIB", "appLicenseStatusComponentName"),
        ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireType"),
        ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireDate"),
        ("BLUECOAT-LICENSE-MIB", "appLicenseStatusLicenseState"))
)
if mibBuilder.loadTexts:
    appLicenseStateTrap.setStatus(
        "current"
    )


# Notifications groups

appLicenseMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 3, 1)
)
appLicenseMIBNotifGroup.setObjects(
    ("BLUECOAT-LICENSE-MIB", "appLicenseStateTrap")
)
if mibBuilder.loadTexts:
    appLicenseMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

appLicenseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 1, 1)
)
appLicenseMIBCompliance.setObjects(
    ("BLUECOAT-LICENSE-MIB", "appLicenseMIBGroup")
)
if mibBuilder.loadTexts:
    appLicenseMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-LICENSE-MIB",
    **{"LicenseState": LicenseState,
       "LicenseExpireType": LicenseExpireType,
       "appLicenseMIB": appLicenseMIB,
       "appLicenseMIBObjects": appLicenseMIBObjects,
       "appLicense": appLicense,
       "appLicenseStatusTable": appLicenseStatusTable,
       "appLicenseStatusEntry": appLicenseStatusEntry,
       "appLicenseStatusIndex": appLicenseStatusIndex,
       "appLicenseStatusApplicationName": appLicenseStatusApplicationName,
       "appLicenseStatusFeatureName": appLicenseStatusFeatureName,
       "appLicenseStatusComponentName": appLicenseStatusComponentName,
       "appLicenseStatusExpireType": appLicenseStatusExpireType,
       "appLicenseStatusExpireDate": appLicenseStatusExpireDate,
       "appLicenseStatusLicenseState": appLicenseStatusLicenseState,
       "appLicenseMIBNotifications": appLicenseMIBNotifications,
       "appLicenseMIBNotificationsPrefix": appLicenseMIBNotificationsPrefix,
       "appLicenseStateTrap": appLicenseStateTrap,
       "appLicenseMIBConformance": appLicenseMIBConformance,
       "appLicenseMIBCompliances": appLicenseMIBCompliances,
       "appLicenseMIBCompliance": appLicenseMIBCompliance,
       "appLicenseMIBGroups": appLicenseMIBGroups,
       "appLicenseMIBGroup": appLicenseMIBGroup,
       "appLicenseMIBNotifGroups": appLicenseMIBNotifGroups,
       "appLicenseMIBNotifGroup": appLicenseMIBNotifGroup}
)
