# SNMP MIB module (ARUBAWIRED-POWERSUPPLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-POWERSUPPLY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:23 2025
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

arubaWiredPowerSupply = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2)
)
if mibBuilder.loadTexts:
    arubaWiredPowerSupply.setRevisions(
        ("2025-02-26 00:00",
         "2024-12-16 00:00",
         "2023-05-09 00:00",
         "2023-03-28 00:00",
         "2020-01-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredPSUNotifications_ObjectIdentity = ObjectIdentity
arubaWiredPSUNotifications = _ArubaWiredPSUNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 0)
)
_ArubaWiredPowerSupplyTable_Object = MibTable
arubaWiredPowerSupplyTable = _ArubaWiredPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPowerSupplyTable.setStatus("current")
_ArubaWiredPowerSupplyEntry_Object = MibTableRow
arubaWiredPowerSupplyEntry = _ArubaWiredPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1)
)
arubaWiredPowerSupplyEntry.setIndexNames(
    (0, "ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUGroupIndex"),
    (0, "ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUSlotIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredPowerSupplyEntry.setStatus("current")


class _ArubaWiredPSUGroupIndex_Type(Integer32):
    """Custom type arubaWiredPSUGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredPSUGroupIndex_Type.__name__ = "Integer32"
_ArubaWiredPSUGroupIndex_Object = MibTableColumn
arubaWiredPSUGroupIndex = _ArubaWiredPSUGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 1),
    _ArubaWiredPSUGroupIndex_Type()
)
arubaWiredPSUGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUGroupIndex.setStatus("current")


class _ArubaWiredPSUSlotIndex_Type(Integer32):
    """Custom type arubaWiredPSUSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredPSUSlotIndex_Type.__name__ = "Integer32"
_ArubaWiredPSUSlotIndex_Object = MibTableColumn
arubaWiredPSUSlotIndex = _ArubaWiredPSUSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 2),
    _ArubaWiredPSUSlotIndex_Type()
)
arubaWiredPSUSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUSlotIndex.setStatus("current")


class _ArubaWiredPSUName_Type(DisplayString):
    """Custom type arubaWiredPSUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredPSUName_Type.__name__ = "DisplayString"
_ArubaWiredPSUName_Object = MibTableColumn
arubaWiredPSUName = _ArubaWiredPSUName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 3),
    _ArubaWiredPSUName_Type()
)
arubaWiredPSUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUName.setStatus("current")


class _ArubaWiredPSUState_Type(DisplayString):
    """Custom type arubaWiredPSUState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredPSUState_Type.__name__ = "DisplayString"
_ArubaWiredPSUState_Object = MibTableColumn
arubaWiredPSUState = _ArubaWiredPSUState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 4),
    _ArubaWiredPSUState_Type()
)
arubaWiredPSUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUState.setStatus("current")


class _ArubaWiredPSUProductName_Type(DisplayString):
    """Custom type arubaWiredPSUProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredPSUProductName_Type.__name__ = "DisplayString"
_ArubaWiredPSUProductName_Object = MibTableColumn
arubaWiredPSUProductName = _ArubaWiredPSUProductName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 5),
    _ArubaWiredPSUProductName_Type()
)
arubaWiredPSUProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUProductName.setStatus("current")


class _ArubaWiredPSUSerialNumber_Type(DisplayString):
    """Custom type arubaWiredPSUSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredPSUSerialNumber_Type.__name__ = "DisplayString"
_ArubaWiredPSUSerialNumber_Object = MibTableColumn
arubaWiredPSUSerialNumber = _ArubaWiredPSUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 6),
    _ArubaWiredPSUSerialNumber_Type()
)
arubaWiredPSUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUSerialNumber.setStatus("current")


class _ArubaWiredPSUInstantaneousPower_Type(Integer32):
    """Custom type arubaWiredPSUInstantaneousPower based on Integer32"""
    defaultValue = 0


_ArubaWiredPSUInstantaneousPower_Type.__name__ = "Integer32"
_ArubaWiredPSUInstantaneousPower_Object = MibTableColumn
arubaWiredPSUInstantaneousPower = _ArubaWiredPSUInstantaneousPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 7),
    _ArubaWiredPSUInstantaneousPower_Type()
)
arubaWiredPSUInstantaneousPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUInstantaneousPower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPSUInstantaneousPower.setUnits("Watts")


class _ArubaWiredPSUMaximumPower_Type(Integer32):
    """Custom type arubaWiredPSUMaximumPower based on Integer32"""
    defaultValue = 0


_ArubaWiredPSUMaximumPower_Type.__name__ = "Integer32"
_ArubaWiredPSUMaximumPower_Object = MibTableColumn
arubaWiredPSUMaximumPower = _ArubaWiredPSUMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 8),
    _ArubaWiredPSUMaximumPower_Type()
)
arubaWiredPSUMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUMaximumPower.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPSUMaximumPower.setUnits("Watts")


class _ArubaWiredPSUNumberFailures_Type(Integer32):
    """Custom type arubaWiredPSUNumberFailures based on Integer32"""
    defaultValue = 0


_ArubaWiredPSUNumberFailures_Type.__name__ = "Integer32"
_ArubaWiredPSUNumberFailures_Object = MibTableColumn
arubaWiredPSUNumberFailures = _ArubaWiredPSUNumberFailures_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 9),
    _ArubaWiredPSUNumberFailures_Type()
)
arubaWiredPSUNumberFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUNumberFailures.setStatus("current")


class _ArubaWiredPSUAirflowDirection_Type(DisplayString):
    """Custom type arubaWiredPSUAirflowDirection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredPSUAirflowDirection_Type.__name__ = "DisplayString"
_ArubaWiredPSUAirflowDirection_Object = MibTableColumn
arubaWiredPSUAirflowDirection = _ArubaWiredPSUAirflowDirection_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 10),
    _ArubaWiredPSUAirflowDirection_Type()
)
arubaWiredPSUAirflowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUAirflowDirection.setStatus("current")


class _ArubaWiredPSUStateEnum_Type(Integer32):
    """Custom type arubaWiredPSUStateEnum based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("faultAbsent", 2),
          ("faultInput", 3),
          ("faultOutput", 4),
          ("faultPOE", 5),
          ("faultNoRecov", 6),
          ("alert", 7),
          ("unknown", 8),
          ("unsupported", 9),
          ("warning", 10),
          ("init", 11),
          ("empty", 12),
          ("faultAirflow", 13),
          ("faultRedundancy", 14),
          ("faultMixedInput", 15),
          ("overvoltage", 16),
          ("undervoltage", 17))
    )


_ArubaWiredPSUStateEnum_Type.__name__ = "Integer32"
_ArubaWiredPSUStateEnum_Object = MibTableColumn
arubaWiredPSUStateEnum = _ArubaWiredPSUStateEnum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 1, 1, 11),
    _ArubaWiredPSUStateEnum_Type()
)
arubaWiredPSUStateEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPSUStateEnum.setStatus("current")
_ArubaWiredPowerSupplyConformance_ObjectIdentity = ObjectIdentity
arubaWiredPowerSupplyConformance = _ArubaWiredPowerSupplyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 99)
)
_ArubaWiredPowerSupplyCompliances_ObjectIdentity = ObjectIdentity
arubaWiredPowerSupplyCompliances = _ArubaWiredPowerSupplyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 99, 1)
)
_ArubaWiredPowerSupplyGroups_ObjectIdentity = ObjectIdentity
arubaWiredPowerSupplyGroups = _ArubaWiredPowerSupplyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 99, 2)
)

# Managed Objects groups

arubaWiredPowerSupplyTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 99, 2, 1)
)
arubaWiredPowerSupplyTableGroup.setObjects(
      *(("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUGroupIndex"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUSlotIndex"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUName"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUState"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUProductName"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUSerialNumber"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUInstantaneousPower"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUMaximumPower"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUNumberFailures"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUAirflowDirection"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUStateEnum"))
)
if mibBuilder.loadTexts:
    arubaWiredPowerSupplyTableGroup.setStatus("current")


# Notification objects

arubaWiredPSUStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 0, 1)
)
arubaWiredPSUStateNotification.setObjects(
      *(("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUGroupIndex"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUSlotIndex"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUState"))
)
if mibBuilder.loadTexts:
    arubaWiredPSUStateNotification.setStatus(
        "current"
    )


# Notifications groups

arubaWiredPSUNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 99, 2, 2)
)
arubaWiredPSUNotificationsGroup.setObjects(
    ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUStateNotification")
)
if mibBuilder.loadTexts:
    arubaWiredPSUNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredPowerSupplyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2, 99, 1, 1)
)
arubaWiredPowerSupplyCompliance.setObjects(
      *(("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPowerSupplyTable"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPSUNotificationsGroup"),
        ("ARUBAWIRED-POWERSUPPLY-MIB", "arubaWiredPowerSupplyTableGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredPowerSupplyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-POWERSUPPLY-MIB",
    **{"arubaWiredPowerSupply": arubaWiredPowerSupply,
       "arubaWiredPSUNotifications": arubaWiredPSUNotifications,
       "arubaWiredPSUStateNotification": arubaWiredPSUStateNotification,
       "arubaWiredPowerSupplyTable": arubaWiredPowerSupplyTable,
       "arubaWiredPowerSupplyEntry": arubaWiredPowerSupplyEntry,
       "arubaWiredPSUGroupIndex": arubaWiredPSUGroupIndex,
       "arubaWiredPSUSlotIndex": arubaWiredPSUSlotIndex,
       "arubaWiredPSUName": arubaWiredPSUName,
       "arubaWiredPSUState": arubaWiredPSUState,
       "arubaWiredPSUProductName": arubaWiredPSUProductName,
       "arubaWiredPSUSerialNumber": arubaWiredPSUSerialNumber,
       "arubaWiredPSUInstantaneousPower": arubaWiredPSUInstantaneousPower,
       "arubaWiredPSUMaximumPower": arubaWiredPSUMaximumPower,
       "arubaWiredPSUNumberFailures": arubaWiredPSUNumberFailures,
       "arubaWiredPSUAirflowDirection": arubaWiredPSUAirflowDirection,
       "arubaWiredPSUStateEnum": arubaWiredPSUStateEnum,
       "arubaWiredPowerSupplyConformance": arubaWiredPowerSupplyConformance,
       "arubaWiredPowerSupplyCompliances": arubaWiredPowerSupplyCompliances,
       "arubaWiredPowerSupplyCompliance": arubaWiredPowerSupplyCompliance,
       "arubaWiredPowerSupplyGroups": arubaWiredPowerSupplyGroups,
       "arubaWiredPowerSupplyTableGroup": arubaWiredPowerSupplyTableGroup,
       "arubaWiredPSUNotificationsGroup": arubaWiredPSUNotificationsGroup}
)
