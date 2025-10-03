# SNMP MIB module (Juniper-AUTOCONFIGURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-AUTOCONFIGURE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:54 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniAutoConfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48)
)
if mibBuilder.loadTexts:
    juniAutoConfMIB.setRevisions(
        ("2004-07-26 19:54",
         "2002-11-22 16:08",
         "2002-11-22 15:24",
         "2000-11-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniAutoConfEncaps(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              17,
              19)
        )
    )
    namedValues = NamedValues(
        *(("ip", 0),
          ("ppp", 1),
          ("pppoe", 17),
          ("bridgedEthernet", 19))
    )



# MIB Managed Objects in the order of their OIDs

_JuniAutoConfObjects_ObjectIdentity = ObjectIdentity
juniAutoConfObjects = _JuniAutoConfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1)
)
_JuniAutoConf_ObjectIdentity = ObjectIdentity
juniAutoConf = _JuniAutoConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1)
)
_JuniAutoConfTable_Object = MibTable
juniAutoConfTable = _JuniAutoConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniAutoConfTable.setStatus("current")
_JuniAutoConfEntry_Object = MibTableRow
juniAutoConfEntry = _JuniAutoConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1)
)
juniAutoConfEntry.setIndexNames(
    (0, "Juniper-AUTOCONFIGURE-MIB", "juniAutoConfIfIndex"),
    (0, "Juniper-AUTOCONFIGURE-MIB", "juniAutoConfEncaps"),
)
if mibBuilder.loadTexts:
    juniAutoConfEntry.setStatus("current")
_JuniAutoConfIfIndex_Type = InterfaceIndex
_JuniAutoConfIfIndex_Object = MibTableColumn
juniAutoConfIfIndex = _JuniAutoConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 1),
    _JuniAutoConfIfIndex_Type()
)
juniAutoConfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAutoConfIfIndex.setStatus("current")
_JuniAutoConfEncaps_Type = JuniAutoConfEncaps
_JuniAutoConfEncaps_Object = MibTableColumn
juniAutoConfEncaps = _JuniAutoConfEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 2),
    _JuniAutoConfEncaps_Type()
)
juniAutoConfEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAutoConfEncaps.setStatus("current")
_JuniAutoConfEnable_Type = JuniEnable
_JuniAutoConfEnable_Object = MibTableColumn
juniAutoConfEnable = _JuniAutoConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 3),
    _JuniAutoConfEnable_Type()
)
juniAutoConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAutoConfEnable.setStatus("current")
_JuniAutoConfLockoutSupported_Type = TruthValue
_JuniAutoConfLockoutSupported_Object = MibTableColumn
juniAutoConfLockoutSupported = _JuniAutoConfLockoutSupported_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 4),
    _JuniAutoConfLockoutSupported_Type()
)
juniAutoConfLockoutSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAutoConfLockoutSupported.setStatus("current")


class _JuniAutoConfLockoutMin_Type(Integer32):
    """Custom type juniAutoConfLockoutMin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniAutoConfLockoutMin_Type.__name__ = "Integer32"
_JuniAutoConfLockoutMin_Object = MibTableColumn
juniAutoConfLockoutMin = _JuniAutoConfLockoutMin_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 5),
    _JuniAutoConfLockoutMin_Type()
)
juniAutoConfLockoutMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAutoConfLockoutMin.setStatus("current")


class _JuniAutoConfLockoutMax_Type(Integer32):
    """Custom type juniAutoConfLockoutMax based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniAutoConfLockoutMax_Type.__name__ = "Integer32"
_JuniAutoConfLockoutMax_Object = MibTableColumn
juniAutoConfLockoutMax = _JuniAutoConfLockoutMax_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 6),
    _JuniAutoConfLockoutMax_Type()
)
juniAutoConfLockoutMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAutoConfLockoutMax.setStatus("current")


class _JuniAutoConfLockoutTime_Type(Integer32):
    """Custom type juniAutoConfLockoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniAutoConfLockoutTime_Type.__name__ = "Integer32"
_JuniAutoConfLockoutTime_Object = MibTableColumn
juniAutoConfLockoutTime = _JuniAutoConfLockoutTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 7),
    _JuniAutoConfLockoutTime_Type()
)
juniAutoConfLockoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAutoConfLockoutTime.setStatus("current")


class _JuniAutoConfLockoutElapsedTime_Type(Integer32):
    """Custom type juniAutoConfLockoutElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniAutoConfLockoutElapsedTime_Type.__name__ = "Integer32"
_JuniAutoConfLockoutElapsedTime_Object = MibTableColumn
juniAutoConfLockoutElapsedTime = _JuniAutoConfLockoutElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 8),
    _JuniAutoConfLockoutElapsedTime_Type()
)
juniAutoConfLockoutElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAutoConfLockoutElapsedTime.setStatus("current")


class _JuniAutoConfNextLockoutTime_Type(Integer32):
    """Custom type juniAutoConfNextLockoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniAutoConfNextLockoutTime_Type.__name__ = "Integer32"
_JuniAutoConfNextLockoutTime_Object = MibTableColumn
juniAutoConfNextLockoutTime = _JuniAutoConfNextLockoutTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 9),
    _JuniAutoConfNextLockoutTime_Type()
)
juniAutoConfNextLockoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAutoConfNextLockoutTime.setStatus("current")
_JuniAutoConfMIBConformance_ObjectIdentity = ObjectIdentity
juniAutoConfMIBConformance = _JuniAutoConfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4)
)
_JuniAutoConfMIBCompliances_ObjectIdentity = ObjectIdentity
juniAutoConfMIBCompliances = _JuniAutoConfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1)
)
_JuniAutoConfMIBGroups_ObjectIdentity = ObjectIdentity
juniAutoConfMIBGroups = _JuniAutoConfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2)
)

# Managed Objects groups

juniAutoConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 1)
)
juniAutoConfGroup.setObjects(
    ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfEnable")
)
if mibBuilder.loadTexts:
    juniAutoConfGroup.setStatus("obsolete")

juniAutoConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 2)
)
juniAutoConfGroup2.setObjects(
      *(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutSupported"),
        ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutMin"),
        ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutMax"),
        ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutTime"),
        ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutElapsedTime"),
        ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfNextLockoutTime"))
)
if mibBuilder.loadTexts:
    juniAutoConfGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniAutoConfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 1)
)
juniAutoConfCompliance.setObjects(
    ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfGroup")
)
if mibBuilder.loadTexts:
    juniAutoConfCompliance.setStatus(
        "obsolete"
    )

juniAutoConfCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 2)
)
juniAutoConfCompliance2.setObjects(
    ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfGroup2")
)
if mibBuilder.loadTexts:
    juniAutoConfCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-AUTOCONFIGURE-MIB",
    **{"JuniAutoConfEncaps": JuniAutoConfEncaps,
       "juniAutoConfMIB": juniAutoConfMIB,
       "juniAutoConfObjects": juniAutoConfObjects,
       "juniAutoConf": juniAutoConf,
       "juniAutoConfTable": juniAutoConfTable,
       "juniAutoConfEntry": juniAutoConfEntry,
       "juniAutoConfIfIndex": juniAutoConfIfIndex,
       "juniAutoConfEncaps": juniAutoConfEncaps,
       "juniAutoConfEnable": juniAutoConfEnable,
       "juniAutoConfLockoutSupported": juniAutoConfLockoutSupported,
       "juniAutoConfLockoutMin": juniAutoConfLockoutMin,
       "juniAutoConfLockoutMax": juniAutoConfLockoutMax,
       "juniAutoConfLockoutTime": juniAutoConfLockoutTime,
       "juniAutoConfLockoutElapsedTime": juniAutoConfLockoutElapsedTime,
       "juniAutoConfNextLockoutTime": juniAutoConfNextLockoutTime,
       "juniAutoConfMIBConformance": juniAutoConfMIBConformance,
       "juniAutoConfMIBCompliances": juniAutoConfMIBCompliances,
       "juniAutoConfCompliance": juniAutoConfCompliance,
       "juniAutoConfCompliance2": juniAutoConfCompliance2,
       "juniAutoConfMIBGroups": juniAutoConfMIBGroups,
       "juniAutoConfGroup": juniAutoConfGroup,
       "juniAutoConfGroup2": juniAutoConfGroup2}
)
