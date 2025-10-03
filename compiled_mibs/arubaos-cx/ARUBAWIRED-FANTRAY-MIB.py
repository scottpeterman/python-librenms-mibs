# SNMP MIB module (ARUBAWIRED-FANTRAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-FANTRAY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:07 2025
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

(arubaWiredChassisMIB,) = mibBuilder.importSymbols(
    "ARUBAWIRED-CHASSIS-MIB",
    "arubaWiredChassisMIB")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

arubaWiredFanTray = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4)
)
if mibBuilder.loadTexts:
    arubaWiredFanTray.setRevisions(
        ("2023-03-31 00:00",
         "2020-02-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredFanTrayNotifications_ObjectIdentity = ObjectIdentity
arubaWiredFanTrayNotifications = _ArubaWiredFanTrayNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 0)
)
_ArubaWiredFanTrayTable_Object = MibTable
arubaWiredFanTrayTable = _ArubaWiredFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1)
)
if mibBuilder.loadTexts:
    arubaWiredFanTrayTable.setStatus("current")
_ArubaWiredFanTrayEntry_Object = MibTableRow
arubaWiredFanTrayEntry = _ArubaWiredFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1)
)
arubaWiredFanTrayEntry.setIndexNames(
    (0, "ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayGroupIndex"),
    (0, "ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTraySlotIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredFanTrayEntry.setStatus("current")


class _ArubaWiredFanTrayGroupIndex_Type(Integer32):
    """Custom type arubaWiredFanTrayGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredFanTrayGroupIndex_Type.__name__ = "Integer32"
_ArubaWiredFanTrayGroupIndex_Object = MibTableColumn
arubaWiredFanTrayGroupIndex = _ArubaWiredFanTrayGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 1),
    _ArubaWiredFanTrayGroupIndex_Type()
)
arubaWiredFanTrayGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredFanTrayGroupIndex.setStatus("current")


class _ArubaWiredFanTraySlotIndex_Type(Integer32):
    """Custom type arubaWiredFanTraySlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredFanTraySlotIndex_Type.__name__ = "Integer32"
_ArubaWiredFanTraySlotIndex_Object = MibTableColumn
arubaWiredFanTraySlotIndex = _ArubaWiredFanTraySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 2),
    _ArubaWiredFanTraySlotIndex_Type()
)
arubaWiredFanTraySlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredFanTraySlotIndex.setStatus("current")


class _ArubaWiredFanTrayName_Type(DisplayString):
    """Custom type arubaWiredFanTrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredFanTrayName_Type.__name__ = "DisplayString"
_ArubaWiredFanTrayName_Object = MibTableColumn
arubaWiredFanTrayName = _ArubaWiredFanTrayName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 3),
    _ArubaWiredFanTrayName_Type()
)
arubaWiredFanTrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanTrayName.setStatus("current")


class _ArubaWiredFanTrayState_Type(DisplayString):
    """Custom type arubaWiredFanTrayState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredFanTrayState_Type.__name__ = "DisplayString"
_ArubaWiredFanTrayState_Object = MibTableColumn
arubaWiredFanTrayState = _ArubaWiredFanTrayState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 4),
    _ArubaWiredFanTrayState_Type()
)
arubaWiredFanTrayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanTrayState.setStatus("current")


class _ArubaWiredFanTrayProductName_Type(DisplayString):
    """Custom type arubaWiredFanTrayProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ArubaWiredFanTrayProductName_Type.__name__ = "DisplayString"
_ArubaWiredFanTrayProductName_Object = MibTableColumn
arubaWiredFanTrayProductName = _ArubaWiredFanTrayProductName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 5),
    _ArubaWiredFanTrayProductName_Type()
)
arubaWiredFanTrayProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanTrayProductName.setStatus("current")


class _ArubaWiredFanTraySerialNumber_Type(DisplayString):
    """Custom type arubaWiredFanTraySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredFanTraySerialNumber_Type.__name__ = "DisplayString"
_ArubaWiredFanTraySerialNumber_Object = MibTableColumn
arubaWiredFanTraySerialNumber = _ArubaWiredFanTraySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 6),
    _ArubaWiredFanTraySerialNumber_Type()
)
arubaWiredFanTraySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanTraySerialNumber.setStatus("current")


class _ArubaWiredFanTrayNumberFans_Type(Integer32):
    """Custom type arubaWiredFanTrayNumberFans based on Integer32"""
    defaultValue = 0


_ArubaWiredFanTrayNumberFans_Type.__name__ = "Integer32"
_ArubaWiredFanTrayNumberFans_Object = MibTableColumn
arubaWiredFanTrayNumberFans = _ArubaWiredFanTrayNumberFans_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 7),
    _ArubaWiredFanTrayNumberFans_Type()
)
arubaWiredFanTrayNumberFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanTrayNumberFans.setStatus("current")


class _ArubaWiredFanTrayStateEnum_Type(Integer32):
    """Custom type arubaWiredFanTrayStateEnum based on Integer32"""
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
        *(("unknown", 1),
          ("empty", 2),
          ("initializing", 3),
          ("ready", 4),
          ("down", 5),
          ("unsupported", 6))
    )


_ArubaWiredFanTrayStateEnum_Type.__name__ = "Integer32"
_ArubaWiredFanTrayStateEnum_Object = MibTableColumn
arubaWiredFanTrayStateEnum = _ArubaWiredFanTrayStateEnum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 1, 1, 8),
    _ArubaWiredFanTrayStateEnum_Type()
)
arubaWiredFanTrayStateEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanTrayStateEnum.setStatus("current")
_ArubaWiredFanTrayConformance_ObjectIdentity = ObjectIdentity
arubaWiredFanTrayConformance = _ArubaWiredFanTrayConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99)
)
_ArubaWiredFanTrayCompliances_ObjectIdentity = ObjectIdentity
arubaWiredFanTrayCompliances = _ArubaWiredFanTrayCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99, 1)
)
_ArubaWiredFanTrayGroups_ObjectIdentity = ObjectIdentity
arubaWiredFanTrayGroups = _ArubaWiredFanTrayGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99, 2)
)

# Managed Objects groups

arubaWiredFanTrayTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99, 2, 1)
)
arubaWiredFanTrayTableGroup.setObjects(
      *(("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayName"),
        ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayState"),
        ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayProductName"),
        ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTraySerialNumber"),
        ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayNumberFans"),
        ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayStateEnum"))
)
if mibBuilder.loadTexts:
    arubaWiredFanTrayTableGroup.setStatus("current")


# Notification objects

arubaWiredFanTrayStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 0, 1)
)
arubaWiredFanTrayStateNotification.setObjects(
      *(("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayName"),
        ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayState"))
)
if mibBuilder.loadTexts:
    arubaWiredFanTrayStateNotification.setStatus(
        "current"
    )


# Notifications groups

arubaWiredFanTrayNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99, 2, 2)
)
arubaWiredFanTrayNotificationsGroup.setObjects(
    ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayStateNotification")
)
if mibBuilder.loadTexts:
    arubaWiredFanTrayNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredFanTrayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4, 99, 1, 1)
)
arubaWiredFanTrayCompliance.setObjects(
      *(("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayTable"),
        ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayNotificationsGroup"),
        ("ARUBAWIRED-FANTRAY-MIB", "arubaWiredFanTrayTableGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredFanTrayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-FANTRAY-MIB",
    **{"arubaWiredFanTray": arubaWiredFanTray,
       "arubaWiredFanTrayNotifications": arubaWiredFanTrayNotifications,
       "arubaWiredFanTrayStateNotification": arubaWiredFanTrayStateNotification,
       "arubaWiredFanTrayTable": arubaWiredFanTrayTable,
       "arubaWiredFanTrayEntry": arubaWiredFanTrayEntry,
       "arubaWiredFanTrayGroupIndex": arubaWiredFanTrayGroupIndex,
       "arubaWiredFanTraySlotIndex": arubaWiredFanTraySlotIndex,
       "arubaWiredFanTrayName": arubaWiredFanTrayName,
       "arubaWiredFanTrayState": arubaWiredFanTrayState,
       "arubaWiredFanTrayProductName": arubaWiredFanTrayProductName,
       "arubaWiredFanTraySerialNumber": arubaWiredFanTraySerialNumber,
       "arubaWiredFanTrayNumberFans": arubaWiredFanTrayNumberFans,
       "arubaWiredFanTrayStateEnum": arubaWiredFanTrayStateEnum,
       "arubaWiredFanTrayConformance": arubaWiredFanTrayConformance,
       "arubaWiredFanTrayCompliances": arubaWiredFanTrayCompliances,
       "arubaWiredFanTrayCompliance": arubaWiredFanTrayCompliance,
       "arubaWiredFanTrayGroups": arubaWiredFanTrayGroups,
       "arubaWiredFanTrayTableGroup": arubaWiredFanTrayTableGroup,
       "arubaWiredFanTrayNotificationsGroup": arubaWiredFanTrayNotificationsGroup}
)
