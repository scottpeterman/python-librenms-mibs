# SNMP MIB module (ARUBAWIRED-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-FAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:06 2025
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

arubaWiredFan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5)
)
if mibBuilder.loadTexts:
    arubaWiredFan.setRevisions(
        ("2023-03-31 00:00",
         "2020-02-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredFanNotifications_ObjectIdentity = ObjectIdentity
arubaWiredFanNotifications = _ArubaWiredFanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 0)
)
_ArubaWiredFanTable_Object = MibTable
arubaWiredFanTable = _ArubaWiredFanTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1)
)
if mibBuilder.loadTexts:
    arubaWiredFanTable.setStatus("current")
_ArubaWiredFanEntry_Object = MibTableRow
arubaWiredFanEntry = _ArubaWiredFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1)
)
arubaWiredFanEntry.setIndexNames(
    (0, "ARUBAWIRED-FAN-MIB", "arubaWiredFanGroupIndex"),
    (0, "ARUBAWIRED-FAN-MIB", "arubaWiredFanTrayIndex"),
    (0, "ARUBAWIRED-FAN-MIB", "arubaWiredFanSlotIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredFanEntry.setStatus("current")


class _ArubaWiredFanGroupIndex_Type(Integer32):
    """Custom type arubaWiredFanGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredFanGroupIndex_Type.__name__ = "Integer32"
_ArubaWiredFanGroupIndex_Object = MibTableColumn
arubaWiredFanGroupIndex = _ArubaWiredFanGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1, 1),
    _ArubaWiredFanGroupIndex_Type()
)
arubaWiredFanGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredFanGroupIndex.setStatus("current")


class _ArubaWiredFanTrayIndex_Type(Integer32):
    """Custom type arubaWiredFanTrayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredFanTrayIndex_Type.__name__ = "Integer32"
_ArubaWiredFanTrayIndex_Object = MibTableColumn
arubaWiredFanTrayIndex = _ArubaWiredFanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1, 2),
    _ArubaWiredFanTrayIndex_Type()
)
arubaWiredFanTrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredFanTrayIndex.setStatus("current")


class _ArubaWiredFanSlotIndex_Type(Integer32):
    """Custom type arubaWiredFanSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredFanSlotIndex_Type.__name__ = "Integer32"
_ArubaWiredFanSlotIndex_Object = MibTableColumn
arubaWiredFanSlotIndex = _ArubaWiredFanSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1, 3),
    _ArubaWiredFanSlotIndex_Type()
)
arubaWiredFanSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredFanSlotIndex.setStatus("current")


class _ArubaWiredFanName_Type(DisplayString):
    """Custom type arubaWiredFanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredFanName_Type.__name__ = "DisplayString"
_ArubaWiredFanName_Object = MibTableColumn
arubaWiredFanName = _ArubaWiredFanName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1, 4),
    _ArubaWiredFanName_Type()
)
arubaWiredFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanName.setStatus("current")


class _ArubaWiredFanState_Type(DisplayString):
    """Custom type arubaWiredFanState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredFanState_Type.__name__ = "DisplayString"
_ArubaWiredFanState_Object = MibTableColumn
arubaWiredFanState = _ArubaWiredFanState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1, 5),
    _ArubaWiredFanState_Type()
)
arubaWiredFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanState.setStatus("current")


class _ArubaWiredFanProductName_Type(DisplayString):
    """Custom type arubaWiredFanProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredFanProductName_Type.__name__ = "DisplayString"
_ArubaWiredFanProductName_Object = MibTableColumn
arubaWiredFanProductName = _ArubaWiredFanProductName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1, 6),
    _ArubaWiredFanProductName_Type()
)
arubaWiredFanProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanProductName.setStatus("current")


class _ArubaWiredFanSerialNumber_Type(DisplayString):
    """Custom type arubaWiredFanSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredFanSerialNumber_Type.__name__ = "DisplayString"
_ArubaWiredFanSerialNumber_Object = MibTableColumn
arubaWiredFanSerialNumber = _ArubaWiredFanSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1, 7),
    _ArubaWiredFanSerialNumber_Type()
)
arubaWiredFanSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanSerialNumber.setStatus("current")
_ArubaWiredFanRPM_Type = Integer32
_ArubaWiredFanRPM_Object = MibTableColumn
arubaWiredFanRPM = _ArubaWiredFanRPM_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1, 8),
    _ArubaWiredFanRPM_Type()
)
arubaWiredFanRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanRPM.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredFanRPM.setUnits("RPM")


class _ArubaWiredFanAirflowDirection_Type(DisplayString):
    """Custom type arubaWiredFanAirflowDirection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredFanAirflowDirection_Type.__name__ = "DisplayString"
_ArubaWiredFanAirflowDirection_Object = MibTableColumn
arubaWiredFanAirflowDirection = _ArubaWiredFanAirflowDirection_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1, 9),
    _ArubaWiredFanAirflowDirection_Type()
)
arubaWiredFanAirflowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanAirflowDirection.setStatus("current")


class _ArubaWiredFanStateEnum_Type(Integer32):
    """Custom type arubaWiredFanStateEnum based on Integer32"""
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
          ("empty", 2),
          ("uninitialized", 3),
          ("ok", 4),
          ("fault", 5))
    )


_ArubaWiredFanStateEnum_Type.__name__ = "Integer32"
_ArubaWiredFanStateEnum_Object = MibTableColumn
arubaWiredFanStateEnum = _ArubaWiredFanStateEnum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 1, 1, 10),
    _ArubaWiredFanStateEnum_Type()
)
arubaWiredFanStateEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredFanStateEnum.setStatus("current")
_ArubaWiredFanConformance_ObjectIdentity = ObjectIdentity
arubaWiredFanConformance = _ArubaWiredFanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 99)
)
_ArubaWiredFanCompliances_ObjectIdentity = ObjectIdentity
arubaWiredFanCompliances = _ArubaWiredFanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 99, 1)
)
_ArubaWiredFanGroups_ObjectIdentity = ObjectIdentity
arubaWiredFanGroups = _ArubaWiredFanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 99, 2)
)

# Managed Objects groups

arubaWiredFanTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 99, 2, 1)
)
arubaWiredFanTableGroup.setObjects(
      *(("ARUBAWIRED-FAN-MIB", "arubaWiredFanName"),
        ("ARUBAWIRED-FAN-MIB", "arubaWiredFanState"),
        ("ARUBAWIRED-FAN-MIB", "arubaWiredFanProductName"),
        ("ARUBAWIRED-FAN-MIB", "arubaWiredFanSerialNumber"),
        ("ARUBAWIRED-FAN-MIB", "arubaWiredFanRPM"),
        ("ARUBAWIRED-FAN-MIB", "arubaWiredFanAirflowDirection"),
        ("ARUBAWIRED-FAN-MIB", "arubaWiredFanStateEnum"))
)
if mibBuilder.loadTexts:
    arubaWiredFanTableGroup.setStatus("current")


# Notification objects

arubaWiredFanStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 0, 1)
)
arubaWiredFanStateNotification.setObjects(
      *(("ARUBAWIRED-FAN-MIB", "arubaWiredFanName"),
        ("ARUBAWIRED-FAN-MIB", "arubaWiredFanState"))
)
if mibBuilder.loadTexts:
    arubaWiredFanStateNotification.setStatus(
        "current"
    )


# Notifications groups

arubaWiredFanNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 99, 2, 2)
)
arubaWiredFanNotificationsGroup.setObjects(
    ("ARUBAWIRED-FAN-MIB", "arubaWiredFanStateNotification")
)
if mibBuilder.loadTexts:
    arubaWiredFanNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredFanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5, 99, 1, 1)
)
arubaWiredFanCompliance.setObjects(
      *(("ARUBAWIRED-FAN-MIB", "arubaWiredFanTable"),
        ("ARUBAWIRED-FAN-MIB", "arubaWiredFanNotificationsGroup"),
        ("ARUBAWIRED-FAN-MIB", "arubaWiredFanTableGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredFanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-FAN-MIB",
    **{"arubaWiredFan": arubaWiredFan,
       "arubaWiredFanNotifications": arubaWiredFanNotifications,
       "arubaWiredFanStateNotification": arubaWiredFanStateNotification,
       "arubaWiredFanTable": arubaWiredFanTable,
       "arubaWiredFanEntry": arubaWiredFanEntry,
       "arubaWiredFanGroupIndex": arubaWiredFanGroupIndex,
       "arubaWiredFanTrayIndex": arubaWiredFanTrayIndex,
       "arubaWiredFanSlotIndex": arubaWiredFanSlotIndex,
       "arubaWiredFanName": arubaWiredFanName,
       "arubaWiredFanState": arubaWiredFanState,
       "arubaWiredFanProductName": arubaWiredFanProductName,
       "arubaWiredFanSerialNumber": arubaWiredFanSerialNumber,
       "arubaWiredFanRPM": arubaWiredFanRPM,
       "arubaWiredFanAirflowDirection": arubaWiredFanAirflowDirection,
       "arubaWiredFanStateEnum": arubaWiredFanStateEnum,
       "arubaWiredFanConformance": arubaWiredFanConformance,
       "arubaWiredFanCompliances": arubaWiredFanCompliances,
       "arubaWiredFanCompliance": arubaWiredFanCompliance,
       "arubaWiredFanGroups": arubaWiredFanGroups,
       "arubaWiredFanTableGroup": arubaWiredFanTableGroup,
       "arubaWiredFanNotificationsGroup": arubaWiredFanNotificationsGroup}
)
