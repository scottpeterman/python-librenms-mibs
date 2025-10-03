# SNMP MIB module (ARUBAWIRED-TEMPSENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-TEMPSENSOR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:29 2025
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

arubaWiredTempSensor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3)
)
if mibBuilder.loadTexts:
    arubaWiredTempSensor.setRevisions(
        ("2020-02-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredTempSensorNotifications_ObjectIdentity = ObjectIdentity
arubaWiredTempSensorNotifications = _ArubaWiredTempSensorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 0)
)
_ArubaWiredTempSensorTable_Object = MibTable
arubaWiredTempSensorTable = _ArubaWiredTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1)
)
if mibBuilder.loadTexts:
    arubaWiredTempSensorTable.setStatus("current")
_ArubaWiredTempSensorEntry_Object = MibTableRow
arubaWiredTempSensorEntry = _ArubaWiredTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1, 1)
)
arubaWiredTempSensorEntry.setIndexNames(
    (0, "ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorGroupIndex"),
    (0, "ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorSlotTypeIndex"),
    (0, "ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorSlotIndex"),
    (0, "ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredTempSensorEntry.setStatus("current")


class _ArubaWiredTempSensorGroupIndex_Type(Integer32):
    """Custom type arubaWiredTempSensorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredTempSensorGroupIndex_Type.__name__ = "Integer32"
_ArubaWiredTempSensorGroupIndex_Object = MibTableColumn
arubaWiredTempSensorGroupIndex = _ArubaWiredTempSensorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1, 1, 1),
    _ArubaWiredTempSensorGroupIndex_Type()
)
arubaWiredTempSensorGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredTempSensorGroupIndex.setStatus("current")


class _ArubaWiredTempSensorSlotTypeIndex_Type(Integer32):
    """Custom type arubaWiredTempSensorSlotTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredTempSensorSlotTypeIndex_Type.__name__ = "Integer32"
_ArubaWiredTempSensorSlotTypeIndex_Object = MibTableColumn
arubaWiredTempSensorSlotTypeIndex = _ArubaWiredTempSensorSlotTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1, 1, 2),
    _ArubaWiredTempSensorSlotTypeIndex_Type()
)
arubaWiredTempSensorSlotTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredTempSensorSlotTypeIndex.setStatus("current")


class _ArubaWiredTempSensorSlotIndex_Type(Integer32):
    """Custom type arubaWiredTempSensorSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredTempSensorSlotIndex_Type.__name__ = "Integer32"
_ArubaWiredTempSensorSlotIndex_Object = MibTableColumn
arubaWiredTempSensorSlotIndex = _ArubaWiredTempSensorSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1, 1, 3),
    _ArubaWiredTempSensorSlotIndex_Type()
)
arubaWiredTempSensorSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredTempSensorSlotIndex.setStatus("current")


class _ArubaWiredTempSensorIndex_Type(Integer32):
    """Custom type arubaWiredTempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredTempSensorIndex_Type.__name__ = "Integer32"
_ArubaWiredTempSensorIndex_Object = MibTableColumn
arubaWiredTempSensorIndex = _ArubaWiredTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1, 1, 4),
    _ArubaWiredTempSensorIndex_Type()
)
arubaWiredTempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredTempSensorIndex.setStatus("current")


class _ArubaWiredTempSensorName_Type(DisplayString):
    """Custom type arubaWiredTempSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ArubaWiredTempSensorName_Type.__name__ = "DisplayString"
_ArubaWiredTempSensorName_Object = MibTableColumn
arubaWiredTempSensorName = _ArubaWiredTempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1, 1, 5),
    _ArubaWiredTempSensorName_Type()
)
arubaWiredTempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredTempSensorName.setStatus("current")


class _ArubaWiredTempSensorState_Type(DisplayString):
    """Custom type arubaWiredTempSensorState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredTempSensorState_Type.__name__ = "DisplayString"
_ArubaWiredTempSensorState_Object = MibTableColumn
arubaWiredTempSensorState = _ArubaWiredTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1, 1, 6),
    _ArubaWiredTempSensorState_Type()
)
arubaWiredTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredTempSensorState.setStatus("current")
_ArubaWiredTempSensorTemperature_Type = Integer32
_ArubaWiredTempSensorTemperature_Object = MibTableColumn
arubaWiredTempSensorTemperature = _ArubaWiredTempSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1, 1, 7),
    _ArubaWiredTempSensorTemperature_Type()
)
arubaWiredTempSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredTempSensorTemperature.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredTempSensorTemperature.setUnits("millidegrees Celsius")
_ArubaWiredTempSensorMinTemp_Type = Integer32
_ArubaWiredTempSensorMinTemp_Object = MibTableColumn
arubaWiredTempSensorMinTemp = _ArubaWiredTempSensorMinTemp_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1, 1, 8),
    _ArubaWiredTempSensorMinTemp_Type()
)
arubaWiredTempSensorMinTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredTempSensorMinTemp.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredTempSensorMinTemp.setUnits("millidegrees Celsius")
_ArubaWiredTempSensorMaxTemp_Type = Integer32
_ArubaWiredTempSensorMaxTemp_Object = MibTableColumn
arubaWiredTempSensorMaxTemp = _ArubaWiredTempSensorMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 1, 1, 9),
    _ArubaWiredTempSensorMaxTemp_Type()
)
arubaWiredTempSensorMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredTempSensorMaxTemp.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredTempSensorMaxTemp.setUnits("millidegrees Celsius")
_ArubaWiredTempSensorConformance_ObjectIdentity = ObjectIdentity
arubaWiredTempSensorConformance = _ArubaWiredTempSensorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 99)
)
_ArubaWiredTempSensorCompliances_ObjectIdentity = ObjectIdentity
arubaWiredTempSensorCompliances = _ArubaWiredTempSensorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 99, 1)
)
_ArubaWiredTempSensorGroups_ObjectIdentity = ObjectIdentity
arubaWiredTempSensorGroups = _ArubaWiredTempSensorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 99, 2)
)

# Managed Objects groups

arubaWiredTempSensorTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 99, 2, 1)
)
arubaWiredTempSensorTableGroup.setObjects(
      *(("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorName"),
        ("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorState"),
        ("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorTemperature"),
        ("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorMinTemp"),
        ("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorMaxTemp"))
)
if mibBuilder.loadTexts:
    arubaWiredTempSensorTableGroup.setStatus("current")


# Notification objects

arubaWiredTempSensorStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 0, 1)
)
arubaWiredTempSensorStateNotification.setObjects(
      *(("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorName"),
        ("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorState"))
)
if mibBuilder.loadTexts:
    arubaWiredTempSensorStateNotification.setStatus(
        "current"
    )


# Notifications groups

arubaWiredTempSensorNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 99, 2, 2)
)
arubaWiredTempSensorNotificationsGroup.setObjects(
    ("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorStateNotification")
)
if mibBuilder.loadTexts:
    arubaWiredTempSensorNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredTempSensorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3, 99, 1, 1)
)
arubaWiredTempSensorCompliance.setObjects(
      *(("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorTable"),
        ("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorNotificationsGroup"),
        ("ARUBAWIRED-TEMPSENSOR-MIB", "arubaWiredTempSensorTableGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredTempSensorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-TEMPSENSOR-MIB",
    **{"arubaWiredTempSensor": arubaWiredTempSensor,
       "arubaWiredTempSensorNotifications": arubaWiredTempSensorNotifications,
       "arubaWiredTempSensorStateNotification": arubaWiredTempSensorStateNotification,
       "arubaWiredTempSensorTable": arubaWiredTempSensorTable,
       "arubaWiredTempSensorEntry": arubaWiredTempSensorEntry,
       "arubaWiredTempSensorGroupIndex": arubaWiredTempSensorGroupIndex,
       "arubaWiredTempSensorSlotTypeIndex": arubaWiredTempSensorSlotTypeIndex,
       "arubaWiredTempSensorSlotIndex": arubaWiredTempSensorSlotIndex,
       "arubaWiredTempSensorIndex": arubaWiredTempSensorIndex,
       "arubaWiredTempSensorName": arubaWiredTempSensorName,
       "arubaWiredTempSensorState": arubaWiredTempSensorState,
       "arubaWiredTempSensorTemperature": arubaWiredTempSensorTemperature,
       "arubaWiredTempSensorMinTemp": arubaWiredTempSensorMinTemp,
       "arubaWiredTempSensorMaxTemp": arubaWiredTempSensorMaxTemp,
       "arubaWiredTempSensorConformance": arubaWiredTempSensorConformance,
       "arubaWiredTempSensorCompliances": arubaWiredTempSensorCompliances,
       "arubaWiredTempSensorCompliance": arubaWiredTempSensorCompliance,
       "arubaWiredTempSensorGroups": arubaWiredTempSensorGroups,
       "arubaWiredTempSensorTableGroup": arubaWiredTempSensorTableGroup,
       "arubaWiredTempSensorNotificationsGroup": arubaWiredTempSensorNotificationsGroup}
)
