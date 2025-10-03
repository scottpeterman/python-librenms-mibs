# SNMP MIB module (ARUBAWIRED-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-MODULE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:17 2025
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

arubaWiredModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6)
)
if mibBuilder.loadTexts:
    arubaWiredModule.setRevisions(
        ("2021-07-01 00:00",
         "2021-01-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredModuleNotifications_ObjectIdentity = ObjectIdentity
arubaWiredModuleNotifications = _ArubaWiredModuleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 0)
)
_ArubaWiredModuleTable_Object = MibTable
arubaWiredModuleTable = _ArubaWiredModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1)
)
if mibBuilder.loadTexts:
    arubaWiredModuleTable.setStatus("current")
_ArubaWiredModuleEntry_Object = MibTableRow
arubaWiredModuleEntry = _ArubaWiredModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1)
)
arubaWiredModuleEntry.setIndexNames(
    (0, "ARUBAWIRED-MODULE-MIB", "arubaWiredModuleGroupIndex"),
    (0, "ARUBAWIRED-MODULE-MIB", "arubaWiredModuleTypeIndex"),
    (0, "ARUBAWIRED-MODULE-MIB", "arubaWiredModuleSlotIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredModuleEntry.setStatus("current")


class _ArubaWiredModuleGroupIndex_Type(Integer32):
    """Custom type arubaWiredModuleGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredModuleGroupIndex_Type.__name__ = "Integer32"
_ArubaWiredModuleGroupIndex_Object = MibTableColumn
arubaWiredModuleGroupIndex = _ArubaWiredModuleGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 1),
    _ArubaWiredModuleGroupIndex_Type()
)
arubaWiredModuleGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredModuleGroupIndex.setStatus("current")


class _ArubaWiredModuleTypeIndex_Type(Integer32):
    """Custom type arubaWiredModuleTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredModuleTypeIndex_Type.__name__ = "Integer32"
_ArubaWiredModuleTypeIndex_Object = MibTableColumn
arubaWiredModuleTypeIndex = _ArubaWiredModuleTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 2),
    _ArubaWiredModuleTypeIndex_Type()
)
arubaWiredModuleTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredModuleTypeIndex.setStatus("current")


class _ArubaWiredModuleSlotIndex_Type(Integer32):
    """Custom type arubaWiredModuleSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredModuleSlotIndex_Type.__name__ = "Integer32"
_ArubaWiredModuleSlotIndex_Object = MibTableColumn
arubaWiredModuleSlotIndex = _ArubaWiredModuleSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 3),
    _ArubaWiredModuleSlotIndex_Type()
)
arubaWiredModuleSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredModuleSlotIndex.setStatus("current")


class _ArubaWiredModuleName_Type(DisplayString):
    """Custom type arubaWiredModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredModuleName_Type.__name__ = "DisplayString"
_ArubaWiredModuleName_Object = MibTableColumn
arubaWiredModuleName = _ArubaWiredModuleName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 4),
    _ArubaWiredModuleName_Type()
)
arubaWiredModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredModuleName.setStatus("current")


class _ArubaWiredModuleType_Type(DisplayString):
    """Custom type arubaWiredModuleType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredModuleType_Type.__name__ = "DisplayString"
_ArubaWiredModuleType_Object = MibTableColumn
arubaWiredModuleType = _ArubaWiredModuleType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 5),
    _ArubaWiredModuleType_Type()
)
arubaWiredModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredModuleType.setStatus("current")


class _ArubaWiredModuleState_Type(DisplayString):
    """Custom type arubaWiredModuleState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredModuleState_Type.__name__ = "DisplayString"
_ArubaWiredModuleState_Object = MibTableColumn
arubaWiredModuleState = _ArubaWiredModuleState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 6),
    _ArubaWiredModuleState_Type()
)
arubaWiredModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredModuleState.setStatus("current")


class _ArubaWiredModuleProductDescription_Type(DisplayString):
    """Custom type arubaWiredModuleProductDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ArubaWiredModuleProductDescription_Type.__name__ = "DisplayString"
_ArubaWiredModuleProductDescription_Object = MibTableColumn
arubaWiredModuleProductDescription = _ArubaWiredModuleProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 7),
    _ArubaWiredModuleProductDescription_Type()
)
arubaWiredModuleProductDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredModuleProductDescription.setStatus("current")


class _ArubaWiredModuleSerialNumber_Type(DisplayString):
    """Custom type arubaWiredModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredModuleSerialNumber_Type.__name__ = "DisplayString"
_ArubaWiredModuleSerialNumber_Object = MibTableColumn
arubaWiredModuleSerialNumber = _ArubaWiredModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 8),
    _ArubaWiredModuleSerialNumber_Type()
)
arubaWiredModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredModuleSerialNumber.setStatus("current")


class _ArubaWiredModuleProductNumber_Type(DisplayString):
    """Custom type arubaWiredModuleProductNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredModuleProductNumber_Type.__name__ = "DisplayString"
_ArubaWiredModuleProductNumber_Object = MibTableColumn
arubaWiredModuleProductNumber = _ArubaWiredModuleProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 9),
    _ArubaWiredModuleProductNumber_Type()
)
arubaWiredModuleProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredModuleProductNumber.setStatus("current")


class _ArubaWiredModuleAdminState_Type(DisplayString):
    """Custom type arubaWiredModuleAdminState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredModuleAdminState_Type.__name__ = "DisplayString"
_ArubaWiredModuleAdminState_Object = MibTableColumn
arubaWiredModuleAdminState = _ArubaWiredModuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 10),
    _ArubaWiredModuleAdminState_Type()
)
arubaWiredModuleAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredModuleAdminState.setStatus("current")


class _ArubaWiredModulePowerPriority_Type(Integer32):
    """Custom type arubaWiredModulePowerPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ArubaWiredModulePowerPriority_Type.__name__ = "Integer32"
_ArubaWiredModulePowerPriority_Object = MibTableColumn
arubaWiredModulePowerPriority = _ArubaWiredModulePowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 11),
    _ArubaWiredModulePowerPriority_Type()
)
arubaWiredModulePowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredModulePowerPriority.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredModulePowerPriority.setUnits("None")


class _ArubaWiredModuleUnrecognizedDescriptor_Type(DisplayString):
    """Custom type arubaWiredModuleUnrecognizedDescriptor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ArubaWiredModuleUnrecognizedDescriptor_Type.__name__ = "DisplayString"
_ArubaWiredModuleUnrecognizedDescriptor_Object = MibTableColumn
arubaWiredModuleUnrecognizedDescriptor = _ArubaWiredModuleUnrecognizedDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 1, 1, 12),
    _ArubaWiredModuleUnrecognizedDescriptor_Type()
)
arubaWiredModuleUnrecognizedDescriptor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredModuleUnrecognizedDescriptor.setStatus("current")
_ArubaWiredModuleConformance_ObjectIdentity = ObjectIdentity
arubaWiredModuleConformance = _ArubaWiredModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 99)
)
_ArubaWiredModuleCompliances_ObjectIdentity = ObjectIdentity
arubaWiredModuleCompliances = _ArubaWiredModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 99, 1)
)
_ArubaWiredModuleGroups_ObjectIdentity = ObjectIdentity
arubaWiredModuleGroups = _ArubaWiredModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 99, 2)
)

# Managed Objects groups

arubaWiredModuleTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 99, 2, 1)
)
arubaWiredModuleTableGroup.setObjects(
      *(("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleName"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleType"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleState"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleProductDescription"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleSerialNumber"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleProductNumber"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleAdminState"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModulePowerPriority"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleUnrecognizedDescriptor"))
)
if mibBuilder.loadTexts:
    arubaWiredModuleTableGroup.setStatus("current")


# Notification objects

arubaWiredModuleStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 0, 1)
)
arubaWiredModuleStateNotification.setObjects(
      *(("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleType"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleName"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleState"))
)
if mibBuilder.loadTexts:
    arubaWiredModuleStateNotification.setStatus(
        "current"
    )

arubaWiredModuleInsertedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 0, 2)
)
arubaWiredModuleInsertedNotification.setObjects(
      *(("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleType"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleName"))
)
if mibBuilder.loadTexts:
    arubaWiredModuleInsertedNotification.setStatus(
        "current"
    )

arubaWiredModuleRemovedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 0, 3)
)
arubaWiredModuleRemovedNotification.setObjects(
      *(("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleType"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleName"))
)
if mibBuilder.loadTexts:
    arubaWiredModuleRemovedNotification.setStatus(
        "current"
    )

arubaWiredModuleUnrecognizedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 0, 4)
)
arubaWiredModuleUnrecognizedNotification.setObjects(
      *(("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleType"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleName"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleUnrecognizedDescriptor"))
)
if mibBuilder.loadTexts:
    arubaWiredModuleUnrecognizedNotification.setStatus(
        "current"
    )


# Notifications groups

arubaWiredModuleNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 99, 2, 2)
)
arubaWiredModuleNotificationsGroup.setObjects(
      *(("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleStateNotification"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleInsertedNotification"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleRemovedNotification"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleUnrecognizedNotification"))
)
if mibBuilder.loadTexts:
    arubaWiredModuleNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6, 99, 1, 1)
)
arubaWiredModuleCompliance.setObjects(
      *(("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleTable"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleNotificationsGroup"),
        ("ARUBAWIRED-MODULE-MIB", "arubaWiredModuleTableGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-MODULE-MIB",
    **{"arubaWiredModule": arubaWiredModule,
       "arubaWiredModuleNotifications": arubaWiredModuleNotifications,
       "arubaWiredModuleStateNotification": arubaWiredModuleStateNotification,
       "arubaWiredModuleInsertedNotification": arubaWiredModuleInsertedNotification,
       "arubaWiredModuleRemovedNotification": arubaWiredModuleRemovedNotification,
       "arubaWiredModuleUnrecognizedNotification": arubaWiredModuleUnrecognizedNotification,
       "arubaWiredModuleTable": arubaWiredModuleTable,
       "arubaWiredModuleEntry": arubaWiredModuleEntry,
       "arubaWiredModuleGroupIndex": arubaWiredModuleGroupIndex,
       "arubaWiredModuleTypeIndex": arubaWiredModuleTypeIndex,
       "arubaWiredModuleSlotIndex": arubaWiredModuleSlotIndex,
       "arubaWiredModuleName": arubaWiredModuleName,
       "arubaWiredModuleType": arubaWiredModuleType,
       "arubaWiredModuleState": arubaWiredModuleState,
       "arubaWiredModuleProductDescription": arubaWiredModuleProductDescription,
       "arubaWiredModuleSerialNumber": arubaWiredModuleSerialNumber,
       "arubaWiredModuleProductNumber": arubaWiredModuleProductNumber,
       "arubaWiredModuleAdminState": arubaWiredModuleAdminState,
       "arubaWiredModulePowerPriority": arubaWiredModulePowerPriority,
       "arubaWiredModuleUnrecognizedDescriptor": arubaWiredModuleUnrecognizedDescriptor,
       "arubaWiredModuleConformance": arubaWiredModuleConformance,
       "arubaWiredModuleCompliances": arubaWiredModuleCompliances,
       "arubaWiredModuleCompliance": arubaWiredModuleCompliance,
       "arubaWiredModuleGroups": arubaWiredModuleGroups,
       "arubaWiredModuleTableGroup": arubaWiredModuleTableGroup,
       "arubaWiredModuleNotificationsGroup": arubaWiredModuleNotificationsGroup}
)
