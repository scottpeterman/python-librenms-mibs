# SNMP MIB module (ARUBAWIRED-POWER-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-POWER-STAT-MIB
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

arubaWiredPowerStat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8)
)
if mibBuilder.loadTexts:
    arubaWiredPowerStat.setRevisions(
        ("2023-07-25 00:00",
         "2023-06-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RealDecTwo(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs

_ArubaWiredPowerStatNotifications_ObjectIdentity = ObjectIdentity
arubaWiredPowerStatNotifications = _ArubaWiredPowerStatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 0)
)
_ArubaWiredPowerStatObjects_ObjectIdentity = ObjectIdentity
arubaWiredPowerStatObjects = _ArubaWiredPowerStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1)
)
_ArubaWiredPowerStatSys_ObjectIdentity = ObjectIdentity
arubaWiredPowerStatSys = _ArubaWiredPowerStatSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0)
)
_ArubaWiredPowerStatTable_Object = MibTable
arubaWiredPowerStatTable = _ArubaWiredPowerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPowerStatTable.setStatus("current")
_ArubaWiredPowerStatEntry_Object = MibTableRow
arubaWiredPowerStatEntry = _ArubaWiredPowerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1)
)
arubaWiredPowerStatEntry.setIndexNames(
    (0, "ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatGroupIndex"),
    (0, "ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatTypeIndex"),
    (0, "ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatSlotIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredPowerStatEntry.setStatus("current")


class _ArubaWiredPowerStatGroupIndex_Type(Integer32):
    """Custom type arubaWiredPowerStatGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredPowerStatGroupIndex_Type.__name__ = "Integer32"
_ArubaWiredPowerStatGroupIndex_Object = MibTableColumn
arubaWiredPowerStatGroupIndex = _ArubaWiredPowerStatGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 1),
    _ArubaWiredPowerStatGroupIndex_Type()
)
arubaWiredPowerStatGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPowerStatGroupIndex.setStatus("current")


class _ArubaWiredPowerStatTypeIndex_Type(Integer32):
    """Custom type arubaWiredPowerStatTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArubaWiredPowerStatTypeIndex_Type.__name__ = "Integer32"
_ArubaWiredPowerStatTypeIndex_Object = MibTableColumn
arubaWiredPowerStatTypeIndex = _ArubaWiredPowerStatTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 2),
    _ArubaWiredPowerStatTypeIndex_Type()
)
arubaWiredPowerStatTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPowerStatTypeIndex.setStatus("current")


class _ArubaWiredPowerStatSlotIndex_Type(Integer32):
    """Custom type arubaWiredPowerStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredPowerStatSlotIndex_Type.__name__ = "Integer32"
_ArubaWiredPowerStatSlotIndex_Object = MibTableColumn
arubaWiredPowerStatSlotIndex = _ArubaWiredPowerStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 3),
    _ArubaWiredPowerStatSlotIndex_Type()
)
arubaWiredPowerStatSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPowerStatSlotIndex.setStatus("current")


class _ArubaWiredPowerStatName_Type(DisplayString):
    """Custom type arubaWiredPowerStatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredPowerStatName_Type.__name__ = "DisplayString"
_ArubaWiredPowerStatName_Object = MibTableColumn
arubaWiredPowerStatName = _ArubaWiredPowerStatName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 4),
    _ArubaWiredPowerStatName_Type()
)
arubaWiredPowerStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPowerStatName.setStatus("current")


class _ArubaWiredPowerStatType_Type(DisplayString):
    """Custom type arubaWiredPowerStatType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredPowerStatType_Type.__name__ = "DisplayString"
_ArubaWiredPowerStatType_Object = MibTableColumn
arubaWiredPowerStatType = _ArubaWiredPowerStatType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 5),
    _ArubaWiredPowerStatType_Type()
)
arubaWiredPowerStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPowerStatType.setStatus("current")


class _ArubaWiredPowerStatPowerConsumed_Type(Integer32):
    """Custom type arubaWiredPowerStatPowerConsumed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_ArubaWiredPowerStatPowerConsumed_Type.__name__ = "Integer32"
_ArubaWiredPowerStatPowerConsumed_Object = MibTableColumn
arubaWiredPowerStatPowerConsumed = _ArubaWiredPowerStatPowerConsumed_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 6),
    _ArubaWiredPowerStatPowerConsumed_Type()
)
arubaWiredPowerStatPowerConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPowerStatPowerConsumed.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPowerStatPowerConsumed.setUnits("Watts")


class _ArubaWiredPowerStatPowerConsumedAverage_Type(RealDecTwo):
    """Custom type arubaWiredPowerStatPowerConsumedAverage based on RealDecTwo"""
    defaultValue = 0


_ArubaWiredPowerStatPowerConsumedAverage_Type.__name__ = "RealDecTwo"
_ArubaWiredPowerStatPowerConsumedAverage_Object = MibTableColumn
arubaWiredPowerStatPowerConsumedAverage = _ArubaWiredPowerStatPowerConsumedAverage_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 7),
    _ArubaWiredPowerStatPowerConsumedAverage_Type()
)
arubaWiredPowerStatPowerConsumedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredPowerStatPowerConsumedAverage.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPowerStatPowerConsumedAverage.setUnits("Watts")


class _ArubaWiredPowerStatPowerConsumedAveragePeriod_Type(Integer32):
    """Custom type arubaWiredPowerStatPowerConsumedAveragePeriod based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_ArubaWiredPowerStatPowerConsumedAveragePeriod_Type.__name__ = "Integer32"
_ArubaWiredPowerStatPowerConsumedAveragePeriod_Object = MibTableColumn
arubaWiredPowerStatPowerConsumedAveragePeriod = _ArubaWiredPowerStatPowerConsumedAveragePeriod_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 8),
    _ArubaWiredPowerStatPowerConsumedAveragePeriod_Type()
)
arubaWiredPowerStatPowerConsumedAveragePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredPowerStatPowerConsumedAveragePeriod.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredPowerStatPowerConsumedAveragePeriod.setUnits("seconds")
_ArubaWiredPowerStatConformance_ObjectIdentity = ObjectIdentity
arubaWiredPowerStatConformance = _ArubaWiredPowerStatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 2)
)
_ArubaWiredPowerStatCompliances_ObjectIdentity = ObjectIdentity
arubaWiredPowerStatCompliances = _ArubaWiredPowerStatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 2, 1)
)
_ArubaWiredPowerStatGroups_ObjectIdentity = ObjectIdentity
arubaWiredPowerStatGroups = _ArubaWiredPowerStatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 2, 2)
)

# Managed Objects groups

arubaWiredPowerStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 2, 2, 1)
)
arubaWiredPowerStatTableGroup.setObjects(
      *(("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatName"),
        ("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatType"),
        ("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatPowerConsumed"),
        ("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatPowerConsumedAverage"),
        ("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatPowerConsumedAveragePeriod"))
)
if mibBuilder.loadTexts:
    arubaWiredPowerStatTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredPowerStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 2, 1, 1)
)
arubaWiredPowerStatCompliance.setObjects(
    ("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatTableGroup")
)
if mibBuilder.loadTexts:
    arubaWiredPowerStatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-POWER-STAT-MIB",
    **{"RealDecTwo": RealDecTwo,
       "arubaWiredPowerStat": arubaWiredPowerStat,
       "arubaWiredPowerStatNotifications": arubaWiredPowerStatNotifications,
       "arubaWiredPowerStatObjects": arubaWiredPowerStatObjects,
       "arubaWiredPowerStatSys": arubaWiredPowerStatSys,
       "arubaWiredPowerStatTable": arubaWiredPowerStatTable,
       "arubaWiredPowerStatEntry": arubaWiredPowerStatEntry,
       "arubaWiredPowerStatGroupIndex": arubaWiredPowerStatGroupIndex,
       "arubaWiredPowerStatTypeIndex": arubaWiredPowerStatTypeIndex,
       "arubaWiredPowerStatSlotIndex": arubaWiredPowerStatSlotIndex,
       "arubaWiredPowerStatName": arubaWiredPowerStatName,
       "arubaWiredPowerStatType": arubaWiredPowerStatType,
       "arubaWiredPowerStatPowerConsumed": arubaWiredPowerStatPowerConsumed,
       "arubaWiredPowerStatPowerConsumedAverage": arubaWiredPowerStatPowerConsumedAverage,
       "arubaWiredPowerStatPowerConsumedAveragePeriod": arubaWiredPowerStatPowerConsumedAveragePeriod,
       "arubaWiredPowerStatConformance": arubaWiredPowerStatConformance,
       "arubaWiredPowerStatCompliances": arubaWiredPowerStatCompliances,
       "arubaWiredPowerStatCompliance": arubaWiredPowerStatCompliance,
       "arubaWiredPowerStatGroups": arubaWiredPowerStatGroups,
       "arubaWiredPowerStatTableGroup": arubaWiredPowerStatTableGroup}
)
