# SNMP MIB module (ALCATEL-IND1-INLINE-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-INLINE-POWER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:27 2025
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

(pethTraps,
 softentIND1InLinePower) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "pethTraps",
    "softentIND1InLinePower")

(pethMainPseEntry,
 pethPsePortEntry) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseEntry",
    "pethPsePortEntry")

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

alcatelIND1INLINEPOWERMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1INLINEPOWERMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaPethObjects_ObjectIdentity = ObjectIdentity
alaPethObjects = _AlaPethObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1)
)
_AlaPethPsePortTable_Object = MibTable
alaPethPsePortTable = _AlaPethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaPethPsePortTable.setStatus("current")
_AlaPethPsePortEntry_Object = MibTableRow
alaPethPsePortEntry = _AlaPethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaPethPsePortEntry.setStatus("current")


class _AlaPethPsePortPowerMaximum_Type(Integer32):
    """Custom type alaPethPsePortPowerMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 20000),
    )


_AlaPethPsePortPowerMaximum_Type.__name__ = "Integer32"
_AlaPethPsePortPowerMaximum_Object = MibTableColumn
alaPethPsePortPowerMaximum = _AlaPethPsePortPowerMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 1, 1, 1),
    _AlaPethPsePortPowerMaximum_Type()
)
alaPethPsePortPowerMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethPsePortPowerMaximum.setStatus("current")


class _AlaPethPsePortPowerActual_Type(Integer32):
    """Custom type alaPethPsePortPowerActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_AlaPethPsePortPowerActual_Type.__name__ = "Integer32"
_AlaPethPsePortPowerActual_Object = MibTableColumn
alaPethPsePortPowerActual = _AlaPethPsePortPowerActual_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 1, 1, 2),
    _AlaPethPsePortPowerActual_Type()
)
alaPethPsePortPowerActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethPsePortPowerActual.setStatus("current")


class _AlaPethPsePortPowerStatus_Type(Integer32):
    """Custom type alaPethPsePortPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOn", 1),
          ("powerOff", 2))
    )


_AlaPethPsePortPowerStatus_Type.__name__ = "Integer32"
_AlaPethPsePortPowerStatus_Object = MibTableColumn
alaPethPsePortPowerStatus = _AlaPethPsePortPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 1, 1, 3),
    _AlaPethPsePortPowerStatus_Type()
)
alaPethPsePortPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethPsePortPowerStatus.setStatus("current")


class _AlaPethPsePortPowerClass_Type(Integer32):
    """Custom type alaPethPsePortPowerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class5", 5))
    )


_AlaPethPsePortPowerClass_Type.__name__ = "Integer32"
_AlaPethPsePortPowerClass_Object = MibTableColumn
alaPethPsePortPowerClass = _AlaPethPsePortPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 1, 1, 4),
    _AlaPethPsePortPowerClass_Type()
)
alaPethPsePortPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPethPsePortPowerClass.setStatus("current")
_AlaPethMainPseTable_Object = MibTable
alaPethMainPseTable = _AlaPethMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaPethMainPseTable.setStatus("current")
_AlaPethMainPseEntry_Object = MibTableRow
alaPethMainPseEntry = _AlaPethMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaPethMainPseEntry.setStatus("current")


class _AlaPethMainPseAdminStatus_Type(Integer32):
    """Custom type alaPethMainPseAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AlaPethMainPseAdminStatus_Type.__name__ = "Integer32"
_AlaPethMainPseAdminStatus_Object = MibTableColumn
alaPethMainPseAdminStatus = _AlaPethMainPseAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 2, 1, 1),
    _AlaPethMainPseAdminStatus_Type()
)
alaPethMainPseAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPseAdminStatus.setStatus("current")


class _AlaPethMainPseMaxPower_Type(Integer32):
    """Custom type alaPethMainPseMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36, 800),
    )


_AlaPethMainPseMaxPower_Type.__name__ = "Integer32"
_AlaPethMainPseMaxPower_Object = MibTableColumn
alaPethMainPseMaxPower = _AlaPethMainPseMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 2, 1, 2),
    _AlaPethMainPseMaxPower_Type()
)
alaPethMainPseMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPseMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    alaPethMainPseMaxPower.setUnits("Watts")


class _AlaPethMainPsePriorityDisconnect_Type(Integer32):
    """Custom type alaPethMainPsePriorityDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPethMainPsePriorityDisconnect_Type.__name__ = "Integer32"
_AlaPethMainPsePriorityDisconnect_Object = MibTableColumn
alaPethMainPsePriorityDisconnect = _AlaPethMainPsePriorityDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 2, 1, 3),
    _AlaPethMainPsePriorityDisconnect_Type()
)
alaPethMainPsePriorityDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPsePriorityDisconnect.setStatus("current")


class _AlaPethMainPseCapacitorDetect_Type(Integer32):
    """Custom type alaPethMainPseCapacitorDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPethMainPseCapacitorDetect_Type.__name__ = "Integer32"
_AlaPethMainPseCapacitorDetect_Object = MibTableColumn
alaPethMainPseCapacitorDetect = _AlaPethMainPseCapacitorDetect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 2, 1, 4),
    _AlaPethMainPseCapacitorDetect_Type()
)
alaPethMainPseCapacitorDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPseCapacitorDetect.setStatus("current")


class _AlaPethMainPsePriority_Type(Integer32):
    """Custom type alaPethMainPsePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_AlaPethMainPsePriority_Type.__name__ = "Integer32"
_AlaPethMainPsePriority_Object = MibTableColumn
alaPethMainPsePriority = _AlaPethMainPsePriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 2, 1, 5),
    _AlaPethMainPsePriority_Type()
)
alaPethMainPsePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPsePriority.setStatus("current")


class _AlaPethMainPseComboPort_Type(Integer32):
    """Custom type alaPethMainPseComboPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPethMainPseComboPort_Type.__name__ = "Integer32"
_AlaPethMainPseComboPort_Object = MibTableColumn
alaPethMainPseComboPort = _AlaPethMainPseComboPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 2, 1, 6),
    _AlaPethMainPseComboPort_Type()
)
alaPethMainPseComboPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPseComboPort.setStatus("current")
_AlaPethNotificationObjects_ObjectIdentity = ObjectIdentity
alaPethNotificationObjects = _AlaPethNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 3)
)


class _PethSourceSlot_Type(Integer32):
    """Custom type pethSourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PethSourceSlot_Type.__name__ = "Integer32"
_PethSourceSlot_Object = MibScalar
pethSourceSlot = _PethSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 3, 1),
    _PethSourceSlot_Type()
)
pethSourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethSourceSlot.setStatus("current")


class _PethSourcePort_Type(Integer32):
    """Custom type pethSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_PethSourcePort_Type.__name__ = "Integer32"
_PethSourcePort_Object = MibScalar
pethSourcePort = _PethSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 1, 3, 2),
    _PethSourcePort_Type()
)
pethSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethSourcePort.setStatus("current")
_AlaPethConformance_ObjectIdentity = ObjectIdentity
alaPethConformance = _AlaPethConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 2)
)
_AlaPethCompliances_ObjectIdentity = ObjectIdentity
alaPethCompliances = _AlaPethCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 2, 1)
)
_AlaPethGroups_ObjectIdentity = ObjectIdentity
alaPethGroups = _AlaPethGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 2, 2)
)
_AlaPethMain_ObjectIdentity = ObjectIdentity
alaPethMain = _AlaPethMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 3)
)
_AlaPethMainTable_Object = MibTable
alaPethMainTable = _AlaPethMainTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaPethMainTable.setStatus("current")
_AlaPethMainEntry_Object = MibTableRow
alaPethMainEntry = _AlaPethMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 3, 1, 1)
)
alaPethMainEntry.setIndexNames(
    (0, "ALCATEL-IND1-INLINE-POWER-MIB", "alaPethMainIndex"),
)
if mibBuilder.loadTexts:
    alaPethMainEntry.setStatus("current")


class _AlaPethMainIndex_Type(Integer32):
    """Custom type alaPethMainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaPethMainIndex_Type.__name__ = "Integer32"
_AlaPethMainIndex_Object = MibTableColumn
alaPethMainIndex = _AlaPethMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 3, 1, 1, 1),
    _AlaPethMainIndex_Type()
)
alaPethMainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPethMainIndex.setStatus("current")


class _AlaPethMainPowerRedundancy_Type(Integer32):
    """Custom type alaPethMainPowerRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPethMainPowerRedundancy_Type.__name__ = "Integer32"
_AlaPethMainPowerRedundancy_Object = MibTableColumn
alaPethMainPowerRedundancy = _AlaPethMainPowerRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 3, 1, 1, 2),
    _AlaPethMainPowerRedundancy_Type()
)
alaPethMainPowerRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPethMainPowerRedundancy.setStatus("current")
pethPsePortEntry.registerAugmentions(
    ("ALCATEL-IND1-INLINE-POWER-MIB",
     "alaPethPsePortEntry")
)
alaPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions(
    ("ALCATEL-IND1-INLINE-POWER-MIB",
     "alaPethMainPseEntry")
)
alaPethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())

# Managed Objects groups

alaPethPsePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 2, 2, 1)
)
alaPethPsePortGroup.setObjects(
      *(("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethPsePortPowerMaximum"),
        ("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethPsePortPowerActual"),
        ("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethPsePortPowerStatus"),
        ("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethPsePortPowerClass"))
)
if mibBuilder.loadTexts:
    alaPethPsePortGroup.setStatus("current")

alaPethMainPseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 2, 2, 2)
)
alaPethMainPseGroup.setObjects(
      *(("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethMainPseAdminStatus"),
        ("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethMainPseMaxPower"),
        ("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethMainPsePriorityDisconnect"),
        ("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethMainPseCapacitorDetect"),
        ("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethMainPsePriority"),
        ("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethMainPseComboPort"))
)
if mibBuilder.loadTexts:
    alaPethMainPseGroup.setStatus("current")


# Notification objects

pethPwrSupplyConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 17, 0, 1)
)
pethPwrSupplyConflict.setObjects(
    ("ALCATEL-IND1-INLINE-POWER-MIB", "pethSourceSlot")
)
if mibBuilder.loadTexts:
    pethPwrSupplyConflict.setStatus(
        "current"
    )

pethPwrSupplyNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 17, 0, 2)
)
pethPwrSupplyNotSupported.setObjects(
    ("ALCATEL-IND1-INLINE-POWER-MIB", "pethSourceSlot")
)
if mibBuilder.loadTexts:
    pethPwrSupplyNotSupported.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

alaPethCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 2, 1, 1)
)
alaPethCompliance.setObjects(
      *(("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethPsePortGroup"),
        ("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethMainPseGroup"))
)
if mibBuilder.loadTexts:
    alaPethCompliance.setStatus(
        "current"
    )

alaPethPseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 1, 2, 1, 2)
)
alaPethPseCompliance.setObjects(
      *(("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethPsePortGroup"),
        ("ALCATEL-IND1-INLINE-POWER-MIB", "alaPethMainPseGroup"))
)
if mibBuilder.loadTexts:
    alaPethPseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-INLINE-POWER-MIB",
    **{"alcatelIND1INLINEPOWERMIB": alcatelIND1INLINEPOWERMIB,
       "alaPethObjects": alaPethObjects,
       "alaPethPsePortTable": alaPethPsePortTable,
       "alaPethPsePortEntry": alaPethPsePortEntry,
       "alaPethPsePortPowerMaximum": alaPethPsePortPowerMaximum,
       "alaPethPsePortPowerActual": alaPethPsePortPowerActual,
       "alaPethPsePortPowerStatus": alaPethPsePortPowerStatus,
       "alaPethPsePortPowerClass": alaPethPsePortPowerClass,
       "alaPethMainPseTable": alaPethMainPseTable,
       "alaPethMainPseEntry": alaPethMainPseEntry,
       "alaPethMainPseAdminStatus": alaPethMainPseAdminStatus,
       "alaPethMainPseMaxPower": alaPethMainPseMaxPower,
       "alaPethMainPsePriorityDisconnect": alaPethMainPsePriorityDisconnect,
       "alaPethMainPseCapacitorDetect": alaPethMainPseCapacitorDetect,
       "alaPethMainPsePriority": alaPethMainPsePriority,
       "alaPethMainPseComboPort": alaPethMainPseComboPort,
       "alaPethNotificationObjects": alaPethNotificationObjects,
       "pethSourceSlot": pethSourceSlot,
       "pethSourcePort": pethSourcePort,
       "alaPethConformance": alaPethConformance,
       "alaPethCompliances": alaPethCompliances,
       "alaPethCompliance": alaPethCompliance,
       "alaPethPseCompliance": alaPethPseCompliance,
       "alaPethGroups": alaPethGroups,
       "alaPethPsePortGroup": alaPethPsePortGroup,
       "alaPethMainPseGroup": alaPethMainPseGroup,
       "alaPethMain": alaPethMain,
       "alaPethMainTable": alaPethMainTable,
       "alaPethMainEntry": alaPethMainEntry,
       "alaPethMainIndex": alaPethMainIndex,
       "alaPethMainPowerRedundancy": alaPethMainPowerRedundancy,
       "pethPwrSupplyConflict": pethPwrSupplyConflict,
       "pethPwrSupplyNotSupported": pethPwrSupplyNotSupported}
)
